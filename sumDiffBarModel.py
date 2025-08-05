from manim import *
config.tex_template = TexTemplateLibrary.ctex
config.frame_height = 12  # 增加垂直空间（默认8）
config.frame_width = config.frame_height * 16/9  # 保持16:9比例
class SumDiffLineModel(Scene):
    def construct(self):
        # Parameters
        sum_val = 13
        diff_val = 5
        unit = 0.8  # 进一步增加单位长度

        # Calculations
        small_num = (sum_val - diff_val) / 2
        big_num = small_num + diff_val
        
        w_small = small_num * unit
        w_big = big_num * unit
        w_diff = diff_val * unit

        # 1) 更大的标题和问题描述
        title = Text("和差问题", font_size=72, color=YELLOW)
        problem = Text("已知两数之和为13，差为5，求这两个数", 
                     font_size=48, color=BLUE)
        
        title_group = VGroup(title, problem).arrange(DOWN, buff=0.5)
        self.play(Write(title_group))
        self.play(title_group.animate.to_edge(UP, buff=1.0))
        self.wait(3)

        # 3) 更大的线段模型
        # 调整整体位置向下移动
        line_group_center = DOWN * 0.5
        
        # 大数线段
        big_line = Line(ORIGIN, RIGHT * w_big, stroke_width=20, color=BLUE_B)
        big_line.move_to(line_group_center + UP*1.5 + RIGHT*1)
        
        # 标记大数中的小数部分
        small_part = Line(big_line.get_start(), big_line.get_start()+RIGHT*w_small, 
                         stroke_width=20, color=GREEN_B)
        diff_part = Line(small_part.get_end(), big_line.get_end(),
                        stroke_width=20, color=RED_C)
        
        label_big = Text("大数", font_size=48, color=BLUE_B).next_to(big_line, LEFT, buff=1.0)
        
        # 小数线段
        small_line = Line(ORIGIN, RIGHT * w_small, stroke_width=20, color=GREEN_B)
        small_line.next_to(big_line, DOWN, buff=1.5).align_to(big_line, LEFT)
        
        label_small = Text("小数", font_size=48, color=GREEN_B).next_to(small_line, LEFT, buff=1.0)
        
        # 动画展示
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

        # 高亮大数中的小数部分
        self.play(
            Transform(big_line.copy().set_color(GREEN_B), small_part.copy()),
            run_time=1.5
        )
        self.add(small_part, diff_part)
        self.remove(big_line)
        big_line = VGroup(small_part, diff_part)
        self.wait(3)

        # 更大的和差标注
        brace_sum = Brace(VGroup(big_line, small_line), RIGHT, buff=0.5)
        label_sum = MathTex("和=13", font_size=48, color=YELLOW_D).next_to(brace_sum, RIGHT, buff=0.4)
        
        brace_diff = Brace(diff_part, UP, buff=0.4)
        label_diff = MathTex("差=5", font_size=48, color=RED_C).next_to(brace_diff, UP, buff=0.4)
        
        self.play(
            GrowFromCenter(brace_sum),
            FadeIn(label_sum, shift=LEFT),
            GrowFromCenter(brace_diff),
            FadeIn(label_diff, shift=UP),
            run_time=1.5
        )
        self.wait(1.5)

        # 4) 移除差的部分
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

        # 显示剩余部分（更大的标注）
        brace_remain = Brace(VGroup(small_part, small_line), UP, buff=0.4)
        label_remain = MathTex(r"\text{剩余} = 13 - 5 = 8", font_size=48, color=WHITE).next_to(brace_remain, UP, buff=0.2)
        self.play(
            GrowFromCenter(brace_remain),
            FadeIn(label_remain, shift=UP),
            run_time=1.5
        )
        self.wait(1)

        # 5) 显示等分计算（更大的标注）
        brace1 = Brace(small_part, DOWN, buff=0.4)
        #label1 = MathTex(r"\frac{8}{2} = 4", font_size=48, color=BLUE_D).next_to(brace1, DOWN, buff=0.4)
        brace2 = Brace(small_line, DOWN, buff=0.4)
        label2 = MathTex(r"\frac{8}{2} = 4", font_size=48, color=BLUE_D).next_to(brace2, DOWN, buff=0.4)
        
        self.play(
            LaggedStart(
                GrowFromCenter(brace1),
               # Write(label1),
                GrowFromCenter(brace2),
                Write(label2),
                lag_ratio=0.7
            ),
            run_time=2
        )
        self.wait(5)

        # 6) 更大的最终答案展示
        answer_content = VGroup(
            MathTex(r"\text{小数} = \frac{13 - 5}{2} = 4", font_size=54, color=GREEN_B),
            MathTex(r"\text{大数} = 4 + 5 = 9", font_size=54, color=BLUE_B)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)
        
        answer_box = SurroundingRectangle(
            answer_content,
            buff=0.7,
            color=YELLOW,
            corner_radius=0.4,
            stroke_width=5
        )
        # answer_group = VGroup(answer_box, answer_content).next_to(formula_group, DOWN, aligned_edge=LEFT, buff=1.0)
        
         # 2) 更大的公式展示
        formula = MathTex(
            r"\text{大数} &= \frac{\text{和} + \text{差}}{2} \\",
            r"\text{小数} &= \frac{\text{和} - \text{差}}{2}",
            font_size=54
        ).set_color_by_tex("大数", BLUE_B).set_color_by_tex("小数", GREEN_B)
        
        formula_box = SurroundingRectangle(formula, buff=0.5, color=WHITE, corner_radius=0.2)
        formula_group = VGroup(formula_box, formula).to_corner(DL).shift(UP*1.0)
        
        self.play(FadeIn(formula_group))
        self.wait(3)
        self.play(formula_group.animate.scale(1.0))  # 不再缩小
        self.wait(3)

        # self.play(
        #     FadeIn(answer_group),
        #     run_time=1.5
        # )
        # self.wait(3)