from manim import *
config.tex_template = TexTemplateLibrary.ctex

class SumDiffLineModel(Scene):
    def construct(self):
        # Parameters
        sum_val = 13
        diff_val = 5
        unit = 0.5  # Increased unit length for better visibility

        # Calculations
        small_num = (sum_val - diff_val) / 2  # (13-5)/2 = 4
        big_num = small_num + diff_val       # 4+5 = 9
        
        w_small = small_num * unit      # Visual length: 4*0.5 = 2.0
        w_big = big_num * unit          # Visual length: 9*0.5 = 4.5
        w_diff = diff_val * unit        # Visual length: 5*0.5 = 2.5

        # 1) Title with better spacing
        title = Text("和差问题", font_size=48, color=YELLOW)
        problem = Text("已知两数之和为13，差为5，求这两个数", 
                     font_size=36, color=BLUE)
        
        title_group = VGroup(title, problem).arrange(DOWN, buff=0.5)
        self.play(Write(title_group))
        self.play(title_group.animate.to_edge(UP, buff=0.5))
        self.wait(1)

        # 2) Show formula first (top-left)
        formula = MathTex(
            r"\text{大数} &= \frac{\text{和} + \text{差}}{2} \\",
            r"\text{小数} &= \frac{\text{和} - \text{差}}{2}",
            font_size=40
        ).set_color_by_tex("大数", BLUE_B).set_color_by_tex("小数", GREEN_B)
        
        formula_box = SurroundingRectangle(formula, buff=0.3, color=WHITE, corner_radius=0.2)
        formula_group = VGroup(formula_box, formula).to_edge(LEFT).shift(UP*0.5)
        
        self.play(FadeIn(formula_group))
        self.wait(3)
        self.play(formula_group.animate.scale(0.8))
        self.wait(3)

        # 3) Draw accurate line models (more centered)
        # Big number line (top)
        big_line = Line(ORIGIN, RIGHT * w_big, stroke_width=12, color=BLUE_B)
        big_line.shift(UP*0.5 + RIGHT*1)  # Reduced right shift to center more
        
        # Mark the small number portion on big line
        small_part = Line(big_line.get_start(), big_line.get_start()+RIGHT*w_small, 
                         stroke_width=12, color=GREEN_B)
        diff_part = Line(small_part.get_end(), big_line.get_end(),
                        stroke_width=12, color=RED_C)
        
        label_big = Text("大数", font_size=32, color=BLUE_B).next_to(big_line, LEFT, buff=0.5)
        
        # Small number line (bottom) - exactly matches the small part of big number
        small_line = Line(ORIGIN, RIGHT * w_small, stroke_width=12, color=GREEN_B)
        small_line.next_to(big_line, DOWN, buff=1.0).align_to(big_line, LEFT)
        
        label_small = Text("小数", font_size=32, color=GREEN_B).next_to(small_line, LEFT, buff=0.5)
        
        # Animate line creation
        self.play(
            LaggedStart(
                Create(big_line),
                Write(label_big),
                Create(small_line),
                Write(label_small),
                lag_ratio=0.5
            ),
            run_time=4
        )
        self.wait(4)

        # Highlight the small number portion in big line
        self.play(
            Transform(big_line.copy().set_color(GREEN_B), small_part.copy()),
            run_time=1.5
        )
        self.add(small_part, diff_part)
        self.remove(big_line)
        big_line = VGroup(small_part, diff_part)
        self.wait(3)

        # Sum and difference annotations
        brace_sum = Brace(VGroup(big_line, small_line), RIGHT, buff=0.3)
        label_sum = MathTex("和=13", font_size=36, color=YELLOW_D).next_to(brace_sum, RIGHT, buff=0.2)
        
        brace_diff = Brace(diff_part, UP, buff=0.2)
        label_diff = MathTex("差=5", font_size=36, color=RED_C).next_to(brace_diff, UP, buff=0.2)
        
        self.play(
            GrowFromCenter(brace_sum),
            FadeIn(label_sum, shift=LEFT),
            GrowFromCenter(brace_diff),
            FadeIn(label_diff, shift=UP),
            run_time=1.5
        )
        self.wait(1.5)

        # 4) Remove difference section with animation
        self.play(
            diff_part.animate.set_color(GREY),
            brace_diff.animate.set_color(GREY),
            label_diff.animate.set_color(GREY),
            run_time=0.7
        )
        self.play(
            FadeOut(diff_part),
            FadeOut(brace_diff),
            FadeOut(label_diff),
            run_time=0.8
        )
        self.wait(0.5)

        # Show remaining length (now we have two identical small parts)
        brace_remain = Brace(VGroup(small_part, small_line), UP, buff=0.2)
        label_remain = MathTex(r"\text{剩余} = 13 - 5 = 8", font_size=36, color=GREEN_D).next_to(brace_remain, UP, buff=0.2)
        self.play(
            GrowFromCenter(brace_remain),
            FadeIn(label_remain, shift=UP),
            run_time=1.5
        )
        self.wait(1)

        # 5) Show equal division with calculation
        brace1 = Brace(small_part, DOWN, buff=0.2)
        label1 = MathTex(r"\frac{8}{2} = 4", font_size=36, color=BLUE_D).next_to(brace1, DOWN, buff=0.2)
        brace2 = Brace(small_line, DOWN, buff=0.2)
        label2 = MathTex(r"\frac{8}{2} = 4", font_size=36, color=BLUE_D).next_to(brace2, DOWN, buff=0.2)
        
        self.play(
            LaggedStart(
                # GrowFromCenter(brace1),
                # Write(label1),
                GrowFromCenter(brace2),
                Write(label2),
                lag_ratio=0.7
            ),
            run_time=2
        )
        self.wait(2)

        # 6) Final answer moved to bottom left
        answer_content = VGroup(
            MathTex(r"\text{小数} = \frac{13 - 5}{2} = 4", font_size=40, color=GREEN_B),
            MathTex(r"\text{大数} = 4 + 5 = 9", font_size=40, color=BLUE_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        answer_box = SurroundingRectangle(
            answer_content,
            buff=0.5,
            color=YELLOW,
            corner_radius=0.3,
            stroke_width=3
        )
        answer_group = VGroup(answer_box, answer_content).next_to(formula_group, DOWN, aligned_edge=LEFT, buff=0.5)
        
        self.play(
            FadeIn(answer_group),
            run_time=1.5
        )
        self.wait(3)