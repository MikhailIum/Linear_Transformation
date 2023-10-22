import math

from manim import *

class LinearTransformation(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=False,
        )

    def construct(self):
        a = 1
        b = 2
        c = 2
        d = 4
        matrix = [[a, b], [c, d]]

        self.add_background_mobject(Line((-7, -7 * (-0.5), 0), (7, 7 * (-0.5), 0), color=YELLOW))
        # self.add_transformable_mobject(Line((-7, -7 * 2, 0), (7, 7 * -2, 0), color=YELLOW))
        # self.add_transformable_mobject(Line((-7, -14, 0), (7, 14, 0), color=YELLOW))
        # self.add_transformable_mobject(Line((-7, 3.5, 0), (7, -3.5, 0), color=YELLOW))

        self.add_transformable_mobject(ImageMobject("bee.png"))
        # self.add_transformable_mobject(Circle(math.sqrt(1/math.pi), color=RED))
        # self.add_transformable_mobject(Circle(0.5, color=YELLOW))


        self.add_background_mobject(MathTex(
            "\\begin{bmatrix}" + str(a) + "& " + str(b) + "\\\\\\\\" + str(c) + "&" + str(d) + "\\end{bmatrix}").to_edge(UL))
        self.apply_matrix(matrix)
        self.wait()