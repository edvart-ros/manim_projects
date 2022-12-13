from manim import *
import numpy as np

def f(x):
    return 10*x**3+10*x**2-1

def df_dx(x):
    return 30*x**2+20*x

def next_guess(x):
    return x-f(x)/df_dx(x)




class NewtonsMethod(Scene):
    def construct(self):


        #introduce newtons method, display equation
        eq = Tex("\\underline{Newton's Method:}")
        eq.shift(0.9*UP)
        self.play(Write(eq))
        eq0 = Tex("$x_{n+1} = x_n -\\frac{f(x_n)}{f'(x_n)}$")
        self.play(Write(eq0))
        self.wait(2)

        #remove text and shift equation to corner
        self.play(Uncreate(eq))
        self.play(eq0.animate.shift(4.5*RIGHT, 3*DOWN), color=BLUE)

        #draw rectangle around equation
        rect1 = Rectangle(width=4.7, height=1.6)
        rect1.shift(4.5*RIGHT, 3*DOWN)
        self.play(Create(rect1))

        #add coordinate plane
        plane = NumberPlane(
            background_line_style={
                "stroke_width": 3,
                "stroke_opacity": 0.3
            }
        )
        self.play(Create(plane))

        #display f(x)
        eq1=Tex("$f(x) = 10x^3+10x^2-1$", font_size=35)
        eq1.shift(3*UP, 4*RIGHT)        

        #define axes
        ax = Axes(
            x_range=[-1.6, 1.6, 0.2672],
            y_range=[-0.8, 0.8, 0.2672],
            #axis_config={"include_numbers": True}
            )
        
        #define f(x) curve
        curve = ax.plot(lambda x: 10*x**3+10*x**2-1, color=RED)
        
        #draw f(x)
        self.play(Create(ax, run_time=1))
        self.wait(1)
        self.play(Create(curve, run_time=3), Write(eq1))

        #define first guess
        x_0 = -0.1

        #draw dashed line from first guess up to the function
        eq2 = Tex('$x_0$', font_size=35).move_to(ax.c2p(x_0, 0.1, 0))
        dot_0 = Dot(color=BLUE).move_to(ax.c2p(x_0, 0, 0))
        dashed_0 = DashedLine(ax.c2p(x_0, 0, 0), ax.coords_to_point(x_0, f(x_0), 0), dash_length=0.15, color=BLUE)
        self.play(Create(dot_0), Create(eq2))
        self.play(Create(dashed_0))

        #mark value f(x_0)
        eq3= Tex('$f(x_0)$', font_size=35).shift(1*LEFT, 3.4*DOWN)
        dot_1 = Dot(color=BLUE).move_to(ax.coords_to_point(x_0, f(x_0), 0))
        self.play(Create(dot_1), Create(eq3))
        self.wait(1)


        #define tangent line
        tangent1 = ax.plot(lambda x: df_dx(x_0)*(x-x_0)+f(x_0), color=BLUE)

        #display tangent equation
        eq4=Tex("$f'(x_0)\cdot (x-x_0)+f(x_0)$", font_size=35)
        eq4.shift(3*UP, 2*LEFT)


        #draw tangent line
        self.play(Create(tangent1, run_time = 1, Reverse=True), Write(eq4))
        self.wait(2)

        #animate next guess
        x_1 = -0.63529
        eq5= Tex('$f(x_1)$', font_size=35).shift(1*LEFT, 3.4*DOWN)
        dot_2 = Dot(color=BLUE).move_to(ax.coords_to_point(x_0, f(x_0), 0))
        self.play(Create(dot_2))
        self.wait(0.3)
        self.play(dot_2.animate.shift([ax.c2p(x_1-x_0, -f(x_0), 0)]))

        #clear clutter
        self.wait(3)
        self.play(Uncreate(tangent1), Uncreate(eq4), Uncreate(eq3), Uncreate(eq5))



        #mark and repeat guessing
        eq2 = Tex('$x_1$', font_size=35).move_to(ax.c2p(x_1, -0.1, 0))
        dot_3 = Dot(color=BLUE).move_to(ax.c2p(x_1, 0, 0))
        dashed_0 = DashedLine(ax.c2p(x_1, 0, 0), ax.c2p(x_1, f(x_1), 0), dash_length=0.15, color=BLUE)
        self.play(Create(dot_3), Create(eq2))
        self.play(Create(dashed_0))

        #mark f(x_1)
        dot_4 = Dot(color=BLUE).move_to(ax.c2p(x_1, f(x_1), 0))
        self.play(Create(dot_4))
        self.wait(1)

        #tangent line
        tangent2 = ax.plot(lambda x: df_dx(x_1)*(x-x_1)+f(x_1), color=BLUE)
        self.play(Create(tangent2, run_time = 1, Reverse=True), Write(eq4))
        self.wait(2)


        "herfra og utover begynte jeg å bli litt lei, og ville bare bli ferdig med prosjektet :-)"


        #mark and repeat guessing
        x_2 = next_guess(x_1)
        eq2 = Tex('$x_2$', font_size=35).move_to(ax.c2p(x_2, 0.1, 0))

        dot_5 = Dot(color=BLUE).move_to(ax.c2p(x_1, f(x_1), 0))
        self.play(dot_5.animate.shift([ax.c2p(x_2-x_1, -f(x_1), 0)]))
        dashed_0 = DashedLine(ax.c2p(x_2, 0, 0), ax.c2p(x_2, f(x_2), 0), dash_length=0.15, color=BLUE)
        self.play(Create(eq2))
        self.play(Create(dashed_0))

        dot_6 = Dot(color=BLUE).move_to(ax.c2p(x_2, f(x_2), 0))
        self.play(Create(dot_6))
        self.wait(1)

        self.play(Uncreate(tangent2))

        tangent3 = ax.plot(lambda x: df_dx(x_2)*(x-x_2)+f(x_2), color=BLUE)
        self.play(Create(tangent3, run_time = 1, Reverse=True), Write(eq4))
        self.wait(2)

