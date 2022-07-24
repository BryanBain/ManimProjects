from manim import *

class Probability_AND(Scene):
    def construct(self):
        title = Title("Probability: AND")
        self.play(Write(title))
        self.wait()
        self.play(Uncreate(title))
        self.wait()

        circleA = Circle(radius = 2, color=RED, fill_color=RED, fill_opacity = 0.4).shift(1.5*LEFT)
        locationA = circleA.point_at_angle(135*DEGREES)
        lblA = Tex(r"$A$").set_color(RED).next_to(locationA, UP+LEFT).scale(1.25)
        A_Group = VGroup(circleA, lblA)
        self.play(Create(A_Group))
        self.wait()

        circleB = Circle(radius = 2, color=BLUE, fill_color=BLUE, fill_opacity = 0.4).shift(1.5*RIGHT)
        locationB = circleB.point_at_angle(45*DEGREES)
        lblB = Tex(r"$B$").set_color(BLUE).next_to(locationB, UP+RIGHT).scale(1.25)
        B_Group = VGroup(circleB, lblB)
        self.play(Create(B_Group))
        self.wait()

        intersect = Intersection(circleA, circleB, color=YELLOW, fill_opacity=1)
        self.play(Create(intersect))
        self.wait()

        intersect_tex = Tex(r"$A \cap B$", color=YELLOW).move_to([0,3,0]).scale(1.25)
        self.play(Write(intersect_tex))
        self.wait()
        arrow = Arrow(2.5*UP, 1.25*UP, fill_opacity = 1).set_color(YELLOW).scale(1.5)
        self.play(Create(arrow))
        self.wait()

class Probability_OR(Scene):
    def construct(self):
        # self.add(NumberPlane())
        title = Title("Probability: OR")
        self.play(Write(title))
        self.wait()
        self.play(Uncreate(title))
        self.wait()

        circleA = Circle(radius = 2, color=RED, fill_color=RED, fill_opacity = 0.4).shift(1.5*LEFT)
        locationA = circleA.point_at_angle(135*DEGREES)
        lblA = Tex(r"$A$").set_color(RED).next_to(locationA, UP+LEFT).scale(1.25)
        A_Group = VGroup(circleA, lblA)
        self.play(Create(A_Group))
        self.wait()

        circleB = Circle(radius = 2, color=BLUE, fill_color=BLUE, fill_opacity = 0.4).shift(1.5*RIGHT)
        locationB = circleB.point_at_angle(45*DEGREES)
        lblB = Tex(r"$B$").set_color(BLUE).next_to(locationB, UP+RIGHT).scale(1.25)
        B_Group = VGroup(circleB, lblB)
        self.play(Create(B_Group))
        self.wait(2)

        intersect = Intersection(circleA, circleB, color=PURPLE, fill_opacity=0.8)
        self.play(Create(intersect))
        self.wait()
        self.play(Indicate(intersect))
        self.wait()

        self.play(Indicate(circleA))
        self.wait()

        diffB = Difference(circleB, circleA, color=BLUE, fill_opacity=0.8)
        self.play(Indicate(diffB))
        self.wait()

        self.remove(A_Group, B_Group, intersect, diffB)
        self.wait()

        self.play(Create(B_Group))
        probB_tex = Tex(r"$P(B)$", color=BLUE).next_to(B_Group, DOWN)
        self.play(Write(probB_tex))
        self.wait()
        self.play(Indicate(intersect))
        self.wait()
        self.play(Uncreate(intersect), Transform(circleB, diffB))
        self.wait()
        minus = Tex(r"$-$", color=YELLOW).next_to(probB_tex, 2*RIGHT)
        probAND_tex = Tex(r"$P(A \cap B)$", color=YELLOW).next_to(minus, 2*RIGHT)
        self.play(Create(VGroup(minus, probAND_tex)))
        self.wait()

        self.play(Create(A_Group))
        probA_tex = Tex(r"$P(A)$", color=RED).next_to(A_Group, DOWN)
        self.play(Write(probA_tex))
        self.wait()
        plus = Tex(r"$+$").move_to(2.5*DOWN)
        self.play(Write(plus))

        equals = Tex(r"$=$").next_to(probA_tex, 2*LEFT)
        probOR_tex = Tex(r"$P(A \cup B)$").next_to(equals, 2*LEFT)
        self.play(Write(probOR_tex))
        self.play(Write(equals))
        self.wait()

        formula = VGroup(probOR_tex, equals, probA_tex, plus, probB_tex, minus, probAND_tex)
        self.play(Create(SurroundingRectangle(formula, color=GREEN)))
        self.wait()

