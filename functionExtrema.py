from manim import *
import numpy as np 

class FunctionExtrema(Scene):
	def construct(self):
		ax = Axes(
			x_range=[-3,3],
			y_range=[-4,4],
			tips = False
			)

		def func(x):
			return x**3 + x**2 - 3*x - 1

		graph = ax.get_graph(func, color = RED)

		t = ValueTracker(-2.50)

		initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
		dot = Dot(point = initial_point)
		dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))

		x_space = np.linspace(*ax.x_range[:2],200)
		max_index = func(x_space).argmax()


		self.add(ax, graph, dot)
		self.play(t.animate.set_value(x_space[max_index]))
		self.wait()
