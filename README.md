# AidDrop

## Continguts
- [Que és AidDrop?](#que-és-aiddrop)
- [Instal·lació del projecte](#installació-del-projecte)
- [Programari utilitzat](#programari-utilitzat)
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

### Diagrama de fluxe
El següent diagrama mostra les accions que pendria en cada cas pensat el nostre dron.


### Inter-connexió entre dispositius
Amb fritzing s'ha pogut crear un diagrama que representa la inter-connexió entre els nostres components de hardware. Les connexions s'han dirigit en la major mesura possible a una placa on s'han soldat els cables per crear aquestes inter-connexions que ens interessen.


### Algorísmica
#### -Reconeixement de formes humanes
S'utilitza openCV per fer aquest reconeixement, per iniciar el procés, es configura la càmera amb els seus pins corresponents i es carrega un classificador de Haar. Un cop està preparat, es fa una captura continua de frames on es busquen formes humanes i si en troba, observa també la posició d'aquestes formes en respecte al centre de la imatge, també permet mostrar la imatge analitzada per una pantalla per si es vol revisar. Un cop ha acabat amb la feina, neteja els recursos utilitzats i deixa espai per propers usos.

#### -Moviment de la pinça
Es un simple moviment d'obrir i tancar la pinça, aquest moviment es fa en funció dels resultats del reconeixement de formes humanes, si es detecta una persona, la pinça s'obre i deixa caure el que porti, en cas contrari no s'obrirà.

#### -Moviment del dron
Amb mission planer s'assignen els waypoints que es vol que segueixi el dron, inclosos d'on s'enlaira i on es vol que aterri. El control d'estabilitat i la potència dels motors es farà automaticament durant el vol.
