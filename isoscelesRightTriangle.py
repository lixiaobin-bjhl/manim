from manim import *
import numpy as np

config.tex_template = TexTemplateLibrary.ctex

class IsoscelesRightTriangle(Scene):
    def construct(self):
        # 标题
        title = Text("等腰直角三角形性质演示", font_size=48).to_edge(UP)
        subtitle = Text("高 = 底边长度 / 2", font_size=36, color=YELLOW).next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(1)

        # 创建等腰直角三角形
        triangle, labels = self.create_triangle()
        self.play(Create(triangle), Write(labels))
        self.wait(2)

        # 显示三角形各部分名称
        self.label_triangle_parts(triangle)
        self.wait(2)

        # 演示高是底边的一半
        self.show_height_property(triangle)
        self.wait(2)

        # 数学证明
        self.show_proof(triangle)
        self.wait(3)

    def create_triangle(self):
        # 定义三角形尺寸
        self.base_len = 4  # 底边长度
        self.height_val = 2  # 高度（满足h=底边/2）
        
        # 顶点坐标
        A = LEFT*self.base_len/2 + DOWN*self.height_val/2
        B = RIGHT*self.base_len/2 + DOWN*self.height_val/2 
        C = UP*self.height_val/2  # 顶点在正上方
        
        triangle = Polygon(A, B, C, color=BLUE, fill_opacity=0.3)
        
        # 顶点标签
        labels = VGroup(
            Text("A", font_size=24).next_to(A, DL, buff=0.1),
            Text("B", font_size=24).next_to(B, DR, buff=0.1),
            Text("C", font_size=24).next_to(C, UP, buff=0.1),
        )
        
        return triangle, labels

    def label_triangle_parts(self, triangle):
        A, B, C = triangle.get_vertices()
        
        # 标记底边
        base = Line(A, B, color=RED)
        base_label = Text("底边", font_size=24, color=RED).next_to(base, DOWN, buff=0.2)
        
        # 标记两腰
        left_leg = Line(A, C, color=GREEN)
        right_leg = Line(B, C, color=GREEN)
        leg_label = Text("腰", font_size=24, color=GREEN).next_to(left_leg, LEFT, buff=0.2)
        
        # 直角标记
        right_angle = RightAngle(
            Line(A, B), Line(B, C),
            length=0.3,
            color=YELLOW
        )
        
        self.play(
            LaggedStart(
                Create(base), Write(base_label),
                Create(left_leg), Create(right_leg), Write(leg_label),
                Create(right_angle),
                lag_ratio=0.3
            ),
            run_time=2
        )
        self.wait(1)

    def show_height_property(self, triangle):
        A, B, C = triangle.get_vertices()
        
        # 绘制高（从直角顶点C到底边AB）
        foot = self.get_foot(C, A, B)
        height_line = DashedLine(C, foot, color=PURPLE, stroke_width=4)
        height_label = MathTex("h", color=PURPLE, font_size=28).next_to(height_line, RIGHT, buff=0.1)
        
        # 测量底边
        base_measure = DoubleArrow(
            A + UP*0.3, B + UP*0.3,
            buff=0,
            color=RED,
            tip_length=0.2
        )
        base_text = MathTex(f"{self.base_len:.1f}", color=RED, font_size=28)\
                   .next_to(base_measure, UP, buff=0.1)
        
        # 测量高
        height_measure = DoubleArrow(
            foot + LEFT*0.3, C + LEFT*0.3,
            buff=0,
            color=PURPLE,
            tip_length=0.2
        )
        height_text = MathTex(f"{self.height_val:.1f}", color=PURPLE, font_size=28)\
                    .next_to(height_measure, LEFT, buff=0.1)
        
        # 关系式
        relation = MathTex(
            r"h = \frac{\text{底边}}{2} = \frac{" + f"{self.base_len:.1f}" + r"}{2} = " + f"{self.height_val:.1f}",
            font_size=36,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Create(height_line), Write(height_label))
        self.wait(1)
        
        self.play(
            LaggedStart(
                Create(base_measure), Write(base_text),
                Create(height_measure), Write(height_text),
                lag_ratio=0.5
            ),
            run_time=2
        )
        self.wait(1)
        
        self.play(Write(relation))
        self.wait(2)

    def show_proof(self, triangle):
        A, B, C = triangle.get_vertices()
        
        # 证明步骤
        proof_steps = VGroup(
            Text("1. 设等腰直角三角形$ABC$，$\\angle C=90^\\circ$", font_size=28),
            Text("2. $AC=BC$，设$AC=BC=x$", font_size=28),
            Text(f"3. 底边$AB={self.base_len:.1f}$", font_size=28),
            Text("4. 根据勾股定理：$x^2 + x^2 = AB^2$", font_size=28),
            Text(f"5. $2x^2 = {self.base_len**2:.1f} \\Rightarrow x = {self.base_len/np.sqrt(2):.1f}$", font_size=28),
            Text("6. 面积计算：$\\frac{1}{2}AB \\cdot h = \\frac{1}{2}AC \\cdot BC$", font_size=28),
            Text(f"7. $\\frac{1}{2}\\cdot{self.base_len:.1f}\\cdot h = \\frac{1}{2}\\cdot{self.base_len/np.sqrt(2):.1f}^2$", font_size=28),
            Text(f"8. 解得 $h = \\frac{{AB}}{2} = {self.height_val:.1f}$", font_size=28, color=YELLOW)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(RIGHT)
        
        for step in proof_steps:
            self.play(Write(step))
            self.wait(0.5)
        
        self.wait(2)

    def get_foot(self, point, A, B):
        """计算点到直线 AB 的垂足"""
        v = B - A
        t = np.dot(point - A, v) / np.dot(v, v)
        t = max(0, min(1, t))  # 限制在线段范围内
        return A + t * v