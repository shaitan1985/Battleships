class Game(object):

    def __init__(self):
        self.menu = some_menu()
        self.field = Field()
        self.coords = self.field.get_new_coords()


    def draw_all(self):
        #отрисовать меню

        self.field.draw_field()



    def make_shot(self, coord):

        ship = self.field.make_shot(coord)

        killed = ship.make_shot()

        #change counts

    def start(self):


        while self.coords:

            draw_all()

            choice = input('Введите x,y: ').replace(" ").split(',')
            choice.make_shot()
            self.field.make_shot(self.coords.get(choice), choice)

