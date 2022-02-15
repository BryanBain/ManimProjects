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
        matrix_A_txt = Tex(r"$A = \begin{bmatrix} 1 & -2 \\ 1 & 0 \end{bmatrix}$").move_to(LEFT)
        self.play(Write(matrix_A_txt))
        self.wait()
        matrix_B_txt = Tex(r"$B = \begin{bmatrix} -1 & 4 \\ 5 & 6 \end{bmatrix}$").next_to(matrix_A_txt, 2*RIGHT)
        self.play(Write(matrix_B_txt))
        self.wait(2)
        not_AB = Tex(r"$AB \neq \begin{bmatrix} -1 & -8 \\ 5 & 0 \end{bmatrix}$").to_edge(DOWN, buff=1)
        self.play(Write(not_AB))
        self.wait(2)
        intro_group = VGroup(title, intro_txt1, matrix_A_txt, matrix_B_txt, not_AB)
        self.play(Uncreate(intro_group))
        self.wait()

        explanation = Tex("Multiplying by a matrix tells us where $\hat{\imath}$ and $\hat{\jmath}$ end up.")
        self.play(Write(explanation))
        self.wait()
        self.play(explanation.animate.to_edge(UP))
        self.wait()
        matrix_A = Matrix([[1,-2],[1,0]])
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

class MatrixMultIntro2(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(self, show_coordinates=True)
    def construct(self):
        matrix_A = [[1,-2],[1,0]]
        title = Tex("Multiplying by ")
        matrix_A_txt = Matrix(matrix_A).next_to(title, RIGHT)
        i_col = matrix_A_txt.get_columns()[0]
        j_col = matrix_A_txt.get_columns()[1]
        i_col_box = SurroundingRectangle(i_col, color='#83C167')
        j_col_box = SurroundingRectangle(j_col, color='#FC6255')
        title_grp = VGroup(title, matrix_A_txt, i_col_box, j_col_box)
        self.add_title(title_grp)
        self.wait()
        self.apply_matrix(matrix_A)
        self.wait()


class LinearTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            # show_coordinates=True,
            # leave_ghost_vectors=True,
        )
    def construct(self):
        i_hat_lbl = Tex(r"$\hat{\imath}$").next_to((1,0,0), DOWN).set_color('#83C167')
        j_hat_lbl = Tex(r"$\hat{\jmath}$").next_to((0,1,0), LEFT).set_color('#FC6255')
        basis_grp = VGroup(i_hat_lbl, j_hat_lbl)
        self.play(Write(basis_grp))
        vec = self.add_vector([1,3])
        vec_txt = Tex(r"$\begin{bmatrix} 1 \\ 3\end{bmatrix}$"
                    ).next_to(vec.get_tip(), RIGHT).set_color(YELLOW)
        self.play(Write(vec_txt))
        self.wait()
        self.get_basis_vector_labels
        matrix_A = [[1,-2],[1,0]]
        matrix_A_txt = Matrix(matrix_A).next_to(vec_txt, LEFT)
        self.play(Write(matrix_A_txt))
        i_col = matrix_A_txt.get_columns()[0]
        j_col = matrix_A_txt.get_columns()[1]
        self.play(Create(SurroundingRectangle(i_col, color='#83C167')))
        self.play(Create(SurroundingRectangle(j_col, color='#FC6255')))
        self.remove(basis_grp)
        self.wait()
        self.apply_matrix(matrix_A)
        self.wait()
        self.write_vector_coordinates(vec).set_color(YELLOW)
        self.wait()
        new_ihat = Line(start=(0,0,0), end=(1,1,0), color=GREEN).add_tip()
        self.play(Create(new_ihat))
        self.wait()
        self.play(Create(SurroundingRectangle(vec_txt[0][1], color='#83C167')))
        self.wait()
        i_brace = BraceBetweenPoints((0,0,0), (1,1,0), color=GREEN)
        self.play(Create(i_brace))
        self.wait()
        i_brace_txt = i_brace.get_text("$1\hat\imath$",buff=0.1).set_color(GREEN)
        self.play(Write(i_brace_txt))
        self.wait()
        self.play(Create(SurroundingRectangle(vec_txt[0][2], color='#FC6255')))
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


class MatrixTimesMatrix(LinearTransformationScene):
    config.frame_width = 18
    config.frame_height = 40
    def __init__(self):
        LinearTransformationScene.__init__(
            self, 
            background_plane_kwargs={'x_range':(-9,9), 'y_range':(-9,9)},
            foreground_plane_kwargs={'x_range':[-9,9], 'y_range':(-9,9)},
            show_coordinates=True,
            # leave_ghost_vectors=True
        )
    def construct(self):
        matrix1 = [[2,1], [1,2]]
        matrix2 = [[1,-1], [1,3]]
        matrix1_txt = Matrix(matrix1).move_to((-6,2,0))
        matrix2_txt = Matrix(matrix2).next_to(matrix1_txt, RIGHT)
        product = VGroup(matrix1_txt, matrix2_txt)
        self.add(product)
        self.wait()
        self.apply_matrix(matrix2)
        self.wait()
        self.apply_matrix(matrix1)
        self.wait()

