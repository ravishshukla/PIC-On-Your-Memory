import os
import random
import game_config as gc
from pygame import image, transform

animals_count=dict((a,0) for a in gc.ASSET_FILES) # this initially set value 0 for all the keys, the keys beign our asset files

def available_animals():
    return [a for a, c in animals_count.items() if c < 2]

class Animal:
    def __init__(self,index): # index in the num of tiles we want
        self.index = index
        self.row = index // gc.NUM_TILES_SIDE    # if no. of  tiles(index)=4 then no. of roww= 4/(nu of tiles on each side we want here it is = 4)= 4/4=1
        self.col = index %gc.NUM_TILES_SIDE # changes Row whenever a div by 4 is reached eg:   0 1 2 3
                                                                                           #   4 5 6 7
                                                                                          #    8 9 10 11
                                                                                          #    .........
        self.name = random.choice(available_animals())
        animals_count[self.name] += 1

        self.image_path = os.path.join(gc.ASSET_DIR, self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN,gc.IMAGE_SIZE - 2*gc.MARGIN)) #Remove the margins while considering the image size
        self.box = self.image.copy() #make copy of this image
        self.box.fill((200, 200, 200)) #fill method to gray it out
        self.skip = False #  If its set to True then the imaage of that instance will not be used in the game board

