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
        box0 = SurroundingRectangle(problem[0][1:3])
        self.play(Create(box0))
        self.wait()
        self.play(Uncreate(box0))
        self.wait()
        unsimplified_answer[0].next_to(divisor[0], 5*RIGHT)     
        unsimplified_answer[1].next_to(divisor[0], 12.5*RIGHT)
        unsimplified_answer[2].next_to(divisor[0], 20.5*RIGHT)
        unsimplified_answer[3].next_to(divisor[1], 2.5*RIGHT)
        unsimplified_answer[4].next_to(divisor[1], 10.5*RIGHT)
        self.play(Write(unsimplified_answer[0]))
        self.wait()

        check= Tex(r"\checkmark", color= GREEN, stroke_width=3).scale(1.5) 
        self.play(Write(check.move_to(problem[0][1])))
        self.wait()

        step_1_scratch_work = Tex(r"$\displaystyle\frac{x^3}{x}$", r"$=x^2$").to_edge(LEFT).scale(0.9)
        self.play(Write(step_1_scratch_work[0]))
        self.wait()
        self.play(Write(step_1_scratch_work[1]))
        self.wait()

        dividend = Tex(r"$x^2$", r"$6x$", r"$7$")
        dividend[0].move_to((-2,2.5,0))
        dividend[1].next_to(dividend[0], 6*RIGHT)
        self.play(Write(dividend[0]))
        self.play(Uncreate(step_1_scratch_work))
        self.wait()
     
        self.play(Write(unsimplified_answer[3]))
        self.wait()

        cell_focus(-2,-1)
        self.wait()
        cell_focus(0,1)
        unknown_quantity = Tex(r"?").next_to(divisor[0], 12.5*RIGHT)
        self.play(Write(unknown_quantity))
        self.wait()

        box1 = SurroundingRectangle(problem[0][3:7])
        self.play(Create(box1))
        self.wait()
        self.play(Uncreate(box1))

        step_2_scratch_work = Tex(r"$-2x^2 + \mathord{?} = 4x^2$").to_edge(LEFT).scale(0.9)
        self.play(Write(step_2_scratch_work))
        self.wait()
        step_2_answer = Tex(r"$\mathord{?} = 6x^2$").to_edge(LEFT).scale(0.9)
        self.play(Transform(step_2_scratch_work, step_2_answer))
        self.wait()
        self.play(ReplacementTransform(unknown_quantity, unsimplified_answer[1]))
        self.play(Uncreate(step_2_scratch_work))
        self.wait()
        
        check2= Tex(r"\checkmark", color= GREEN, stroke_width=3).scale(1.5) 
        self.play(Write(check2.move_to(problem[0][4:6])))
        self.wait()

        col2_hdr_work = Tex(r"$\displaystyle \frac{6x^2}{x}$", r"$=6x$").to_edge(LEFT).scale(0.9)
        self.play(Write(col2_hdr_work))
        self.wait()
        col2_hdr = dividend[1]
        self.play(Write(col2_hdr))
        self.wait()
        self.play(Uncreate(col2_hdr_work))
        self.wait()

        self.play(Write(unsimplified_answer[4]))
        self.wait()

        cell_focus(0,-1)
        self.wait()
        cell_focus(2,1)
        unknown_quantity1 = Tex(r"$\mathord{?}$").next_to(divisor[0], 20.5*RIGHT)
        self.play(Write(unknown_quantity1))
        self.wait()

        box2 = SurroundingRectangle(problem[0][7:10])
        self.play(Create(box2))
        self.wait()
        self.play(Uncreate(box2))

        step_3_scratch_work = Tex(r"$-12x + \mathord{?} = -5x$").to_edge(LEFT).scale(0.9)
        self.play(Write(step_3_scratch_work))
        self.wait()
        step_3_answer = Tex(r"$\mathord{?} = 7x$").to_edge(LEFT).scale(0.9)
        self.play(Transform(step_3_scratch_work, step_3_answer))
        self.wait()
        self.play(ReplacementTransform(unknown_quantity1, unsimplified_answer[2]))
        self.play(Uncreate(step_3_scratch_work))
        self.wait()
        
        check3 = Tex(r"\checkmark", color= GREEN, stroke_width=3).scale(1.5) 
        self.play(Write(check3.move_to(problem[0][8:10])))
        self.wait()
        