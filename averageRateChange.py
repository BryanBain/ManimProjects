from manim import *

class AverageRateOfChange(Scene):
    def construct(self):
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
