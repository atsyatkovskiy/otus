from otus_my_homework.lesson6.geometric_figure import Figure, Square, Triangle, Rectangle, Circle

test = Figure()
#triangle = Triangle(5)
#rectangle = Rectangle()
#circle = Circle()


class Tests:

    square = Square(6)

    def test_triangle_angles_num(self):
        assert self.square.angles_num() == 4