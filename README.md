# AidDrop

![img3](https://i.imgur.com/3Jg5n3V.jpeg)

## Continguts
- [Que és AidDrop?](#que-és-aiddrop)
- [Instal·lació del projecte](#installació-del-projecte)
- [Programari utilitzat](#programari-utilitzat)
- [Components a destacar](#components-a-destacar)
- [Diagrama de fluxe](#diagrama-de-fluxe)
- [Inter-connexió entre dispositius](#inter-connexió-entre-dispositius)
- [Algorísmica](#algorísmica)
  - [Reconeixement de formes humanes](#-reconeixement-de-formes-humanes)
  - [Moviment de la pinça](#-moviment-de-la-pinça)
  - [Moviment del dron](#-moviment-del-dron)


## Dron de enviament de subministraments d'emergència

### Que és AidDrop?
AidDrop és un dron capaç de fer entrega de material i subministraments en casos d'emergències en llocs de difícil accés.

### Instal·lació del projecte
Carregar el fitxer cam3.py a la raspberry pi.
Assegurar-se de tenir totes les llibreries necessaries.

### Programari utilitzat
- Fritzing: Diagrama d'inter-connexió de components
- PyCharm: Edició de codi Python
- Arduino IDE: Edició de codi Arduino
- opencv / cv2: Processament d'imatges.
- pyzbar: Lectura de codis de barres i QR.
- TinkerCad: Modelatge
- Betaflight: Proves de controlador de vol i motors
- Mission Planer: Programació de vol i proves de controlador de vol i motors

### Components a destacar
Entre tots els components utilitzats aquests son els més destacables:

- Raspberry Pi Zero 2 W
  
![Raspberry Pi Zero 2 W](Components/Imatges/Raspberry%20Pi%20Zero%202%20W.jpg)

- Raspberry Module V2

![Raspberry Module V2](Components/Imatges/Raspberry%20Module%20V2.jpg)

- Omnibus f4v3s plus
  
![Omnibus f4v3s plus](Components/Imatges/Omnibus%20f4v3s%20plus.jpg)

- Modul GPS GY-NEO6MV2
  
![Modul GPS GY-NEO6MV2](Components/Imatges/Modul%20GPS%20GY-NEO6MV2.jpg)

### Diagrama de fluxe
Els següents diagrames mostren les accions que pendria el nostre dron en un plantejament inicial del projecte i en la versió final.
Inicialment utilitzavem sensors de distància els quals influeixen en la trajectòria de vol, seguint el flux mostrat a continuació:

![img](https://i.imgur.com/NUjBuhI.jpeg)

Però finalment hem optat per a canviar el giroscòpi per un controlador de vol, reduïnt l'ús d'aquests sensors i obtenint aquest flux algo més simple condicionat per aquest controlador:

![img2](https://i.imgur.com/ZjItTtv.jpeg)

### Inter-connexió entre dispositius
Amb fritzing s'ha pogut crear un diagrama que representa la inter-connexió entre els nostres components de hardware. Les connexions s'han dirigit en la major mesura possible a una placa on s'han soldat els cables per crear aquestes inter-connexions que ens interessen.

![img3](https://i.imgur.com/whUJSb5.jpeg)

FC = Flight Controller

ESC = Electric Speed Controller

PWR = Positive

GND = Ground


Les connexions a seguir per a realitzar el projecte son:
- Interruptor: es connecta al PWR de la bateria. Com aquest component conmuta a la pia central, es connecta a una pia lateral i a aquesta central.
- FC: s'alimenta directament de la bateria ja que te reguladors de voltatge. Per tant, BAT del FC a PWR després de l'interruptor i GND de FC a GND de la bateria.
- Motors Brushless: PWR del motor a PWR del ESC, GND al GND del ESC i el de dades al restant. Si es vol invertir el sentit de gir del motor, es creua GND amb PWR.
- ESC: Tots els PWR de tots els ESC van directament a bateria (els nostres ESC's aguanten més de 7,4v) i després de l'interruptor, els GND a GND de bateria, i, dels tres cables prims centrals, PWR a 5 volts del FC, GND a GND del FC i el cable blanc a mX del FC (si és motor 1, doncs a m1, si és motor 2, m2...)
- GPS: GND a GND el FC, PWR a 5v del FC, Rx a TX del FC i Tx a RX del FC. En el nostre cas s'ha configurat el port UART6 per al GPS, per tant, s'utilitza a T6 i R6.
- RaspBerry: S'alimenta a partir dels 5v i GND del FC. Els pins de transmissió de dades Rx i Tx s'utilitzen com a transmissió de wifi serial al FC. Es configura el port UART1 per a aquesta funcionalitat; Rx i Tx de la RaspBerry a R1 i T1 del FC.
- Servomotor: es connecta a la RaspBerry; 5 volts, gnd i dades al pin escollit.
- Brunzidor: es connecta a la RaspBerry; 5 volts a 5 volts i GND a GND.
#
Cal destacar que s'utilitza una placa protoboard per a realitzar linies de GND i 5 volts, extrets del FC.
### Algorísmica
#### -Reconeixement de formes humanes
S'utilitza openCV per fer aquest reconeixement, per iniciar el procés, es configura la càmera amb els seus pins corresponents i es carrega un classificador de Haar. Un cop està preparat, es fa una captura continua de frames on es busquen formes humanes i si en troba, observa també la posició d'aquestes formes en respecte al centre de la imatge, també permet mostrar la imatge analitzada per una pantalla per si es vol revisar. Un cop ha acabat amb la feina, neteja els recursos utilitzats i deixa espai per propers usos.

#### -Moviment de la pinça
Es un simple moviment d'obrir i tancar la pinça, aquest moviment es fa en funció dels resultats del reconeixement de formes humanes, si es detecta una persona, la pinça s'obre i deixa caure el que porti, en cas contrari no s'obrirà.

#### -Moviment del dron
Amb mission planer s'assignen els waypoints que es vol que segueixi el dron, inclosos d'on s'enlaira i on es vol que aterri. El control d'estabilitat i la potència dels motors es farà automaticament durant el vol.
A continuació es mostra el test unitari dels motors amb les respectives hèlixs en posició òptima respecte l'aerodinàmica:

![gif1](https://i.imgur.com/eAoRxSL.gif)

[https://www.youtube.com/watch?v=jxWcWve5M-k](https://www.youtube.com/watch?v=jxWcWve5M-k)
