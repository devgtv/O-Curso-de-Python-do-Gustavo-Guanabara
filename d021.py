# Faça um programa em Python que abra e reproduza um áudio MP3.

import pygame
pygame.init()
pygame.mixer.music.load('Ex01.mp3')
pygame.mixer.music.play()
pygame.event.wait()