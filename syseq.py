from manim import *

class SystemsOfEquations(Scene):
    def construct(self):
        grid = NumberPlane()
        dot = Dot(ORIGIN)

        ihat = Arrow(ORIGIN, [1,0,0], buff=0, color=RED)
        jhat = Arrow(ORIGIN, [0,1,0], buff=0, color=PURPLE)

        ihat_text = MathTex(r"\hat \imath").next_to(ihat.get_end(), RIGHT + DOWN)
        jhat_text = MathTex(r"\hat \jmath").next_to(jhat.get_end(), UP + RIGHT)

        self.add(grid, dot, ihat, jhat, ihat_text, jhat_text)
