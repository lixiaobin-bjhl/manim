from manim import *

config.tex_template = TexTemplateLibrary.ctex

class MeetProblem(Scene):
    def construct(self):
        # 参数设置
        total_distance = 20  # 总距离20米
        v_a = 2  # 小明速度 2 m/s
        v_b = 3  # 小红速度 3 m/s
        meet_time = total_distance / (v_a + v_b)  # 相遇时间4秒
        
        # 计算各自行走距离（保持8:12的比例）
        distance_a = 8  # 小明行走8米
        distance_b = 12  # 小红行走12米
        
        # 调整路线长度和初始位置（更紧凑的布局）
        road_length = 10  # 路线总长度（视觉效果）
        scale_factor = road_length / total_distance  # 缩放因子
        
        # 标题
        title = Text("相遇问题", font_size=48).set_color(BLUE)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP, buff=0.5))
        self.wait(0.5)

        # 公式部分
        formula = MathTex(r"\text{相遇时间} = \frac{\text{路程}}{\text{速度和}}", font_size=36)
        self.play(Write(formula))
        self.wait(2)
        self.play(formula.animate.next_to(title, DOWN, buff=0.8))
        self.wait(0.5)

        # 路程线（按比例缩短）
        road = Line(LEFT * (distance_b*scale_factor), 
                   RIGHT * (distance_a*scale_factor), 
                   color=GRAY).shift(DOWN * 1)
        self.play(Create(road))
        self.wait(1)

        meet_offset = (distance_b - distance_a)/total_distance * 10  # 按比例计算偏移量


        # 两个小人 - 按比例调整初始位置
        person_a = SVGMobject("person.svg").scale(0.5).set_color(RED)\
                   .move_to(LEFT * (distance_b*scale_factor) + DOWN * 1)  # 从-7.2出发
        person_b = SVGMobject("person.svg").scale(0.5).set_color(GREEN)\
                   .move_to(RIGHT * (distance_a*scale_factor) + DOWN * 1)  # 从4.8出发
        self.play(FadeIn(person_a), FadeIn(person_b))
        self.wait(1)

        # 小人名字
        name_a = Text("小明", color=RED, font_size=24).next_to(person_a, DOWN, buff=0.2)
        name_b = Text("小红", color=GREEN, font_size=24).next_to(person_b, DOWN, buff=0.2)
        self.play(Write(name_a), Write(name_b))
        self.wait(2)

        # 小人速度
        speed_a = MathTex(r"2\, \text{m/s}", color=RED, font_size=30).next_to(person_a, UP, buff=0.3)
        speed_b = MathTex(r"3\, \text{m/s}", color=GREEN, font_size=30).next_to(person_b, UP, buff=0.3)
        self.play(Write(speed_a), Write(speed_b))
        self.wait(0.5)

        # 路程标注
        distance = MathTex(r"20\, \text{m}", font_size=28).next_to(road, UP, buff=0.4)
        self.play(Write(distance))
        self.wait(1)

        # 相遇公式演示
        time_calculation = MathTex(
            r"\frac{20}{2+3} = 4\, \text{秒}",
            font_size=32
        ).next_to(formula, DOWN, buff=0.6)
        self.play(Write(time_calculation))
        self.wait(2)

        # 动画展示相遇 - 按比例移动
        self.play(
            person_a.animate.shift(RIGHT * (distance_a*scale_factor)),  # 向右移动4.8
            person_b.animate.shift(LEFT * (distance_b*scale_factor)),   # 向左移动7.2
            run_time=meet_time,
            rate_func=linear,
        )
        self.wait(1)

        # 相遇点标注（现在偏左）
        meet_point = Dot(color=YELLOW).move_to(DOWN * 1 + LEFT * meet_offset)
        meet_text = Text("相遇点", color=YELLOW, font_size=24).next_to(meet_point, DOWN, buff=1)
        self.play(FadeIn(meet_point), Write(meet_text))
        
        # 显示行走距离（按比例调整位置）
        dist_label_a = MathTex(r"8\, \text{m}", color=RED, font_size=24)\
                      .next_to(road.get_start(), DOWN, buff=0.3).shift(RIGHT*1.5)
        dist_label_b = MathTex(r"12\, \text{m}", color=GREEN, font_size=24)\
                      .next_to(road.get_end(), DOWN, buff=0.3).shift(LEFT*1.5)
        self.play(Write(dist_label_a), Write(dist_label_b))
        
        self.wait(2)
        
        # 结束动画
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)