################################################
################################################

        #get next root
        x_3 = next_guess(x_2)
        #create root at previous point and shift to next root
        dot_7 = Dot(color=BLUE).move_to(ax.c2p(x_2, f(x_2), 0))
        self.play(dot_7.animate.shift([ax.c2p(x_3-x_2, -f(x_2), 0)]))
        #remove tangent line
        self.play(Uncreate(tangent3))
        #mark root with text
        eq7 = Tex('$x_3$', font_size=35).move_to(ax.c2p(x_3, -0.1, 0))
        self.play(Create(eq7))
        #create dashed line up  to intersection
        dashed_1 = DashedLine(ax.c2p(x_3, 0, 0), ax.c2p(x_3, f(x_3), 0), dash_length=0.15, color=BLUE)
        self.play(Create(dashed_1))
        #mark intersection
        dot_8 = dot_7 = Dot(color=BLUE).move_to(ax.c2p(x_3, f(x_3), 0))
        self.play(Create(dot_8))
        self.wait(1)
        #create next tangent
        tangent4 = ax.plot(lambda x: df_dx(x_3)*(x-x_3)+f(x_3), color=BLUE)
        self.play(Create(tangent4), run_time = 1)


################################################
################################################

        #make dots smaller and remove equation
        #get next root
        x_4 = next_guess(x_3)
        #create root at previous point and shift to next root
        dot_8 = Dot(color=BLUE, radius=0.075).move_to(ax.c2p(x_3, f(x_3), 0))
        self.play(dot_8.animate.shift([ax.c2p(x_4-x_3, -f(x_3), 0)]))
        #remove tangent line
        self.play(Uncreate(tangent4))
        #create dashed line up  to intersection
        dashed_1 = DashedLine(ax.c2p(x_4, 0, 0), ax.c2p(x_4, f(x_4), 0), dash_length=0.15, color=BLUE)
        self.play(Create(dashed_1))
        #mark intersection
        dot_9 = dot_7 = Dot(color=BLUE, radius=0.075).move_to(ax.c2p(x_4, f(x_4), 0))
        self.play(Create(dot_9))
        self.wait(1)
        #create next tangent
        tangent5 = ax.plot(lambda x: df_dx(x_4)*(x-x_4)+f(x_4), color=BLUE)
        self.play(Create(tangent5), run_time = 1)


# ################################################
# ################################################

        #get next root
        x_5 = next_guess(x_4)
        #create root at previous point and shift to next root
        dot_10 = Dot(color=BLUE, radius=0.075).move_to(ax.c2p(x_4, f(x_4), 0))
        self.play(dot_10.animate.shift([ax.c2p(x_5-x_4, -f(x_4), 0)]))
        #remove tangent line
        self.play(Uncreate(tangent5))
        #create dashed line up  to intersection
        dashed_2 = DashedLine(ax.c2p(x_5, 0, 0), ax.c2p(x_5, f(x_5), 0), dash_length=0.15, color=BLUE)
        self.play(Create(dashed_2))
        #mark intersection
        dot_10 = Dot(color=BLUE, radius=0.075).move_to(ax.c2p(x_5, f(x_5), 0))
        self.play(Create(dot_10))
        self.wait(1)
        #create next tangent
        #tangent5 = ax.plot(lambda x: df_dx(x_5)*(x-x_5)+f(x_5), color=BLUE)
        #self.play(Create(tangent5), run_time = 1)













