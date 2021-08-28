from manim import *

class SolveIneq(Scene):
	def construct(self):
		# text=Text("\\justifying {First we conceptualize an undirected graph  ${G}$  as a union of a finite number of line segments residing in  ${\\mathbb{{{C}}}}$ . By taking our earlier parametrization, we can create an almost trivial extension to  ${\\mathbb{{{R}}}}^{{{3}}}$ . In the following notation, we write a bicomplex number of a 2-tuple of complex numbers, the latter of which is multiplied by the constant  ${j}$ .  ${z}_{{0}}\\in{\\mathbb{{{C}}}}_{{>={0}}}$  is an arbitrary point in the upper half plane from which the contour integral begins. The function  ${\\tan{{\\left(\\frac{{{\\theta}-{\\pi}}}{{z}}\\right)}}}:{\\left[{0},{2}{\\pi}\\right)}\\to{\\left[-\\infty,\\infty\\right)}$  ensures that the vertices at  $\\infty$  for the Schwarz-Christoffel transform correspond to points along the branch cut at  ${\\mathbb{{{R}}}}_{{+}}$ .}")
		# text.scale(0.6)
		# self.play(FadeIn(text))
		# self.wait(1)
		# self.play(FadeOut(text))

		intro_text = Text("Solving inequalities is a lot like solving equations.")
		intro_text1 = Text("However, you will need to flip the inequality sign \n"
			"when you multiply or divide both sides by a \n"
			"negative number.", t2c = {'[61:]': BLUE}, t2w = {'[61:]': BOLD},
			t2s = {'flip': ITALIC}, disable_ligatures = True)
		intro_text1.scale(0.95)
		intro_text.shift(UP*2)

		intro_text2 = Text("You will also have to graph your solution on a number line.")
		intro_text2.scale(0.8)

		tbl = Table([
			['Open', 'Left'],
			['Open', 'Right'],
			['Closed', 'Left'],
			['Closed', 'Right']
			],
			row_labels = [Text('<'), Text('>'), Text('≤'), Text('≥')], 
			col_labels = [Text('Circle'), Text('Shade')])

		ex1 = Text("Example 1. Solve and graph your solution on a number line.",
			t2c = {'[:9]': RED}, t2w = {'[:9]': BOLD}).scale(0.8)
		eq1 = MathTex(r"-2x + 7 &\\geq 5x + 10 &")
		eq2 = MathTex(r"-2x + 7 &\\geq 5x + 10 \\ -5x & -5x")

		numLine = NumberLine([-5,5],include_numbers = True)
		vec = Vector([-4,0], buff = 0.15, color=YELLOW)
		dot = Dot([0,0,0], radius = 0.15, color=YELLOW)
		# circ = Circle(radius = 0.15, color=YELLOW).move_to(RIGHT*2)

		self.play(Write(intro_text))
		self.wait()
		self.play(Write(intro_text1))
		self.wait()
		self.remove(intro_text, intro_text1)
		self.play(Write(intro_text2))
		self.wait()
		self.remove(intro_text2)
		self.play(Write(tbl))
		self.wait()
		self.remove(tbl)
		self.wait()
		self.play(Write(ex1))
		self.wait()
		self.remove(ex1)
		self.play(Write(eq1))
		self.play(Write(eq2))
		self.remove(eq1)
		self.play(Write(numLine))
		self.play(Write(dot))
		# self.play(Write(circ))
		self.play(Write(vec))

