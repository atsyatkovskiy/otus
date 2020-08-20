from lesson6.geometric_figure import Figure, Square, Triangle, Rectangle, Circle
import pytest
import math


class TestsSquare:

    # проверка на кол-во углов Square
    @pytest.mark.parametrize("value_a", argvalues=[5])
    def test_square_angles_num(self, value_a):
        square = Square(value_a)
        assert square.angles_num == 4

    # проверка атрибута name Square
    @pytest.mark.parametrize("value_a", argvalues=[9])
    def test_square_name(self, value_a):
        square = Square(value_a)
        assert square.name == "Square"

    # проверка на валидность значения стороны Square
    @pytest.mark.parametrize("value_a", argvalues=[0, -5, -88])
    def test_square_validate(self, value_a):
        square = Square(value_a)
        assert False == square.validate

    # проверка расчета периметра Square
    @pytest.mark.parametrize("value_a", argvalues=[3, 5, 12])
    def test_square_perimeter(self, value_a):
        square = Square(value_a)
        perimeter = value_a * 4
        assert square.perimeter == perimeter

    # проверка расчета площади Square
    @pytest.mark.parametrize("value_a", argvalues=[5, 22, 101])
    def test_square_area(self, value_a):
        square = Square(value_a)
        area = value_a ** 2
        assert square.area == area

    # проверка расчета сумм площадей Square и Triangle
    # проверка на экземпляр класса
    @pytest.mark.parametrize("value_a", argvalues=[9, 4])
    @pytest.mark.parametrize("value_b", argvalues=[3, 6])
    @pytest.mark.parametrize("value_c", argvalues=[6, 5])
    @pytest.mark.parametrize("value_d", argvalues=[5, 7])
    def test_square_area_adder(self, value_a, value_b, value_c, value_d):
        square = Square(value_a)
        area_s = value_a ** 2

        triangle = Triangle(value_b, value_c, value_d)
        per = (value_b + value_c + value_d) / 2
        area_t = (math.sqrt(per * (per - value_b) * (per - value_c) * (per - value_d)))

        print(square.adder(triangle), area_s + area_t)

        assert square.adder(triangle) == area_s + area_t
        assert isinstance(triangle, Figure) == True


class TestsTriangle:

    # проверка на кол-во углов Triangle
    def test_triangle_angles_num(self):
        triangle = Triangle(2, 3, 5)
        assert triangle.angles_num == 3

    # проверка атрибута name Triangle
    def test_triangle_name(self):
        triangle = Triangle(2, 3, 5)
        assert triangle.name == "Triangle"

    # проверка на валидность значений сторон Triangle
    @pytest.mark.parametrize("value_a", argvalues=[0, 2, 4])
    @pytest.mark.parametrize("value_b", argvalues=[-4, 0, 10])
    @pytest.mark.parametrize("value_c", argvalues=[-5, 5, 55])
    def test_triangle_validate(self, value_a, value_b, value_c):
        print(value_a, value_b, value_c)
        triangle = Triangle(value_a, value_b, value_c)
        assert False == triangle.validate

    # проверка расчета периметра Triangle
    @pytest.mark.parametrize("value_a", argvalues=[3, 4])
    @pytest.mark.parametrize("value_b", argvalues=[6, 5])
    @pytest.mark.parametrize("value_c", argvalues=[4, 7])
    def test_triangle_perimeter(self, value_a, value_b, value_c):
        triangle = Triangle(value_a, value_b, value_c)
        perimeter = value_a + value_b + value_c
        assert triangle.perimeter == perimeter

    # проверка расчета площади Triangle
    @pytest.mark.parametrize("value_a", argvalues=[3, 6])
    @pytest.mark.parametrize("value_b", argvalues=[6, 5])
    @pytest.mark.parametrize("value_c", argvalues=[5, 7])
    def test_triangle_area(self, value_a, value_b, value_c):
        triangle = Triangle(value_a, value_b, value_c)
        per = (value_a + value_b + value_c) / 2
        area = (math.sqrt(per * (per - value_a) * (per - value_b) * (per - value_c)))
        assert triangle.area == area


class TestsRectangle:

    # проверка на кол-во углов Rectangle
    @pytest.mark.parametrize("value_a", argvalues=[3])
    @pytest.mark.parametrize("value_b", argvalues=[6])
    def test_rectangle_angles_num(self, value_a, value_b):
        rectangle = Rectangle(value_a, value_b)
        assert rectangle.angles_num == 4

    # проверка атрибута name Rectangle
    @pytest.mark.parametrize("value_a", argvalues=[6])
    @pytest.mark.parametrize("value_b", argvalues=[5])
    def test_rectangle_name(self, value_a, value_b):
        rectangle = Rectangle(value_a, value_b)
        assert rectangle.name == "Rectangle"

    # проверка на валидность значения сторон Rectangle
    @pytest.mark.parametrize("value_a", argvalues=[0, 5])
    @pytest.mark.parametrize("value_b", argvalues=[-9, -4])
    def test_rectangle_validate(self, value_a, value_b):
        rectangle = Rectangle(value_a, value_b)
        assert False == rectangle.validate

    # проверка расчета периметра Rectangle
    @pytest.mark.parametrize("value_a", argvalues=[7, 5])
    @pytest.mark.parametrize("value_b", argvalues=[9, 4])
    def test_rectangle_perimeter(self, value_a, value_b):
        rectangle = Rectangle(value_a, value_b)
        perimeter = 2 * (value_a + value_b)
        assert rectangle.perimeter == perimeter

    # проверка расчета площади Rectangle
    @pytest.mark.parametrize("value_a", argvalues=[3, 12])
    @pytest.mark.parametrize("value_b", argvalues=[9, 44])
    def test_rectangle_area(self, value_a, value_b):
        rectangle = Rectangle(value_a, value_b)
        area = value_a * value_b
        assert rectangle.area == area


class TestsCircle:

    # проверка на кол-во углов Circle
    @pytest.mark.parametrize("value_r", argvalues=[4])
    def test_circle_angles_num(self, value_r):
        circle = Circle(value_r)
        assert circle.angles_num == 0

    # проверка атрибута name Circle
    @pytest.mark.parametrize("value_r", argvalues=[4])
    def test_circle_name(self, value_r):
        circle = Circle(value_r)
        assert circle.name == "Circle"

    # проверка на валидность значения стороны Circle
    @pytest.mark.parametrize("value_r", argvalues=[0, -5, -88])
    def test_circle_validate(self, value_r):
        circle = Circle(value_r)
        assert False == circle.validate

    # проверка расчета периметра Circle
    @pytest.mark.parametrize("value_r", argvalues=[3, 5, 12])
    def test_circle_perimeter(self, value_r):
        circle = Circle(value_r)
        perimeter = 2 * math.pi * value_r
        assert circle.perimeter == perimeter

    # проверка расчета площади Circle
    @pytest.mark.parametrize("value_r", argvalues=[5, 22, 101])
    def test_circle_area(self, value_r):
        circle = Circle(value_r)
        area = math.pi * (value_r ** 2)
        assert circle.area == area

    # проверка расчета сумм площадей Circle и Square
    # проверка на экземпляр класса
    @pytest.mark.parametrize("value_r", argvalues=[5, 22, 101])
    @pytest.mark.parametrize("value_a", argvalues=[7, 4, 33])
    def test_circle_area_adder(self, value_r, value_a):
        circle = Circle(value_r)
        area_c = math.pi * (value_r ** 2)

        square = Square(value_a)
        area_s = value_a ** 2
        assert circle.adder(square) == area_s + area_c
        assert isinstance(square, Figure) == True
