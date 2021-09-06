from manim import *

class LogsExps(Scene):
	def construct(self):
		title = Title("Logarithms and Exponents")
		intro = Text("Logarithms allow us to find the value of an exponent \n"
			"when we know the base and result.").scale(0.9)
		expon_form = Tex('base', r'$^\text{exponent}$', r'$=$', 'result')
		base = expon_form[0]
		exponent = expon_form[1]
		result = expon_form[2]
		expon_form.set_color_by_tex('as', YELLOW)
		expon_form.set_color_by_tex('ext{exponent', BLUE)
		expon_form.set_color_by_tex('esul', ORANGE)

		log_form = Tex(r'$\log$', r'$_\text{base}$', r'$($', 'result', r'$)$', r'$=$', 'exponent' )
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

		# expon_form = MathTex("\\text{base} ^ \\text{exponent} = \\text{result} ")
		# log_form = MathTex("\\log_{\\text{base}}\\left(\\text{result}\\right) = \\text{exponent}")
		# log = log_form[0][0:3]
		# base = log_form[0][3:7]
		# lp = log_form[0][7]
		# rp = log_form[0][14]
		# parentheses = VGroup(lp, rp)
		# result = log_form[0][8:14]
		# equals = log_form[0][15]
		# exponent = log_form[0][16:]
		base_arrow = Arrow(start=[-1.65,1.9,0], end=[-1.65,-0.2,0], color=YELLOW)
		result_arrow = Arrow(start=[1.65,1.9,0], end=[-0.6,0.1,0], color=ORANGE)

		self.add(title)
		self.play(Write(intro))
		self.wait()
		self.remove(title, intro)
		self.wait()
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
		self.play(Write(log_expon))
		# self.play(Write(exp_arrow))
		# self.play(Write(log))
		# self.play(Write(base.shift(DOWN)))
		
		self.wait()
		# self.play(Write(parentheses))
		# self.play(Write(result))
		# self.play(Write(equals))
		# self.play(Write(exponent))
		# self.remove(log, base, parentheses, result, equals, exponent)
