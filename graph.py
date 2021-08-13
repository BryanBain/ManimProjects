from manim import *
import math

class Graph(Scene):
    def construct(self):
        axes = Axes(
                x_range=[-4,4],
                y_range=[-4,4]
                )
        graph = axes.get_graph(lambda x: math.fabs(x), color=RED)
        
        self.play(Create(axes), Create(graph))
        self.wait()
        
        dot = Dot()
        self.add(dot)
        self.play(MoveAlongPath(dot,graph), run_time=4, rate_func=linear)
