from manim import *

config.tex_template = TexTemplateLibrary.ctex

class TriangleHeightFormula(Scene):
    def construct(self):
        # 创建三角形
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 2, 0], color=BLUE)
        triangle.scale(0.8).shift(LEFT * 3 + UP * 0.5)

        # 标注底和高
        base_label = MathTex(r"\text{底}").next_to(triangle, DOWN).shift(RIGHT * 1.5)
        height_label = MathTex(r"\text{高}").next_to(triangle.get_top(), UP)

        base_line = Underline(base_label, color=WHITE)
        height_line = DashedLine(triangle.get_top(), [0, -1, 0] + triangle.get_top() * 0)

        # 公式：面积 = (底 × 高) / 2
        formula_area = MathTex(r"\text{面积} = \frac{\text{底} \times \text{高}}{2}")
        formula_area.shift(RIGHT * 2 + UP * 1.5).scale(1.2)

        # 动画开始
        self.play(Create(triangle))
        self.play(Create(base_line), Write(base_label))
        self.play(Create(height_line), Write(height_label))
        self.wait(0.5)

        self.play(Write(formula_area))
        self.wait(1)

        # 推导高公式
        formula_height = MathTex(r"\text{高} = \frac{2 \times \text{面积}}{\text{底}}")
        formula_height.shift(RIGHT * 2 + DOWN * 1).scale(1.2)

        self.play(TransformMatchingTex(formula_area.copy(), formula_height))
        self.wait(1)

        # 加强调解
        box = SurroundingRectangle(formula_height, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(2)