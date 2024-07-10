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
El flux principal del robot consisteix en una sèrie de moviments/desplaçaments, ja siguin horitzontals o verticals, que mouen el dron d'una posició Origen a una posició Destí. S'efectua un reconeixement de persones per deixar un objecte mèdic a la ubicació objectiu i es torna a la posició Origen.

La idea principal era utilitzar la placa Arduino Nano com a controladora de vol juntament amb el giroscopi i els sensors de distància. En cada moviment efectuat pel dron, es comprovaria si hi ha hagut cap variació no esperada en l'eix del dron per tal de corregir-la. S'esquiven els possibles obstacles que es detectin en cada tram.

En arribar al destí (amb comprovacions periòdiques amb el GPS), es busca una persona i, si es troba, es deixa caure un objecte mèdic. Finalment, es torna a la ubicació inicial determinada pel GPS i s'aterrarà.

El diagrama de flux de la idea principal i general del programa que s'acaba de comentar és el següent:


![img](https://i.imgur.com/NUjBuhI.jpeg)


Degut al curt període per a l'entrega, s'utilitza un controlador de vol en comptes de la placa Arduino Nano i el giroscopi, ometent la part dels sensors de distància per modificar la trajectòria lleugerament en cas d'un obstacle imminent. El flux principal del robot ara no consta de sensors, i les comprovacions periòdiques de l'estabilitat del dron es controlen de manera automatitzada.

Aquest seria el diagrama de flux del projecte realitzat finalment:


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
- GPS: GND a GND el FC, PWR a 5v del FC, Rx a TX del FC i Tx a RX del FC. En el nostre cas s'ha configurat el port UART6 per al GPS, per tant, s'utilitza T6 i R6.
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
El moviment del drone ha estat programat mitjançant mission planner, que és un software de planificació i control de vol. Aquest programa preoveix d'eines tant pel moviment del drone, indicant al FC com ha de reaccionar en tot moment en funció de tots els inputs que rebi durant la missió, com per les probes unitaries dels diferents components del drone.
#
###### -Probes unitaries:
- GPS: Al connectar el controlador de vol a mission planner es pot comprovar que les posicions llegides pel GPS eren correctes mitjançant el mapa integrat que té l'aplicació.
- Motors: Hem realitzat probes de motors amb l'objectiu de  poder orientar correctament la seva rotació i la seva distribució acord amb el frimeware instal·lat al FC, evitant possibles errors de hardware que poguessin comprometre l' integritat del drone.
 # 
 ###### -Pla de vol

- Etapes de vol: Les etapes de vol utilitzades en aquest projecte son: 
    - Enlairament: Etapa on el dorne inicia els motors i s'eleva a una alçada especifica proporcionada prèviament per l'usuari
    - Desplaçament a desti: El drone es mou en linea recta fins a la coordenada indicada com a destí
    - Desplaçament circular: Sobre un punt es realitza un recorregut circular de radi indicat per l'usuari amb l'objectiu de reconeixer una figura humana.
    - Desplaçament a origen: Un cop finalitzada la ultima etapa el drone tornara en linea recta fins al punt on ha realitzat l'enlairament i aterrarà 
- Simulació: Aquesta eina permet poder visualitzar el resultat esperat alhora de programar una missió sense necessitat de realitzar un vol real.

#

![gif1](https://i.imgur.com/eAoRxSL.gif)

[https://www.youtube.com/watch?v=jxWcWve5M-k](https://www.youtube.com/watch?v=jxWcWve5M-k)
