from manim import *

class SysEq(LinearTransformationScene):
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
        point = Dot((3,-1,0), color=YELLOW).scale(1.5)
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

class Example1a(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
    
    def construct(self):
        title = Tex(r"$\begin{bmatrix} -2 & 2 \\ 2 & 1 \end{bmatrix}$",
        r"$\begin{bmatrix} x \\ y \end{bmatrix} = $",
        r"$\begin{bmatrix} 4 \\ -1 \end{bmatrix}$")
        self.add_title(title)

        point = Dot((4,-1,0), color=YELLOW).scale(1.5)
        self.add(point)
        matrix = [ [-2,2], [2,1] ]
        self.apply_matrix(matrix)
        self.wait()

        i_sol = Vector((2,-2)).set_color('#83C167')
        self.play(Create(i_sol))
        self.wait()
        j_sol = Line(start=[2,-2,0], end=[4,-1,0]).add_tip().set_color('#FC6255')
        self.play(Create(j_sol))
        self.wait()
        i_brace = BraceBetweenPoints([0,0,0], [2,-2,0]).set_color('#83C167')
        self.play(Create(i_brace))
        i_sol_lbl = i_brace.get_text("$-1\hat\imath$", buff=0.1).set_color('#83C167')
        self.play(Write(i_sol_lbl))
        self.wait()
        j_brace = BraceBetweenPoints([2,-2,0], [4,-1,0]).set_color('#FC6255')
        self.play(Create(j_brace))
        j_brace_lbl = j_brace.get_text("$1\hat\jmath$", buff=0.1).set_color('#FC6255')
        self.play(Write(j_brace_lbl))
        self.wait()
        answer = Tex(r"$\begin{bmatrix} -1 \\ 1 \end{bmatrix}$").to_edge(UR+0.75*DOWN, buff=1)
        self.play(Write(answer))
        self.play(Create(SurroundingRectangle(answer)))
        self.wait()

class Example1b(LinearTransformationScene):
    config.frame_width = 20
    config.frame_height = 12
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & 1 \\ 2 & 1 \end{bmatrix}$",
        r"$\begin{bmatrix} x \\ y \end{bmatrix} = $",
        r"$\begin{bmatrix} 1 \\ 3 \end{bmatrix}$").to_edge(UL)
        self.add_title(title)

        point = Dot((1,3,0), color=YELLOW).scale(1.5)
        self.add(point)
        matrix = [ [1,1], [2,1] ]
        self.apply_matrix(matrix)
        self.wait()

        i_sol = Line(start=[1,2,0], end=[2,4,0]).add_tip().set_color('#83C167')
        self.play(Create(i_sol))
        self.wait()
        j_sol = Line(start=[2,4,0], end=[1,3,0]).add_tip().set_color('#FC6255')
        self.play(Create(j_sol))
        self.wait()
        i_brace = BraceBetweenPoints([0,0,0], [2,4,0]).set_color('#83C167')
        self.play(Create(i_brace))
        i_sol_lbl = i_brace.get_text("$2\hat\imath$", buff=0.2).set_color('#83C167')
        self.play(Write(i_sol_lbl))
        self.wait()
        j_brace = BraceBetweenPoints([2,4,0], [1,3,0]).set_color('#FC6255')
        self.play(Create(j_brace))
        j_brace_lbl = j_brace.get_text("$-1\hat\jmath$", buff=0.1).set_color('#FC6255')
        self.play(Write(j_brace_lbl))
        self.wait()
        answer = Tex(r"$\begin{bmatrix} 2 \\ -1 \end{bmatrix}$").move_to((4,2,0))
        self.play(Write(answer))
        self.play(Create(SurroundingRectangle(answer)))
        self.wait()

class InfiniteSolutionsIntro(LinearTransformationScene):
    # config.frame_width = 20
    # config.frame_height = 12
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & -2 \\ -2 & 4 \end{bmatrix}$",
        r"$\begin{bmatrix} x \\ y \end{bmatrix} = $",
        r"$\begin{bmatrix} 2 \\ -4 \end{bmatrix}$").to_edge(UR+3*DOWN, buff=4)
        self.add_title(title)

        point = Dot((2,-4,0), color=YELLOW).scale(1.5)
        self.add(point)
        matrix = [ [1,-2], [-2,4] ]
        self.apply_matrix(matrix)
        self.wait()

class NoSolutionsIntro(LinearTransformationScene):
    # config.frame_width = 20
    # config.frame_height = 12
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & -2 \\ -2 & 4 \end{bmatrix}$",
        r"$\begin{bmatrix} x \\ y \end{bmatrix} = $",
        r"$\begin{bmatrix} 2 \\ 3 \end{bmatrix}$").to_edge(UR+3*DOWN, buff=4)
        self.add_title(title)

        point = Dot((2,3,0), color=YELLOW).scale(1.5)
        self.add(point)
        matrix = [ [1,-2], [-2,4] ]
        self.apply_matrix(matrix)
        self.wait()

class Example2a(LinearTransformationScene):
    # config.frame_width = 20
    # config.frame_height = 12
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 1 & -2 \\ 2 & -4 \end{bmatrix}$",
        r"$\begin{bmatrix} x \\ y \end{bmatrix} = $",
        r"$\begin{bmatrix} 4 \\ 5 \end{bmatrix}$").to_edge(UL+3*DOWN, buff=4)
        self.add_title(title)

        point = Dot((4,5,0), color=YELLOW).scale(1.5)
        self.add(point)
        matrix = [ [1,-2], [2,-4] ]
        self.apply_matrix(matrix)
        self.wait()

class Example2b(LinearTransformationScene):
    # config.frame_width = 20
    # config.frame_height = 12
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            background_plane_kwargs={'x_range':[-10,10,1],
                                    'y_range':[-8,8,1]}
        )
    def construct(self):
        title = Tex(r"$\begin{bmatrix} 2 & -2 \\ 1 & -1 \end{bmatrix}$",
        r"$\begin{bmatrix} x \\ y \end{bmatrix} = $",
        r"$\begin{bmatrix} 4 \\ 2 \end{bmatrix}$").to_edge(UL+3*DOWN, buff=4)
        self.add_title(title)

        point = Dot((4,2,0), color=YELLOW).scale(1.5)
        self.add(point)
        matrix = [ [2,-2], [1,-1] ]
        self.apply_matrix(matrix)
        self.wait()