import pygame as pg
from pygame.math import Vector2

# the Enemy class
class Enemy(pg.sprite.Sprite):

    def __init__(self, junctions, image):
        super().__init__()

        # set other constants
        self.image = image
        self.junctions = junctions
        self.pos = Vector2(self.junctions[0])
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.target_junction = 1 # the next junction to move to

        # set target data
        self.health = 50
        self.speed = 0.5
        self.bounty = 25

    def update(self, env):
        self.move(env)
        self.check_alive(env)

    def move(self, env):
        # look for target waypoint
        if self.target_junction < len(self.junctions):
            self.target = Vector2(self.junctions[self.target_junction])
            direction = self.target - self.pos

            # move towards target
            distance = direction.length()
            # if the distance is more than the speed, move
            if distance >= self.speed:
                self.pos += direction.normalize() * self.speed
            else:
                # if the distance is less than the speed, move to the next target
                if distance > 0:
                    self.pos += direction.normalize() * distance
                self.target_junction += 1

            # update the position of the sprite
            self.rect.center = self.pos

        else:
            # if there are no more targets, stop moving
            env.life -= 1
            self.kill()

    def check_alive(self, env):
        if self.health <= 0:
            env.money += self.bounty
            self.kill()
