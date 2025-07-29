from manim import *
import numpy as np

config.tex_template = TexTemplateLibrary.ctex

class DragCurtainModel(Scene):
    def construct(self):
        # 设置中文显示
        Text.set_default(font="Microsoft YaHei")
        
        # 颜色定义
        PARALLEL_LINE_COLOR = LIGHT_GREY
        BASE_LINE_COLOR = RED
        HEIGHT_LINE_COLOR = YELLOW
        TRIANGLE_COLOR = "#4682B4"  # 钢蓝色
        TEXT_COLOR = WHITE
        HIGHLIGHT_COLOR = "#FFD700"  # 金色
        
        # ========== 1. 标题动画 ==========
        title = Text("拖窗帘模型演示", font_size=48, gradient=(BLUE, TEAL))
        subtitle = Text("同底等高面积不变原理", font_size=24, color=HIGHLIGHT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        # 标题入场动画
        self.play(
            Write(title, run_time=1.5),
            FadeIn(subtitle, shift=DOWN*0.5),
        )
        self.wait(3)
        
        # 标题移动至顶部
        title_group = VGroup(title, subtitle)
        self.play(
            title_group.animate.to_edge(UP, buff=0.5).scale(0.8),
            run_time=1.2
        )
        self.wait(3)
        
        # ========== 2. 创建平行线系统 ==========
        line1 = Line(start=4*LEFT+2*DOWN, end=4*RIGHT+2*DOWN, 
                    color=PARALLEL_LINE_COLOR, stroke_width=4)
        line2 = Line(start=4*LEFT+2*UP, end=4*RIGHT+2*UP, 
                    color=PARALLEL_LINE_COLOR, stroke_width=4)
        
        # 平行线创建动画
        self.play(
            LaggedStart(
                Create(line1),
                Create(line2),
                lag_ratio=0.7
            ),
            run_time=1.8
        ) 
        
        # ========== 3. 创建底边和高度 ==========
        base_start = line1.get_start() + RIGHT*1.5
        base_end = line1.get_start() + RIGHT*3.5
        base_line = Line(base_start, base_end, 
                        color=BASE_LINE_COLOR, stroke_width=6)
        
        # 底边标签（带下划线强调）
        base_label = VGroup(
            Text("固定底边 = 2cm", font_size=26, color=BASE_LINE_COLOR),
            Underline(Text("固定底边 = 2cm", font_size=26), color=BASE_LINE_COLOR)
        )
        base_label.next_to(base_line, DOWN*1.2)
        
        height_line = DashedLine(base_start, base_start+UP*4, 
                               color=HEIGHT_LINE_COLOR, stroke_width=4)
        
        # 高度标签（带双向箭头）
        height_label = VGroup(
            Text("高度固定 = 4cm", font_size=24, color=HEIGHT_LINE_COLOR)
        ).arrange(RIGHT, buff=0.2)
        height_label.next_to(height_line, RIGHT, buff=0.3)
        
        # 底边和高度动画
        self.play(
            GrowFromEdge(base_line, LEFT),
            run_time=1.2
        )
        self.play(
            Write(base_label),
            run_time=1
        )
        self.play(
            GrowFromPoint(height_line, height_line.get_start()),
            run_time=1.5
        )
        self.play(
            FadeIn(height_label, shift=LEFT*0.5),
            run_time=1
        )
        self.wait(3)
        
        # ========== 4. 创建初始三角形 ==========
        vertex = base_start + RIGHT*1 + UP*4
        triangle = Polygon(base_start, base_end, vertex,
                         color=TRIANGLE_COLOR, 
                         fill_opacity=0.7,
                         stroke_width=4)
        
        # 面积公式分步展示
        formula_title = Text("面积计算过程:", font_size=28, color=HIGHLIGHT_COLOR)
        formula_title.to_edge(RIGHT).shift(LEFT*1 + UP*1.5)
        
        formula_steps = VGroup(
            MathTex(r"S = \frac{1}{2} \times \text{底边} \times \text{高}", font_size=32),
            MathTex(r"= \frac{1}{2} \times 2 \times 4", font_size=32),
            MathTex(r"= 4\ \text{cm}^2", font_size=36, color=HIGHLIGHT_COLOR)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        formula_steps.next_to(formula_title, DOWN, aligned_edge=LEFT)
        
        # 三角形和公式动画
        self.play(
            DrawBorderThenFill(triangle),
            run_time=1.8
        )
        self.play(
            Write(formula_title),
            run_time=1
        )
        for step in formula_steps:
            self.play(
                Write(step),
                run_time=1.2
            )
            self.wait(2)
        self.wait(3)
        
        # 顶点移动路径
        vertex_positions = [
            base_start + 0.8*RIGHT + UP*4,
            base_start + 3.2*RIGHT + UP*4,
            base_start + 1.5*RIGHT + UP*4,
            base_start + 2.5*RIGHT + UP*4,
            base_start + 1.0*RIGHT + UP*4
        ]
        
        # 创建移动轨迹虚线
        trace_line = DashedVMobject(Line(vertex_positions[0], vertex_positions[1]), 
                                  num_dashes=20, color=GRAY)
        
        self.play(
            Create(trace_line),  # 这里替换了原来的ShowCreation
            run_time=1.5
        )
        
        for i, pos in enumerate(vertex_positions):
            new_triangle = Polygon(base_start, base_end, pos,
                                 color=TRIANGLE_COLOR, 
                                 fill_opacity=0.7)
            
            # 顶点标记
            vertex_mark = VGroup(
                Dot(pos, color=HIGHLIGHT_COLOR, radius=0.1),
                Text(f"位置{i+1}", font_size=20, color=WHITE).next_to(pos, UP, buff=0.15)
            )
            
            self.play(
                Transform(triangle, new_triangle),
                FadeIn(vertex_mark),
                run_time=1.5,
                rate_func=smooth
            )
            self.wait(2)
            self.play(
                FadeOut(vertex_mark),
                run_time=0.5
            )
        
        # ========== 6. 原理总结 ==========
        principle_box = RoundedRectangle(
            width=5, height=3.5, 
            corner_radius=0.2,
            color=HIGHLIGHT_COLOR,
            fill_color=BLACK, 
            fill_opacity=0.8,
            stroke_width=3
        )
        principle_box.to_edge(LEFT).shift(RIGHT*0.5)
        self.wait(3) 
        principle_title = Text("总结", font_size=28, color=HIGHLIGHT_COLOR)
        principle_title.move_to(principle_box.get_top()).shift(DOWN*0.5)
        
        principles = VGroup(
            Text("1. 底边固定", font_size=20),
            Text("2. 顶点在上方随意滑动", font_size=20),
            Text("3. 高度固定", font_size=20),
            Text("4. 面积 = ½ × 底边 × 高", font_size=20),
            Text("5. 面积保持不变", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        principles.move_to(principle_box)
        
        self.play(
            FadeIn(principle_box, scale=0.9),
            run_time=1.2
        )
        self.play(
            Write(principle_title),
            run_time=0.8
        )
        for item in principles:
            self.play(
                FadeIn(item, shift=RIGHT*0.3),
                run_time=0.7
            )
            self.wait(1)
        
        # ========== 7. 最终强调 ==========
        # final_highlight = VGroup(
        #     SurroundingRectangle(base_line, color=RED, buff=0.15),
        #     SurroundingRectangle(height_line, color=YELLOW, buff=0.15),
        #     triangle.copy().set_stroke(width=6)
        # )
        
        # self.play(
        #     Create(final_highlight),  # 这里替换了原来的ShowCreation
        #     principles[-1].animate.scale(1.2).set_color(GOLD),
        #     run_time=2
        # )
        # self.wait(2)
        
        # 结束动画
        # self.play(
        #     FadeOut(final_highlight),
        #     principles[-1].animate.scale(1/1.2),
        #     run_time=1
        # )
        self.wait(2)