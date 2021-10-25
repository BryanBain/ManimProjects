from manim import *

class DataSet(Scene):
	def construct(self):
		axes = Axes(x_range = [0,55,5], y_range = [-6,66,6]).add_coordinates()

		dot0 = Dot(axes.c2p(31,43), color=YELLOW)
		dot1 = Dot(axes.c2p(11,14), color=YELLOW)
		dot2 = Dot(axes.c2p(22,22), color=YELLOW)
		dot3 = Dot(axes.c2p(40,57), color=YELLOW)
		dot4 = Dot(axes.c2p(18,18), color=YELLOW)
		dot5 = Dot(axes.c2p(18,23), color=YELLOW)
		dot6 = Dot(axes.c2p(27,39), color=YELLOW)
		dot7 = Dot(axes.c2p(45,60), color=YELLOW)
		dot8 = Dot(axes.c2p(25,30), color=YELLOW)
		dot9 = Dot(axes.c2p(35,48), color=YELLOW)

		points = VGroup(dot0,dot1,dot2,dot3,dot4,dot5,dot6,dot7,dot8,dot9)
		self.add(axes)
		self.play(Create(points))

		func1 = lambda x: 1.25*x
		reg_eq = lambda x: 1.513534*x - 5.768144

		line1 = axes.get_graph(func1)
		self.play(Create(line1))
		self.wait()
		line2 = axes.get_graph(reg_eq)
		self.play(Transform(line1,line2), run_time=2)
		self.wait()
		self.remove(line1, line2)

		# Regression equation: y-hat = 1.5135347194978421x - 5.7681443703413038