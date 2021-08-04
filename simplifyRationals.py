from manim import *
import numpy as np

class SimplifyRationals(Scene):
	def construct(self):
		section_name = Title("Simplifying Rational Expressions").scale(1.5)
		step1 = Text("1. Factor the numerator and denominator completely.", 
			t2c={' Facto':RED}
			)
		step2 = Text("2. Divide out any common factors.")
		VGroup(step1, step2).arrange(DOWN, buff=1)
		self.add(section_name)
		self.wait()
		self.play(FadeOut(section_name, run_time=1))
		self.play(FadeIn(step1), run_time=2)
		self.play(FadeIn(step2), run_time=2)
		self.play(FadeOut(step1, run_time=1))
		self.play(FadeOut(step2, run_time=1))

		directions = Text("Example 1. Simplify each completely.")
		self.add(directions)
		self.wait()
		self.play(FadeOut(directions, run_time=1))

		ex1 = MathTex("\\frac{x^2+4x+3}{x+1}").scale(2)
		self.play(FadeIn(ex1),run_time = 2)
		self.wait()
		ex1_1 = MathTex("\\frac{(x+1)(x+3)}{x+1}").scale(2)
		self.play(ReplacementTransform(ex1, ex1_1))
		self.wait()
		ex1_1a = MathTex("\\frac{(x+1)(x+3)}{x+1}").scale(2)
		self.play(FadeToColor(ex1_1a[0][1:4], YELLOW))
		self.play(FadeToColor(ex1_1a[0][11:14], YELLOW))
		self.play(ReplacementTransform(ex1_1, ex1_1a))
		ex1_2 = MathTex("\\frac{1(x+3)}{1}").scale(2)
		self.play(ReplacementTransform(ex1_1a, ex1_2))
		self.play(FadeToColor(ex1_2[0][0], YELLOW))
		self.play(FadeToColor(ex1_2[0][-1], YELLOW))
		self.wait()
		ex1_3 = MathTex("(x+3)").scale(2)
		self.play(ReplacementTransform(ex1_2, ex1_3))