from otus_my_homework.lesson6.geometric_figure import Figure, Square, Triangle, Rectangle, Circle
import pytest

test = Figure()
#triangle = Triangle(5)
#rectangle = Rectangle()
#circle = Circle()


class Tests_square:

    square = Square(6)

    def test_triangle_angles_num(self):
        assert self.square.angles_num() == 4

    @pytest.mark.parametrize("vars_", argvalues=[5, 375])
    def test_multi(self, vars_):
        a = vars_ * 10
        square1 = Square(vars_)
        assert a == square1.increase_sum