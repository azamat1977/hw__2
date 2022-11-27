#Repositorie name changed on hw_2
class Figure:
    def __init__(self):
        self.unit = '"Square"'
        self.width = 25
        self.length = 25

    def area_calc(self):
        return self.width*self.length

    def get_unit_area(self):
        print(f'\nFigure {self.unit} has width side is {self.width}cm, length is {self.length}cm'
            f' and square area is {self.area_calc()}cm.')


figure_unit = Figure()
figure_unit.get_unit_area()


class Circle(Figure):
    def __init__(self):
        super().__init__()
        self.unit = "'Circle'"
        self.pi = 3.1425
        self.__radius = 2

    def circle_calc_area(self):
        return self.pi*self.__radius*self.__radius

    def get_circle_info(self):
        print(f'\nFigure {self.unit} has area {self.circle_calc_area()} cm')


circle_area = Circle()
circle_area.get_circle_info()


class RightTriangle(Figure):
    def __init__(self):
        super().__init__()
        self.unit = '"Triangle"'
        self.__side_a = 5
        self.__side_b = 8
        self.area = 20

    def side_c(self):
        return self.area - (self.__side_a + self.__side_b)

    def get_triangle_info(self):
        print(f'\nFigure {self.unit} has following side measurements: side a: {self.__side_a}cm,'
        f'side b: {self.__side_b}cm and side c: {self.side_c()}cm\n'
        f'The area of the {self.unit} is {self.area}cm')


triangle_area = RightTriangle()
triangle_area.get_triangle_info()



