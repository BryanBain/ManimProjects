from manim import *
from numpy import half

class ComplexTrig(Scene):
    def construct(self):
        intro_text = Tex("We know the familiar $x$, $y$, and $r$:").move_to(2*UP)
        self.play(Write(intro_text))
        self.wait()
        self.play(Uncreate(intro_text))
        axes = Axes(x_range = [0, 5, 1], y_range = [0, 5, 1], 
                    axis_config={'include_ticks':False}).shift(0.5*UP)
        self.play(Create(axes))
        point = Dot(axes.c2p(3,2))
        self.wait()
        self.play(Create(point))
        self.wait()
        point_lbl = Tex(r"$(x,y)$").next_to(point, RIGHT)
        self.play(Write(point_lbl))
        self.wait()
        hypotenuse = Line(axes.c2p(0,0), point, color=YELLOW).add_tip()
        self.play(Create(hypotenuse))
        theta = Tex(r"$\theta$").move_to(axes.c2p(0.75,0.25))
        self.play(Write(theta))
        self.wait()
        horiz_brace = Brace(Line(axes.c2p(0,0), axes.c2p(3,0)), color=BLUE)
        horiz_txt = horiz_brace.get_text("$x$").set_color(BLUE)
        self.play(Create(horiz_brace))
        self.play(Write(horiz_txt))
        self.wait()
        vert_brace = BraceBetweenPoints(axes.c2p(3,0), axes.c2p(3,2)).set_color(RED)
        vert_txt = vert_brace.get_text("$y$").set_color(RED)
        self.play(Create(vert_brace))
        self.play(Write(vert_txt))
        self.wait()
        hypot_brace = BraceBetweenPoints(axes.c2p(3,2), axes.c2p(0,0)).set_color(YELLOW)
        hypot_txt = hypot_brace.get_text("$r$").set_color(YELLOW)
        self.play(Create(hypot_brace))
        self.play(Write(hypot_txt))
        self.wait()
        self.remove(axes, point, point_lbl, hypotenuse, horiz_brace, 
        horiz_txt, vert_brace, vert_txt, hypot_brace, hypot_txt, theta)
        self.wait()

        complex_txt = Tex("With complex numbers, our plane becomes")
        self.play(Write(complex_txt))
        self.wait()
        self.play(Uncreate(complex_txt))
        complex_point_lbl = Tex(r"$(x,iy)$").next_to(point, RIGHT, buff=0.5)
        complex_vert_txt = vert_brace.get_text("$iy$").set_color(RED)
        horiz_vector = Line(start=axes.c2p(0,0), end=axes.c2p(3,0), color=BLUE).add_tip()
        vert_vector = Line(start=axes.c2p(3,0), end=axes.c2p(3,2), color=RED).add_tip()
        complex_resultant = Tex(r"$r = x + yi$").move_to(2*UP)
        complex_stuff = VGroup(axes, point, complex_point_lbl, hypotenuse, 
                            horiz_brace, horiz_txt, vert_brace, hypot_brace,
                            horiz_vector, vert_vector, hypot_txt, complex_vert_txt, 
                            complex_resultant, theta)
        self.play(Create(complex_stuff))
        self.wait()
        cosine = Tex(r"$\cos\left(\theta\right) = \dfrac{x}{r}$").to_edge(UR, buff=1)
        polar_x = Tex(r"$x = r\cos\left(\theta\right)$").next_to(cosine, 1.5*DOWN)
        self.play(Write(cosine))
        self.wait()
        self.play(Write(polar_x))
        self.wait()
        r_cos_theta = Tex(r"$r\cos(\theta)$", color=BLUE).move_to(horiz_txt)
        self.play(ReplacementTransform(horiz_txt, r_cos_theta))
        self.wait()
        self.remove(cosine, polar_x)
        sine = Tex(r"$\sin\left(\theta\right) = \dfrac{y}{r}$").to_edge(UR, buff=1)
        polar_y = Tex(r"$y = r\sin\left(\theta\right)$").next_to(sine, 1.5*DOWN)
        self.play(Write(sine))
        self.wait()
        self.play(Write(polar_y))
        self.wait()
        ir_sin_theta = Tex(r"$ir\sin(\theta)$", color=RED).next_to(vert_brace)
        self.play(ReplacementTransform(complex_vert_txt, ir_sin_theta))
        self.wait()
        self.remove(sine, polar_y)

        new_r = Tex(r"$r = x\cos(\theta) + iy\sin(\theta)$", color=YELLOW).move_to(2*UP)
        self.play(ReplacementTransform(complex_resultant, new_r))
        self.wait()

