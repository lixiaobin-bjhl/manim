from manim import *
import numpy as np

class TriangleHeights(Scene):
    def construct(self):
        # 标题
        title = Text("三角形的高线演示", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 创建三个三角形
        triangles = VGroup(
            self.create_acute_triangle().shift(LEFT*3.5),
            self.create_right_triangle(),
            self.create_obtuse_triangle().shift(RIGHT*3.5),
        )
        labels = VGroup(
            Text("锐角三角形", font_size=26).next_to(triangles[0], DOWN, buff=0.5),
            Text("直角三角形", font_size=26).next_to(triangles[1], DOWN, buff=0.5),
            Text("钝角三角形", font_size=26).next_to(triangles[2], DOWN, buff=0.5),
        )
        self.play(
            LaggedStart(
                Create(triangles[0]), Write(labels[0]),
                Create(triangles[1]), Write(labels[1]),
                Create(triangles[2]), Write(labels[2]),
                lag_ratio=0.3
            )
        )
        self.wait(3)

        # 分别展示高线
        self.show_heights(triangles[0], "acute")
        self.wait(3)
        self.show_heights(triangles[1], "right")
        self.wait(3)
        self.show_heights(triangles[2], "obtuse")
        self.wait(3)

    def create_acute_triangle(self):
        pts = [LEFT*2 + DOWN, RIGHT*2 + DOWN, UP*1.5]
        return Polygon(*pts, color=BLUE)

    def create_right_triangle(self):
        pts = [LEFT + DOWN, RIGHT + DOWN, LEFT + UP]
        return Polygon(*pts, color=GREEN)

    def create_obtuse_triangle(self):
        A = LEFT*2 + DOWN*1.5
        B = RIGHT*1.5 + DOWN*1.5
        C = DOWN*0.5   # ∠ACB > 90°
        return Polygon(A, B, C, color=RED)

    def show_heights(self, triangle: Polygon, ttype: str):
        A, B, C = triangle.get_vertices()
        centroid = (A + B + C) / 3

        # 顶点标签
        labs = VGroup(
            Text("A", font_size=24).next_to(A, DL if ttype=="obtuse" else DOWN, buff=0.1),
            Text("B", font_size=24).next_to(B, DR if ttype=="obtuse" else DOWN, buff=0.1),
            Text("C", font_size=24).next_to(C, UP, buff=0.1),
        )
        self.play(FadeIn(labs))
        self.wait(3)
        colors = [YELLOW, PURPLE, ORANGE]

        def make_internal_right_angle(P, X, Y, foot, color):
            # 选出通向三角形内部的点 S
            v_in = centroid - foot
            S = X if np.dot(X - foot, v_in) > np.dot(Y - foot, v_in) else Y
            # 方向向量
            d1 = P - foot
            d2 = S - foot
            # 单位化
            if np.linalg.norm(d1) < 1e-6 or np.linalg.norm(d2) < 1e-6:
                return None
            u1 = d1 / np.linalg.norm(d1)
            u2 = d2 / np.linalg.norm(d2)
            # 构造短线段
            eps = 0.3
            l1 = Line(foot, foot + u1 * eps)
            l2 = Line(foot, foot + u2 * eps)
            # 画小方块
            return RightAngle(l1, l2, length=0.2, color=color)

        if ttype == "acute":
            for i, (P, (X, Y)) in enumerate([(A, (B, C)), (B, (A, C)), (C, (A, B))]):
                foot = self.get_foot(P, X, Y)
                h = DashedLine(P, foot, color=colors[i])
                ang = make_internal_right_angle(P, X, Y, foot, colors[i])
                self.play(Create(h), Create(ang))
                self.wait(3)
            note = Text("所有高都在三角形内部", font_size=24, color=WHITE)\
                   .next_to(triangle, UP, buff=0.5)
            self.play(Write(note))
            self.wait(1)

        elif ttype == "right":
            # AB 和 AC 本身就是高
            h1 = Line(A, B, color=colors[0])
            h2 = Line(A, C, color=colors[1])
            r1 = RightAngle(h1, h2, length=0.3, color=colors[0])
            r2 = RightAngle(h2, h1, length=0.3, color=colors[1])
            # 从 A 到 BC 的高
            footA = self.get_foot(A, B, C)
            h3 = DashedLine(A, footA, color=colors[2])
            ang3 = make_internal_right_angle(A, B, C, footA, colors[2])
            self.play(Create(h1), Create(r1),
                      Create(h2), Create(r2),
                      Create(h3), Create(ang3))
            self.wait(3)
            note = Text("直角边即为高", font_size=24, color=WHITE)\
                   .next_to(triangle, UP, buff=0.5)
            self.play(Write(note))
            self.wait(3)

        else:  # obtuse
            # C 点的高（内部）
            footC = self.get_foot(C, A, B)
            hC = DashedLine(C, footC, color=colors[2])
            aC = make_internal_right_angle(C, A, B, footC, colors[2])
            self.play(Create(hC), Create(aC))
            self.wait(3)
            # A 点的高（外部）
            footA = self.get_foot(A, B, C)
            footA_ext = self.get_foot(A, B, C, extend=True)
            hA = DashedLine(A, footA_ext, color=colors[0])
            extA = DashedLine(footA, footA_ext, color=colors[0],
                              stroke_opacity=0.6, dash_length=0.08)
            aA = make_internal_right_angle(A, B, C, footA_ext, colors[0])
            self.play(Create(hA), Create(extA), Create(aA))
            self.wait(3)
            # B 点的高（外部）
            footB = self.get_foot(B, A, C)
            footB_ext = self.get_foot(B, A, C, extend=True)
            hB = DashedLine(B, footB_ext, color=colors[1])
            extB = DashedLine(footB, footB_ext, color=colors[1],
                              stroke_opacity=0.6, dash_length=0.08)
            aB = make_internal_right_angle(B, A, C, footB_ext, colors[1])
            self.play(Create(hB), Create(extB), Create(aB))
            self.wait(3)
            note = Text("两条高在三角形外部", font_size=24, color=WHITE)\
                   .next_to(triangle, UP, buff=0.8)
            self.play(Write(note))
            self.wait(3)

    def get_foot(self, point, A, B, extend=False):
        """计算点到直线 AB 的垂足"""
        v = B - A
        t = np.dot(point - A, v) / np.dot(v, v)
        if not extend:
            t = max(0, min(1, t))
        return A + t * v