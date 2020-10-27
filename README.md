# Robot Operating System
Guy-Vianney Krakowiak, Baptiste Marlet, Alexandre


### 2.1.1. Comprendre le descripteur URDF
##### Que representent les rectangles
Les rectangles representent les ros topics, sections.
##### Que representent les bulles
Les bulles representent les noeud (moteurs).
##### Que représentent les flèches et surtout les valeurs xyz et rpy associées ?
Ce sont les topics ros. Les valeurs xyz sont les valeurs de mouvements demande au moteur dans les axes x,y et z, et rpy sont des valeurs d'angles de rotations autour d'axes.

### 2.1.2.a. Topics du robot
##### Quel est son nom ?
Le nom du topic est joint_states
##### Quel est le type de message qu'il transmet ?
Le type est sensor_msg/JoinState
##### A quelle fréquence (en Hertz) est-ce qu'il met à jour l'état des joints ?
Average rate : 29,9 Hz

### 2.1.2.a. Topics du robot
##### Quel est son nom ?
set_compliant
##### Quel est le type de service qu'il transmet ?
std_rvs/SetBool
##### Quels sont les champs de la requête de ce service ?
Argument Data, un booleen. Pour appeler rosservice call, il faut mettre 0 ou 1.
##### Quels sont les champs de la réponse de ce service ?
Un String indiquant la reussite ou l'echec et un booleen 0 ou 1.
##### Appelez ce service pour activer et désactiver le mode compliant et essayer de faire bouger votre robot à la main à chaque fois. Que déduisez-vous de la signification du mode compliant ?
Le mode compliant permet de bouger le robot a la main sans resistance.

### 2.2.2. Planification
##### Que désigne le robot gris parfois mobile mais lent ?
Le robot gris designe le robot dans sa position actuelle.
##### Que désigne le robot orange (fixe) ?
Le robot orange est dans la position d'arrive apres le mouvement prevu.
##### Que désigne le robot gris qui répète infiniment un mouvement rapide ?
Le mouvement que le robot va faire lorsque on execute le plan.
##### Dans RViz, activer l'affichage du modèle de collision dans Displays, Scene Robot, Show Robot Collision, quelle est la forme de ce modèle utilisé par OMPL pour simplifier le calcul des collisions ?
Des formes cylndriques

### 2.2.3. Planning groups
##### Quelle est la différence entre ces 2 groupes ?
Dans arm on manipule le bras mais la pince reste immobile. dans arm and finger, nous pouvons manipuler la pince.
##### Quel est le groupe pour lequel le goal est le plus facilement manipulable et pourquoi ?
Le plus facilement manipulable est arm and finger.
##### Déduisez-en ce que désigne exactement un planning group
C'est un ensemble de moteurs que l'on peux deplacer ensemble en deplacant le goal.

### 2.2.4. Transformations tf
##### Comment est nommé le repère de base ?
Base link
##### Comment sont nommés les deux effecteurs finaux possibles ?
moving tip et fixed tip
##### Avec rosrun tf tf_echo, déterminez quelle est la position actuel d'un effecteur dans le repère de base. Ses coordonnées peuvent vous servir pour les définir comme cible à atteindre par la suite.


![Simulation d'obstacle](/IMG/obstacle.png)
