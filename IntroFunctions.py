from manim import *

class IntroFunctions(Scene):
	def construct(self):
		func_def = Text("A function is a relation \nin which each element of the domain\n"
			"has only one element in the range.", t2c={' functio':YELLOW})

		self.play(Write(func_def), run_time = 2)
		self.remove(func_def)

		vlt = Text("In other words, if you plot the relation,\n"
			"each vertical line hits the plot \n"
			"exactly once.")
		self.play(Write(vlt), run_time = 2)
		self.remove(vlt)

		ex1a = Tex(r"$\{(1,5), \, (2, 5), \, (3, 7), \, (4, 8)\}$")

		self.play(Write(ex1a), run_time = 3)
		self.play(ex1a.animate.shift(UP*3))

		ex1a_axes = Axes(x_range = [0,5,1], y_range = [0,9,1]).add_coordinates()
		x1a = 1
		y1a = 5
		x2a = 2
		y2a = 5
		x3a = 3
		y3a = 7
		x4a = 4
		y4a = 8

		self.play(Create(ex1a_axes))

		point1a = [ex1a_axes.c2p(x1a, y1a)]
		dot1a = Dot(point1a, radius=0.2, color=ORANGE)
		point2a = [ex1a_axes.c2p(x2a, y2a)]
		dot2a = Dot(point2a, radius=0.2, color=ORANGE)
		point3a = [ex1a_axes.c2p(x3a, y3a)]
		dot3a = Dot(point3a, radius=0.2, color=ORANGE)
		point4a = [ex1a_axes.c2p(x4a, y4a)]
		dot4a = Dot(point4a, radius=0.2, color=ORANGE)
		dot_ex1a = VGroup(dot1a, dot2a, dot3a, dot4a)
		
		self.play(Write(dot_ex1a))
		self.remove(ex1a)

		line1a = Line(ex1a_axes.c2p(1,0,0), ex1a_axes.c2p(1,9,0))
		self.play(Create(line1a))
		line2a = Line(ex1a_axes.c2p(2,0,0), ex1a_axes.c2p(2,9,0))
		self.play(Create(line2a))
		line3a = Line(ex1a_axes.c2p(3,0,0), ex1a_axes.c2p(3,9,0))
		self.play(Create(line3a))
		line4a = Line(ex1a_axes.c2p(4,0,0), ex1a_axes.c2p(4,9,0))
		self.play(Create(line4a))

		self.remove(ex1a_axes, dot_ex1a, line1a, line2a, line3a, line4a)

		ex1b = Tex(r"$\{(5,1), \, (5,2), \, (7,3), \, (8,4)\}$")
		self.play(Write(ex1b), run_time = 3)
		self.play(ex1b.animate.shift(UP*3))
		ex1b_axes = Axes(x_range=[0,9,1], y_range=[0,5,1]).add_coordinates()

		x1b = 5
		y1b = 1
		x2b = 5
		y2b = 2
		x3b = 7
		y3b = 3
		x4b = 8
		y4b = 4

		self.play(Create(ex1b_axes))
		point1b = [ex1b_axes.c2p(x1b, y1b)]
		dot1b = Dot(point1b, radius=0.2, color=ORANGE)
		point2b = [ex1b_axes.c2p(x2b, y2b)]
		dot2b = Dot(point2b, radius=0.2, color=ORANGE)
		point3b = [ex1b_axes.c2p(x3b, y3b)]
		dot3b = Dot(point3b, radius=0.2, color=ORANGE)
		point4b = [ex1b_axes.c2p(x4b, y4b)]
		dot4b = Dot(point4b, radius=0.2, color=ORANGE)
		dot_ex1b = VGroup(dot1b, dot2b, dot3b, dot4b)
		
		self.play(Write(dot_ex1b))
		self.remove(ex1b)

		line1b = Line(ex1b_axes.c2p(5,0,0), ex1b_axes.c2p(5,5,0))
		self.play(Create(line1b))
		self.play(Create(SurroundingRectangle(VGroup(dot1b, dot2b))))
		self.remove(ex1b_axes, line1b, dot_ex1b)
