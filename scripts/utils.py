import os
import pygame

# quick function to load img quickly
def load_img(path, colorkey=None, alpha=True):
    img = pygame.image.load(path).convert() if not alpha else pygame.image.load(path).convert_alpha()
    img.set_colorkey(colorkey)
    return img

# function to load images from a directory into a list of imgs (Surface)
def load_imgs(path, colorkey=None, alpha=True):
    imgs_list = []
    for img_file in os.listdir(path):
        img_path = path + '/' + img_file
        img = pygame.image.load(img_path).convert() if not alpha else pygame.image.load(img_path).convert_alpha()
        img.set_colorkey(colorkey)
        imgs_list.append(img)
    return imgs_list

