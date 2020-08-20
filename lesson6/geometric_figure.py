import math


class Figure:
    area = 0
    perimeter = 0

    def adder(self, other):
        if isinstance(other, Figure):
            # print("self.area", self.area, "other.area", other.area)
            return self.area + other.area
        print("Ошибка: не экземпляр класса Figure")
        return False


class Square(Figure):

    def __init__(self, a):
        self.a = a

    angels = 4
    name = "Square"

    @property
    def validate(self):
        if self.a > 0:
            return True
        print("Ошибка: отрицательное значение или 0")
        return False

    @property
    def angles_num(self):
        # print(f'angles {self.name} = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if self.validate:
            perimeter = self.a * 4
            # print(f'perimeter {self.name} =', self.perimeter)
            return perimeter

    @property
    def area(self):
        if self.validate:
            area = self.a ** 2
            # print(f'area {self.name} =', self.area)
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
    name = "Triangle"

    @property
    def validate(self):
        if min(self.a, self.b, self.c) > 0:
            if (self.a + self.c) > self.b:
                if (self.a + self.b) > self.c:
                    if (self.b + self.c) > self.a:
                        return True
            print("Ошибка: сумма длин каждых двух сторон должна быть больше длины третьей стороны")
            return False
        print("Ошибка: отрицательное значение или 0")
        return False

    @property
    def angles_num(self):
        # print(f'angles {self.name} = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if self.validate:
            perimeter = self.a + self.b + self.c
            # print(f'perimeter {self.name} =', perimeter)
            return perimeter

    @property
    def area(self):
        if self.validate:
            per = self.perimeter / 2
            area = (math.sqrt(per * (per - self.a) * (per - self.b) * (per - self.c)))
            # print(f'area {self.name} =', self.area)
            return area


class Rectangle(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    angels = 4
    name = "Rectangle"

    @property
    def validate(self):
        if self.a != self.b:
            if min(self.a, self.b) > 0:
                return True
            print("Ошибка: отрицательное значение или 0")
            return False
        print("Ошибка: стороны не могут быть равны")
        return False

    @property
    def angles_num(self):
        # print(f'angles {self.name} = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if self.validate:
            perimeter = 2 * (self.a + self.b)
            # print(f'perimeter {self.name} =', self.perimeter)
            return perimeter

    @property
    def area(self):
        if self.validate:
            area = self.a * self.b
            # print(f'area {self.name} =', self.area)
            return area


class Circle(Figure):

    def __init__(self, r):
        self.r = r

    angels = 0
    name = "Circle"

    @property
    def validate(self):
        if self.r > 0:
            return True
        print("Ошибка: отрицательное значение или 0")
        return False

    @property
    def angles_num(self):
        # print(f'angles {self.name} = {self.angels}')
        return self.angels

    @property
    def perimeter(self):
        if self.validate:
            perimeter = 2 * math.pi * self.r
            # print(f'perimeter {self.name} =', self.perimeter)
            return perimeter

    @property
    def area(self):
        if self.validate:
            area = math.pi * (self.r ** 2)
            # print(f'area {self.name} =', self.area)
            return area



if __name__ == '__main__':
    # fig1 = Square(5)
    # print(fig1.angles_num)
    # print(fig1.perimeter)
    # print(fig1.area)

    fig2 = Triangle(2, 3, 4)
    # fig2 = Triangle(2, 4, 5)

    # print(fig2.angles_num)
    # print(fig2.perimeter)
    print(fig2.area)
    # print(fig2.validate)

    # fig3 = Rectangle(6, 7)
    # print(fig3.perimeter)
    # print(fig3.area)
    # print(fig3.angles_num)
    # print(fig3.validate)

    # fig4 = Circle(10)
    # print(fig4.perimeter)
    # print(fig4.area)
    # print(fig4.angles_num)
    # print(fig4.validate)

    # print(fig1.adder(fig2))
    # print(fig2.adder(fig1))
    # print(fig1.adder(fig3))
    # print(fig3.adder(fig1))
    # print(fig2.adder(fig3))
    # print(fig3.adder(fig4))
    # print(fig4.adder(fig1))
    # print(fig2.adder(fig4))

    # raise ValueError("Ошибка: сумма длин каждых двух сторон должна быть больше длины третьей стороны")

