from manim import *

class InverseIntro(Scene):
    def construct(self):
        title = Title("Inverse Matrices")
        self.play(Write(title))
        self.wait()
        matrixA = Matrix([ [1,-2], [1,0] ]).move_to(UP)
        self.play(Write(matrixA))
        self.wait()

class IntroTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self, 
                show_coordinates = True,
                leave_ghost_vectors = True,
                )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & 1 \\ -2 & 0 \end{bmatrix}$").to_edge(UL)
        self.add_title(title)
        matrix = [ [1,-2], [1,0] ]
        self.apply_matrix(matrix)
        self.wait()
        dot = Dot([1,0,0]).scale(1.25).set_color(GREEN)
        self.play(Create(dot))
        self.wait()
        self.play(Indicate(dot))
        self.wait()
