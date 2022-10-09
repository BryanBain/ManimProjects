from manim import *

class Intro(Scene):
    def construct(self):
        plane = NumberPlane()

        parent_func = plane.plot(lambda x: np.sqrt(x), x_range=[0,7], color=YELLOW)
        parent_func_lbl = Tex(r"$f(x) = \sqrt{x}$").next_to(parent_func, UP).set_color(YELLOW)

        self.play(Create(plane))
        self.play(Create(parent_func))
        self.wait()
        self.play(Write(parent_func_lbl))
        self.wait()

        right_shift = plane.plot(lambda x: np.sqrt(x-2), x_range=[2,7], color=BLUE)
        right_shift_lbl = Tex(r"$f(x-2) = \sqrt{x-2}$").set_color(BLUE).next_to(right_shift, UP)
        self.play(ReplacementTransform(parent_func, right_shift))
        self.play(ReplacementTransform(parent_func_lbl, right_shift_lbl))
        self.wait()

        reflect_y = plane.plot(lambda x: np.sqrt(-x-2), x_range=[-7,-2], color=ORANGE)
        reflect_y_lbl = Tex(r"$f(-x-2) = \sqrt{-x-2}$").set_color(ORANGE).next_to(reflect_y, DOWN)
        self.play(ReplacementTransform(right_shift, reflect_y))
        self.play(ReplacementTransform(right_shift_lbl, reflect_y_lbl))
        self.wait()

        shift_up = plane.plot(lambda x: np.sqrt(-x-2)+1, x_range=[-7,-2], color=GREEN)
        shift_up_lbl = Tex(r"$f(-x-2)+1 = \sqrt{x-2} + 1$").set_color(GREEN).next_to(shift_up, RIGHT)
        self.play(ReplacementTransform(reflect_y, shift_up))
        self.play(ReplacementTransform(reflect_y_lbl, shift_up_lbl))
        self.wait()