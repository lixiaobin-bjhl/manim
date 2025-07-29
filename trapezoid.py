from manim import *

config.tex_template = TexTemplateLibrary.ctex

class TriangleTrapezoidAreas(Scene):
    def construct(self):
        slow_rate = 0.9
        
        # Title
        title = Text("三角形与梯形面积公式", font_size=40)
        self.play(Write(title), run_time=2*slow_rate)
        self.wait(1*slow_rate)
        self.play(title.animate.to_edge(UP))
        self.wait(1*slow_rate)
        
        # Triangle section
        tri_title = Text("三角形", font_size=30).next_to(title, DOWN)
        self.play(Write(tri_title), run_time=1.5*slow_rate)
        self.wait(0.5*slow_rate)
        
        # Create triangle
        triangle = Polygon([-3, -1, 0], [3, -1, 0], [0, 2, 0], color=BLUE)
        base_line = Line(triangle.get_vertices()[0], triangle.get_vertices()[1], color=YELLOW)
        self.play(Create(triangle), run_time=2*slow_rate)
        self.wait(1*slow_rate)
        
        # Show base
        base_label = MathTex("a", color=YELLOW).next_to(base_line, DOWN)
        self.play(Create(base_line), Write(base_label), run_time=1.5*slow_rate)
        self.wait(1*slow_rate)
        
        # Draw height
        height_line = DashedLine([0, -1, 0], [0, 2, 0], color=RED)
        height_label = MathTex("h", color=RED).next_to(height_line, LEFT)
        self.play(Create(height_line), Write(height_label), run_time=2*slow_rate)
        self.wait(1.5*slow_rate)
        
        # Show area formula
        area_formula = MathTex(
            r"\text{S三角形面积} = \frac{1}{2} \times a \times h", 
            color=GREEN
        ).next_to(triangle, DOWN, buff=0.8)
        self.play(Write(area_formula), run_time=3*slow_rate)
        self.wait(3*slow_rate)
        
        # Clear triangle section
        self.play(
            FadeOut(triangle),
            FadeOut(base_line),
            FadeOut(base_label),
            FadeOut(height_line),
            FadeOut(height_label),
            FadeOut(area_formula),
            run_time=1.5*slow_rate
        )
        
        # Trapezoid section
        trap_title = Text("梯形", font_size=30).next_to(title, DOWN)
        self.play(Transform(tri_title, trap_title), run_time=1.5*slow_rate)
        self.wait(0.5*slow_rate)
        
        # Create trapezoid
        trapezoid = Polygon([-3, -1, 0], [2, -1, 0], [1, 2, 0], [-2, 2, 0], color=BLUE)
        base1 = Line(trapezoid.get_vertices()[0], trapezoid.get_vertices()[1], color=YELLOW)
        base2 = Line(trapezoid.get_vertices()[3], trapezoid.get_vertices()[2], color=YELLOW)
        self.play(Create(trapezoid), run_time=2*slow_rate)
        self.wait(1*slow_rate)
        
        # Show bases
        base1_label = MathTex("b", color=YELLOW).next_to(base1, DOWN)
        base2_label = MathTex("a", color=YELLOW).next_to(base2, UP, buff=0.2)
        self.play(
            Create(base1),
            Create(base2),
            Write(base1_label),
            Write(base2_label),
            run_time=2*slow_rate
        )
        self.wait(1.5*slow_rate)
        
        # Draw height
        trap_height = DashedLine([-0.5, -1, 0], [-0.5, 2, 0], color=RED)
        height_label = MathTex("h", color=RED).next_to(trap_height, LEFT)
        self.play(
            Create(trap_height),
            Write(height_label),
            run_time=2*slow_rate
        )
        self.wait(1.5*slow_rate)
        trap_area = MathTex(r"\text{S梯形面积} = \frac{1}{2} \times (a + b) \times h", color=GREEN)
        trap_area.next_to(trapezoid, DOWN, buff=1)
        self.play(Write(trap_area), run_time=3*slow_rate)
        self.wait(4*slow_rate)
        
        # Final clean up
        self.play(
            FadeOut(trapezoid),
            FadeOut(base1),
            FadeOut(base2),
            FadeOut(base1_label),
            FadeOut(base2_label),
            FadeOut(trap_height),
            FadeOut(height_label),
            FadeOut(trap_area),
            FadeOut(trap_title),
            FadeOut(title),
            run_time=2*slow_rate
        )
