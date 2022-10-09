from manim import *

class MultiplyPolynom(Scene):
    def construct(self):
        problem = Tex(r"$(x-2)(x^2+6x+7)$").to_edge(UP)
        self.play(Write(problem))
        self.wait()
        grid = Rectangle(width=6, height=4, grid_xstep=2, grid_ystep=2)
        self.play(FadeIn(grid))
        self.wait()
        divisor = Tex(r"$x$", r"$-2$")
        divisor[0].move_to((-3.5,1,0))
        divisor[1].move_to((-3.5,-1,0))
        self.play(Write(VGroup(divisor[0], divisor[1])))
        self.wait()
        dividend = Tex(r"$x^2$", r"$+6x$", r"$+7$")
        dividend[0].move_to((-2,2.5,0))
        dividend[1].next_to(dividend[0], 5*RIGHT)
        dividend[2].next_to(dividend[1], 5*RIGHT)
        self.play(Write(VGroup(dividend[0], dividend[1], dividend[2])))
        self.wait()

        def cell_focus(x,y):
            highlight = Rectangle(width=2, height=2, 
                        grid_xstep=2, grid_ystep=2, 
                        color=YELLOW)
            self.play(Indicate(highlight.move_to((x,y,0))))
            self.remove(highlight)
        
        cell_focus(-2,1)    # Upper left cell
        self.wait()

        unsimplified_answer = Tex(r"$x^3$", r"$6x^2$", r"$7x$",
                                r"$-2x^2$", r"$-12x$", r"$-14$")
        unsimplified_answer[0].next_to(divisor[0], 5*RIGHT)     
        self.play(Write(unsimplified_answer[0]))
        self.wait()

        cell_focus(0,1)     # Upper middle cell
        self.wait()

        unsimplified_answer[1].next_to(unsimplified_answer[0], 5*RIGHT)
        self.play(Write(unsimplified_answer[1]))
        self.wait()

        cell_focus(2,1)     # Upper right cell
        self.wait()

        unsimplified_answer[2].next_to(unsimplified_answer[1], 6*RIGHT)
        self.play(Write(unsimplified_answer[2]))
        self.wait()

        cell_focus(-2,-1)   # Bottom left cell
        self.wait()

        unsimplified_answer[3].next_to(divisor[1], 2.5*RIGHT)
        self.play(Write(unsimplified_answer[3]))
        self.wait()

        cell_focus(0,-1)    # Bottom middle cell
        self.wait()

        unsimplified_answer[4].next_to(unsimplified_answer[3], 4*RIGHT)
        self.play(Write(unsimplified_answer[4]))
        self.wait()

        cell_focus(2,-1)    # Bottom right cell
        self.wait()

        unsimplified_answer[5].next_to(unsimplified_answer[4], 4*RIGHT)
        self.play(Write(unsimplified_answer[5]))
        self.wait()

        simplified_answer = Tex(r"$x^3+4x^2-5x-14$").to_edge(2*DOWN)
        cell_focus(-2,1)
        self.play(Write(simplified_answer[0][0:2]))
        self.wait()

        cell_focus(-2,-1)
        cell_focus(0,1)
        self.play(Write(simplified_answer[0][2:6]))
        self.wait()

        cell_focus(0,-1)
        cell_focus(2,1)
        self.play(Write(simplified_answer[0][6:9]))
        self.wait()

        cell_focus(2,-1)
        self.play(Write(simplified_answer[0][9:]))
        self.wait()

        answer = SurroundingRectangle(simplified_answer, corner_radius=0.2)
        self.play(Create(answer))
        self.wait()

class PolynomDivNoRemainder(Scene):
    def construct(self):
        problem = Tex(r"$\left(x^3 + 4x^2 - 5x - 14\right) \div (x-2)$").to_edge(UP)
        self.play(Write(problem))
        self.wait()

        grid = Rectangle(width=6, height=4, grid_xstep=2, grid_ystep=2)
        self.play(FadeIn(grid))
        self.wait()
        divisor = Tex(r"$x$", r"$-2$")
        divisor[0].move_to((-3.5,1,0))
        divisor[1].move_to((-3.5,-1,0))
        self.play(Write(VGroup(divisor[0], divisor[1])))
        self.wait()

        def cell_focus(x,y):
            highlight = Rectangle(width=2, height=2, 
                        grid_xstep=2, grid_ystep=2, 
                        color=YELLOW)
            self.play(Indicate(highlight.move_to((x,y,0))))
            self.remove(highlight)
        
        cell_focus(-2,1)    # Upper left cell
        self.wait()

        unsimplified_answer = Tex(r"$x^3$", r"$6x^2$", r"$7x$",
                                r"$-2x^2$", r"$-12x$", r"$-14$")
        unsimplified_answer[0].next_to(divisor[0], 5*RIGHT)     
        self.play(Write(unsimplified_answer[0]))
        self.wait()

        check= Tex(r"\checkmark", color= GREEN, stroke_width=3).scale(1) 
        self.play(Write(check.next_to(problem[0][1],UP)))
        self.wait()

        step_1_scratch_work = Tex(r"$\displaystyle\frac{x^3}{x}$", r"$=x^2$").to_edge(LEFT + UP)
        self.play(Write(step_1_scratch_work[0]))
        self.wait()
        self.play(Write(step_1_scratch_work[1]))
        self.wait()

        dividend = Tex(r"$x^2$", r"$+6x$", r"$+7$")
        dividend[0].move_to((-2,2.5,0))
        self.play(Write(dividend[0]))
        self.wait()