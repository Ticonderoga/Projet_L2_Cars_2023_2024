#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:00:13 2023

@author: phil
"""

import pygame
from math import cos, sin, pi
from random import randint

pygame.init()  # Initialise pygame

# Permet de gérer la vitesse du jeu
clock = pygame.time.Clock()
FPS = 60

# pygame.display Permet de nommer la fenetre, voir ses dimensions, parametres d'initialisation
pygame.display.set_caption("Drift")
HEIGHT = 920
WIDTH = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

colors = [
    "#8FBCBB",
    "#88C0D0",
    "#81A1C1",
    "#5E81AC",
    "#BF616A",
    "#D08770",
    "#EBCB8B",
    "#A3BE8C",
    "#B48EAD",
]

# Les images utilisées dans le jeu
# player_img = pygame.image.load("./Player_small.png")
# arrow_img = pygame.image.load("./arrow.png")
# target_img = pygame.image.load("./target.png")


# class Player(pygame.sprite.Sprite):
#     def __init__(self, x=0, y=0):
#         super().__init__()
#         self.image = player_img
#         self.origin_image = self.image
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.centerx = self.x
#         self.rect.centery = self.y
#         self.angle = 0

#     def draw(self):
#         screen.blit(self.image, self.rect)

#     def rotate(self, sens=1):
#         self.angle = self.angle + 0.5 * sens
#         self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
#         self.rect = self.image.get_rect(center=self.rect.center)


# class Projectile(pygame.sprite.Sprite):
#     """
#     Classe qui simule le trajet d'un projectile, il faut donc sa position en x,y ainsi que son angle de rotation.
#     Par contre sa vitesse est fixée dans le code
#     """

#     def __init__(self, x, y, angle):
#         super().__init__()
#         self.image = arrow_img
#         self.origin_image = self.image
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.centerx = self.x
#         self.rect.centery = self.y
#         self.angle = angle
#         self.velocity = 20
#         self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
#         self.rect = self.image.get_rect(center=self.rect.center)

#     def move(self):
#         """
#         méthode permettant de déplacer la flèche

#         """
#         velocity_x = cos(self.angle * pi / 180) * self.velocity
#         velocity_y = sin(self.angle * pi / 180) * self.velocity
#         self.rect.x = self.rect.x + velocity_x
#         self.rect.y = self.rect.y - velocity_y

#         # permet de supprimer la flèche si l'on sort de l'écran
#         if not screen.get_rect().contains(self.rect):
#             self.remove()
#             self.kill()
#             shoot = False
#         self.draw()

#     def draw(self):
#         """
#         méthode permettant d'afficher l'image à l'écran

#         """
#         screen.blit(self.image, self.rect)

#     def update(self, ang_rotation):
#         """
#         méthode permettant de tourner la flèche selon un certain angle

#         Parameters
#         ----------
#         ang_rotation : float
#             angle de rotation.

#         """
#         self.image = pygame.transform.rotozoom(self.origin_image, self.angle + ang_rotation, 1)
#         self.rect = self.image.get_rect(center=self.rect.center)
#         self.angle = self.angle + ang_rotation


# class Layer:
#     """
#     Classe permettant de créer un couche qui va dévier la flèche, la valeur deflect correspond
#     à l'angle de déviation.
#     """

#     def __init__(self, left=200, top=0, width=200, height=HEIGHT, color=colors[6], deflect=0):
        
#         self.left = left
#         self.top = top
#         self.width = width
#         self.height = height
#         self.color = color
#         self.rect = pygame.draw.rect(screen, color, [left, top, width, height], width=0)
#         self.deflect = deflect

#     def draw(self):
#         pygame.draw.rect(screen, self.color, [self.left, self.top, self.width, self.height], width=0)

#     def move(self):
#         self.left = self.left + 5 * sin(frame_count/30)
#         self.rect.left = self.left

# class Target(pygame.sprite.Sprite):
#     def __init__(self, x=0, y=0):
#         super().__init__()
#         self.image = target_img
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.centerx = self.x
#         self.rect.centery = self.y

#     def draw(self):
#         screen.blit(self.image, self.rect)

if __name__ == "__main__":
    frame_count = 0
    # player = Player(50, HEIGHT // 2)
    # target = Target(WIDTH - (50 + randint(0, 100)), randint(50, HEIGHT - 50))
    # shoot = False
    running = True
    # layer1 = Layer(width=50, deflect=4)
    # layer2 = Layer(left=400, color=colors[5], deflect=-5)
    # layers = [layer1, layer2]
    while running:
        # Level creation
        frame_count = frame_count+ 1
        screen.fill(colors[0])
        # for layer in layers :
        #     layer.draw()
        
        # player.draw()
        # target.draw()

        # Gestion des entrées au clavier
        for event in pygame.event.get():
            # Handle the closing
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                keypressed = event.key
                if keypressed == pygame.K_SPACE:
                    print("space bar")
                elif keypressed == pygame.K_RIGHT:
                    print('a droite')
                elif keypressed == pygame.K_LEFT:
                    print('a gauche')
                    
                    # proj = Projectile(player.x, player.y, player.angle)
            else:
                keypressed = 0

        # Pour K_RIGHT ou K_LEFT on peut laisser la touche enfoncée
        # if keypressed == pygame.K_RIGHT:
        #     player.rotate(1)
        # elif keypressed == pygame.K_LEFT:
        #     player.rotate(-1)

        # On tire un projectile et vérifier si il traverse une couche (layer)
        # if shoot:
        #     proj.move()
        #     for layer in layers:
        #         if layer.rect.collidepoint(proj.rect.centerx, proj.rect.centery):
        #             proj.update(layer.deflect)
        #     if target.rect.collidepoint(proj.rect.centerx, proj.rect.centery):
        #         print("Gagné")
        #         pygame.quit()
        #     else :
        #         layer2.move()
                
        pygame.display.flip()
        clock.tick(FPS)
