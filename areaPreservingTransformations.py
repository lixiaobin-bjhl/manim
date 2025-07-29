from manim import *

class AreaPreservingTransformations(Scene):
    def construct(self):
        # Set animation speed
        slow_rate = 0.8
        
        # Title
        title = Text("等积变换", font_size=48, color=YELLOW)
        subtitle = Text("面积保持不变的图形变换", font_size=32, color=BLUE_B)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), run_time=2*slow_rate)
        self.play(FadeIn(subtitle), run_time=1.5*slow_rate)
        self.wait(2*slow_rate)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1*slow_rate)
        
        # Initialize shapes
        rectangle = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.5)
        parallelogram = Polygon([-2, -1, 0], [2, -1, 0], [3, 1, 0], [-1, 1, 0], 
                              color=GREEN, fill_opacity=0.5)
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [0, 3, 0], 
                         color=RED, fill_opacity=0.5)
        
        # Show initial rectangle with area
        self.play(Create(rectangle), run_time=2*slow_rate)
        area_label = MathTex("A = 8").next_to(rectangle, UP)
        self.play(Write(area_label), run_time=1.5*slow_rate)
        self.wait(2*slow_rate)
        
        # Transform rectangle to parallelogram (shear)
        self.play(
            rectangle.animate.become(parallelogram),
            area_label.animate.next_to(parallelogram, UP),
            run_time=3*slow_rate
        )
        self.play(Transform(area_label, MathTex("A = 8").next_to(parallelogram, UP)),
                 run_time=1*slow_rate)
        self.wait(2*slow_rate)
        
        # Show height change but area remains
        base_line = Line(parallelogram.get_vertices()[0], parallelogram.get_vertices()[1], color=YELLOW)
        height_line = DashedLine(
            parallelogram.get_vertices()[1], 
            [parallelogram.get_vertices()[1][0], parallelogram.get_vertices()[2][1], 0],
            color=YELLOW
        )
        base_label = Text("底边").next_to(base_line, DOWN)
        height_label = Text("高").next_to(height_line, RIGHT)
        
        self.play(
            Create(base_line),
            Create(height_line),
            Write(base_label),
            Write(height_label),
            run_time=2*slow_rate
        )
        self.wait(3*slow_rate)
        self.play(
            FadeOut(base_line),
            FadeOut(height_line),
            FadeOut(base_label),
            FadeOut(height_label),
            run_time=1*slow_rate
        )
        
        # Transform parallelogram to triangle (area-preserving)
        self.play(
            parallelogram.animate.become(triangle),
            area_label.animate.next_to(triangle, UP),
            run_time=3*slow_rate
        )
        self.play(Transform(area_label, MathTex("A = 8").next_to(triangle, UP)),
                 run_time=1*slow_rate)
        self.wait(2*slow_rate)
        
        # Show triangle dimensions
        tri_base = Line(triangle.get_vertices()[0], triangle.get_vertices()[1], color=YELLOW)
        tri_height = DashedLine(
            triangle.get_vertices()[1],
            [triangle.get_vertices()[1][0], triangle.get_vertices()[2][1], 0],
            color=YELLOW
        )
        tri_base_label = Text("底边 = 4").next_to(tri_base, DOWN)
        tri_height_label = Text("高 = 4").next_to(tri_height, RIGHT)
        
        self.play(
            Create(tri_base),
            Create(tri_height),
            Write(tri_base_label),
            Write(tri_height_label),
            run_time=2*slow_rate
        )
        self.wait(3*slow_rate)
        
        # Final transformation back to rectangle
        new_rectangle = Rectangle(width=2, height=4, color=PURPLE, fill_opacity=0.5)
        self.play(
            triangle.animate.become(new_rectangle),
            area_label.animate.next_to(new_rectangle, UP),
            run_time=3*slow_rate
        )
        self.play(Transform(area_label, MathTex("A = 8").next_to(new_rectangle, UP)),
                 run_time=1*slow_rate)
        self.wait(3*slow_rate)
        
        # Show all areas are equal
        conclusion = Text("面积在变换过程中保持不变", font_size=36, color=GREEN)
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion), run_time=2*slow_rate)
        self.wait(4*slow_rate)
        
        # Clean up
        self.play(
            FadeOut(new_rectangle),
            FadeOut(area_label),
            FadeOut(conclusion),
            FadeOut(tri_base),
            FadeOut(tri_height),
            FadeOut(tri_base_label),
            FadeOut(tri_height_label),
            run_time=2*slow_rate
        )