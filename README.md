# Projet L2 Cars 2023-2024

## Mise en place de la route.

* c'est la route qui défile et pas la voiture. 
  
  * Il faut mettre en place un vertical scrolling
    * Des possibilités  [ici](http://www.google.com/search?q=vertical+scrollling+pygame)
    * des exemples de code :
      * [Geeksforgeeks](https://www.geeksforgeeks.org/creating-a-scrolling-background-in-pygame/)
      * [TechwithTim](https://www.techwithtim.net/tutorials/game-development-with-python/side-scroller-pygame/background)
      * [basic example](https://stackoverflow.com/questions/17240442/how-to-make-the-background-continuously-scrolling-with-pygame)
  * c'est un jeu d'images qui sont placées en fond
  
    * Au minimum 2 images en même temps (haut et bas)
  
* Collision avec la route
  
  * Les collisions dans Pygame sont entre des rect -> Pb avec la route
  
  * Pour gérer une collision au pixel il faut faire des [mask](https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_mask.md) 
  
  * Les images doivent être préparées en amont avec les masks
  
  
## Des obstacles qui descendent verticalement

* Plus facile à gérer au niveau des collisions
* Chaque objet peut avoir des mouvements spécifiques
* Ca devient plus lourd avec plusieurs objets et le jeu n'est plus le même