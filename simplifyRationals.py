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
		num_common_factor_1_1a = ex1_1a[0][1:4]
		den_common_factor_1_1a = ex1_1a[0][11:14]
		common_factors_1_1a = VGroup(num_common_factor_1_1a, den_common_factor_1_1a)
		self.play(FadeToColor(common_factors_1_1a, YELLOW, run_time=0.01))
		self.play(ReplacementTransform(ex1_1, ex1_1a))
		ex1_2 = MathTex("\\frac{1(x+3)}{1}").scale(2)
		self.play(ReplacementTransform(ex1_1a, ex1_2))
		num_common_factor1_2 = ex1_2[0][0]
		den_common_factor1_2 = ex1_2[0][-1]
		common_factors1_2 = VGroup(num_common_factor1_2, den_common_factor1_2)
		self.play(FadeToColor(common_factors1_2, YELLOW, run_time=0.01))
		self.wait()
		ex1_3 = MathTex("(x+3)").scale(2)
		self.play(ReplacementTransform(ex1_2, ex1_3))
		self.play(FadeOut(ex1_3))

		ex2 = MathTex("\\frac{x^2+7x+10}{x+2}").scale(2)
		self.play(FadeIn(ex2), run_time = 2)
		self.wait()
		ex2_1 = MathTex("\\frac{(x+2)(x+5)}{x+2}").scale(2)
		self.play(ReplacementTransform(ex2, ex2_1))
		self.wait()
		num_common_factor_2_1 = ex2_1[0][1:4]
		den_common_factor_2_1 = ex2_1[0][11:14]
		common_factors_2_1 = VGroup(num_common_factor_2_1, den_common_factor_2_1)
		self.play(FadeToColor(common_factors_2_1, YELLOW, run_time=0.01))
		self.wait()
		ex2_2 = MathTex("\\frac{1(x+5)}{1}").scale(2)
		self.play(ReplacementTransform(ex2_1, ex2_2))
		self.wait()
		num_common_factor_2_2 = ex2_2[0][0]
		den_common_factor_2_2 = ex2_2[0][-1]
		common_factors_2_2 = VGroup(num_common_factor_2_2, den_common_factor_2_2)
		self.play(FadeToColor(common_factors_2_2, YELLOW, run_time=0.01))
		# self.play(FadeToColor(ex2_2[0][0], YELLOW, run_time=0.01))
		# self.play(FadeToColor(ex2_2[0][-1], YELLOW, run_time=0.01))
		self.wait()
		ex2_3 = MathTex("x+5").scale(2)
		self.play(ReplacementTransform(ex2_2, ex2_3))
		self.play(FadeOut(ex2_3))

		ex3 = MathTex("\\frac{x^2-7x-18}{2x^2+3x-2}").scale(2)
		self.play(FadeIn(ex3), run_time=2)
		self.wait()
		ex3_1 = MathTex("\\frac{(x-9)(x+2)}{(2x-1)(x+2)}").scale(2)
		self.play(ReplacementTransform(ex3, ex3_1))
		self.wait()
		num_common_factor_3_1 = ex3_1[0][6:9]
		den_common_factor_3_1 = ex3_1[0][18:21]
		common_factors_3_1 = VGroup(num_common_factor_3_1, den_common_factor_3_1)
		self.play(FadeToColor(common_factors_3_1, YELLOW, run_time=0.01))
		self.wait()
		ex3_2 = MathTex("\\frac{(x-9)1}{(2x-1)1}").scale(2)
		self.play(ReplacementTransform(ex3_1, ex3_2))
		self.wait()

		num_common_factor_3_2 = ex3_2[0][5]
		den_common_factor_3_2 = ex3_2[0][-1]
		common_factors_3_2 = VGroup(num_common_factor_3_2, den_common_factor_3_2)
		self.play(FadeToColor(common_factors_3_2, YELLOW, run_time=0.01))
		# self.play(FadeToColor(ex2_2[0][0], YELLOW, run_time=0.01))
		# self.play(FadeToColor(ex2_2[0][-1], YELLOW, run_time=0.01))
		self.wait()
		ex3_3 = MathTex("\\frac{x-9}{2x-1}").scale(2)
		self.play(ReplacementTransform(ex3_2, ex3_3))
		self.play(FadeOut(ex3_3))