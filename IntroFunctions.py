from manim import *

class IntroFunctions(Scene):
	def construct(self):
		title = Title("Intro to Functions")
		self.play(Write(title))
		self.wait()

		rel_def = Text("A relation is a set (a list) of ordered pairs.", t2c={' relatio': YELLOW})
		self.play(Write(rel_def), run_time = 2)
		self.play(rel_def.animate.shift(UP*2))
		self.wait()

		domain_def = Text("The domain is the set (the list) of all input values (x).", t2c={' domai':YELLOW}).scale(0.9)
		self.play(Write(domain_def), run_time = 2)
		self.play(domain_def.animate.shift(UP))
		self.wait()

		range_def = Text("The range is the set (the list) of all output values (y).", t2c={' rang':YELLOW}).scale(0.9)
		self.play(Write(range_def), run_time = 2)
		self.wait()
		self.remove(title, rel_def, domain_def, range_def)

		func_def = Text("A function is a relation \nin which each element of the domain\n"
			"has only one element in the range.", t2c={' functio':YELLOW})

		self.play(Write(func_def), run_time = 2)
		self.wait(2)
		self.remove(func_def)

		func_machine = Text("Functions are like machines that accept an input (x)\n"
			"processes it, and then gives an output (y).")
		self.play(Write(func_machine), run_time = 3)
		self.wait(2)
		self.remove(func_machine)

		phone = Text("Sending a text message is a function.")
		self.play(Write(phone))
		self.play(phone.animate.shift(3*UP))
		phone_input = Text("The message itself is the input.")
		self.play(Write(phone_input))
		self.play(phone_input.animate.shift(2*UP))
		phone_machine = Text("Pressing the SEND button processes the text.")
		self.play(Write(phone_machine))
		self.play(phone_machine.animate.shift(UP))
		phone_output = Text("The recipient getting the message is the output.")
		self.play(Write(phone_output))
		self.wait(2)
		self.remove(phone, phone_input, phone_machine, phone_output)

		vlt_intro = Text("We can determine if a relation is a function by\n"
			"drawing vertical lines through the graph of the relation.").scale(0.9)
		self.play(Write(vlt_intro))
		self.play(vlt_intro.animate.shift(2*UP))

		test = Text("The Vertical Line Test is a visual way to determine\n"
			"if a relation is a function.", t2c = {'[3:19]': BLUE})
		self.play(Write(test), run_time = 2)
		self.wait(2)
		erase = VGroup(vlt_intro, test)
		self.play(Unwrite(erase))

		vlt = Text("In other words, if you plot the relation,\n"
			"each vertical line hits the plot \n"
			"either exactly once or not at all.")
		self.play(Write(vlt), run_time = 2)
		self.wait(2)
		self.remove(vlt)

class Example1(Scene):
	def construct(self):
		ex1a = Tex(r"$\{(1,5), \, (2, 5), \, (3, 7), \, (4, 8)\}$")

		self.play(Write(ex1a), run_time = 3)
		self.play(ex1a.animate.shift(UP*3))
		self.wait()

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
		self.wait(2)

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
		rectangle = SurroundingRectangle(VGroup(dot1b, dot2b))
		self.play(Create(rectangle))
		self.wait(2)
		self.remove(ex1b_axes, line1b, dot_ex1b, rectangle)
		self.wait()

		ex2a_axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], axis_config={'include_ticks':False})
		self.play(Create(ex2a_axes))
		def ex2a_func(x):
			return -0.5*x - 0.5
		graph_2a = ex2a_axes.get_graph(ex2a_func)
		self.play(Create(graph_2a))
		self.wait()
		ex2a_lines = VGroup()
		num_lines = 10
		for i in range(num_lines+1):
			ex2a_lines.add(Line(ex2a_axes.c2p((-2.25+4.5*i/num_lines), -3, 0), ex2a_axes.c2p((-2.25+4.5*i/num_lines), 3, 0), color=ORANGE))
		self.play(FadeIn(ex2a_lines), run_time=2)
		self.wait(2)
		self.remove(ex2a_axes, graph_2a, ex2a_lines)

		ex2b_axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], axis_config={'include_ticks':False})
		self.play(Create(ex2b_axes))
		def ex2b_func(x):
			return -0.5*x*x + 0.5
		graph_2b = ex2b_axes.get_graph(ex2b_func)
		self.play(Create(graph_2b))
		self.wait()
		ex2b_lines = VGroup()
		num_lines = 10
		for i in range(num_lines+1):
			ex2b_lines.add(Line(ex2b_axes.c2p((-2.25+4.5*i/num_lines), -3, 0), ex2b_axes.c2p((-2.25+4.5*i/num_lines), 3, 0), color=ORANGE))
		self.play(FadeIn(ex2b_lines), run_time=2)
		self.wait(2)
		self.remove(ex2b_axes, graph_2b, ex2b_lines)

		ex2c_axes = Axes(x_range=[-3,3,1], y_range=[-3,3,1], axis_config={'include_ticks':False})
		self.play(Create(ex2c_axes))
		ellipse = Ellipse(width = 3, height = 1.5)
		self.play(Create(ellipse))
		self.wait()
		line3c = Line(ex2c_axes.c2p(-0.25,-3,0), ex2c_axes.c2p(-0.25,3,0))
		self.play(Create(line3c))
		self.wait(2)

		self.remove(ex2c_axes, ellipse, line3c)



