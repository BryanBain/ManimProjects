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
        dividend = Tex(r"$x^2$", r"$6x$", r"$7$")
        dividend[0].move_to((-2,2.5,0))
        dividend[1].next_to(dividend[0], 6*RIGHT)
        dividend[2].next_to(dividend[0], 15*RIGHT)
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
        self.wait(2)

class PolynomDivNoRemainder(Scene):
    def construct(self):
        intro_txt = Text("When dividing polynomials, \n"
                    "we are looking for the \"column header values\" of the grid.").scale(0.7)
        self.play(Write(intro_txt))
        self.wait(2)
        self.play(Uncreate(intro_txt))

        problem = Tex(r"$\left(x^3 + 4x^2 - 5x - 14\right) \div (x-2)$").to_edge(UP)
        self.play(Write(problem))
        self.wait()

        # Set up the grid and row labels
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
        unsimplified_answer[5].next_to(divisor[1], 18.5*RIGHT)

        self.play(Write(unsimplified_answer[0]))
        self.wait()

        check= Tex(r"\checkmark", color= GREEN, stroke_width=3) 
        self.play(Write(check.next_to(problem[0][1], UP)))
        self.wait()

        col_1_scratch_work = Tex(r"$\displaystyle\frac{x^3}{x}$", r"$=x^2$").to_edge(LEFT).scale(0.9)
        self.play(Write(col_1_scratch_work[0]))
        self.wait()
        self.play(Write(col_1_scratch_work[1]))
        self.wait()

        dividend = Tex(r"$x^2$", r"$6x$", r"$7$").set_color(RED)
        dividend[0].move_to((-2,2.5,0))
        dividend[1].next_to(dividend[0], 6*RIGHT)
        dividend[2].next_to(dividend[0], 15*RIGHT)
        col1_hdr = dividend[0]
        self.play(Write(col1_hdr))
        self.play(Uncreate(col_1_scratch_work))
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
        
        check2= Tex(r"\checkmark", color= GREEN, stroke_width=3)
        self.play(Write(check2.next_to(problem[0][4:6], 0.5*UP)))
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

        check3 = Tex(r"\checkmark", color= GREEN, stroke_width=3) 
        self.play(Write(check3.next_to(problem[0][8:10], UP)))
        self.wait()

        col3_hdr_work = Tex(r"$\displaystyle \frac{7x}{x}$", r"$=7$").to_edge(LEFT).scale(0.9)
        self.play(Write(col3_hdr_work))
        self.wait()
        col3_hdr = dividend[2]
        self.play(Write(col3_hdr))
        self.wait()
        self.play(Uncreate(col3_hdr_work))
        self.wait()

        self.play(Write(unsimplified_answer[5]))
        self.wait()

        cell_focus(2,-1)
        self.wait()
        box3 = SurroundingRectangle(problem[0][10:13])
        self.play(Create(box3))
        self.wait()
        self.play(Uncreate(box3))
        self.wait()
        check4 = Tex(r"\checkmark", color= GREEN, stroke_width=3)
        self.play(Write(check4.next_to(problem[0][11:14], 0.5*UP)))
        self.wait()

        self.play(Indicate(unsimplified_answer))
        self.wait()

        quotient = Tex(r"$=x^2 + 6x + 7$", color=RED).next_to(problem, RIGHT)
        self.play(Write(quotient))
        self.wait()
        
