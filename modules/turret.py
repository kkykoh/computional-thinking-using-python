import pygame as pg
import math

# load the turret images
range_turret_1_image = pg.image.load('assets/images/range1.png').convert_alpha()
range_turret_2_image = pg.image.load('assets/images/range2.png').convert_alpha()
range_turret_3_image = pg.image.load('assets/images/range3.png').convert_alpha()
range_turret_4_image = pg.image.load('assets/images/range4.png').convert_alpha()

# the Turret class
class Turret(pg.sprite.Sprite):

    original_image = range_turret_1_image

    def __init__(self, pos, env):
        super().__init__()

        # set other constants
        self.pos = pos

        # calculate center of the image
        self.angle = 90
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.center = tuple([(x + 0.5) * env.TILE_SIZE for x in self.pos])
        self.rect = self.image.get_rect()
        self.rect.center = self.center

        # set turret type constants
        self.cooldown = 1500
        self.range = 90
        self.damage = 10
        self.cost = 50
        
        # set turret variables
        self.last_shot = pg.time.get_ticks()
        self.target = None

        self.set_range()

    def set_range(self):
        # create circle to show the range
        self.range_circle = pg.Surface((self.range*2, self.range*2))
        self.range_circle.fill((0, 0, 0))
        self.range_circle.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_circle, "white", (self.range, self.range), self.range)
        self.range_circle.set_alpha(100)
        self.range_rect = self.range_circle.get_rect()
        self.range_rect.center = self.rect.center


    def update(self, enemies):
        if self.target:
            self.reset()
        else:
            # search for a new target if the turret is idle
            if pg.time.get_ticks() - self.last_shot > self.cooldown:
                self.search_target(enemies)

    def search_target(self, enemies):
        # to be implemented in exercise
        pass

    def reset(self):
        self.last_shot = pg.time.get_ticks()
        self.target = None


    def draw(self, screen):
        self.image = pg.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        screen.blit(self.image, self.rect)
        screen.blit(self.range_circle, self.range_rect)



