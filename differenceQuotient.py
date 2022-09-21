from manim import *

class DiffQuotIntro(Scene):
    def construct(self):
        title = Title("Difference Quotient")
        self.play(Write(title))
        self.wait()
        avgRateChng = Text("Recall the average rate of change of a function \n"
                            "is the slope of the line connecting two given points",
                            t2c = {"average rate of change ": YELLOW}).scale(0.75)
        x1y1 = Tex(r"$(x_1, f(x_1)) \text{ and } (x_2, f(x_2))$").next_to(avgRateChng, DOWN)
        self.play(Write(avgRateChng))
        self.play(Write(x1y1))
        self.wait()
        group = VGroup(avgRateChng, x1y1)
        self.play(group.animate.move_to(UP))
        self.wait()
        arc_formula = Tex(r"$\frac{f(x_2)-f(x_1)}{x_2-x_1}$").next_to(group, 4*DOWN).scale(1.5)
        self.play(Write(arc_formula))
        self.wait()

class DifferenceQuotient(Scene):
    def construct(self):
        ax = NumberPlane(
            axis_config = {"stroke_opacity": 0},
            background_line_style={"stroke_opacity": 0}
            )
        func = lambda x: x**3 + x**2 - 2*x
        graph = ax.plot(func, color=YELLOW)
        self.play(Create(ax))
        self.play(Create(graph))
        self.wait()
        p1 = Dot((-1.75,func(-1.75),0), color=RED).scale(1.5)
        self.play(Create(p1))
        self.wait()
        p1txt = Tex(r"$(x, f(x))$", color=RED).next_to(p1, LEFT)
        self.play(Write(p1txt))
        self.wait()
        hiddenPoint = [1.5, func(-1.75), 0] # used for underbrace horizontal distance h
        brace = BraceBetweenPoints([-1.75,func(-1.75),0], hiddenPoint)
        bracelbl = BraceLabel(brace, "h")
        self.play(Write(bracelbl))
        self.wait()
        p2 = Dot((1.5, func(1.5), 0), color=RED).scale(1.5)
        self.play(Create(p2))
        self.wait()
        p2txt = Tex(r"$(x+h, f(x+h))$", color=RED).next_to(p2, RIGHT)
        self.play(Write(p2txt))
        self.wait()
        self.play(Uncreate(bracelbl))
        self.play(Create(Line(p1, p2).set_color(RED)))
        self.wait()
        diffQuot1 = Tex(r"$m = \frac{f(x+h)-f(x)}{x+h-x}$").to_edge(DR, buff=1.5).scale(1.75)
        self.play(Write(diffQuot1))
        self.wait()
        diffQuot2 = Tex(r"$m = \frac{f(x+h)-f(x)}{h}$").to_edge(DR, buff=1.5).scale(1.75)
        self.play(ReplacementTransform(diffQuot1, diffQuot2))
        self.wait()


        