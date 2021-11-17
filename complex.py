from manim import *
import math

class Complex(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()
        self.play(Create(plane))
        dot1 = Dot(plane.c2p(2,3), color=YELLOW)
        lbl1 = Tex(r"$2+3i$").next_to(dot1, UR)
        dot2 = Dot(plane.c2p(-4,-1), color=GREEN)
        lbl2 = Tex(r"$-4-i$").next_to(dot2, UL)
        self.wait()
        point1 = VGroup(dot1, lbl1)
        self.play(Write(point1))
        self.wait()
        point2 = VGroup(dot2, lbl2)
        self.play(Write(point2))
        self.wait()

        vec1 = Line(plane.c2p(0,0), plane.c2p(2,3), color=YELLOW).add_tip()
        self.play(Create(vec1))
        self.wait()
        vec2 = Line(plane.c2p(0,0), plane.c2p(-4,-1), color=GREEN).add_tip()
        self.play(Create(vec2))
        self.wait()

        self.remove(point1, point2, plane, vec1, vec2)
        self.wait()

class AddVecs(Scene):
  def construct(self):
    title = Title("Adding and Subtracting Complex Numbers")
    self.play(Write(title))
    self.wait()

    intro_text1 = Tex(r"Adding and subtracting complex numbers works just like")
    intro_text2 = Tex(r"adding and subtracting expressions in algebra.").next_to(intro_text1, DOWN)
    intro_text = VGroup(intro_text1, intro_text2)
    self.play(Write(intro_text))
    self.wait()
    self.remove(title, intro_text)
    
    example = Tex(r"$(2+3i)$", r"$+$", r"$(-4-i)$").to_edge(UR, buff=1)
    answer = Tex(r"$-2 + 2i$").next_to(example, 1.5*DOWN)
    self.play(Write(example))
    self.wait()
    plane = ComplexPlane(x_range = [-5,5,1], y_range = [-5,5,1],
                         x_length = 8, y_length=8).add_coordinates().to_edge(LEFT)
    self.play(Create(plane))
    self.wait()

    real1 = example[0][1]
    real1_box = SurroundingRectangle(real1)
    real2 = example[2][1:3]
    real2_box = SurroundingRectangle(real2)
    self.play(Create(real1_box))
    self.play(Create(real2_box))
    self.wait()
    self.play(Write(answer[0][0:2]))
    self.wait()
    self.remove(real1_box, real2_box)
    self.wait()

    imag1 = example[0][3:5]
    imag1_box = SurroundingRectangle(imag1)
    imag2 = example[2][3:5]
    imag2_box = SurroundingRectangle(imag2)
    self.play(Create(imag1_box))
    self.play(Create(imag2_box))
    self.wait()
    self.play(Write(answer[0][2:]))
    self.wait()
    self.remove(imag1_box, imag2_box)
    self.wait()
    answer_box = SurroundingRectangle(answer, color=RED)
    self.play(Create(answer_box))
    self.wait()

    answer_dot = Dot(plane.c2p(-2,2), color=YELLOW)
    answer_vec = Line(start=plane.c2p(0,0), end=plane.c2p(-2,2), 
                      color=YELLOW).add_tip()
    self.play(Create(answer_dot))
    vec1 = Line(start=plane.c2p(0,0), end=plane.c2p(2,3)).add_tip()
    self.play(Create(vec1))
    self.wait()
    self.play(example[0][1:5].animate.move_to(plane.c2p(2,1.5)).scale(0.7))
    self.wait()
    vec2 = Line(start=plane.c2p(2,3), end=plane.c2p(-2,2),
                color=ORANGE).add_tip()
    self.play(Create(vec2))
    self.wait()
    self.play(example[2][1:5].animate.move_to(plane.c2p(-1,2.75)).scale(0.7))
    self.wait()
    self.play(Create(answer_vec))
    self.wait()
    self.play(answer.animate.move_to(plane.c2p(-2,1)).scale(0.7))
    self.wait()

    
class SubVecs(Scene):
  def construct(self):
    example = Tex(r"$(2+3i)$", r"$-$", r"$(-4-i)$").to_edge(UR, buff=1)
    answer = Tex(r"$6 + 4i$").next_to(example, 1.5*DOWN)
    self.play(Write(example))
    self.wait()
    plane = ComplexPlane(x_range = [0,7,1], y_range = [0,6,1],
                         x_length = 8, y_length=6).add_coordinates().to_edge(LEFT)
    self.play(Create(plane))
    self.wait()

    real1 = example[0][1]
    real1_box = SurroundingRectangle(real1)
    real2 = example[2][1:3]
    real2_box = SurroundingRectangle(real2)
    self.play(Create(real1_box))
    self.play(Create(real2_box))
    self.wait()
    self.play(Write(answer[0][0]))
    self.wait()
    self.remove(real1_box, real2_box)
    self.wait()

    imag1 = example[0][3:5]
    imag1_box = SurroundingRectangle(imag1)
    imag2 = example[2][3:5]
    imag2_box = SurroundingRectangle(imag2)
    self.play(Create(imag1_box))
    self.play(Create(imag2_box))
    self.wait()
    self.play(Write(answer[0][1:]))
    self.wait()
    self.remove(imag1_box, imag2_box)
    self.wait()
    answer_box = SurroundingRectangle(answer, color=RED)
    self.play(Create(answer_box))
    self.wait()

    answer_dot = Dot(plane.c2p(6,4), color=YELLOW)
    answer_vec = Line(start=plane.c2p(0,0), end=plane.c2p(6,4), 
                      color=YELLOW).add_tip()
    self.play(Create(answer_dot))
    vec1 = Line(start=plane.c2p(0,0), end=plane.c2p(2,3)).add_tip()
    self.play(Create(vec1))
    self.wait()
    self.play(example[0][1:5].animate.move_to(plane.c2p(0.75,2)).scale(0.7))
    self.wait()
    vec2 = Line(start=plane.c2p(2,3), end=plane.c2p(6,4),
                color=ORANGE).add_tip()
    self.play(Create(vec2))
    self.wait()
    self.play(example[1:3].animate.move_to(plane.c2p(3.5,3.75)).scale(0.7))
    self.wait()
    self.play(Create(answer_vec))
    self.wait()
    self.play(answer.animate.move_to(plane.c2p(4,2.25)).scale(0.7))
    self.wait()

class MultVecs(Scene):
  def construct(self):
    intro_text = Tex(r"Multiplying complex numbers is like multiplying expressions in algebra.").scale(0.8)
    self.play(Write(intro_text))
    self.wait()
    self.remove(intro_text)

    alg_example = Tex(r"\begin{align*}(4+3x)(2+x) &= 4(2) + 4(x) + 2(3x) + 3x(x) \\ &= 8 + 4x + 6x + 3x^2 \\ &= 3x^2 + 10x + 8\end{align*}").to_edge(UP, buff=1)
    self.play(Write(alg_example[0][:11]))  # (4+3x)(2+x)
    self.wait()
    self.play(Write(alg_example[0][11:33]))  # 4(2) + 4(x) + 3x(2) + 3x(x)
    self.wait()
    self.play(Write(alg_example[0][33:45]))  # 8 + 4x + 6x + 3x^2
    self.wait()
    self.play(Write(alg_example[0][45:]))  # 3x^2 + 10x + 8
    self.wait()
    self.play(Uncreate(alg_example))
    self.wait()

    example = Tex(r"$(4+3i)$", r"$(2+i)$").to_edge(UP, buff=1)
    self.play(Write(example))

    example1 = Tex(r"The only difference is we substitue $-1$")
    example2 = Tex(r"in for $i^2$ and then simplify.").next_to(example1, DOWN)
    additional_info = VGroup(example1, example2)
    self.play(Write(additional_info))
    self.wait()
    self.remove(additional_info)
    self.wait()

    complex_example = Tex(r"\begin{align*}(4+3i)(2+i) &= 4(2) + 4(i) + 3i(2) + 3i(i) \\ &= 8 + 4i + 6i + 3i^2 \\ &= 3i^2 + 10i + 8 \\ &= 3(-1) + 10i + 8 \\ &= -3 + 10i + 8 \\ &= 5 + 10i \end{align*}")
    self.play(Write(complex_example[0][:11]))  # (4+3i)(2+i)
    self.wait()
    self.play(Write(complex_example[0][11:33]))  # 4(2) + 4(i) + 2(3i) + 3i(i)
    self.wait()
    self.play(Write(complex_example[0][33:45]))  # 8 + 4i + 6i + 3i^2
    self.wait()
    self.play(Write(complex_example[0][45:55]))  # 3i^2 + 10i + 8
    self.wait()
    i2_box = SurroundingRectangle(complex_example[0][47:49])  # highlight i^2
    self.play(Create(i2_box))
    self.wait()
    self.play(Write(complex_example[0][55:67]))  # 3(-1) + 10i + 8
    self.wait()
    self.remove(i2_box)
    self.play(Write(complex_example[0][67:76]))  # -3 + 10i + 8
    self.wait()
    self.play(Write(complex_example[0][76:]))  # 5 + 10i
    self.wait()
    self.play(Uncreate(example))
    self.play(Uncreate(complex_example))
    self.wait()

    plane = ComplexPlane(x_range = [0,11,1], y_range = [0,11,1],
                         x_length = 8, y_length=8).add_coordinates().to_edge(LEFT).scale(0.95)
    self.play(Create(plane))
    self.wait()
    example = Tex(r"$4+3i$", r"$2+i$")
    complex_num1 = example[0].to_edge(UR, buff=1).set_color(YELLOW)
    self.play(Write(complex_num1))
    vec1 = Line(start=plane.c2p(0,0), end=plane.c2p(4,3), color=YELLOW).add_tip()
    self.wait()
    dot1 = Dot(plane.c2p(4,3), color=YELLOW)
    self.play(Create(dot1))
    self.wait()
    self.play(Create(vec1))
    self.wait()
    complex_num2 = example[1].next_to(complex_num1, DOWN).set_color(BLUE)
    self.play(Write(complex_num2))
    self.wait()
    vec2 = Line(start=plane.c2p(0,0), end=plane.c2p(2,1), color=BLUE).add_tip()
    self.wait()
    dot2 = Dot(plane.c2p(2,1), color=BLUE)
    self.play(Create(dot2))
    self.wait()
    self.play(Create(vec2))
    self.wait()
    answer = Tex(r"$5 + 10i$").next_to(complex_num2, DOWN).set_color(RED)
    answer_dot = Dot(plane.c2p(5,10), color=RED)
    self.play(Write(answer))
    self.play(Create(answer_dot))
    self.wait()
    answer_vec = Line(start=plane.c2p(0,0), end=plane.c2p(5,10), color=RED).add_tip()
    self.play(Create(answer_vec))
    self.wait()

    self.remove(vec2, answer_vec)
    self.wait()

    brace1 = BraceBetweenPoints(plane.c2p(4,3), plane.c2p(0,0), color=YELLOW)
    self.play(Create(brace1))
    self.wait()
    vec1_mag = brace1.get_text("5", buff=0.1).set_color(YELLOW)
    self.play(Write(vec1_mag))
    self.remove(complex_num1)
    self.wait()
    vec1_mag_text = Tex(r"Length of vector 1 is 5", color=YELLOW).to_edge(UR, buff=0.2)
    self.play(Write(vec1_mag_text))
    self.wait()
    self.remove(vec1, brace1, vec1_mag)
    self.wait()

    self.play(Create(vec2))
    self.wait()
    brace2 = BraceBetweenPoints(plane.c2p(2,1), plane.c2p(0,0), color=BLUE)
    self.play(Create(brace2))
    self.wait()
    vec2_mag = brace2.get_text("2.24", buff=0.1).set_color(BLUE)
    self.play(Write(vec2_mag))
    self.remove(complex_num2)
    self.wait()
    vec2_mag_text = Tex(r"Length of vector 2 is 2.24", color=BLUE).next_to(vec1_mag_text, DOWN, buff=0.1).scale(0.95)
    self.play(Write(vec2_mag_text))
    self.wait()
    self.remove(vec2, brace2, vec2_mag)
    self.wait()

    self.play(Create(answer_vec))
    self.wait()
    answer_brace = BraceBetweenPoints(plane.c2p(5,10), plane.c2p(0,0), color=RED)
    self.play(Create(answer_brace))
    self.wait()
    answer_mag = answer_brace.get_text("11.2", buff=0.1).set_color(RED)
    self.play(Write(answer_mag))
    self.remove(answer)
    self.wait()
    answer_mag_text = Tex(r"Length of vector 3 is 11.2", color=RED).next_to(vec2_mag_text, DOWN, buff=0.1).scale(0.95)
    self.play(Write(answer_mag_text))
    self.wait()

    self.remove(dot1, dot2, answer_dot, answer_vec, answer_brace, answer_mag)
    self.wait()

    self.play(Write(vec1))
    self.wait()

    x_axis = Line(plane.c2p(0,0), plane.c2p(5,0))
    vec1_angle = Angle(x_axis, vec1, radius=1.5)
    self.play(Create(vec1_angle))
    value = DecimalNumber(vec1_angle.get_value(degrees=True), unit="^{\circ}", color=YELLOW)
    self.play(Write(value.next_to(vec1_angle, RIGHT ,buff=0.5)))
    self.wait()
    self.play(Write(value.next_to(answer_mag_text, DOWN)))
    self.play(Uncreate(vec1_angle))
    self.play(Uncreate(value))
    self.play(Uncreate(vec1))
    self.wait()

    self.play(Create(vec2))
    self.wait()
    vec2_angle = Angle(x_axis, vec2, radius=1.5)
    self.play(Create(vec2_angle))
    value2 = DecimalNumber(vec2_angle.get_value(degrees=True), unit="^{\circ}", color=BLUE)
    self.play(Write(value2.next_to(vec2_angle, RIGHT ,buff=0.25)))
    self.wait()
    self.play(Uncreate(vec2))
    self.play(Uncreate(vec2_angle))
    self.play(Uncreate(value2))
    self.wait()

    self.play(Create(answer_vec))
    self.wait()
    answer_vec_angle = Angle(x_axis, answer_vec, radius=1.5)
    self.play(Create(answer_vec_angle))
    value3 = DecimalNumber(answer_vec_angle.get_value(degrees=True), unit="^{\circ}", color=RED)
    self.play(Write(value3.next_to(answer_vec_angle, RIGHT ,buff=0.25)))
    self.wait()
    self.play(Uncreate(answer_vec))
    self.play(Uncreate(answer_vec_angle))
    self.play(Uncreate(value3))
    self.wait()



    