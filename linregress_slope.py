from manim import *

class LinRegressSlope1(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(0,9,1), y_range=(-2,7,1)).add_coordinates().to_edge(LEFT)
        points = [[1,1], [2,3], [3,4], [4,6]]
        tbl = MathTable(points, col_labels=[Tex(r"$x$"), Tex(r"$y$")]).to_edge(RIGHT)
        dots = VGroup(
            Dot(plane.c2p(1,1), radius=0.1, color=YELLOW,), 
            Dot(plane.c2p(2,3), radius=0.1, color=YELLOW), 
            Dot(plane.c2p(3,4), radius=0.1, color=YELLOW), 
            Dot(plane.c2p(4,6), radius=0.1, color=YELLOW)
        )
        self.play(Create(plane))
        self.play(Create(tbl))
        self.play(Create(dots))
        self.wait()

        reg_eq = lambda x: 1.6*x - 0.5
        line1 = plane.plot(reg_eq, color=RED)
        self.play(Create(line1))
        self.wait()

        xmean = 2.5
        ymean = 3.5

        ymean_line = plane.plot(lambda x: ymean)
        xmean_line = Line(start = plane.c2p(xmean,0,0), end=plane.c2p(xmean,7,0))
        mean_lines = VGroup(ymean_line, xmean_line)
        self.play(Create(mean_lines))
        self.wait()
        self.play(Uncreate(tbl))
        self.wait()

        xmean_tex = Tex(r"$\overline{x}=2.5$").to_edge(RIGHT)
        ymean_tex = Tex(r"$\overline{y}=3.5$").next_to(xmean_tex, DOWN)
        self.play(Write(VGroup(xmean_tex, ymean_tex)))
        self.wait()
        mean_dot = Dot(plane.c2p(2.5,3.5), radius=0.2, color=WHITE)
        self.play(Create(mean_dot))
        self.wait()

class LinRegressSlope2(Scene):
    def construct(self):
        plane = NumberPlane(x_range = (-3,3,1), y_range = (-3,3,1)).add_coordinates().shift(LEFT*3.5).scale(0.9)
        points = [[-1.5,-2.5], [-0.5,-0.5], [0.5,0.5], [1.5,2.5]]
        tbl = MathTable(points, 
        col_labels=[Tex(r"$x-\overline{x}$"), Tex(r"$y-\overline{y}$")]
        ).to_edge(RIGHT)
        dots = VGroup(
            Dot(plane.c2p(-1.5,-2.5), radius=0.1, color=YELLOW,), 
            Dot(plane.c2p(-0.5,-0.5), radius=0.1, color=YELLOW), 
            Dot(plane.c2p(0.5,0.5), radius=0.1, color=YELLOW), 
            Dot(plane.c2p(1.5,2.5), radius=0.1, color=YELLOW)
        )
        self.play(Create(plane))
        self.play(Create(tbl))
        self.play(Create(dots))
        self.wait()
        self.play(FadeOut(tbl))
        self.wait()

        m = ValueTracker(-5)
        resid_eq = lambda x: m.get_value()*x

        lineA = always_redraw(lambda: Line(plane.c2p(-1.5,-2.5), plane.c2p(-1.5,resid_eq(-1.5))))
        lineB = always_redraw(lambda: Line(plane.c2p(-0.5,-0.5), plane.c2p(-0.5,resid_eq(-0.5))))
        lineC = always_redraw(lambda: Line(plane.c2p(0.5,0.5), plane.c2p(0.5,resid_eq(0.5))))
        lineD = always_redraw(lambda: Line(plane.c2p(1.5,2.5), plane.c2p(1.5,resid_eq(1.5))))

        lines = VGroup(lineA, lineB, lineC, lineD)

        axes = Axes(x_range=[-2,5,1], y_range=[0,10,1],
                    x_length=8, y_length=8).add_coordinates().shift(3.5*RIGHT).scale(0.8)
        self.play(Create(axes))

        # I used quadratic regression to get the equation of the parabola.
        parabola = always_redraw(
            lambda : axes.plot(
                lambda x: 5*x**2 - 16*x + 13, x_range=[-5.05, m.get_value()]
            )
        )

        self.play(Create(parabola))
        self.wait()

        line1 = always_redraw(lambda: plane.plot(resid_eq, color=RED))
        self.play(Create(line1))
        self.wait()

        self.play(Create(lines))
        self.wait()

        self.play(
            m.animate.set_value(5),
            run_time=8
        )
        self.wait(2)

        vertex = Dot(axes.c2p(1.6,0.2), color=ORANGE)
        self.play(Create(vertex))

        arrow = Arrow(start=axes.c2p(3,1), end=axes.c2p(1.6,0.2), color=ORANGE)
        vertex_lbl = Tex(r"$(1.6, 0.2)$").next_to(arrow, UR).set_color(ORANGE)
        self.play(Create(arrow))
        self.wait()
        self.play(Write(vertex_lbl))
        self.wait()
        self.play(Indicate(vertex_lbl[0][1:4]))
        self.wait()

class LinRegressSlope3(Scene):
    def construct(self):
        slope_int = Tex(r"$y = mx + b$").scale(1.25)
        self.play(Write(slope_int))
        self.wait()
        slope_int_means = Tex(r"$\overline{y} = m\overline{x} + b$").scale(1.25)
        self.play(ReplacementTransform(slope_int, slope_int_means))
        self.wait()
        slope_int_means_step2 = Tex(r"$3.5 = 1.6(2.5) + b$").scale(1.25)
        self.play(ReplacementTransform(slope_int_means, slope_int_means_step2))
        self.wait()
        slope_int_means_step3 = Tex(r"$3.5 = 4 + b$").scale(1.25)
        self.play(ReplacementTransform(slope_int_means_step2, slope_int_means_step3))
        self.wait()
        slope_int_means_step4 = Tex(r"$-0.5 = b$").scale(1.25)
        self.play(ReplacementTransform(slope_int_means_step3, slope_int_means_step4))
        self.wait(2)
        self.play(Uncreate(slope_int_means_step4))
        self.wait()

        plane = NumberPlane(x_range=(0,6,1), y_range=(-2,7,1)).add_coordinates().to_edge(LEFT, buff=0.5)
        dots = VGroup(
            Dot(plane.c2p(1,1), radius=0.1, color=YELLOW,), 
            Dot(plane.c2p(2,3), radius=0.1, color=YELLOW), 
            Dot(plane.c2p(3,4), radius=0.1, color=YELLOW), 
            Dot(plane.c2p(4,6), radius=0.1, color=YELLOW)
        )
        self.play(Create(plane))
        self.play(Create(dots))
        self.wait()

        reg_eq = lambda x: 1.6*x - 0.5
        line1 = plane.plot(reg_eq, color=RED)
        self.play(Create(line1))
        self.wait()

        reg_eq_tex = Tex(r"$y = 1.6x - 0.5$").scale(1.25).to_edge(RIGHT, buff=1)
        self.play(Write(reg_eq_tex))
        self.wait()
        self.play(Create(SurroundingRectangle(reg_eq_tex, buff=0.2, corner_radius=0.2)))
        self.wait(2)









        
