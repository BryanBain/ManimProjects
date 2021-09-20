from manim import *

class ComplexNumbers(Scene):
	def construct(self):
		plane = ComplexPlane().add_coordinates()
		self.add(plane)

		d1 = Dot(plane.n2p(3+1j), color=YELLOW)
		label1 = Tex(r'$3+i$', color=YELLOW).next_to(d1, UR)
		vec1 = Vector([3,1], color=YELLOW)

		d2 = Dot(plane.n2p(1+2j), color=BLUE)
		label2 = Tex(r'$1+2i$', color=BLUE).next_to(d2, UL)
		vec2 = Vector([1,2], color=BLUE)
		vec2.generate_target()
		vec2.target.shift(3*RIGHT + 1*UP)

		d3 = Dot(plane.n2p(4+3j), color=PURPLE)
		label3 = Tex(r'$4+3i$', color=PURPLE).next_to(plane.n2p(2+1.25j), UP + LEFT)
		vec3 = Vector([4,3], color=PURPLE)


		self.play(Create(d1))
		self.play(Write(label1))
		self.play(Create(vec1))
		self.remove(label1)

		self.play(Create(d2))
		self.play(Write(label2))
		self.play(Create(vec2))
		self.remove(label2)
		self.wait()

		self.remove(d1, d2)
		self.play(MoveToTarget(vec2))
		self.play(Create(d3))
		self.play(Create(vec3))
		self.play(Write(label3))
		self.wait()

		