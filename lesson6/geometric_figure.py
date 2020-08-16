import math


class Figure:
    area = 0
    perimeter = 0


class Square(Figure):

    def __init__(self, a):
        self.a = a

    angels = 4
    name = "квадрат"

    def angles_num(self):
        print(f'Количество углов {self.name}а = {self.angels}')
        return self.angels

    def area_square(self):
        if self.a > 0:
            self.area = self.a ** 2
            print(f'площадь {self.name}а =', self.area)
            return self.area

    def perimeter_square(self):
        if self.a > 0:
            self.perimeter = self.a * 4
            print(f'периметр {self.name}а =', self.perimeter)
            return self.perimeter

    @property
    def increase_sum(self):
        return self.a * 10


# fig = Square(6)
# fig.angles_num()
# fig.area_square()
# fig.perimeter_square()


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    angels = 3
    name = "треугольник"

    def angles_num(self):
        print(f'Количество углов {self.name}а = {self.angels}')

    def perimeter_triangle(self):
        if self.a and self.b and self.c > 0:
            self.perimeter = self.a + self.b + self.c
            print(f'периметр {self.name}а =', self.perimeter)
            return self.perimeter / 2

    def area_triangle(self):
        if self.a and self.b and self.c > 0:
            per = self.perimeter_triangle()
            self.area = per * (math.sqrt((per - self.a) * (per - self.b) * (per - self.c)))
            print(f'площадь {self.name}а =', self.area)
            return self.area


# fig_triangle = Triangle(3, 4, 5)
# fig_triangle.angles_num()
# fig_triangle.perimeter_triangle()
# fig_triangle.area_triangle()


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    angels = 4
    name = "прямоугольник"

    def angles_num(self):
        print(f'Количество углов {self.name}а = {self.angels}')

    def perimeter_rectangle(self):
        if self.a and self.b > 0:
            self.perimeter = 2 * (self.a + self.b)
            print(f'периметр {self.name}а =', self.perimeter)

    def area_rectangle(self):
        if self.a and self.b > 0:
            self.area = self.a * self.b
            print(f'площадь {self.name}а =', self.area)
            return self.area


# fig_rectangle = Rectangle(3, 4)
# fig_rectangle.angles_num()
# fig_rectangle.perimeter_rectangle()
# fig_rectangle.area_rectangle()


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    angels = 0
    name = "круг"

    def angles_num(self):
        print(f'Количество углов {self.name}а = {self.angels}')

    def perimeter_circle(self):
        if self.r > 0:
            self.perimeter = 2 * math.pi * self.r
            print(f'периметр {self.name}а =', self.perimeter)

    def area_circle(self):
        if self.r > 0:
            self.area = math.pi * (self.r ** 2)
            print(f'площадь {self.name}а =', self.area)
            return self.area

    def add_square(self, area_other):
        # добавить условие, если это не геометрическая фигура, то выдать ошибку, что передан неправильный класс
        summ_area = self.area_circle() + area_other
        print("Сумма площадей = ", summ_area)

#
# fig_circle = Circle(3)
# fig_circle.angles_num()
# fig_circle.perimeter_circle()
# fig_circle.area_circle()
#fig_circle.add_square(fig_rectangle.area_rectangle())