class PolynomDivWithRemainder(Scene):
    def construct(self):
        problem = Tex(r"$\left(5x^3 - 2x^2 + 1\right) \div (x-3)$").to_edge(UP)
        problem_alt = Tex(r"$\left(5x^3 - 2x^2 + 0x + 1\right) \div (x-3)$").to_edge(UP)
        self.play(Write(problem))
        self.wait()
        self.play(ReplacementTransform(problem, problem_alt))
        self.wait()

        grid = Rectangle(width=8, height=4, grid_xstep=2, grid_ystep=2)
        self.play(FadeIn(grid))
        self.wait()
        divisor = Tex(r"$x$", r"$-3$")
        divisor[0].move_to((-4.5,1,0))
        self.play(Write(divisor[0]))
        self.wait()
        divisor[1].move_to((-4.5,-1,0))
        self.play(Write(divisor[1]))
        self.wait()

        cell0_0 = Tex(r"$5x^3$").move_to((-3,1,0))
        self.play(Write(cell0_0))
        box0 = SurroundingRectangle(problem_alt[0][1:4])
        self.play(Create(box0))
        self.wait()
        self.play(Uncreate(box0))
        self.wait()
        check1 = Tex(r"\checkmark", color= GREEN, stroke_width=3)
        self.play(Write(check1.next_to(problem_alt[0][1:4], 0.5*UP)))
        self.wait()

        col0_wrk = Tex(r"$\dfrac{5x^3}{x}=5x^2$").to_edge(LEFT + UP).scale(0.8)
        self.play(Write(col0_wrk))
        self.wait()
        col0_hdr = Tex(r"$5x^2$", color=RED).move_to((-3,2.5,0))
        self.play(Write(col0_hdr))
        self.wait()
        self.play(FadeOut(col0_wrk))
        self.wait()

        cell1_0 = Tex(r"$-15x^2$").move_to((-3,-1,0))
        self.play(Write(cell1_0))
        self.wait()

        def cell_focus(x,y):
            highlight = Rectangle(width=2, height=2, 
                        grid_xstep=2, grid_ystep=2, 
                        color=YELLOW)
            self.play(Indicate(highlight.move_to((x,y,0))))
            self.remove(highlight)

        cell_focus(-3,-1)
        self.wait()
        cell_focus(-1,1)
        self.wait()
        box1 = SurroundingRectangle(problem_alt[0][4:8])
        self.play(Create(box1))
        self.wait()
        self.play(Uncreate(box1))
        self.wait()

        cell0_1_wrk = Tex(r"$-15x^2 + \mathord{?} = -2x^2$").scale(0.8).to_edge(LEFT + UP)
        self.play(Write(cell0_1_wrk))
        self.wait()
        cell0_1_wrkA = Tex(r"$\mathord{?} = 13x^2$").scale(0.8).to_edge(LEFT + UP)
        self.play(ReplacementTransform(cell0_1_wrk, cell0_1_wrkA))
        self.wait()
        cell0_1 = Tex(r"$13x^2$").move_to((-1,1,0))
        self.play(Write(cell0_1))
        self.play(FadeOut(cell0_1_wrkA))
        self.wait()

        check2 = Tex(r"\checkmark", color= GREEN, stroke_width=3)
        self.play(Write(check2.next_to(problem_alt[0][4:8], 0.5*UP)))
        self.wait()

        col1_wrk = Tex(r"$\displaystyle \frac{13x^2}{x}=13x$").to_edge(LEFT + UP).scale(0.8)
        self.play(Write(col1_wrk))
        self.wait()
        col1_hdr = Tex(r"$13x$", color=RED).move_to((-1,2.5,0))
        self.play(Write(col1_hdr))
        self.play(FadeOut(col1_wrk))
        self.wait()
        cell1_1 = Tex(r"$-39x$").move_to((-1,-1,0))
        self.play(Write(cell1_1))
        self.wait()

        cell_focus(-1,-1)
        self.wait()
        cell_focus(1,1)
        self.wait()
        box2 = SurroundingRectangle(problem_alt[0][8:11])
        self.play(Create(box2))
        self.wait()
        self.play(Uncreate(box2))
        self.wait()

        cell0_2_wrk = Tex(r"$-39x + \mathord{?} = 0x$").to_edge(LEFT + UP).scale(0.8)
        self.play(Write(cell0_2_wrk))
        cell0_2_wrkA = Tex(r"$\mathord{?} = 39x$").to_edge(LEFT + UP).scale(0.8)
        self.play(ReplacementTransform(cell0_2_wrk, cell0_2_wrkA))
        self.wait()
        cell0_2 = Tex(r"$39x$").move_to((1,1,0))
        self.play(Write(cell0_2))
        self.play(FadeOut(cell0_2_wrkA))
        self.wait()

        check3 = Tex(r"\checkmark", color= GREEN, stroke_width=3)
        self.play(Write(check3.next_to(problem_alt[0][8:11], 0.5*UP)))
        self.wait()

        col2_wrk = Tex(r"$\displaystyle \frac{39x}{x}=39$").to_edge(LEFT + UP).scale(0.8)
        self.play(Write(col2_wrk))
        self.wait()
        col2_hdr = Tex(r"$39$", color = RED).move_to((1,2.5,0))
        self.play(Write(col2_hdr))
        self.play(FadeOut(col2_wrk))
        self.wait()

        cell1_2 = Tex(r"$-117$").move_to((1,-1,0))
        self.play(Write(cell1_2))
        self.wait()

        cell_focus(1,-1)
        self.wait()

        box3 = SurroundingRectangle(problem_alt[0][11:13])
        self.play(Create(box3))
        self.wait()
        self.play(Uncreate(box3))
        self.wait()

        self.play(Indicate(col2_hdr))
        self.wait()
        col3_hdr = Text("Remainder", color=RED).move_to((3,2.5,0)).scale(0.5)
        self.play(Write(col3_hdr))

        remainder_wrk = Tex(r"$-117 + \mathord{?} = 1$").to_edge(LEFT + UP).scale(0.8)
        self.play(Write(remainder_wrk))
        self.wait()
        remainder_wrkA = Tex(r"$\mathord{?} = 118$").to_edge(LEFT + UP).scale(0.8)
        self.play(ReplacementTransform(remainder_wrk, remainder_wrkA))
        self.wait()
        remainder = Tex(r"$118$", color=RED).move_to((3,1,0))
        self.play(Write(remainder))
        self.play(FadeOut(remainder_wrkA))
        self.wait()
        
        check4 = Tex(r"\checkmark", color= GREEN, stroke_width=3)
        self.play(Write(check4.next_to(problem_alt[0][11:14], 0.5*UP)))
        self.wait()

        quotient = Tex(r"$5x^2 + 13x + 39 + \frac{118}{x-3}$", color=RED).move_to((0,-3,0))
        self.play(Write(quotient))
        quotient_box = SurroundingRectangle(quotient, corner_radius = 0.2)
        self.play(Create(quotient_box))
        self.wait()

