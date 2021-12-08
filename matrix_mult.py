from manim import *

class MatrixMultIntro(Scene):
    def construct(self):
        title = Title("Matrix Multiplication")
        self.play(Write(title))
        self.wait()
        intro_txt1 = Text("Matrix multiplication does not work the way you might think.").scale(0.8).move_to(UP)
        self.play(Write(intro_txt1))
        self.wait()
        matrix_A_txt = Tex(r"$A = \begin{bmatrix} 3 & -2 \\ 1 & 0 \end{bmatrix}$").move_to(LEFT)
        self.play(Write(matrix_A_txt))
        self.wait()
        matrix_B_txt = Tex(r"$B = \begin{bmatrix} -1 & 4 \\ 5 & 6 \end{bmatrix}$").next_to(matrix_A_txt, 2*RIGHT)
        self.play(Write(matrix_B_txt))
        self.wait()
        not_AB = Tex(r"$AB \neq \begin{bmatrix} -3 & -8 \\ 5 & 0 \end{bmatrix}$").to_edge(DOWN, buff=1)
        self.play(Write(not_AB))
        self.wait()
        intro_group = VGroup(title, intro_txt1, matrix_A_txt, matrix_B_txt, not_AB)
        self.play(Uncreate(intro_group))
        self.wait()

        explanation = Tex("Multiplying by a matrix tells us where $\hat{\imath}$ and $\hat{\jmath}$ end up.")
        self.play(Write(explanation))
        self.wait()
        self.play(explanation.animate.to_edge(UP))
        self.wait()

