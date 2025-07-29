from manim import *

class ObtuseTriangle(Scene):
    def construct(self):
        # 定义三个顶点
        A = np.array([0, 0, 0])
        B = np.array([3, 0, 0])
        C = np.array([1, 1, 0])

        # 绘制三角形
        triangle = Polygon(A, B, C, color=BLUE)
        self.play(Create(triangle))

        # 绘制顶点并标记
        dots = VGroup(Dot(A), Dot(B), Dot(C))
        labels = VGroup(
            Tex("A").next_to(A, DOWN + LEFT),
            Tex("B").next_to(B, DOWN + RIGHT),
            Tex("C").next_to(C, UP)
        )
        self.play(FadeIn(dots), Write(labels))

        # 在顶点 C 处标出钝角
        angle_C = Angle(
            Line(C, A),
            Line(C, B),
            radius=0.5,
            color=YELLOW
        )
        angle_label = MathTex(r"\theta > 90^\circ").next_to(angle_C, UR)
        self.play(Create(angle_C), Write(angle_label))

        self.wait(2)