from manim import *

class Derivative(Scene):
    def construct(self):
        ax = Axes(x_range=[-8,8,1], y_range=[0,18,2], 
        axis_config={"include_tip": False, "include_numbers":True})
        f = lambda x: x**2 + 1
        func = ax.plot(f).set_color(BLUE)

        

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
        dot1 = always_redraw(       # value at x = 3
            lambda: Dot(color=RED)
            .move_to(
                ax.c2p(
                    x.get_value(), 
                    func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(       # initial value at x = 4
            lambda: Dot(color=PURPLE)
            .move_to(
                ax.c2p(
                    x.get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value())
                )
            )
        )
        function_text = (           
            Tex(r"$f(x) = x^2 + 1$")
            .move_to(ax.c2p(-6,12))
            .set_color(BLUE)
        )
        slope_value_text = (
            Tex("Slope value: ")
            .to_edge(LEFT, buff=0.2)
            .set_color(RED)
            .add_background_rectangle()
        )
        sec_slope_value = always_redraw(        # updates the value of the average rate of change
            lambda: DecimalNumber(num_decimal_places=5)
            .set_value(( f(x.get_value()+dx.get_value())-f(x.get_value()) ) / dx.get_value())
            .next_to(slope_value_text, RIGHT, buff=0.1)
            .set_color(RED)
        )
            

        self.add(ax,func)
        self.wait()
        self.play(Write(function_text))
        self.wait()
        self.play(Create(VGroup(dot1, dot2, secant)))
        self.wait()
        self.play(Create(VGroup(slope_value_text, sec_slope_value)))
        self.wait()
        self.play(dx.animate.set_value(0.000001), run_time = 8, rate_func=rate_functions.ease_out_sine)
        self.wait()
        tan_slope = Tex(r"$\frac{dy}{dx} = 6 \text{ at } x = 3$").next_to(dot1, RIGHT).set_color(RED)
        self.play(Write(tan_slope))
        self.wait()

