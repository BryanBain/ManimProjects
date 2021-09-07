from manim import *

class LogsExps(Scene):
	def construct(self):
		title = Title("Logarithms and Exponents")
		intro = Text("Logarithms allow us to find the value of an exponent \n"
			"when we know the base and result.").scale(0.9)
		intro2 = Text("For instance suppose we want to know what x is in", t2s={'x':ITALIC}).next_to(intro, DOWN*1.5).scale(0.9)
		intro3 = Tex(r"$2^x = 50$").next_to(intro2, DOWN*2).scale(1.5)

		ax = Axes(x_range=[-2,7], y_range=[0,60,10]).add_coordinates()

		def double(x):
			return 2**x

		graph = ax.get_graph(double, color=RED)
		dot = Dot(ax.c2p(5.64,50), color=BLUE)
		dotted_lines = ax.get_lines_to_point(ax.c2p(5.64,50), color=BLUE)
		func_name = Tex(r'$f(x)=2^x$', color=RED).next_to(dot, UR)

		expon_form = Tex('base', r'$^\text{exponent}$', r'$\, = \,$', 'result')
		base = expon_form[0]
		exponent = expon_form[1]
		result = expon_form[2]
		expon_form.set_color_by_tex('as', YELLOW)
		expon_form.set_color_by_tex('ext{exponent', BLUE)
		expon_form.set_color_by_tex('esul', ORANGE)

		log_form = Tex(r'$\log$', r'$_\text{base}$', r'$($', 'result', r'$)$', r'$\, = \,$', 'exponent' )
		log_form.set_color_by_tex('ext{base', YELLOW)
		log_form.set_color_by_tex('xponen', BLUE)
		log_form.set_color_by_tex('esul', ORANGE)
		log = log_form[0]
		log_base = log_form[1]
		lp = log_form[2]
		log_result = log_form[3]
		rp = log_form[4]
		parentheses = VGroup(lp, rp)
		log_equals = log_form[5]
		log_expon = log_form[6]

		base_arrow = Arrow(start=[-1.65,1.9,0], end=[-1.65,-0.2,0], color=YELLOW)
		result_arrow = Arrow(start=[1.65,1.9,0], end=[-0.6,0.1,0], color=ORANGE)
		expon_arrow = Arrow(start=[-0.75,2,0], end=[1.65,0.1,0], color=BLUE)

		example_text = Text("Example. Write in logarithmic form.", t2c={'Example.':RED}).shift(UP*3)
		example = Tex(r'2', r'$^x$', r'$\, = \,$', '50').next_to(example_text, DOWN*2).scale(1.5)
		answer = Tex(r'$\log$', r'$_2$', r'$($', '50', r'$)$', ' = ', '$x$').next_to(example, DOWN*3).scale(1.5)
		ex_parentheses = VGroup(answer[2], answer[4])

		calc_text = Tex('You can use a calculator to evaluate ', r'$\log_2(50)$:').shift(DOWN)
		calc = Tex(r'$\log_2(50) \approx 5.644$').next_to(calc_text, DOWN*1.5)

		self.add(title)
		self.play(Write(intro))
		self.wait()
		self.play(Write(intro2))
		self.play(Write(intro3))
		self.wait(2)
		self.remove(title, intro, intro2, intro3)
		self.wait()

		self.add(ax, graph, dot, func_name)
		self.wait(2)
		self.play(Write(dotted_lines))
		self.wait()
		self.remove(ax, graph, dotted_lines, dot, func_name)

		self.play(Write(expon_form))
		self.wait()
		self.play(ApplyMethod(expon_form.shift, UP*2))
		self.wait()
		self.play(Write(log))
		self.wait()
		self.play(Write(base_arrow))
		self.wait()
		self.play(Write(log_base))
		self.remove(base_arrow)
		self.play(Write(parentheses))
		self.play(Write(result_arrow))
		self.wait()
		self.play(Write(log_result))
		self.remove(result_arrow)
		self.play(Write(log_equals))
		self.wait()
		self.play(Write(expon_arrow))
		self.play(Write(log_expon))
		self.remove(expon_arrow)
		self.wait(2)
		self.remove(expon_form, log_form, log, parentheses, log_base, log_equals, log_result, log_expon)
		self.wait()

		self.play(Write(example_text))
		self.wait()
		self.play(Write(example))
		self.wait()
		self.play(Write(answer[0]))
		self.play(Indicate(example[0]))
		self.play(Write(answer[1].scale(0.8)))
		self.play(Write(ex_parentheses))
		self.play(Indicate(example[3]))
		self.play(Write(answer[3]))
		self.play(Write(answer[5]))
		self.play(Indicate(example[1]))
		self.play(Write(answer[6]))
		self.play(Create(SurroundingRectangle(answer)))
		self.wait()
		self.remove(example_text, example)
		self.play(Write(calc_text))
		self.wait()
		self.play(Write(calc))
		self.wait()
