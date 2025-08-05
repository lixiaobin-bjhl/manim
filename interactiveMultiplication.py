from manim import *
config.tex_template = TexTemplateLibrary.ctex

class MultiplicationProperties(Scene):
    def construct(self):
        # Parameters
        a, b, c = 2, 3, 4
        cell_size = 0.6
        DEFAULT_FONT_SIZE = 48
        MathTex.set_default(font_size=DEFAULT_FONT_SIZE)
        Tex.set_default(font_size=DEFAULT_FONT_SIZE)
        # Colors
        color_a = BLUE
        color_b = GREEN
        color_c = YELLOW
        
        # Part 1: Commutative Property (a×b = b×a)
        # ========================================
        title_comm = Tex("乘法交换律: $a \\times b = b \\times a$").to_edge(UP)
        self.play(Write(title_comm))
        self.wait(2)
        
        # Create initial rectangle (a×b)
        rect_ab = Rectangle(
            width=b*cell_size,
            height=a*cell_size,
            fill_color=color_a,
            fill_opacity=0.7,
            stroke_color=WHITE
        )
        grid_ab = rect_ab.copy().set_fill(opacity=0).set_stroke(width=0.5, opacity=0.7)
        
        # Create rotated rectangle (b×a)
        rect_ba = Rectangle(
            width=a*cell_size,
            height=b*cell_size,
            fill_color=color_b,
            fill_opacity=0.7,
            stroke_color=WHITE
        ).shift(DOWN*0.5)
        grid_ba = rect_ba.copy().set_fill(opacity=0).set_stroke(width=0.5, opacity=0.7)
        
        # Labels
        label_a = MathTex("a").set_color(color_a)
        label_b = MathTex("b").set_color(color_b)
        
        # Animation for commutative property
        self.play(Create(rect_ab), Create(grid_ab))
        
        # Add dimension labels
        brace_a = Brace(rect_ab, LEFT)
        label_a1 = label_a.copy().next_to(brace_a, LEFT)
        brace_b = Brace(rect_ab, DOWN)
        label_b1 = label_b.copy().next_to(brace_b, DOWN)
        
        self.play(
            GrowFromCenter(brace_a),
            Write(label_a1),
            GrowFromCenter(brace_b),
            Write(label_b1)
        )
        
        # Area label
        area_ab = MathTex("a \\times b").next_to(rect_ab, UP)
        self.play(Write(area_ab))
        self.wait(2)
        
        # Transform to b×a
        self.play(
            Transform(rect_ab, rect_ba),
            Transform(grid_ab, grid_ba),
            Transform(brace_a, Brace(rect_ba, LEFT)),
            Transform(brace_b, Brace(rect_ba, DOWN)),
            label_a1.animate.next_to(Brace(rect_ba, LEFT), LEFT),
            label_b1.animate.next_to(Brace(rect_ba, DOWN), DOWN),
            Transform(area_ab, MathTex("b \\times a").next_to(rect_ba, UP)),
            run_time=2
        )
        self.wait(2)
        
        # Show equation
        eq_comm = MathTex("a \\times b = b \\times a").scale(1.3)
        eq_comm.next_to(rect_ba, DOWN, buff=1)
        self.play(Write(eq_comm))
        self.wait(2)
        
        # Clear for next part
        self.play(
            FadeOut(rect_ab), FadeOut(grid_ab),
            FadeOut(brace_a), FadeOut(brace_b),
            FadeOut(label_a1), FadeOut(label_b1),
            FadeOut(area_ab), FadeOut(eq_comm),
            FadeOut(title_comm)
        )
        
        # Part 2: Distributive Property (a×(b+c) = a×b + a×c)
        # ====================================================
        title_dist = Tex("乘法分配律: $a \\times (b + c) = a \\times b + a \\times c$").to_edge(UP)
        self.play(Write(title_dist))
        self.wait(2)
        
        # Create rectangles
        rect_b = Rectangle(
            width=b*cell_size,
            height=a*cell_size,
            fill_color=color_b,
            fill_opacity=0.7,
            stroke_color=WHITE
        )
        rect_c = Rectangle(
            width=c*cell_size,
            height=a*cell_size,
            fill_color=color_c,
            fill_opacity=0.7,
            stroke_color=WHITE
        )
        
        # Position side by side
        rect_b.move_to(LEFT*(c*cell_size)/2)
        rect_c.move_to(RIGHT*(b*cell_size)/2)
        combined = VGroup(rect_b, rect_c)
        
        # Create the large rectangle
        rect_large = Rectangle(
            width=(b+c)*cell_size,
            height=a*cell_size,
            fill_color=color_a,
            fill_opacity=0.5,
            stroke_color=WHITE
        )
        
        # Grids
        grid_b = rect_b.copy().set_fill(opacity=0).set_stroke(width=0.5, opacity=0.7)
        grid_c = rect_c.copy().set_fill(opacity=0).set_stroke(width=0.5, opacity=0.7)
        grid_large = rect_large.copy().set_fill(opacity=0).set_stroke(width=0.5, opacity=0.7)
        
        # Labels
        label_a2 = label_a.copy()
        label_b2 = label_b.copy()
        label_c = MathTex("c").set_color(color_c)
        
        # Animation for distributive property
        self.play(Create(rect_large), Create(grid_large))
        
        # Add dimension labels
        brace_a_large = Brace(rect_large, LEFT)
        label_a_large = label_a2.next_to(brace_a_large, LEFT)
        brace_bc = Brace(rect_large, DOWN)
        label_bc = MathTex("b + c").next_to(brace_bc, DOWN)
        
        self.play(
            GrowFromCenter(brace_a_large),
            Write(label_a_large),
            GrowFromCenter(brace_bc),
            Write(label_bc)
        )
        
        # Area label
        area_large = MathTex("a \\times (b + c)").next_to(rect_large, UP)
        self.play(Write(area_large))
        self.wait(3)
        
        # Split into two rectangles
        self.play(
            Transform(rect_large, combined),
            Transform(grid_large, VGroup(grid_b, grid_c)),
            FadeOut(brace_bc), FadeOut(label_bc),
            run_time=2
        )
        
        # Add individual braces
        brace_b = Brace(rect_b, DOWN)
        label_b_down = label_b2.next_to(brace_b, DOWN)
        brace_c = Brace(rect_c, DOWN)
        label_c_down = label_c.next_to(brace_c, DOWN)
        
        self.play(
            GrowFromCenter(brace_b), Write(label_b_down),
            GrowFromCenter(brace_c), Write(label_c_down)
        )
        
        # Individual area labels
        area_b = MathTex("a \\times b").move_to(rect_b)
        area_c = MathTex("a \\times c").move_to(rect_c)
        
        self.play(
            Transform(area_large, VGroup(area_b, area_c))
        )
        self.wait(2)
        
        # Show equation
        eq_dist = MathTex("a \\times (b + c)", "=", "a \\times b", "+", "a \\times c").scale(1.3)
        eq_dist.next_to(combined, DOWN, buff=1.2)
        self.play(Write(eq_dist))
        self.wait(2)
        
        # Highlight parts
        box_left = SurroundingRectangle(eq_dist[0], color=color_a)
        box_right = SurroundingRectangle(VGroup(eq_dist[2], eq_dist[4]), color=WHITE)
        
        self.play(Create(box_left))
        self.wait(2)
        self.play(Transform(box_left, box_right))
        self.wait(2)
        
        # Final clean up
        # self.play(*[FadeOut(mob) for mob in self.mobjects])
        # self.wait(1)