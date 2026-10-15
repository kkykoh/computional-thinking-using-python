import pygame as pg

# the Button class
class Button():

    def __init__(self, pos, image, single_click, font, text):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.clicked = False
        self.single_click = single_click

        self.text = font.render(text, True, "black")

    def draw(self, screen):
        mouseover = False
        # get the mouse position
        mouse_pos = pg.mouse.get_pos()

        # check mouseover and click conditions
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                mouseover = True
                if self.single_click:
                    self.clicked = True
        
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw the button
        screen.blit(self.image, self.rect)

        # draw the font
        screen.blit(self.text, (self.rect.centerx + 50, self.rect.centery))

        return mouseover
