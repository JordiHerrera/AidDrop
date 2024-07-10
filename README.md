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
Carregar el fitxer cam2.py a la raspberry pi.
Assegurar-se de tenir totes les llibreries necessaries.

### Programari utilitzat
- Fritzing
- PyCharm: Edició de codi Python
- Arduino IDE: Edició de codi Arduino
- opencv / cv2: Processament d'imatges.
- pyzbar: Lectura de codis de barres i QR.
- Blender: Modelatge 3D

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


### Algorísmica
#### -Reconeixement de formes humanes
S'utilitza openCV per fer aquest reconeixement, per iniciar el procés, es configura la càmera amb els seus pins corresponents i es carrega un classificador de Haar. Un cop està preparat, es fa una captura continua de frames on es busquen formes humanes i si en troba, observa també la posició d'aquestes formes en respecte al centre de la imatge, també permet mostrar la imatge analitzada per una pantalla per si es vol revisar. Un cop ha acabat amb la feina, neteja els recursos utilitzats i deixa espai per propers usos.

#### -Moviment de la pinça
Es un simple moviment d'obrir i tancar la pinça, aquest moviment es fa en funció dels resultats del reconeixement de formes humanes, si es detecta una persona, la pinça s'obre i deixa caure el que porti, en cas contrari no s'obrirà.

#### -Moviment del dron
Amb mission planer s'assignen els waypoints que es vol que segueixi el dron, inclosos d'on s'enlaira i on es vol que aterri. El control d'estabilitat i la potència dels motors es farà automaticament durant el vol.
A continuació es mostra el test unitari dels motors amb les respectives hèlixs en posició òptima respecte l'aerodinàmica:

![gif1](https://i.imgur.com/eAoRxSL.gif)
