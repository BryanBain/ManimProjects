from manim import *
# config.frame_width = 18
# config.frame_height = 32

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
        matrix_A = Matrix([[3,-2],[1,0]])
        self.play(Write(matrix_A))
        self.wait()
        i_box = SurroundingRectangle(matrix_A.get_columns()[0], color=GREEN)
        self.play(Create(i_box))
        self.wait()
        i_hat = Tex(r"$\hat\imath$").next_to(i_box, UP).set_color(GREEN)
        self.play(Write(i_hat))
        self.wait()
        j_box = SurroundingRectangle(matrix_A.get_columns()[1], color=RED)
        self.play(Create(j_box))
        self.wait()
        j_hat = Tex(r"$\hat\jmath$").next_to(j_box, UP).set_color(RED)
        self.play(Write(j_hat))
        self.wait()

class LinearTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            # show_coordinates=True,
            # leave_ghost_vectors=True,
        )
    def construct(self):
        vec = self.add_vector([1,3])
        self.write_vector_coordinates(vec)
        self.wait()
        self.get_basis_vector_labels
        matrix_A = [[1,-2],[1,0]]
        self.apply_matrix(matrix_A)
        self.wait()
        self.write_vector_coordinates(vec)
        self.wait()
        new_ihat = Line(start=(0,0,0), end=(1,1,0), color=GREEN).add_tip()
        self.play(Create(new_ihat))
        self.wait()
        i_brace = BraceBetweenPoints((0,0,0), (1,1,0), color=GREEN)
        self.play(Create(i_brace))
        self.wait()
        i_brace_txt = i_brace.get_text("$1\hat\imath$",buff=0.1).set_color(GREEN)
        self.play(Write(i_brace_txt))
        self.wait()
        new_jhat1 = Line(start=(1,1,0), end=(-1,1,0), color=RED).add_tip()
        self.play(Create(new_jhat1))
        new_jhat2 = Line(start=(-1,1,0), end=(-3,1,0), color=RED).add_tip()
        self.play(Create(new_jhat2))
        new_jhat3 = Line(start=(-3,1,0), end=(-5,1,0), color=RED).add_tip()
        self.play(Create(new_jhat3))
        self.wait()
        j_brace = BraceBetweenPoints((1,1,0), (-5,1,0), color=RED)
        self.play(Create(j_brace))
        self.wait()
        j_brace_txt = j_brace.get_text("$3\hat\jmath$", buff=0.1).set_color(RED)
        self.play(Write(j_brace_txt))
        self.wait()
        matrix1_grp = VGroup(new_ihat, new_jhat1, new_jhat2, new_jhat3, i_brace,
                            i_brace_txt, j_brace, j_brace_txt)
        self.play(Uncreate(matrix1_grp))
        self.wait()
        self.remove(self.write_vector_coordinates(vec))
        matrix_B = [[-1,1],[-1,-2]]
        self.apply_matrix(matrix_B)
        self.wait()

class LinearTransform2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self, 
            background_plane_kwargs={'x_range':(-9,9), 'y_range':(-9,9)},
            foreground_plane_kwargs={'x_range':[-9,9], 'y_range':(-9,9)}
            # show_coordinates=True,
            # leave_ghost_vectors=True,
        )
    def construct(self):
        matrix1 = [[2,1], [1,2]]
        matrix2 = [[1,-1], [1,3]]
        self.apply_matrix(matrix2)
        self.wait()
        self.apply_matrix(matrix1)
        self.wait()

class LinearTransformExample1a(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self,
        show_coordinates = True
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$",
                    r"$\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$")
        self.add_title(title)
        shear_matrix = [[1,2], [0,1]]
        self.apply_matrix(shear_matrix)
        self.wait()
        rotation_matrix = [[0,-1], [1,0]]
        self.apply_matrix(rotation_matrix)
        self.wait()
        answer = Matrix([ [0,-1], [1,2] ], 
                        include_background_rectangle=True).next_to(ORIGIN, 3*RIGHT + UP)
        self.play(Create(answer))
        self.wait()

class LinearTransformExample1b(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self,
        show_coordinates = True
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$",
                    r"$\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$")
        self.add_title(title)
        rotation_matrix = [[0,-1], [1,0]]
        self.apply_matrix(rotation_matrix)
        self.wait()
        shear_matrix = [[1,2], [0,1]]
        self.apply_matrix(shear_matrix)
        self.wait()
        answer = Matrix([ [2,-1], [1,0] ], 
                        include_background_rectangle=True).next_to([2,1,0], RIGHT + DOWN)
        self.play(Create(answer))
        self.wait()
        

