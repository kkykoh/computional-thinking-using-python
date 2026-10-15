import pygame as pg

# the Environment class
class Environment:

    def __init__(self, data, image):
        self.junctions = []
        self.image = image
        self.all_data = data

        # metadata
        self.FPS = 60
        self.SIDE = 300
        
        # enemy metadata
        self.SPAWN_COOLDOWN = 400

        # world metadata
        self.life = 3
        self.money = 100

        # changeable variables
        self.placable = False
        self.place_type = None
        self.last_spawn = pg.time.get_ticks()

    def pre_process(self):
        # set constants
        self.ROWS, self.COLS = self.all_data["height"], self.all_data["width"]
        self.TILE_SIZE = self.all_data["tileheight"]
        self.WIDTH = self.ROWS * self.TILE_SIZE
        self.HEIGHT = self.COLS * self.TILE_SIZE

        # set junctions
        for layer in self.all_data["layers"]:
            if layer["name"] == "junctions":
                for obj in layer["objects"]:
                    junction_data = obj["polyline"]
                    for pt in junction_data:
                        self.junctions.append((obj["x"]+pt["x"], obj["y"]+pt["y"]))
    
    def draw(self, screen):
        # draw the environment
        screen.blit(self.image, (0, 0))

    def reset(self):
        self.life = 3
        self.money = 100
        self.placable = False
        self.place_type = None
        self.last_spawn = pg.time.get_ticks()
