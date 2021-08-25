from manim import *

class AverageRateOfChange(Scene):
    def construct(self):

        text_start = Text("The average rate of change is the slope \n" \
        "of the line between 2 points on a curve.",
            t2c={'[3:22]': ORANGE, '[27:32]': BLUE},
            t2w={'slope': BOLD})

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

        axes = Axes(
                x_range = [-2,4,1],
                y_range = [0,4,1],
                )

        def func(x):
            return 0.5 * (x-1)**2 + 1
        
        graph = axes.get_graph(func)

        x1 = 0
        y1 = func(x1)
        x2 = 3
        y2 = func(x2)
        
        point1 = [axes.coords_to_point(x1, y1)]
        dot1 = Dot(point1, radius = 0.2, color=ORANGE)
        point2 = [axes.coords_to_point(x2, y2)]
        dot2 = Dot(point2, radius = 0.2, color=ORANGE)

        segment = Line(point1, point2, color=ORANGE)

        self.add(graph)
        self.wait()
        self.play(Write(dot1))
        self.wait()
        self.play(Write(dot2))
        self.wait()
        self.play(Write(segment))
