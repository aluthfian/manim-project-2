from manim import *
import numpy as np

config.frame_size = (800,800)

class Formula(Scene):
    def construct(self):
        form_1 = MathTex(r"(a-b)").move_to([0,2,0]).scale(2)
        form_2 = MathTex(r"(a-b)").next_to(form_1, DOWN).scale(2)
        line_1 = Line([-1,0,0],[1,0,0]).next_to(form_2, DOWN).scale(2)
        times_sym = MathTex(r"\times").next_to(line_1, RIGHT).scale(2)
        connect_1 = Arrow(form_1.get_left()+[0.5,0,0],form_2.get_left()+[0.5,0,0],buff=0,stroke_color='#f07fac')
        connect_2 = Arrow(form_1.get_right()-[0.3,0,0],form_2.get_left()+[0.3,0,0],buff=0.25,stroke_color='#8f96ff',stroke_width=10)
        connect_3 = Arrow(form_1.get_right()-[0.5,0,0],form_2.get_right()-[0.5,0,0],buff=0,stroke_color='#f07fac')
        connect_4 = Arrow(form_1.get_left()+[0.3,0,0],form_2.get_right()-[0.3,0,0],buff=0.25,stroke_color='#8f96ff',stroke_width=10)
        a_squared = MathTex(r"a^2", color='#f07fac').next_to(line_1.get_left(), buff=0.4).shift(0.75*DOWN).scale(2)
        plus_ab = MathTex(r"-ab", color='#8f96ff').next_to(a_squared, RIGHT, buff=0.6).shift(0.1*DOWN).scale(2)
        min_ab = MathTex(r"-ab", color='#8f96ff').next_to(plus_ab, DOWN).scale(2)
        b_squared = MathTex(r"+b^2", color='#f07fac').next_to(min_ab, RIGHT, buff=0.6).shift(0.1*UP).scale(2)
        two_ab = MathTex(r"-2ab", color='#8f96ff').next_to(a_squared, RIGHT, buff=0.6).shift(0.1*DOWN).scale(2)
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
        
        self.play(FadeOut(plus_ab), FadeOut(min_ab, target_position=plus_ab), FadeIn(two_ab))
        self.play(b_squared.animate.next_to(two_ab, RIGHT).shift(0.05*UP))
        self.wait(2.0)
        
        form_3 = MathTex(r"(a-b)^2").move_to(form_2.get_center()).scale(2)
        self.play(FadeOut(form_1, target_position=form_2), FadeOut(form_2), FadeOut(times_sym), FadeIn(form_3))
        self.wait(2.0)
        
        self.play(form_3.animate.to_edge(edge=RIGHT, buff=2.0))
        equal = MathTex(r"=").next_to(form_3.get_left(), LEFT, buff=0.6).scale(2)
        self.play(ReplacementTransform(line_1, equal))
        self.play(b_squared.animate.move_to(equal.get_left()-[0.5,0,0], aligned_edge=RIGHT))
        self.play(two_ab.animate.move_to(b_squared.get_left()-[0.5,0,0], aligned_edge=RIGHT))
        self.play(a_squared.animate.move_to(two_ab.get_left()-[0.5,0,0], aligned_edge=RIGHT))

        self.wait(2.0)
        
        pos_b_2 = b_squared.copy().move_to(a_squared.get_right()+[0.5,0,0], aligned_edge=LEFT)
        equal_2 = equal.copy().move_to(pos_b_2.get_right()+[0.5,0,0], aligned_edge=LEFT)
        pos_form3_b = form_3.copy().move_to(equal_2.get_right()+[0.5,0,0], aligned_edge=LEFT)
        two_ab_2 = MathTex(r"+2ab", color='#8f96ff').next_to(pos_form3_b, RIGHT, buff=0.75).scale(2)
        self.play(TransformMatchingTex(two_ab, two_ab_2),
                  b_squared.animate.move_to(a_squared.get_right()+[0.5,0,0], aligned_edge=LEFT),
                  equal.animate.move_to(equal_2.get_center()),
                  form_3.animate.move_to(pos_form3_b.get_center()))
        self.wait(2.0)
