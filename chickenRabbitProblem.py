from manim import *
from manim import TexTemplateLibrary

config.tex_template = TexTemplateLibrary.ctex

class ChickenRabbitProblem(Scene):
    def construct(self):
        # 参数
        heads = 10
        chicken_legs = 2
        rabbit_legs = 4
        total_legs_target = 28
        delta_per = rabbit_legs - chicken_legs  # 换一只鸡为兔，脚数增加 =2

        # STEP 1：题目展示（顶部）
        title = Text("鸡兔同笼", font_size=60, color=BLUE).to_edge(UP, buff=0.5)
        problem = Text("问题：头共 10 只，脚共 28 只，问鸡兔各几只？",
                       font_size=42, color=BLUE).next_to(title, DOWN, buff=0.3)
        self.play(Write(title), Write(problem))
        self.wait(6)


         # STEP 3：详细计算初始脚数（左下角）
        # 先展示"假设全是鸡"
        assumption = Text("假设全是鸡：", font_size=36).to_corner(DL, buff=0.2).shift(UP*3.6)
        self.play(Write(assumption))
        self.wait(2)

        # STEP 2：摆出 10 只"鸡"（中间偏上）
        animals = VGroup(*[
            SVGMobject("chicken.svg").scale(0.3).set_color(YELLOW)
            for _ in range(heads)
        ])
        animals.arrange(RIGHT, buff=0.5).shift(UP * 0.8)
        self.play(FadeIn(animals, lag_ratio=0.1))
        self.wait(2)

       
        
        # 展示10只鸡
        count_text = MathTex("10", "\\text{只鸡}", font_size=38)
        count_text.next_to(assumption, RIGHT)
        self.play(Write(count_text))
        self.wait(2)
        
        # 展示每只鸡2只脚
        per_chicken = MathTex("\\text{每只鸡}", "2", "\\text{只脚}", font_size=38)
        per_chicken.next_to(count_text, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(per_chicken))
        self.wait(2)
        
        # 展示乘法计算过程
        calc_process = MathTex("10", "\\times", "2", "=", "20", font_size=38)
        calc_process.next_to(per_chicken, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(calc_process))
        self.wait(1)
        
        # 用箭头连接鸡和计算
        arrow = Arrow(animals.get_bottom(), calc_process[0].get_top(), buff=0.1, color=YELLOW)
        self.play(Create(arrow))
        self.wait(1)
        
        # 初始脚数结果
        initial_legs = heads * chicken_legs  # 20
        leg_text = Text(f"总脚数：{initial_legs}", font_size=38)
        leg_text.next_to(calc_process, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(leg_text))
        self.wait(1)
        
        # 计算差值
        diff_initial = total_legs_target - initial_legs  # 8
        diff_text = Text(f"还差：28 - 20 = {diff_initial}只脚", font_size=38, color=RED)
        diff_text.next_to(leg_text, DOWN, aligned_edge=LEFT, buff=0.3)
        self.play(Write(diff_text))
        self.wait(9)

        # STEP 4：小学算术"工式"展示（右下角）
        # step1 = MathTex(f"{total_legs_target}", "-", f"{initial_legs}", "=", f"{diff_initial}",
        #                 font_size=38)
        # step1.to_corner(DR, buff=0.5).shift(UP*2)
        # self.play(Write(step1))
        # self.wait(1)
        
        # 展示每换一只增加的脚数
        delta_text = MathTex("\\text{一只兔少算了2只脚， 共差8只脚}",
                           font_size=36)
        delta_text.to_corner(DR, buff=0.5).shift(UP*3)
        self.play(Write(delta_text))
        self.wait(4)
        
        step2 = MathTex(
            r"\text{兔子: }\frac{" + f"{diff_initial}" + "}{" + f"{delta_per}" + "}",
            "=",
            f"{diff_initial//delta_per}",
            font_size=38
        )
        step2.next_to(delta_text, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(Write(step2))
        self.wait(2)
        step3 = MathTex(r"\text{鸡: 10 - 4 = 6}", font_size=38);
        step3.next_to(step2, DOWN, aligned_edge=RIGHT, buff=0.3);
        self.play(Write(step3))
        self.wait(3)

        # 计算出要换的数量
        replacements = diff_initial // delta_per  # 4
         
        # 解释替换数量
        replace_text = MathTex(r"\text{需要将}", f"{replacements}", r"\text{只鸡换成兔}",
                              font_size=38)
        replace_text.next_to(step3, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(Write(replace_text))
        self.wait(2)

        # STEP 5：逐步把前 replacements 只鸡变成兔（动物行列）
        num_rabbit = ValueTracker(0)
        
        # 更新脚数显示
        def update_leg_diff():
            current = (heads - num_rabbit.get_value())*chicken_legs + num_rabbit.get_value()*rabbit_legs
            new_text = Text(f"当前总脚数：{int(current)}", font_size=38)
            new_text.move_to(leg_text)
            return new_text
        
        def update_diff_text():
            current = (heads - num_rabbit.get_value())*chicken_legs + num_rabbit.get_value()*rabbit_legs
            diff = total_legs_target - current
            new_text = Text(f"差值：{diff} 只脚", font_size=38, 
                          color=GREEN if diff == 0 else RED)
            new_text.move_to(diff_text)
            return new_text

        for i in range(replacements):
            rabbit = SVGMobject("rabbit.svg").scale(0.3).set_color(WHITE)
            rabbit.move_to(animals[i].get_center())
            self.play(Transform(animals[i], rabbit), run_time=0.6)
            num_rabbit.increment_value(1)
            self.play(
                Transform(leg_text, update_leg_diff())
                # Transform(diff_text, update_diff_text())
            )
            self.wait(0.4)

        # STEP 6：最终脚数与差值显示"正好"
        self.wait(0.5)
        self.play(FadeOut(diff_text))

        # STEP 7：显示答案（底部居中）
        answer = Text(f"答案：鸡 {heads - replacements} 只，兔 {replacements} 只",
                      font_size=40, color=GREEN)
        answer.to_edge(DOWN, buff=0.8)
        self.play(Write(answer))
        self.play(Circumscribe(answer, color=GREEN, run_time=1))
        self.wait(1)

        # 在第四只兔子上打勾
        # check = Text("✔", font_size=72, color=GREEN)
        # check.move_to(animals[replacements - 1].get_top() + UP * 0.2)
        # self.play(FadeIn(check), run_time=0.8)
        self.wait(5)