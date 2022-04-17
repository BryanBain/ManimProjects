from manim import *

class Derivative(Scene):
    def construct(self):
        ax = Axes(x_range=[-8,8,2], y_range=[0,16,2], 
        axis_config={"include_tip": False, "include_numbers":True})
        func = ax.plot(lambda x: x**2 + 1).set_color(BLUE)

        x = ValueTracker(3)     # Finding the derivative at x = 3
        dx = ValueTracker(1)    # This will start at x = 3 + dx, or 4

        secant = always_redraw(
            lambda: ax.get_secant_slope_group(      # sets up dy/dx visually with secant line from x = 3 to x = 4
                x = x.get_value(),
                graph = func,
                dx = dx.get_value(),
                dy_line_color=PURPLE,
                dx_label = "dx",
                dy_label = "dy",
                secant_line_color=RED,
                secant_line_length=9,
            )
        )
        dot1 = always_redraw(
            lambda: Dot(color=RED)
            .move_to(
                ax.c2p(
                    x.get_value(), 
                    func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot(color=RED)
            .move_to(
                ax.c2p(
                    x.get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value())
                )
            )
        )
        tan_slope = Tex(r"$\frac{dy}{dx} = 6 \text{ at } x = 3$").next_to(dot1, RIGHT).set_color(RED)
        self.add(ax,func)
        self.play(Create(VGroup(dot1, dot2, secant)))
        self.play(dx.animate.set_value(0.0001), run_time = 6)
        self.wait(2)
        self.play(Write(tan_slope))
        self.wait()

