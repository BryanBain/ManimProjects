from manim import *

class LogsExps(Scene):
	def construct(self):
		title = Title("Logarithms and Exponents")
		intro = Text("Logarithms allow us to find the value of an exponent \n"
			"when we know the base and result.").scale(0.9)
		expon_form = MathTex("\\text{base} ^ \\text{exponent} = \\text{result} ")
		log_form = MathTex("\\log_{\\text{base}}\\left(\\text{result}\\right) = \\text{exponent}")
		log = log_form[0][0:3]
		base = log_form[0][3:7]
		lp = log_form[0][7]
		rp = log_form[0][14]
		parentheses = VGroup(lp, rp)
		result = log_form[0][8:14]
		equals = log_form[0][15]
		exponent = log_form[0][16:]
		exp_arrow = Arrow(start=[-0.5,2,0], end=LEFT, color=YELLOW)

		self.add(title)
		self.play(Write(intro))
		self.wait()
		self.remove(title, intro)
		self.wait()
		self.play(Write(expon_form))
		self.wait()
		self.play(ApplyMethod(expon_form.shift, UP*2))
		self.wait()
		# self.play(Write(exp_arrow))
		self.play(Write(log))
		self.play(Write(base))
		self.wait()
		self.play(Write(parentheses))
		self.play(Write(result))
		self.play(Write(equals))
		self.play(Write(exponent))