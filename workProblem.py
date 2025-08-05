from manim import *
config.tex_template = TexTemplateLibrary.ctex

class OptimizedWorkProblem(Scene):
    def construct(self):
        # 问题参数
        total_work = 1  # 总工作量为1
        a_days = 6      # 甲单独完成需要6天
        b_days = 12     # 乙单独完成需要12天
        
        # 计算参数
        a_speed = total_work / a_days
        b_speed = total_work / b_days
        total_speed = a_speed + b_speed
        collab_time = total_work / total_speed

        # 1) 标题和问题描述（顶部居中）
        title = Text("工程问题", font_size=48, color=YELLOW)
        problem = Text(
            "甲单独完成工程需要6天，乙单独需要12天\n两人合作需要多少天完成？",
            font_size=36, 
            color=BLUE,
            line_spacing=1.2
        )
        
        title_group = VGroup(title, problem).arrange(DOWN, buff=0.5)
        self.play(Write(title_group))
        self.play(title_group.animate.to_edge(UP, buff=0.5))
        self.wait(2)

        # 2) 公式展示（右上角，缩小尺寸避免遮挡）
        formula = MathTex(
            r"\text{工效} &= \frac{\text{总量}}{\text{时间}} \\",
            r"\text{时间} &= \frac{\text{总量}}{\text{工效和}}",
            font_size=32  # 缩小字体
        ).set_color_by_tex("效", BLUE_B)
        
        formula_box = SurroundingRectangle(
            formula, 
            buff=0.3, 
            color=WHITE, 
            corner_radius=0.2,
            stroke_width=2
        )
        formula_group = VGroup(formula_box, formula).scale(0.75).to_corner(UR, buff=0.75)
        
        self.play(FadeIn(formula_group))
        self.wait(1.5)

        # 3) 工作条带图示（居中偏左，留出右侧空间）
        unit = 3.5  # 缩短单位长度
        diagram_center = LEFT * 1.5  # 整体向左移动
        
        # 工作总量条（顶部）
        total_bar = Line(ORIGIN, RIGHT * unit, stroke_width=18, color=WHITE)
        total_bar.move_to(diagram_center + UP*1.5)
        total_label = Text("工作总量 = 1", font_size=30).next_to(total_bar, UP, buff=0.4)
        
        # 甲的工作效率
        a_bar = Line(ORIGIN, RIGHT * unit * a_speed, stroke_width=16, color=BLUE_B)
        a_bar.next_to(total_bar, DOWN, buff=1.2).align_to(total_bar, LEFT)
        a_label = Text("甲的工效", font_size=26, color=BLUE_B).next_to(a_bar, UP, buff=0.2)
        a_text = MathTex(r"\frac{1}{6}", "\\text{/天}", font_size=30).next_to(a_bar, DOWN, buff=0.2)
        a_text[0].set_color(BLUE_B)
        
        # 乙的工作效率
        b_bar = Line(ORIGIN, RIGHT * unit * b_speed, stroke_width=16, color=GREEN_B)
        b_bar.next_to(a_bar, DOWN, buff=0.8).align_to(total_bar, LEFT)
        b_label = Text("乙的工效", font_size=26, color=GREEN_B).next_to(b_bar, UP, buff=0.2)
        b_text = MathTex(r"\frac{1}{12}", "\\text{/天}", font_size=30).next_to(b_bar, DOWN, buff=0.2)
        b_text[0].set_color(GREEN_B)
        
        # 动画展示（分阶段显示）
        self.play(
            LaggedStart(
                Create(total_bar),
                Write(total_label),
                lag_ratio=0.8
            ),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            LaggedStart(
                Create(a_bar),
                Write(a_label),
                Write(a_text),
                lag_ratio=0.6
            ),
            run_time=1.8
        )
        self.wait(0.3)
        
        self.play(
            LaggedStart(
                Create(b_bar),
                Write(b_label),
                Write(b_text),
                lag_ratio=0.6
            ),
            run_time=1.8
        )
        self.wait(1)

        # 4) 合作效率展示（右侧对齐，避免重叠）
        collab_bar = Line(ORIGIN, RIGHT * unit * total_speed, stroke_width=16, color=RED_C)
        collab_bar.move_to(diagram_center + DOWN*0.2)
        collab_label = Text("合作工效", font_size=28, color=RED_C).next_to(collab_bar, UP, buff=0.3)
        
        # 使用箭头连接更直观
        arrow1 = CurvedArrow(
            a_bar.get_right() + DOWN*0.2,
            collab_bar.get_left() + UP*0.2,
            color=WHITE,
            angle=-TAU/4
        )
        plus = MathTex("+", font_size=36).move_to(arrow1.get_center())
        
        arrow2 = CurvedArrow(
            b_bar.get_right() + DOWN*0.2,
            collab_bar.get_left() + DOWN*0.2,
            color=WHITE,
            angle=TAU/4
        )
        
        collab_equation = MathTex(
            r"\frac{1}{6}", "+", r"\frac{1}{12}", "=", r"\frac{1}{4}", 
            font_size=34
        ).next_to(collab_bar, DOWN, buff=0.4)
        collab_equation[0].set_color(BLUE_B)
        collab_equation[2].set_color(GREEN_B)
        collab_equation[4].set_color(RED_C)
        
        # self.play(
        #     GrowArrow(arrow1),
        #     GrowArrow(arrow2),
        #     FadeIn(plus),
        #     run_time=1.5
        # )
        # self.wait(0.5)
        
        self.play(
            Create(collab_bar),
            Write(collab_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        self.play(
            Write(collab_equation),
            run_time=2
        )
        self.wait(2)

        # 5) 计算过程（底部左侧，分步显示）
        calculation = VGroup(
            MathTex(r"\text{合作时间} = \frac{\text{总量}}{\text{工效和}}", font_size=34),
            MathTex(r"= \frac{1}{\frac{1}{4}}", font_size=34),
            MathTex(r"= 4 \text{天}", font_size=36, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        
        calculation.shift(DOWN*1.5 + LEFT*3)
        
        calc_box = SurroundingRectangle(
            calculation, 
            buff=0.4, 
            color=YELLOW, 
            corner_radius=0.2,
            stroke_width=2
        )
        
        # 分步动画
        self.play(
            Create(calc_box),
            Write(calculation[0]),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            Write(calculation[1]),
            run_time=1
        )
        self.wait(1)
        
        self.play(
            Write(calculation[2]),
            run_time=1.5
        )
        self.wait(2)

        # 6) 最终答案（底部中央，突出显示）
        answer = Tex("两人合作需要", "4", "天完成", font_size=42)
        answer[1].set_color(YELLOW)
        answer_box = SurroundingRectangle(
            answer, 
            buff=0.5, 
            color=RED, 
            corner_radius=0.3,
            stroke_width=3
        )
        answer_group = VGroup(answer_box, answer).center().shift(DOWN*1.5)
        
        self.play(
            DrawBorderThenFill(answer_box),
            Write(answer),
            run_time=2
        )
        self.wait(3)