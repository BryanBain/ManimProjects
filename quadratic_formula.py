from manim import *

class NewQuadraticFormula(MovingCameraScene):
    def construct(self):
        intro_txt = Text("You may be familiar with the quadratic formula \n for solving equations in the form").scale(0.9).to_edge(UP)
        self.play(Write(intro_txt))
        quadratic = Tex(r"$ax^2 + bx + c = 0$").scale(1.2).next_to(intro_txt, DOWN)
        self.play(Write(quadratic))
        self.wait()
        quad_formula = Tex(r"$x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$").next_to(quadratic, 4*DOWN)
        self.play(Write(quad_formula))
        self.wait()
        self.play(FadeOut(Group(intro_txt, quadratic, quad_formula)))
        self.wait()

        alt_form_txt = Text("However, there is an alternative form").to_edge(UP)
        self.play(Write(alt_form_txt))
        self.wait()
        alt_form = Tex(r"$x = m \pm \sqrt{m^2-c}$").scale(1.2).next_to(alt_form_txt, 2*DOWN)
        self.play(Write(alt_form))
        self.wait()
        m_explanation = Tex("Where ", r"$m = -\frac{b}{2}$").scale(1.2).next_to(alt_form, 2*DOWN)
        self.play(Write(m_explanation))
        self.wait()
        self.play(FadeOut(VGroup(alt_form, alt_form_txt, m_explanation)))
        self.wait()

        eq = Tex(r"$x^2 + 8x + 15$").set_color(YELLOW).to_edge(UP+LEFT, buff=0.5)
        self.play(Write(eq))
        self.wait()
        ax = Axes(
            x_range = [-6,1,1],
            y_range = [-2,3,1],
            tips = False,
            axis_config = {"include_numbers": True}
            )
        self.play(Create(ax))

        func = lambda x: x**2 + 8*x + 15
        func_graph = ax.plot(func).set_color(YELLOW)
        self.play(Create(func_graph))
        self.wait()

        dot1 = Dot(ax.c2p(-5,0)).scale(1.5).set_color(YELLOW)
        dot2 = Dot(ax.c2p(-3,0)).scale(1.5).set_color(YELLOW)
        self.play(Create(VGroup(dot1, dot2)))
        self.wait()

        self.play(FadeOut(func_graph))

        mean_trg = Triangle(color=RED).rotate(60*DEGREES).move_to(ax.c2p(-4,0.15)).scale(0.2)
        self.play(Create(mean_trg))
        self.wait()

        tri_lbl = Tex(r"$m$").move_to(ax.c2p(-4,0.5)).set_color(RED)
        self.play(Write(tri_lbl))
        self.wait()

        m_txt = Tex(r"$m = \frac{1}{2}(-5+(-3)) = -4$").next_to(eq, 2*RIGHT).set_color(RED)
        self.play(Write(m_txt))
        self.wait(2)
        self.play(FadeOut(m_txt))

        lb = BraceBetweenPoints(ax.c2p(-4,0.5), ax.c2p(-5,0.5)).set_color(PURPLE)
        lb_lbl = Tex(r"$\pmb{m-d}$").next_to(lb, UP).set_color(PURPLE)
        self.play(GrowFromCenter(VGroup(lb, lb_lbl)))
        self.wait()

        rb = BraceBetweenPoints(ax.c2p(-4,-0.35), ax.c2p(-3,-0.35)).set_color(PURPLE)
        rb_lbl = Tex(r"$\pmb{m+d}$").next_to(rb, DOWN).set_color(PURPLE)
        self.play(GrowFromCenter(VGroup(rb, rb_lbl)))
        self.wait()

        self.play(self.camera.frame.animate.set(width=20).to_edge(LEFT))
        self.wait()

        step1 = Tex(r"$(m-d)(m+d)=c$").move_to(10*RIGHT).scale(1.25)
        self.play(Write(step1))
        self.wait()
        constant_box = SurroundingRectangle(eq[0][6:])
        step1_box = SurroundingRectangle(step1[0][-1:])
        self.play(Create(VGroup(constant_box, step1_box)))
        self.wait(2)
        self.play(Uncreate(VGroup(constant_box, step1_box)))
        self.wait()
        step2 = Tex(r"$m^2 - d^2 = c$").move_to(10*RIGHT).scale(1.25)
        self.play(Transform(step1, step2))
        self.wait()
        step3 = Tex(r"$-d^2 = -m^2 + c$").move_to(10*RIGHT).scale(1.25)
        self.play(Transform(step1, step3))
        self.wait()
        step4 = Tex(r"$d^2 = m^2 - c$").move_to(10*RIGHT).scale(1.25)
        self.play(Transform(step1, step4))
        self.wait()
        step5 = Tex(r"$d = \sqrt{m^2 - c}$").move_to(10*RIGHT).scale(1.25)
        self.play(Transform(step1, step5))
        self.wait()

        lb_lblA = Tex(r"$\pmb{m-\sqrt{m^2-c}}$").next_to(lb, UP).set_color(PURPLE)
        rb_lblA = Tex(r"$\pmb{m+\sqrt{m^2-c}}$").next_to(rb, DOWN).set_color(PURPLE)
        self.play(Transform(rb_lbl, rb_lblA))
        self.play(Transform(lb_lbl, lb_lblA))
        self.wait()
        self.play(FadeOut(step1))
        self.wait()

        self.play(self.camera.frame.animate.set(width=14).move_to(ORIGIN))
        self.wait()

        answer1 = Tex(r"$x_1 = m - \sqrt{m^2-c}$").set_color(YELLOW).move_to(ax.c2p(-2.5,3))
        self.play(Write(answer1))
        self.wait()
        answer2 = Tex(r"$x_2 = m + \sqrt{m^2-c}$").set_color(YELLOW).next_to(answer1, DOWN)
        self.play(Write(answer2))
        self.play(Create(SurroundingRectangle(VGroup(answer1, answer2))))
        self.wait(2)



