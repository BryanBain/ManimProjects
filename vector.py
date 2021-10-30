from manim import *

class IntroVectors(Scene):
	def construct(self):
		plane = NumberPlane(x_range=(-2,5), y_range=(-2,5)).to_edge(LEFT)
		self.add(plane)
		intro_vec = plane.get_vector([3,4], color=YELLOW)
		self.play(Create(intro_vec))
		v = Matrix([[3],[4]])
		vec_tex = Tex(r"$\vec{v} = $").next_to(v, LEFT)
		vec1 = VGroup(vec_tex, v).shift(2*RIGHT + 2*UP)
		self.play(Write(vec1))

class VectorAddition(VectorScene):
	def construct(self):
		title = Title("Adding Vectors")
		self.play(Write(title))

		v = Matrix([[3],[4]])
		v_tex = Tex(r"$\vec{v} = $").next_to(v, LEFT)
		w = Matrix([[2],[-3]])
		w_tex = Tex(r"$\vec{w} = $").next_to(w, LEFT)
		vec_v = VGroup(v_tex, v)
		vec_w = VGroup(w_tex, w).next_to(vec_v, 2*RIGHT)
		vec_group = VGroup(vec_v, vec_w)
		self.play(Write(vec_group))
		# self.wait()
		self.play(vec_group.animate.shift(1.5*UP))

		addition = Tex(r"$\vec{v} + \vec{w}$")
		self.play(Write(addition))

		VplusW = Matrix([[3],[4]]).next_to(addition,DOWN)
		plus = Tex(r"$+$").next_to(VplusW, RIGHT)
		VplusW_2 = Matrix([[2],[-3]]).next_to(plus,RIGHT)
		equals = Tex(r"$=$").next_to(VplusW_2, RIGHT)
		vec_group2 = VGroup(VplusW, plus, VplusW_2)
		self.play(Write(vec_group2))
		self.play(Write(equals))
		resultant = Matrix([[5],[1]]).next_to(equals,RIGHT)
		self.play(Write(resultant))

		self.remove(title, vec_group, addition, vec_group2, resultant, equals)

		plane = NumberPlane(x_range = (-2,6), y_range=(-4,5)).to_edge(LEFT)
		self.add(plane)
		v_vector = Arrow(plane.c2p(0,0), plane.c2p(3,4), buff=0, color=YELLOW)
		self.play(Create(v_vector))
		w_vector = Arrow(plane.c2p(0,0), plane.c2p(2,-3), buff=0, color=BLUE)
		self.play(Create(w_vector))
		self.play(w_vector.animate.shift(3*RIGHT, 4*UP))
		resultant_vec = Arrow(plane.c2p(0,0), plane.c2p(5,1), buff=0 , color=ORANGE)
		self.play(Create(resultant_vec))
		resultant_tex = Tex(r"$\vec{v}+\vec{w}$", color=ORANGE).next_to(resultant_vec)
		self.play(Write(resultant_tex))

class VectorScaling(Scene):
	def construct(self):
		scalar_def = Text("A scalar is another name for a real number.", t2c={' scala': BLUE})
		self.play(Write(scalar_def))
		self.remove(scalar_def)

		plane = NumberPlane(x_range=[-1,7,1], y_range=[-6,3,1], 
			x_length=8, y_length=8, axis_config={"unit_size":0.5}).add_coordinates().to_edge(LEFT)
		self.play(Create(plane))

		a_vec = Line(plane.c2p(0,0), plane.c2p(3,-2), color=YELLOW).add_tip()
		a_vec_name = Tex(r"$\vec{a}$", color=YELLOW).next_to(a_vec, RIGHT)
		a_vec_lbl = Tex(r"$\vec{a} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}$", color=YELLOW).shift(3*RIGHT)
		a_group = VGroup(a_vec, a_vec_name, a_vec_lbl)
		dbl_vec = Line(plane.c2p(0,0), plane.c2p(6,-4), color=RED).add_tip()
		dbl_vec_name = Tex(r"$2\vec{a}$", color=ORANGE).next_to(a_vec, RIGHT)
		dbl_vec_lbl = Tex(r"$2\vec{a} = \begin{bmatrix} 6 \\ -4 \end{bmatrix}$", color=ORANGE).shift(3*RIGHT)
		dbl_group = VGroup(dbl_vec, dbl_vec_name, dbl_vec_lbl)

		self.play(Create(a_vec))
		self.play(Write(a_vec_name))
		self.wait()
		self.play(Write(a_vec_lbl))
		self.wait()
		self.play(Transform(a_group, dbl_group))
		self.wait()
		self.remove(a_group, dbl_group, plane)
		self.wait()

		plane2 = NumberPlane(x_range=[-5,4,1], y_range=[-3,3,1]).add_coordinates().to_edge(LEFT)
		self.play(Create(plane2))
		self.wait()

		a_vec = Line(plane2.c2p(0,0), plane2.c2p(3,-2), color=YELLOW).add_tip()
		a_vec_name = Tex(r"$\vec{a}$", color=YELLOW).next_to(a_vec, RIGHT)
		a_vec_lbl = Tex(r"$\vec{a} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}$", color=YELLOW).shift(4*RIGHT)
		a_group = VGroup(a_vec, a_vec_name, a_vec_lbl)
		neg_vec = Line(plane2.c2p(0,0), plane2.c2p(-3,2), color=RED).add_tip()
		neg_vec_name = Tex(r"$-\vec{a}$", color=ORANGE).next_to(a_vec, RIGHT)
		neg_vec_lbl = Tex(r"$-\vec{a} = \begin{bmatrix} -3 \\ 2 \end{bmatrix}$", color=ORANGE).shift(4*RIGHT)
		neg_group = VGroup(neg_vec, neg_vec_name, neg_vec_lbl)

		self.play(Create(a_vec))
		self.play(Write(a_vec_name))
		self.wait()
		self.play(Write(a_vec_lbl))
		self.wait()
		self.play(Transform(a_group, neg_group))
		self.wait()
		self.remove(a_group, neg_group, plane2)
		self.wait()