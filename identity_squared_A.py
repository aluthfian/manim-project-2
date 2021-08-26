from manim import *
import numpy as np

config.frame_size = (800,800)

class Formula(Scene):
    def construct(self):
        form_1 = MathTex(r"(a+b)").move_to([0,2,0]).scale(2)
        form_2 = MathTex(r"(a-b)").next_to(form_1, DOWN).scale(2)
        line_1 = Line([-1,0,0],[1,0,0]).next_to(form_2, DOWN).scale(2)
        times_sym = MathTex(r"\times").next_to(line_1, RIGHT).scale(2)
        connect_1 = Arrow(form_1.get_left()+[0.5,0,0],form_2.get_left()+[0.5,0,0],buff=0,stroke_color='#f07fac')
        connect_2 = Arrow(form_1.get_right()-[0.3,0,0],form_2.get_left()+[0.3,0,0],buff=0.25,stroke_color='#8f96ff',stroke_width=10)
        connect_3 = Arrow(form_1.get_right()-[0.5,0,0],form_2.get_right()-[0.5,0,0],buff=0,stroke_color='#f07fac')
        connect_4 = Arrow(form_1.get_left()+[0.3,0,0],form_2.get_right()-[0.3,0,0],buff=0.25,stroke_color='#8f96ff',stroke_width=10)
        a_squared = MathTex(r"a^2", color='#f07fac').next_to(line_1.get_left(), buff=0.4).shift(0.75*DOWN).scale(2)
        plus_ab = MathTex(r"+ab", color='#8f96ff').next_to(a_squared, RIGHT, buff=0.6).shift(0.1*DOWN).scale(2)
        min_ab = MathTex(r"-ab", color='#8f96ff').next_to(plus_ab, DOWN).scale(2)
        b_squared = MathTex(r"-b^2", color='#f07fac').next_to(min_ab, RIGHT, buff=0.6).shift(0.1*UP).scale(2)
        zero = MathTex(r"+0", color='#8f96ff').next_to(a_squared, RIGHT, buff=0.6).shift(0.1*DOWN).scale(2)
        a2_2 = a_squared.copy().scale(2)
        b2_2 = b_squared.copy().scale(2)
        
        self.play(Write(form_1), Write(form_2))
        self.play(Create(line_1), Write(times_sym))
        self.wait(1.0)
        
        self.play(Write(connect_1))
        self.play(Write(a_squared))
        self.play(CounterclockwiseTransform(connect_1, connect_2, path_arc=PI/4))
        self.play(Write(plus_ab))
        self.wait(1.0)
        self.play(FadeOut(connect_1))
        
        self.play(Write(connect_4))
        self.play(Write(min_ab))
        self.play(CounterclockwiseTransform(connect_4, connect_3, path_arc=PI/4))
        self.play(Write(b_squared))
        self.wait(1.0)
        self.play(FadeOut(connect_4))
        
        self.play(FadeOut(plus_ab), FadeOut(min_ab, target_position=plus_ab), FadeIn(zero))
        self.play(b_squared.animate.next_to(zero, RIGHT).shift(0.05*UP))
        self.wait(1.0)
        
        self.play(FadeOut(zero), a_squared.animate.next_to(line_1.get_center(), LEFT, buff=0.4).shift(0.75*DOWN), b_squared.animate.next_to(a_squared.get_right(), RIGHT, buff=0.9))
        self.wait(5.0)
