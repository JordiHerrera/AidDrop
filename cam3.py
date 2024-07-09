import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


def encender_pin(codi_pin):
    GPIO.output(codi_pin, GPIO.HIGH)


def apagar_pin(codi_pin):
    GPIO.output(codi_pin, GPIO.LOW)

def angle_to_percent(angle):
    if angle > 180 or angle < 0:
        return False

    start = 4
    end = 12.5
    ratio = (end - start) / 180  # Calculate ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


GPIO.setmode(GPIO.BOARD)

pwm_gpio = 12
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)

pwm.start(angle_to_percent(180))


# Initialize the camera and set up the stream
camera = PiCamera()
camera.resolution = (320, 240)  # Set resolution
camera.framerate = 15  # Set frame rate
rawCapture = PiRGBArray(camera, size=(320, 240))

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

print('it just works')

square_size = 100
center_x = 320 // 2  # Adjust based on resolution
center_y = 240 // 2  # Adjust based on resolution
top_left = (center_x - square_size // 2, center_y - square_size // 2)
bottom_right = (center_x + square_size // 2, center_y + square_size // 2)

PIN_LED = 17
GPIO.setup(PIN_LED, GPIO.OUT)

# Allow the camera to warm up
time.sleep(0.1)

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)

    top_left = (center_x - square_size // 2, center_y - square_size // 2)
    bottom_right = (center_x + square_size // 2, center_y + square_size // 2)

    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.line(image, (center_x, 0), (center_x, 240), (0, 255, 0), 2)
    cv2.line(image, (0, center_y), (320, center_y), (0, 255, 0), 2)

    for (x, y, w, h) in humans:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print('Figura humana detectada. Estabilitzant...')
        # ser.write(b'RUN_FUNCTION\n')   # Exemple crida funcio de Arduino
        print('X:', x, 'Y:', y, 'W:', w, 'H:', h)

        if top_left[0] <= x <= bottom_right[0] and top_left[1] <= y <= bottom_right[1]:
            print('Figura humana en posicio estable')
            encender_pin(PIN_LED)
            time.sleep(5)
            apagar_pin(PIN_LED)
        else:
            if x < center_x:
                print('Fa falta estabilitzar! La figura és a l esquerra.')
                # Crida arduino
            elif x > center_x:
                print('Fa falta estabilitzar! La figura és a la dreta.')
                # Crida arduino
            if y < center_y:
                print('Fa falta estabilitzar! La figura és a la part superior.')
                # Crida arduino
            elif y > center_y:
                print('Fa falta estabilitzar! La figura és a la part inferior.')
                # Crida arduino
            pwm.ChangeDutyCycle(angle_to_percent(0))
            time.sleep(5)
            pwm.ChangeDutyCycle(angle_to_percent(180))

        print('')
    cv2.imshow('frame', image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)  # Clear the stream for the next frame

    if key == ord('q'):
        break

# When everything is done, release the capture
cv2.destroyAllWindows()
camera.close()
# ser.close()  # Fi connexio Arduino
