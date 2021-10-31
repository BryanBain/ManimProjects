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
		self.wait()

		scalar_explanation = Tex("When we mutliply a vector by a scalar,")
		scalar_explanation2 = Tex("we multiply both coordinate values by the scalar.").next_to(scalar_explanation, DOWN)
		scalar_group = VGroup(scalar_explanation, scalar_explanation2)
		self.play(Write(scalar_group))
		self.wait()
		self.remove(scalar_group)

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
		a_vec_lbl = Tex(r"$\vec{a} = \begin{bmatrix} 3 \\ -2 \end{bmatrix}$", 
			color=YELLOW).shift(4*RIGHT)
		a_group = VGroup(a_vec, a_vec_name, a_vec_lbl)
		neg_vec = Line(plane2.c2p(0,0), plane2.c2p(-3,2), 
			color=RED).add_tip()
		neg_vec_name = Tex(r"$-\vec{a}$", color=ORANGE).next_to(neg_vec, LEFT)
		neg_vec_lbl = Tex(r"$-1\vec{a} = \begin{bmatrix} -3 \\ 2 \end{bmatrix}$", 
			color=ORANGE).shift(4*RIGHT)
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

		example_text = Tex(r"Given $\vec{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}$ and "
			r"$\vec{w}=\begin{bmatrix} -2 \\ 0 \end{bmatrix}$, find $3\vec{v}+\vec{w}$")
		self.play(Write(example_text))
		self.wait()
		self.remove(example_text)

		example_plane = NumberPlane(x_range=[-4,4,1], 
			y_range=[-4,4,1]).add_coordinates().to_edge(LEFT)
		v_example = Line(start=example_plane.c2p(0,0), 
			end=example_plane.c2p(1,-1), color=YELLOW).add_tip()
		v_example_lbl = Tex(r"$\vec{v}$", color=YELLOW).next_to(v_example.get_center())
		v_example_tex = Tex(r"$\vec{v}=\begin{bmatrix} 1 \\ -1 \end{bmatrix}$").shift(3.5*RIGHT + 2*UP)
		self.play(Create(example_plane))
		self.play(Create(v_example))
		self.play(Write(v_example_lbl))
		self.play(Write(v_example_tex))

		w_example = Line(start=example_plane.c2p(0,0), end=example_plane.c2p(-2,0),
			color=BLUE).add_tip()
		w_example_lbl = Tex(r"$\vec{w}$", color=BLUE).next_to(w_example, UP)
		w_example_tex = Tex(r"$\vec{w}=\begin{bmatrix} -2 \\ 0 \end{bmatrix}$").next_to(v_example_tex, RIGHT)
		self.play(Create(w_example))
		self.play(Write(w_example_lbl))
		self.play(Write(w_example_tex))
		w_example_lbl.add_updater(lambda x: x.next_to(w_example, UP))
		scale_v_example = Line(start=example_plane.c2p(0,0), 
			end=example_plane.c2p(3,-3), color=YELLOW).add_tip()
		scale_v_lbl = Tex(r"$3\vec{v}$", color=YELLOW).next_to(scale_v_example)
		scale_v_tex = Tex(r"$3\vec{v} = \begin{bmatrix} 3 \\ -3 \end{bmatrix}$").next_to(w_example_tex, LEFT)
		self.play(Transform(v_example, scale_v_example))
		self.play(Transform(v_example_lbl, scale_v_lbl))
		self.play(Transform(v_example_tex, scale_v_tex))
		example_resultant = Line(start=example_plane.c2p(3,-3), end=example_plane.c2p(1,-3),
			color=BLUE).add_tip()
		self.play(Transform(w_example, example_resultant))
		self.wait()

		vec_sum = Line(start=example_plane.c2p(0,0), end=example_plane.c2p(1,-3),
			color=PURPLE).add_tip()
		vec_sum_lbl = Tex(r"$\vec{v}+\vec{w}$", color=PURPLE).next_to(vec_sum, LEFT)
		vec_sum_tex = Tex(r"$3\vec{v} + \vec{w} = \begin{bmatrix} 1 \\ -3 \end{bmatrix}$", color=PURPLE).next_to(scale_v_tex, 2*DOWN)
		self.wait()
		self.play(Create(vec_sum))
		self.play(Write(vec_sum_lbl))
		self.play(Write(vec_sum_tex))
		self.wait()

