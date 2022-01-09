from manim import *

class AverageRateOfChange(Scene):
    def construct(self):

        text_start = Text("The average rate of change is the slope \n" \
        "of the line between 2 points on a curve.",
            t2c={'average rate of change': ORANGE, 'slope': BLUE},
            t2w={'slope ': BOLD})

        self.play(Write(text_start), run_time=3)
        self.wait()
        self.remove(text_start)

        text_example = Text("For example, in the interval [0, 3],\n" \
            "find the average rate of change of the function"
            )
        text_function = MathTex(r"\\f(x) = 0.5(x-1)^2+1").scale(1.5)
        # text_example1 = Text("in the interval [0, 3]")

        group = VGroup(text_example, text_function).arrange(DOWN)

        self.play(Write(group), run_time = 3)
        self.wait(2)
        self.remove(group)

        work_intro = Tex(r"First, evaluate the function at $x=0$ and $x=3$")

        work1 = MathTex(r"f(0) = 1.5").scale(1.5)
        work2 = MathTex(r"f(3) = 3").scale(1.5)

        self.play(Write(work_intro))
        self.wait()
        self.play(work_intro.animate.shift(UP*3))
        self.wait()
        self.play(Write(text_function))
        self.play(text_function.animate.shift(UP*2.5))
        work_group = VGroup(work1, work2).arrange(DOWN)
        self.play(Write(work_group))
        self.wait(3)
        self.remove(work_intro, work_group, text_function)

        second_text = Tex(r"Now, find the slope of the line connecting (0, 1.5) and (3, 3)")
        self.play(Write(second_text))
        self.wait(2)
        self.remove(second_text)

        axes = Axes(
                x_range = [-2,4,1],
                y_range = [0,4,1],
                )

        def func(x):
            return 0.5 * (x-1)**2 + 1
        
        graph = axes.plot(func)

        x1 = 0
        y1 = func(x1)
        x2 = 3
        y2 = func(x2)
        
        point1 = [axes.coords_to_point(x1, y1)]
        dot1 = Dot(point1, radius = 0.2, color=ORANGE)
        coords_1 = MathTex(r"(0, 1.5)", color=ORANGE).next_to(dot1, LEFT).scale(1.25)
        point2 = [axes.coords_to_point(x2, y2)]
        dot2 = Dot(point2, radius = 0.2, color=ORANGE)
        coords_2 = MathTex(r"(3, 3)", color=ORANGE).next_to(dot2, RIGHT).scale(1.25)

        segment = Line(point1, point2, color=ORANGE)

        self.add(axes, graph)
        self.wait()
        self.play(Write(dot1))
        self.wait()
        self.play(Write(coords_1))
        self.wait()
        self.play(Write(dot2))
        self.wait()
        self.play(Write(coords_2))
        self.wait()
        self.play(Write(segment))
        self.play(FadeOut(VGroup(axes, graph, dot1, coords_1, dot2, coords_2, segment)))

        work = MathTex(r"\frac{3-1.5}{3-0}").scale(1.25)
        work1 = MathTex(r"\frac{1.5}{3}").scale(1.25)
        work2 = MathTex(r"\frac{1}{2}").scale(1.25)

        self.play(Write(work))
        self.wait()
        self.play(ReplacementTransform(work, work1))
        self.wait()
        self.play(ReplacementTransform(work1, work2))
        self.wait()
        self.play(Indicate(work2))
