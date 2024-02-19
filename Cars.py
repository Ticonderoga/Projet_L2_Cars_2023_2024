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
VELOCITY = 3
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

taxi_img = pygame.image.load("./Taxi.png")
rock_img = pygame.image.load("./Taxi.png")

class Voiture(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = taxi_img
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.angle = 0

    def draw(self):
        screen.blit(self.image, self.rect)

    def rotate(self, sens=1):
        self.angle = self.angle + 0.5 * sens
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

class Obstacle(pygame.sprite.Sprite) :
    def __init__(self,x = WIDTH//3, y = 0) :
        super().__init__()
        self.x = x
        self.y = y
        
        self.image = rock_img
        self.origin_image = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.velocity = VELOCITY
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self):
        """
        méthode permettant d'afficher l'image à l'écran

        """
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.x = self.rect.x 
        self.rect.y = self.rect.y + VELOCITY

        # permet de supprimer l'obstacle si l'on sort de l'écran
        if not screen.get_rect().contains(self.rect):
            self.remove()
            self.kill()
        screen.blit(self.image, self.rect)
    
        

        
        

if __name__ == "__main__":
    frame_count = 0
    running = True
    taxi = Voiture(WIDTH //2, HEIGHT // 2)
    obs = Obstacle()
    while running:
        # Level creation
        frame_count = frame_count+ 1
        screen.fill(colors[0])
        taxi.draw()

        # Gestion des entrées au clavier
        for event in pygame.event.get():
            # Handle the closing
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                keypressed = event.key
                if keypressed == pygame.K_SPACE:
                    print("space bar")
                    
                    # proj = Projectile(player.x, player.y, player.angle)
            else:
                keypressed = 0
        if keypressed == pygame.K_RIGHT:
            print('a droite')
            taxi.rotate(-1)

        elif keypressed == pygame.K_LEFT:
            print('a gauche')
            taxi.rotate(1)

        obs.draw()
        pygame.display.flip()
        clock.tick(FPS)