class ComplexMult(Scene):
    def construct(self):
        intro = Tex("Recall that when multiplying complex numbers, "
            "we drew vectors (arrows) to the points in the complex plane.").scale(0.8)
        self.play(Write(intro))
        self.wait()
        intro2 = Tex("We multiplied the length of each vector and added the rotated angles for each number.").scale(0.8)
        self.play(Uncreate(intro))
        self.play(Write(intro2))
        self.wait()
        self.play(Uncreate(intro2))
        intro3 = Tex("For simplicity, we will look at complex numbers on the unit circle.").scale(0.9)
        self.play(Write(intro3))
        self.wait()
        self.play(Uncreate(intro3))

        example = Tex("Example. ", "Multiply ", r"$\left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right)$",
                    r"$\left(-\frac{1}{2} + \frac{\sqrt{3}}{2}i\right)$")
        example[0].set_color(RED)
        self.play(Write(example))
        self.wait()
        self.remove(example)

        axes = Axes(x_range = [-1,1,0.25], y_range=[-1,1,0.25], x_length = 8, y_length=8).add_coordinates()
        self.play(Create(axes))
        self.wait()
        unit_circle = Circle(radius = 4, color=YELLOW)
        self.play(Create(unit_circle))
        self.wait()
        half_sqrt_3 = 0.866
        point1 = Dot(axes.c2p(half_sqrt_3, 0.5), color=BLUE)
        point1_lbl = Tex(r"$\left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right)$").next_to(point1, RIGHT).set_color(BLUE)
        point1_grp = VGroup(point1, point1_lbl)
        self.play(Write(point1_grp))
        self.wait()
        x_axis = Line(start=axes.c2p(0,0), end=axes.c2p(1,0))
        vec1 = Line(start=axes.c2p(0,0), end=point1, color=BLUE)
        self.play(Create(vec1))
        self.wait()
        angle1 = Angle(x_axis, vec1, radius=1, color=BLUE)
        self.play(Create(angle1))
        angle1_value = Integer(angle1.get_value(degrees=True), unit="^{\circ}").next_to(angle1, RIGHT).set_color(BLUE)
        self.play(Write(angle1_value))
        self.wait()
        point2 = Dot(axes.c2p(-0.5,half_sqrt_3), color=RED)
        point2_lbl = Tex(r"$\left(-\frac{1}{2} + \frac{\sqrt{3}}{2}i\right)$").next_to(point2, LEFT).set_color(RED)
        point2_grp = VGroup(point2, point2_lbl)
        self.play(Write(point2_grp))
        self.wait()
        vec2 = Line(start = axes.c2p(0,0), end=point2, color=RED)
        self.play(Create(vec2))
        self.wait()
        angle2 = Angle(x_axis, vec2, radius=0.8, color=RED)
        self.play(Create(angle2))
        angle2_value = Integer(angle2.get_value(degrees=True), unit="^{\circ}").next_to(angle1, UP).set_color(RED)
        self.play(Write(angle2_value))
        self.wait()
        self.remove(angle1, vec1, angle1_value, 
                    angle2, vec2, angle2_value)
        self.wait()
        point3 = Dot(axes.c2p(-1*half_sqrt_3, 0.5), color=YELLOW)
        vec3 = Line(start=axes.c2p(0,0), end=point3, color=YELLOW)
        self.play(Create(vec3))
        self.wait()
        self.play(Create(point3))
        angle3 = Angle(x_axis, vec3, radius=1, color=YELLOW)
        self.play(Create(angle3))
        angle3_value = Integer(angle3.get_value(degrees=True), unit="^{\circ}").next_to(angle3, UP).set_color(YELLOW)
        self.play(Write(angle3_value))
        point3_lbl = Tex(r"$\left(-\frac{\sqrt{3}}{2} + \frac{1}{2}i\right)$").next_to(point3, LEFT).set_color(YELLOW)
        self.play(Write(point3_lbl))
        self.wait()
        self.remove(point1_grp, point2_grp, point3, point3_lbl,
                    axes, unit_circle, angle3_value, angle3, vec3)
        self.wait()

        unit_circle = Circle(radius = 1, color=YELLOW).scale(3)
        center = Dot(ORIGIN)
        self.play(Create(center))
        self.play(Create(unit_circle))
        self.wait()
        radius1 = Line(start=ORIGIN, end=(3,0,0))
        self.play(Create(radius1))
        self.wait()
        dot1 = Dot((3*np.sqrt(2)/2, 3*np.sqrt(2)/2,0))
        self.play(Create(dot1))
        self.wait()
        radiusA = Line(start=ORIGIN, end=dot1)
        self.play(Create(radiusA))
        self.wait()
        angleA = Angle(radius1, radiusA)
        self.play(Create(angleA))
        angleA_lbl = Tex(r"$A$").next_to(angleA, RIGHT + 0.02*UP)
        self.play(Write(angleA_lbl))
        self.wait()
        dot1_lbl = Tex(r"$\cos(A) + i\sin(A)$").next_to(dot1, RIGHT)
        self.play(Write(dot1_lbl))
        self.wait()
        dot2 = Dot((-0.521, 2.954, 0), color=RED)
        self.play(Create(dot2))
        self.wait()
        radiusB = Line(start=ORIGIN, end=dot2, color=RED)
        self.play(Create(radiusB))
        self.wait()
        angleB = Angle(radius1, radiusB, radius=0.5, color=RED)
        self.play(Create(angleB))
        angleB_lbl = Tex(r"$B$").next_to(angleB, UP).set_color(RED)
        self.play(Write(angleB_lbl))
        self.wait()
        dot2_lbl = Tex(r"$\cos(B) + i\sin(B)$").set_color(RED).next_to(dot2, UP)
        self.play(Write(dot2_lbl))
        self.wait()
        dot3 = Dot((-2.457,1.721,0), color=BLUE)
        self.play(Create(dot3))
        self.wait()
        radius_grp = VGroup(radiusA, angleA, angleA_lbl,radiusB, angleB, angleB_lbl)
        self.play(Uncreate(radius_grp))
        self.wait()
        radiusC = Line(start=ORIGIN, end=dot3, color=BLUE)
        self.play(Create(radiusC))
        self.wait()
        angle_sum = Angle(radius1, radiusC,color=BLUE)
        self.play(Create(angle_sum))
        self.wait()
        angle_sum_lbl = Tex(r"$A+B$").next_to(angle_sum, UP).set_color(BLUE)
        self.play(Write(angle_sum_lbl))
        self.wait()
        dot3_lbl = Tex(r"$\cos(A+B) + i\sin(A+B)$").next_to(dot3, 0.5*UP).set_color(BLUE).scale(0.75).shift(2*LEFT)
        self.play(Write(dot3_lbl))
        self.wait()

        self.remove(unit_circle, dot1, dot2, dot3, center,
                    angle_sum, angle_sum_lbl, dot3_lbl,
                    radius1, radiusC, dot2_lbl, dot1_lbl)
        self.wait()

        problem1 = Tex(r"$\cos(A+B)+i\sin(A+B) = \left(\cos(A)+i\sin(A)\right)\left(\cos(B)+i\sin(B)\right)$").move_to(3*UP).scale(0.9)
        self.play(Write(problem1))
        self.wait()
        problem2 = Tex(r"$\cos(A)\cos(B) + \cos(A)\sin(B)i + \sin(A)\cos(B)i + \sin(A)\sin(B)$", r"$i^2$").next_to(problem1, DOWN).scale(0.9)
        self.play(Write(problem2))
        problem2.set_color_by_tex("i^2", RED)
        problem3 = Tex(r"$\cos(A)\cos(B) + \cos(A)\sin(B)i + \sin(A)\cos(B)i - \sin(A)\sin(B)$").next_to(problem2, DOWN).scale(0.9)
        self.play(Write(problem3))
        self.wait()
        problem4 = Tex(r"$\cos(A)\cos(B) - \sin(A)\sin(B) + \left[\sin(A)\cos(B) + \cos(A)\sin(B) \right]i$").next_to(problem3, DOWN).scale(0.9)
        self.play(Write(problem4))
        self.wait()
        cos_box = SurroundingRectangle(problem4[0][0:25], color=YELLOW)
        self.play(Create(cos_box))
        self.wait()
        cos_sum = Tex(r"$\cos(A+B) = \cos(A)\cos(B) - \sin(A)\sin(B)$").next_to(problem4, 1.25*DOWN).set_color(YELLOW)
        self.play(Write(cos_sum))
        self.wait()
        sin_box = SurroundingRectangle(problem4[0][27:-2], color=ORANGE)
        self.play(Create(sin_box))
        self.wait()
        sin_sum = Tex(r"$\sin(A+B) = \sin(A)\cos(B) + \cos(A)\sin(B)$").next_to(cos_sum, DOWN).set_color(ORANGE)
        self.play(Write(sin_sum))
        self.wait()