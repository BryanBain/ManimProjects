from manim import *

class FunctionTransformIntro(Scene):
    def construct(self):
        introText = Tex(r"When working with $f(x \pm a)$, shift the background grid left or right $a$ units.").scale(0.7)
        self.play(Write(introText))
        self.wait()
        # self.play(Uncreate(introText))
        # self.wait()

class HorizontalShift(Scene):
    def construct(self):
        plane = NumberPlane(x_range = (-8.1111111, 8.1111111, 1)).add_coordinates()
        self.play(Create(plane))
        self.wait()
        sqrtTex = Tex(r"$f(x) = \sqrt{x}$").to_edge(UL)
        self.play(Write(sqrtTex))
        self.wait()
        graph = plane.plot(lambda x: np.sqrt(x), x_range=[0,10])
        self.play(Create(graph))
        self.wait()
        text = Tex(r"Replacing $x$ with $x-1$ shifts the background grid 1 space left.").scale(0.7).to_edge(UP)
        self.play(Write(text))
        self.wait()
        self.play(plane.animate.shift(LEFT))
        self.wait()
        sqrtTex2 = Tex(r"$f(x-1) = \sqrt{x-1}$", color=YELLOW).next_to(sqrtTex, DOWN)
        self.play(Write(sqrtTex2))
        self.wait()
        graph2 = plane.plot(lambda x: np.sqrt(x-1), x_range=[1,10], color=YELLOW)
        self.play(Create(graph2))
        self.wait()
        group = VGroup(plane, graph2)
        self.play(group.animate.shift(RIGHT))
        self.wait()

class HorizontalStretch(Scene):
    # def __init__(self):
    #     LinearTransformationScene.__init__(
    #         self,
    #         show_coordinates = True,
    #         show_basis_vectors = False
    #     )
    def construct(self):
        sqrtTex = Tex(r"$f(x) = \sqrt{x}$").to_edge(UL)
        self.play(Write(sqrtTex))
        self.wait()
        graph = NumberPlane(
            x_range=(-14.2222222, 14.2222222,1),
            y_range=(-14.2222222, 14.2222222,1)
            ).add_coordinates()
        self.play(Create(graph))
        self.play(Create(graph.plot(lambda x: np.sqrt(x), x_range=[0,10,0.05])))
        self.wait()
        self.play(graph.animate.scale(0.5))
        # matrix = Matrix([
        #     [0.5,0],
        #     [0,0.5]
        # ])
        # graph.apply_matrix(matrix)
        self.wait()