class BasisVectors(VectorScene):
	def construct(self):
		basis_text = Tex(r"Two important vectors are")
		basis_text2 = Tex(r"$\hat{i} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ and $\hat{j} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$").next_to(basis_text, DOWN)
		basis_text_group = VGroup(basis_text, basis_text2)
		self.play(Write(basis_text_group))
		self.wait()
		self.play(basis_text_group.animate.shift(3*UP))
		basis_text3 = Tex("These will serve as the basis for matrix multiplication.")
		self.play(Write(basis_text3))
		self.wait()
		self.remove(basis_text_group, basis_text3)

		plane = self.add_plane(animate=True)
		self.wait()
		bases = self.get_basis_vectors()
		bases_lbls = self.get_basis_vector_labels()
		self.wait()
		self.play(Create(bases))
		self.play(Create(bases_lbls))
		self.wait()
		self.remove(bases, bases_lbls, plane)
		self.wait()

		basis_combination = Tex(r"Any vector can be written as a combination of a scalar ")
		basis_combination2 = Tex(r"and the basis vectors $\hat{\imath}$ and $\hat{\jmath}.$").next_to(basis_combination, DOWN)
		basis_text = VGroup(basis_combination, basis_combination2)
		self.play(Write(basis_text))
		self.wait()
		self.remove(basis_text)
		self.wait()

		plane = self.add_plane(animate=True)
		self.wait()
		v = self.add_vector([3,2], color=YELLOW)
		self.wait()
		v_coords = self.vector_to_coords(v)
		self.wait()
		v_lbl = Tex(r"$3\hat{\imath} + 2\hat{\jmath}$", color=YELLOW).move_to(4*RIGHT + 2*UP)
		self.wait()
		self.play(Write(v_lbl))
		self.wait()
		self.remove(v, v_lbl, plane)
		self.wait()

		example = Tex("Example.", r"Write ", r"$\vec{w} = \begin{bmatrix} -3 \\ 1 \end{bmatrix}$", r" using the basis vectors $\hat{\imath}$ and $\hat{\jmath}$.",)
		example.set_color_by_tex("xample", '#FE0000')
		self.play(Write(example))
		self.wait()
		self.play(example.animate.shift(2*UP))
		self.wait()
		i_box = SurroundingRectangle(example[2][4:6])
		self.play(Create(i_box))
		self.wait()
		answer = Tex(r"$\vec{w} = -3\hat{\imath}$")
		self.play(Write(answer))
		self.wait()
		self.remove(i_box)
		j_box = SurroundingRectangle(example[2][6])
		self.play(Create(j_box))
		self.wait()
		answer2 = Tex(r"$+\hat{\jmath}$").next_to(answer, RIGHT)
		self.play(Write(answer2))
		self.remove(j_box)
		self.wait()

class Matrices(Scene):
	def construct(self):
		title = Title("Matrices")
		self.play(Write(title))
		definition = Text("A matrix is a rectangular array of numbers.", t2c = {' matri': RED}).move_to(UP)
		self.play(Write(definition))
		self.wait()
		description = Text("It can be composed of vectors or, possibly, scalars").next_to(definition, DOWN)
		self.play(Write(description))
		self.wait()

		m = Matrix([
			[8,6,7,5],
			[3,0,9,-2],
			[0,1,-10,7]
			]).next_to(description, DOWN)
		m_lbl = Tex(r"$A=$").next_to(m, LEFT)
		matrix_example = VGroup(m_lbl, m)
		self.play(Write(matrix_example))
		self.wait()
		self.remove(title, definition, description)
		self.play(matrix_example.animate.shift(3*UP))
		self.wait()
		elements_def = Tex(r"Each of the values in a matrix are called ", r"elements.").next_to(matrix_example, DOWN)
		elements_def.set_color_by_tex('lement',ORANGE)
		self.play(Write(elements_def))
		self.wait()
		element_example = Tex(r"$a_{12}=6$").next_to(elements_def, 2*DOWN)
		self.play(Write(element_example))
		self.wait()
		self.remove(matrix_example, elements_def, element_example)

		vec_matrix1 = Tex(r"We can think of a matrix as ")
		vec_matrix2 = Tex(r"several vectors in the coordinate plane.").next_to(vec_matrix1, DOWN)
		vec_matrix = VGroup(vec_matrix1, vec_matrix2)
		self.play(Write(vec_matrix))
		self.wait()
		self.remove(vec_matrix)

		a = Tex(r"$\begin{bmatrix} 3 & -1 & -5 \\ 2 & -4 & 3 \end{bmatrix}$").to_edge(RIGHT)
		plane = NumberPlane(x_range=[-5,4,1], y_range=[-5,4,1]).add_coordinates().to_edge(LEFT)
		self.play(Create(plane))
		self.wait()
		self.play(Write(a))
		self.wait()
		vec1x = a[0][1]
		vec1y = a[0][6]
		vec1 = VGroup(vec1x, vec1y)
		box1 = SurroundingRectangle(vec1)
		self.play(Create(box1))
		self.wait()
		vec1_draw = Line(plane.c2p(0,0), plane.c2p(3,2), color=YELLOW).add_tip()
		self.play(Create(vec1_draw))
		self.remove(box1)
		self.wait()
		vec2x = a[0][2:4]
		vec2y = a[0][7:9]
		vec2 = VGroup(vec2x, vec2y)
		box2 = SurroundingRectangle(vec2, color=BLUE)
		self.play(Create(box2))
		self.wait()
		vec2_draw = Line(plane.c2p(0,0), plane.c2p(-1,-4), color=BLUE).add_tip()
		self.play(Create(vec2_draw))
		self.remove(box2)
		self.wait()
		vec3x = a[0][4:6]
		vec3y = a[0][9]
		vec3 = VGroup(vec3x, vec3y)
		box3 = SurroundingRectangle(vec3, color=ORANGE)
		self.play(Create(box3))
		self.wait()
		vec3_draw = Line(plane.c2p(0,0), plane.c2p(-5,3), color=ORANGE).add_tip()
		self.play(Create(vec3_draw))
		self.remove(box3)
		self.wait()