class Rotate90CCW(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self
        )
    def construct(self):
        config.frame_width = 16
        config.frame_height = 9
        self.add_unit_square()
        rotate90ccw_txt = Tex(r"Rotate $90^\circ$ counterclockwise $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$")
        rotate90ccw_mat = [ [0,-1], [1,0] ]
        self.add_title(rotate90ccw_txt)
        self.apply_matrix(rotate90ccw_mat)
        self.wait()

class Rotate180(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self,
        show_coordinates=True
        )
    def construct(self):
        config.frame_width = 16
        config.frame_height = 9
        self.add_unit_square()
        rotate90ccw_txt = Tex(r"Rotate $180^\circ$  $\begin{bmatrix} -1 & 0 \\ 0 & -1 \end{bmatrix}$")
        rotate90ccw_mat = [ [-1,0], [0,-1] ]
        self.add_title(rotate90ccw_txt)
        self.apply_matrix(rotate90ccw_mat)
        self.wait()

class Rotate90CW(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self
        )
    def construct(self):
        self.add_unit_square()
        rotate90cw_txt = Tex("Rotate $90^\circ$ clockwise.")
        self.add_title(rotate90cw_txt)
        rotate90cw_mat = [ [0,1], [-1,0] ]
        self.apply_matrix(rotate90cw_mat)
        self.wait()
        self.play(Write(Matrix(rotate90cw_mat).move_to((3,1.5,0))))
        self.wait()

class HorizShear(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self
        )
    def construct(self):
        self.add_unit_square()
        horiz_shear_txt = Tex("Shear horizontally")
        self.add_title(horiz_shear_txt)
        horiz_shear_mat = [ [1,-1], [0,1] ]
        self.apply_matrix(horiz_shear_mat)
        self.wait()
        self.play(Write(Matrix(horiz_shear_mat).move_to((3,1.5,0))))
        self.wait()

class VertShear(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self
        )
    def construct(self):
        self.add_unit_square()
        vert_shear_txt = Tex("Shear vertically")
        self.add_title(vert_shear_txt)
        vert_shear_mat = [ [1,0], [-1,1] ]
        self.apply_matrix(vert_shear_mat)
        self.wait()
        self.play(Write(Matrix(vert_shear_mat).move_to((3,1.5,0))))
        self.wait()

class ScaleUp(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self
        )
    def construct(self):
        self.add_unit_square()
        scl_up_txt = Tex("Scale up")
        self.add_title(scl_up_txt)
        scl_up_mat = [ [2,0], [0,2] ]
        self.apply_matrix(scl_up_mat)
        self.wait()
        self.play(Write(Matrix(scl_up_mat).move_to((3.5,1.5,0))))
        self.wait()

class ScaleDown(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self
        )
    def construct(self):
        self.add_unit_square()
        scl_down_txt = Tex("Scale down")
        self.add_title(scl_down_txt)
        scl_down_mat = [ [0.3,0], [0,0.3] ]
        self.apply_matrix(scl_down_mat)
        self.wait()
        self.play(Write(Matrix(scl_down_mat).move_to((5.5,1.5,0))))
        self.wait()

class MultipleTransform(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self
        )
    def construct(self):
        grandma = ImageMobject("./grandma.jpg").scale(0.25)
        grandma.move_to(ORIGIN, DL)
        self.add_transformable_mobject(grandma)
        rotate180 = [ [-1,0],[0,-1] ]
        self.apply_matrix(rotate180)
        self.wait()
        shear = [ [1,1], [0,2] ]
        self.apply_matrix(shear)
        self.wait()

class LinearTransformExample2a(LinearTransformationScene):
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

class LinearTransformExample2b(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
        self,
        show_coordinates = True
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$",
                    r"$\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$")
        self.add_title(title)
        # self.add_unit_square()
        rotation_matrix = [[0,-1], [1,0]]
        self.apply_matrix(rotation_matrix)
        # self.play(grandma.animate.apply_matrix(rotation_matrix))
        self.wait()
        shear_matrix = [[1,2], [0,1]]
        self.apply_matrix(shear_matrix)
        # self.play(grandma.animate.apply_matrix(shear_matrix))
        self.wait()
        answer = Matrix([ [2,-1], [1,0] ], 
                        include_background_rectangle=True).next_to([2,1,0], RIGHT + DOWN)
        self.play(Create(answer))
        self.wait()