class Ship(object):
    """docstring for Ship"""
    def __init__(self, level):
        self.level = level
        self.strikes = level

    def make_shot(self):
        self.strikes -= 1

        return not bool(self.strikes)







