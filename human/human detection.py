import cv2
#import serial

#ser = serial.Serial('/dev/ttyUSB0', 9600)  # Configurar com necessari per obrir connexió amb placa Arduino

cap = cv2.VideoCapture(1)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Get the frame width
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Get the frame height

human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

print('it just works')

square_size = 100
center_x = frame_width // 2
center_y = frame_height // 2
top_left = (center_x - square_size // 2, center_y - square_size // 2)
bottom_right = (center_x + square_size // 2, center_y + square_size // 2)

print('Top left:', top_left,'Bot right:', bottom_right)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)

    # Draw a square around the center point

    top_left = (center_x - square_size // 2, center_y - square_size // 2)
    bottom_right = (center_x + square_size // 2, center_y + square_size // 2)
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    # Display the resulting frame
    for (x,y,w,h) in humans:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        print('Figura humana detectada. Estabilitzant...')
        #ser.write(b'RUN_FUNCTION\n')   # Exemple crida funcio de Arduino
        print('X:', x, 'Y:', y, 'W:', w, 'H:', h)

        if top_left[0] <= x <= bottom_right[0] and top_left[1] <= y <= bottom_right[1]:
            print('Figura humana en posicio estable')
        else:
            print('Fa falta estabilitzar!')



    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
# ser.close() # Fi connexio Arduino
