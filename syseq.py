from manim import *

class SysEq(LinearTransformationScene, ZoomedScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
        # self.camera.frame.scale(1.5)
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$",
                    r"$\begin{bmatrix} x \\ y \end{bmatrix}$",
                    r"$ = \begin{bmatrix} 3 \\ -1 \end{bmatrix}$").to_edge(UL)
        self.add_title(title)
        point = Dot((3,-1,0), color=YELLOW)
        self.add(point)
        matrix = [ [1,1], [-1,1] ]
        self.apply_matrix(matrix)
        self.wait()

        i_sol = Vector((2,-2)).set_color('#83C167')
        self.play(Create(i_sol))
        self.wait()
        j_sol = Line(start=[2,-2,0], end=[3,-1,0]).add_tip().set_color('#FC6255')
        self.play(Create(j_sol))
        self.wait()
        i_brace = BraceBetweenPoints([0,0,0], [2,-2,0]).set_color('#83C167')
        self.play(Create(i_brace))
        i_sol_lbl = i_brace.get_text("$2\hat\imath$", buff=0.1).set_color('#83C167')
        self.play(Write(i_sol_lbl))
        self.wait()
        j_brace = BraceBetweenPoints([2,-2,0], [3,-1,0]).set_color('#FC6255')
        self.play(Create(j_brace))
        j_brace_lbl = j_brace.get_text("$1\hat\jmath$", buff=0.1).set_color('#FC6255')
        self.play(Write(j_brace_lbl))
        self.wait()
        answer = Tex(r"$\begin{bmatrix} 2 \\ 1 \end{bmatrix}$").to_edge(UR, buff=1)
        self.play(Write(answer))
        self.play(Create(SurroundingRectangle(answer)))
        self.wait()

