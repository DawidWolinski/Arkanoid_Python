from Brick import Brick


# Used for better visualisation of level layouts (in return_layout() function)
class WrapperClass():
    def __init__(self):
        self.value = 100

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)


class LevelCreator:
    def __init__(self):
        self.level_number = 0
        # There are 4 backgrounds, they repeat every 4 levels
        self.number_of_backgrounds = 4
        self.background_rect = []
        self.hp_rect = []
        self.set_rects()
        self.golden_bricks = 0

    # Sets rects of backgrounds and hp images
    def set_rects(self):
        width = 224*3
        height = 240*3
        distance_x = 8*3

        for i in range(self.number_of_backgrounds):
            self.background_rect.append((i*(width + distance_x), 0, width, height))

        hp_width = 16*3
        hp_height = 8*3
        for i in range(self.number_of_backgrounds):
            self.hp_rect.append((i*(width + distance_x)+distance_x, height, hp_width, hp_height))

    def get_background_rect(self, level_number):
        return self.background_rect[level_number % self.number_of_backgrounds]

    def get_hp_rect(self, level_number):
        return self.hp_rect[level_number % self.number_of_backgrounds]

    # Returns list of bricks for each level
    def create_level(self, level_number):
        layout = self.return_layout(level_number)
        bricks = []
        self.golden_bricks = 0

        # Based on layout creates a list of bricks
        if len(layout) > 0 and len(layout) % 13 == 0:
            rows = len(layout)/13
            for i in range(int(rows)):
                for j in range(13):
                    if layout[i*13 + j] != 100:
                        bricks.append(Brick(layout[i*13 + j], (j*16 + 8)*3, (i*8 + 24)*3))
                        if layout[i*13 + j] == 9:
                            self.golden_bricks = self.golden_bricks + 1

        return bricks

    # Returns brick layout of each level with their types and positions
    # They are visual representation of each level inside a code
    def return_layout(self, level_number):
        layout = []

        # Each number denotes specific brick type
        # Row and column represent position of the brick
        # '_' denotes empty space (I had to use wrapper class since all one-digit numbers are already in use)
        _ = WrapperClass()

        if level_number == 0:
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8 ])
            layout.extend([ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4 ])
            layout.extend([ 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7 ])
            layout.extend([ 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ])
            layout.extend([ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6 ])
            layout.extend([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ])

        elif level_number == 1:
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, _, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, 7, _, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, 7, 0, _, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, _, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, _, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, _ ])
            layout.extend([ 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3, _ ])
            layout.extend([ 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4 ])

        elif level_number == 2:
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 5, 5, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 2, 2, 2 ])

        elif level_number == 3:
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, 1, 2, 3, 8, 5, _, 7, 0, 1, 2, 3, _ ])
            layout.extend([ _, 2, 3, 8, 5, 6, _, 0, 1, 2, 3, 8, _ ])
            layout.extend([ _, 3, 8, 5, 6, 7, _, 1, 2, 3, 8, 5, _ ])
            layout.extend([ _, 8, 5, 6, 7, 0, _, 2, 3, 8, 5, 6, _ ])
            layout.extend([ _, 5, 6, 7, 0, 1, _, 3, 8, 5, 6, 7, _ ])
            layout.extend([ _, 6, 7, 0, 1, 2, _, 8, 5, 6, 7, 0, _ ])
            layout.extend([ _, 7, 0, 1, 2, 3, _, 5, 6, 7, 0, 1, _ ])
            layout.extend([ _, 0, 1, 2, 3, 8, _, 6, 7, 0, 1, 2, _ ])
            layout.extend([ _, 1, 2, 3, 8, 5, _, 7, 0, 1, 2, 3, _ ])
            layout.extend([ _, 2, 3, 8, 5, 6, _, 0, 1, 2, 3, 8, _ ])
            layout.extend([ _, 3, 8, 5, 6, 7, _, 1, 2, 3, 8, 5, _ ])
            layout.extend([ _, 8, 5, 6, 7, 0, _, 2, 3, 8, 5, 6, _ ])
            layout.extend([ _, 5, 6, 7, 0, 1, _, 3, 8, 5, 6, 7, _ ])
            layout.extend([ _, 6, 7, 0, 1, 2, _, 8, 5, 6, 7, 0, _ ])

        elif level_number == 4:
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, _, _, _, _, _, _, _, _, _, _ ])
            layout.extend([ _, _, _, 7, _, _, _, _, _, 7, _, _, _ ])
            layout.extend([ _, _, _, 7, _, _, _, _, _, 7, _, _, _ ])
            layout.extend([ _, _, _, _, 7, _, _, _, 7, _, _, _, _ ])
            layout.extend([ _, _, _, _, 7, _, _, _, 7, _, _, _, _ ])
            layout.extend([ _, _, _, 8, 8, 8, 8, 8, 8, 8, _, _, _ ])
            layout.extend([ _, _, _, 8, 8, 8, 8, 8, 8, 8, _, _, _ ])
            layout.extend([ _, _, 8, 8, 4, 8, 8, 8, 4, 8, 8, _, _ ])
            layout.extend([ _, _, 8, 8, 4, 8, 8, 8, 4, 8, 8, _, _ ])
            layout.extend([ _, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, _ ])
            layout.extend([ _, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, _ ])
            layout.extend([ _, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, _ ])
            layout.extend([ _, 8, _, 8, 8, 8, 8, 8, 8, 8, _, 8, _ ])
            layout.extend([ _, 8, _, 8, _, _, _, _, _, 8, _, 8, _ ])
            layout.extend([ _, 8, _, 8, _, _, _, _, _, 8, _, 8, _ ])
            layout.extend([ _, _, _, _, 8, 8, _, 8, 8, _, _, _, _ ])
            layout.extend([ _, _, _, _, 8, 8, _, 8, 8, _, _, _, _ ])

        return layout
