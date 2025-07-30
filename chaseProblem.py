from manim import *

config.tex_template = TexTemplateLibrary.ctex
class ChaseProblem(Scene):
    def construct(self):
        # 1）物理参数
        initial_distance = 16   # 初始距离：小红到小明之间的距离 (m)
        v_a = 1                 # 小明速度 (m/s)
        v_b = 3                 # 小红速度 (m/s)
        catch_time = initial_distance / (v_b - v_a)  # 追上时间 (s)：16/(3-1)=8s
        distance_a = v_a * catch_time  # 小明行走距离：1*8=8 m
        distance_b = v_b * catch_time  # 小红行走距离：3*8=24 m

        # 2）视觉缩放：1 米 = scale_factor 个 manim 单位
        scale_factor = 0.3
        init_vis = initial_distance * scale_factor  # 16*0.3=4.8
        a_vis = distance_a * scale_factor          # 8*0.3=2.4
        b_vis = distance_b * scale_factor          # 24*0.3=7.2

        # 较短的路：两边各留 0.5 单位空白
        margin = 0.5
        road_len = init_vis + b_vis + 2 * margin   # ≈4.8+7.2+1=13

        # 3）标题与公式
        title = Text("追及问题", font_size=48, color=BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, buff=0.5))
        self.wait(2)

        formula = MathTex(
            r"\text{追上时间}=\frac{\text{路程差}}{\text{速度差}}",
            font_size=36
        )
        self.play(Write(formula))
        self.wait(1)
        self.play(formula.animate.next_to(title, DOWN, buff=0.8))
        self.wait(1)

        # 4）画路
        left_end = LEFT * (road_len / 2)
        right_end = RIGHT * (road_len / 2)
        road = Line(left_end, right_end, color=GRAY).shift(DOWN * 1.5)
        self.play(Create(road))
        self.wait(1)

        # 5）放置小红（追赶者）与小明（被追者）
        start_point = left_end + DOWN * 1.5
        person_b = SVGMobject("person.svg").scale(0.5).set_color(PINK)\
                     .move_to(start_point)                              # 小红起点
        person_a = SVGMobject("person.svg").scale(0.5).set_color(BLUE)\
                     .move_to(start_point + RIGHT * init_vis)            # 小明起点
        self.play(FadeIn(person_a), FadeIn(person_b))
        self.wait(1)

        name_a = Text("小明", color=BLUE, font_size=24).next_to(person_a, DOWN, buff=0.2)
        name_b = Text("小红", color=PINK, font_size=24).next_to(person_b, DOWN, buff=0.2)
        self.play(Write(name_a), Write(name_b))
        self.wait(2)

        # 6）初始距离标注
        init_line = Line(person_b.get_bottom(), person_a.get_bottom(), color=YELLOW)
        init_label = MathTex(r"16\,\text{m}", color=YELLOW, font_size=24)\
                         .next_to(init_line, UP, buff=0.2)
        self.play(Create(init_line), Write(init_label))
        self.wait(2)

        # 7）速度标注
        speed_a = MathTex(r"1\,\text{m/s}", color=RED, font_size=30)\
                    .next_to(person_a, UP, buff=0.3)
        speed_b = MathTex(r"3\text{m/s}", color=GREEN, font_size=30)\
                    .next_to(person_b, UP, buff=0.3)
        self.play(Write(speed_a), Write(speed_b))
        self.wait(3)

        # 8）时间计算展示
        time_calc = MathTex(r"\frac{16\,\text{m}}{3,\text{m/s}-1\,\text{m/s}}=8\,\text{秒}", font_size=32)\
                        .next_to(formula, DOWN, buff=0.6)
        self.play(Write(time_calc))
        self.wait(2)

        # 移除初始距离标注
        self.play(FadeOut(init_line), FadeOut(init_label))
        self.wait(0.5)

        # 9）追及动画：小明走 2.4 单位（8m），小红走 7.2 单位（24m）
        shift_a = RIGHT * a_vis
        shift_b = RIGHT * b_vis
        self.play(
            person_a.animate.shift(shift_a),
            person_b.animate.shift(shift_b),
            run_time=catch_time,
            rate_func=linear
        )
        self.wait(2)  # 停下不再移动

        # 10）标注相遇点
        meet_pt = Dot(color=YELLOW).move_to(person_a.get_center())
        meet_txt = Text("追上点", color=YELLOW, font_size=24)\
                   .next_to(meet_pt, UP, buff=0.5)
        self.play(FadeIn(meet_pt), Write(meet_txt))
        self.wait(1)

        # 11）在路上标示实际行走距离
        dist_label_a = MathTex(r"\text{小明走了1m/s × 8s = 8m}", 
                      color=WHITE, font_size=28)\
              .next_to(road.get_start(), DOWN, buff=1.4)\
              .shift(RIGHT * a_vis)
        dist_label_b = MathTex(r"\text{小红走了3m/s × 8s = 24m}", 
                      color=WHITE, font_size=28)\
              .next_to(road.get_start(), DOWN, buff=2)\
              .shift(RIGHT * a_vis)
        self.play(Write(dist_label_a), Write(dist_label_b))
        self.wait(6)