class FunctionMachine(Scene):
	def construct(self):
		intro_text = Text("Functions are nothing more than machines\n"
			"that accept an input and produce an output.")
		self.play(Write(intro_text))
		self.wait(2)
		self.remove(intro_text)

		input_arrow = Arrow(start=LEFT*5, end=LEFT*2, color=YELLOW)
		input_value = Tex("49").next_to(input_arrow, LEFT, buff=0.5).scale(2)
		function_box = Tex(r"$f(x) = \sqrt{x}$")
		box = SurroundingRectangle(function_box, color=RED, buff=0.25)
		machine = VGroup(function_box, box).scale(1.5).next_to(input_arrow, RIGHT)
		self.play(Write(machine))
		self.play(Write(input_value))
		self.play(Create(input_arrow))
		self.wait()
		self.remove(input_arrow, input_value)
		func_eval = Tex(r"$f(49) = \sqrt{49}$")
		self.play(ReplacementTransform(function_box, func_eval))
		output_arrow = Arrow(start=2.25*RIGHT, end=5.25*RIGHT, color=YELLOW)
		self.play(Create(output_arrow))
		output_value = Tex("7").next_to(output_arrow, RIGHT, buff=0.5).scale(2)
		self.play(Write(output_value))
		self.wait()
		self.remove(output_value, output_arrow, func_eval, box)

		ex3_text = Tex("For each of the following, find $f(2)$, $f(-2)$ and $f(0)$.")
		self.play(Write(ex3_text), run_time=2)
		self.wait(2)
		self.remove(ex3_text)

		ex3a1 = MathTex(r"f(x) &= 2x + 3", substrings_to_isolate="x").set_color_by_tex("x", '#00FFEE')
		self.play(Write(ex3a1))

		ex3a1_1 = MathTex(r"f(2) &= 2(2) + 3\\ &= 4 + 3 \\ &= 7").next_to(ex3a1, DOWN)
		line3a_1 = ex3a1_1[0][0:11]
		self.play(Write(line3a_1))
		self.wait()
		line3a_2 = ex3a1_1[0][11:15]
		self.play(Write(line3a_2))
		self.wait()
		answer3a = ex3a1_1[0][15:17]
		self.play(Write(answer3a))
		box3a1_1 = SurroundingRectangle(answer3a[1])
		self.play(Create(box3a1_1))
		self.remove(line3a_1, line3a_2, answer3a, box3a1_1)
		self.wait()

		ex3a1_2 = MathTex(r"f(-2) &= 2(-2) + 3\\ &= -4 + 3 \\ &= -1").next_to(ex3a1, DOWN)
		line3a1_2 = ex3a1_2[0][0:13]
		self.play(Write(line3a1_2))
		line3a1_3 = ex3a1_2[0][13:18]
		self.play(Write(line3a1_3))
		line3a1_4 = ex3a1_2[0][18:21]
		self.play(Write(line3a1_4))
		box3a1_2 = SurroundingRectangle(ex3a1_2[0][19:])
		self.play(Create(box3a1_2))
		self.remove(ex3a1_2, line3a1_2, line3a1_3, line3a1_4, box3a1_2)

		ex3a1_3 = MathTex(r"f(0) &= 2(0) + 3\\ &= 0 + 3 \\ &= 3").next_to(ex3a1, DOWN)
		line3c_1 = ex3a1_3[0][0:11]
		self.play(Write(line3c_1))
		self.wait()
		line3c_2 = ex3a1_3[0][11:15]
		self.play(Write(line3c_2))
		self.wait()
		line3c_3 = ex3a1_3[0][15:17]
		self.play(Write(line3c_3))
		box3a1_3 = SurroundingRectangle(ex3a1_3[0][16])
		self.play(Create(box3a1_3))
		self.remove(ex3a1_3, ex3a1, box3a1_3, line3c_1, line3c_2, line3c_3)

		ex2 = MathTex(r"f(x) &= 3x^2-1", substrings_to_isolate="x").set_color_by_tex("x", '#00FFEE')
		self.play(Write(ex2))

		ex3b1_1 = MathTex(r"f(2) &= 3(2)^2-1 \\ &= 3(4) - 1 \\ &= 12-1 \\ &=11").next_to(ex2, DOWN)
		line3b1_1 = ex3b1_1[0][0:12]
		self.play(Write(line3b1_1))
		self.wait()
		
		# self.play(Write(ex3b1_1))
		box3b1_1 = SurroundingRectangle(ex3b1_1[0][-2:])
		self.play(Create(box3b1_1))
		self.remove(ex3b1_1, box3b1_1)

		ex3b1_2 = MathTex(r"f(-2) &= 3(-2)^2-1 \\ &= 3(4) - 1 \\ &= 12-1 \\ &=11").next_to(ex2, DOWN)
		self.play(Write(ex3b1_2))
		box3b1_2 = SurroundingRectangle(ex3b1_2[0][-2:])
		self.play(Create(box3b1_2))
		self.remove(ex3b1_2, box3b1_2)

		ex3b1_3 = MathTex(r"f(0) &= 3(0)^2-1 \\ &= 3(0) - 1 \\ &= 0-1 \\ &= -1").next_to(ex2, DOWN)
		self.play(Write(ex3b1_3))
		box3b1_3 = SurroundingRectangle(ex3b1_2[0][-2:])
		self.play(Create(box3b1_3))
		self.remove(ex2, ex3b1_3, box3b1_3)

		ex3c_axes = Axes(x_range=[-3,3,1], y_range=[-2,5,1]).add_coordinates()

		def func(x):
			return x**2 - 1

		graph = ex3c_axes.get_graph(func)
		self.play(Create(ex3c_axes))
		self.wait()
		self.add(graph)
		self.wait()

		vline1 = ex3c_axes.get_vertical_line(ex3c_axes.c2p(2, func(2)))
		self.play(Create(vline1))
		dot1 = Dot(ex3c_axes.c2p(2, func(2)), radius = 0.15, color=YELLOW)
		self.play(Create(dot1))
		hline1 = ex3c_axes.get_horizontal_line(ex3c_axes.c2p(2, func(2)))
		self.play(Create(hline1))

		self.remove(vline1, dot1, hline1)

		vline2 = ex3c_axes.get_vertical_line(ex3c_axes.c2p(-2, func(-2)))
		self.play(Create(vline2))
		dot2 = Dot(ex3c_axes.c2p(-2, func(-2)), radius = 0.15, color=YELLOW)
		self.play(Create(dot2))
		hline2 = ex3c_axes.get_horizontal_line(ex3c_axes.c2p(-2, func(-2)))
		self.play(Create(hline2))

		self.remove(vline2, dot2, hline2)

		dot3 = Dot(ex3c_axes.c2p(0, func(0)), radius = 0.15, color=YELLOW)
		self.play(Create(dot3))

		self.remove(dot3, graph, ex3c_axes)

		tbl = Table([["x","-3", "-2", "-1", "0", "1", "2", "3"], 
			["f(x)","-6", "3", "4", '-3', "-8", "6", "-5"]])
		self.play(Create(tbl))
		self.wait()
		self.play(Indicate(tbl.get_entries((1,7))))
		box2 = SurroundingRectangle(tbl.get_entries((2,7)))
		self.play(Create(box2))
		self.wait()
		self.remove(box2)
		self.wait()
		self.play(Indicate(tbl.get_entries((1,3))))
		box3 = SurroundingRectangle(tbl.get_entries((2,3)))
		self.play(Create(box3))
		self.wait()
		self.remove(box3)
		self.wait()
		self.play(Indicate(tbl.get_entries((1,5))))
		box4 = SurroundingRectangle(tbl.get_entries((2,5)))
		self.play(Create(box4))
		self.wait()
		self.remove(box4)
		self.wait()

