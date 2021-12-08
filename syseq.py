from manim import *

class SystemsOfEquations(VectorScene):
    def construct(self):
        plane = self.add_plane(animate = True).add_coordinates()
        self.wait()