from manim import *

class MatrixTransformations(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self, 
            leave_ghost_vectors=True
        )
    def construct(self):
        self.add_title("Rotate 90 Counterclockwise")
        rotate_90 = [[0,-1], [1,0]]
        self.write_vector_coordinates(rotate_90)
        # self.play(Write(lbl))
        self.apply_matrix(rotate_90)
        self.wait()