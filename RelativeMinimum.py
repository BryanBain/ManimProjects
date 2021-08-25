from manim import *
import numpy as np 
import math

class RelativeMinimum(Scene):
	def construct(self):
		ax = Axes(
			x_range=[-3,3],
			y_range=[-4,4],
			tips = False
			)

		def func(x):
			return x**3 + x**2 - 3*x - 1

		graph = ax.get_graph(func, color = RED)

		t = ValueTracker(-1.387)

		initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
		dot = Dot(point = initial_point, color=YELLOW)
		dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))

		x_space = np.linspace(-1.387,3,num=100)

		max_index = func(x_space).argmin()

		text = Text("Relative minimum", color=YELLOW).scale(0.75)
		text1 = MathTex("(0.721, -2.268)", color=YELLOW).scale(1)
		text.next_to([ax.coords_to_point(0.721,-2.268)], DOWN)
		text1.next_to(text, DOWN)

		self.add(ax, graph, dot)
		self.play(t.animate.set_value(x_space[max_index]), run_time=3)
		self.add(text)
		self.wait()
		self.add(text1)
		self.wait()


