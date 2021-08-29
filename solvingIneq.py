from manim import *

class SolveIneq(Scene):
	def construct(self):
		intro_text = Text("Solving inequalities is a lot like solving equations.")
		intro_text1 = Text("However, you will need to flip the inequality sign \n"
			"if you multiply or divide both sides by a \n"
			"negative number.", t2c = {'[59:]': BLUE}, t2w = {'[59:]': BOLD},
			t2s = {'flip': ITALIC}, disable_ligatures = True)
		intro_text1.scale(0.95)
		intro_text.shift(UP*2)

		intro_text2 = Text("You will also have to graph your solution on a number line.")
		intro_text2.scale(0.8)

		intro_text3 = Text("The following table can help for answers in the form").scale(0.8)
		intro_text4 = MathTex("x \\quad \\text{INEQUALITY SIGN} \\quad \\text{NUMBER}").scale(1.2)
		intro_text4.shift(DOWN)
		text3_4 = VGroup(intro_text3, intro_text4)

		tbl = Table([
			['Open', 'Left'],
			['Open', 'Right'],
			['Closed', 'Left'],
			['Closed', 'Right']
			],
			row_labels = [Text('<'), Text('>'), Text('≤'), Text('≥')], 
			col_labels = [Text('Circle'), Text('Shade')])

		ex1 = Text("Example. Solve and graph your solution on a number line.",
			t2c = {'[:8]': '#FF0000'}, t2w = {'[:8]': BOLD}).scale(0.8)
		eq1 = MathTex("-2x + 7 \\geq 5x + 14")
		eq1_step = MathTex("\\text{subtract } 5x \\text{ from both sides}.")
		eq1_step.shift(DOWN)
		eq2 = MathTex("-2x - 5x + 7 \\geq 5x -5x + 14")
		eq3 = MathTex("-7x + 7 \\geq 14")
		eq3_step = MathTex("\\text{subtract } 7 \\text{ from both sides}.")
		eq3_step.shift(DOWN)
		eq4 = MathTex("-7x + 7 - 7 \\geq 14 - 7")
		eq5 = MathTex("-7x \\geq 7")
		eq5_step = MathTex("\\text{divide both sides by } -7.")
		eq5_step.shift(DOWN)
		eq6 = MathTex("\\frac{-7x}{-7} \\geq \\frac{7}{-7}")
		eq7 = MathTex("x \\leq -1", tex_to_color_map={"\\leq":RED})

		numLine = NumberLine([-6,3],include_numbers = True)
		vec = Arrow([0.75,0,0], [-6,0,0], color=YELLOW)
		dot = Dot([0.5,0,0], radius = 0.15, color=YELLOW)

		self.play(Write(intro_text), run_time=4)
		self.play(Write(intro_text1), run_time=6)
		self.remove(intro_text, intro_text1)
		self.play(Write(intro_text2), run_time=3)
		self.remove(intro_text2)
		self.play(Write(text3_4), run_time=3)
		self.wait()
		self.remove(text3_4)
		self.play(Write(tbl))
		self.wait(3)
		self.remove(tbl)
		self.play(Write(ex1))
		self.wait()
		self.remove(ex1)
		self.play(Write(eq1))
		self.play(Write(eq1_step))
		self.play(ReplacementTransform(eq1, eq2), run_time=2)
		self.remove(eq1_step)
		self.play(ReplacementTransform(eq2, eq3), run_time=2)
		self.play(Write(eq3_step))
		self.play(ReplacementTransform(eq3, eq4), run_time=2)
		self.play(ReplacementTransform(eq4, eq5), run_time=2)
		self.remove(eq3_step)
		self.play(Write(eq5_step))
		self.play(ReplacementTransform(eq5, eq6), run_time=2)
		self.play(ReplacementTransform(eq6, eq7), run_time=2)
		self.remove(eq5_step)
		self.wait()
		self.remove(eq7)
		self.play(Write(numLine))
		self.play(Write(dot))
		self.play(Write(vec))

