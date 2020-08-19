import math


class Figure:
    area = 0
    perimeter = 0

    def adder(self, other):
        if isinstance(other, Figure):
            print("self.area", self.area, "other.area_func", other.area)
            return self.area + other.area
        print("Ошибка")


class Square(Figure):

    def __init__(self, a):
        self.a = a

    angels = 4
    name = "квадрат"

    @property
    def angles_num(self):
        # print(f'Количество углов {self.name}а = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if self.a > 0:
            perimeter = self.a * 4
            # print(f'периметр {self.name}а =', self.perimeter)
            return perimeter

    @property
    def area(self):
        if self.a > 0:
            area = self.a ** 2
            # print(f'площадь {self.name}а =', self.area)
            return area

# @property
# def increase_sum(self):
#     return self.a * 10


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    angels = 3
    name = "треугольник"

    # def validate(self):
    #     if min(self.a, self.b, self.c) > 0:
    #         if self.a + self.b > self.c:
    #             pass
    #         elif self.a + self.c > self.b:
    #             pass
    #         elif self.b + self.c > self.a:
    #             pass
    #         raise ValueError("Ошибка: сумма длин каждых двух сторон должна быть больше длины третьей стороны")
    #     raise ValueError("Ошибка, отрицательное значение или 0")

    @property
    def angles_num(self):
        # print(f'Количество углов {self.name}а = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if min(self.a, self.b, self.c) > 0:
            perimeter = self.a + self.b + self.c
            # print(f'периметр {self.name}а =', perimeter)
            return perimeter

    @property
    def area(self):
        if min(self.a, self.b, self.c) > 0:
            per = self.perimeter / 2
            area = (math.sqrt(per * (per - self.a) * (per - self.b) * (per - self.c)))
            # print(f'площадь {self.name}а =', self.area)
            return area


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    angels = 4
    name = "прямоугольник"

    # def validate(self):
    #     if self.a == self.b:
    #         print("Ошибка: стороны не должны быть равны")

    @property
    def angles_num(self):
        # print(f'Количество углов {self.name}а = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if min(self.a, self.b) > 0:
            self.perimeter = 2 * (self.a + self.b)
            # print(f'периметр {self.name}а =', self.perimeter)
            return self.perimeter

    @property
    def area(self):
        if min(self.a, self.b) > 0:
            area = self.a * self.b
            # print(f'площадь {self.name}а =', self.area)
            return area


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    angels = 0
    name = "круг"

    @property
    def angles_num(self):
        print(f'Количество углов {self.name}а = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if self.r > 0:
            perimeter = 2 * math.pi * self.r
            # print(f'периметр {self.name}а =', self.perimeter)
            return perimeter

    @property
    def area(self):
        if self.r > 0:
            area = math.pi * (self.r ** 2)
            # print(f'площадь {self.name}а =', self.area)
            return area

#     def add_square(self, area_other):
#         # добавить условие, если это не геометрическая фигура, то выдать ошибку, что передан неправильный класс
#         summ_area = self.area_circle() + area_other
#         print("Сумма площадей = ", summ_area)


if __name__ == '__main__':
    fig1 = Square(5)
    # print(fig1.angles_num)
    # print(fig1.perimeter_func)
    print(fig1.area)

    fig2 = Triangle(5, 4, 3)
    #fig2 = Triangle(6, 3, 4)

    # print(fig2.angles_num)
    # print(fig2.perimeter_func)
    print(fig2.area)

    fig3 = Rectangle(5, 6)
    # print(fig3.perimeter_func)
    # print(fig3.area_func)
    # print(fig3.angles_num)

    fig4 = Circle(5)
    # print(fig4.perimeter_func)
    # print(fig4.area_func)
    # print(fig4.angles_num)

    print(fig1.adder(fig2))
    print(fig2.adder(fig1))
    print(fig3.adder(fig1))
    print(fig2.adder(fig3))
    print(fig4.adder(fig1))
    print(fig2.adder(fig4))
