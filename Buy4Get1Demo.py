from manim import *

config.tex_template = TexTemplateLibrary.ctex

class Buy4Get1Demo(Scene):
    def construct(self):
        # 标题
        title = Text("买4送1优惠计算", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # 问题描述
        problem = VGroup(
            Text("问题：", font_size=36),
            Text("商品买4个送1个", font_size=36),
            Text("如果要买22个，实际需要支付多少个的钱？", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN, buff=1)
        
        self.play(LaggedStart(*[Write(t) for t in problem], lag_ratio=0.5))
        self.wait(2)
        
        # 计算过程
        calculation = VGroup(
            Tex(r"1. \text{每组优惠数量：}4\text{（买）} + 1\text{（送）} = 5\text{个}", font_size=36),
            Tex(r"2. \text{计算完整组数：}\frac{22}{5} = 4\text{组} \text{余}2\text{个}", font_size=36),
            Tex(r"3. \text{实际支付数量：}4\times4 + 2 = 18\text{个}", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(problem, DOWN, buff=1)
        
        # 可视化分组
        dots = VGroup(*[Dot(color=BLUE) for _ in range(22)]).arrange_in_grid(rows=2, cols=11, buff=0.5)
        dots.next_to(calculation, DOWN, buff=1)
        
        # 绘制分组框
        groups = VGroup()
        for i in range(4):
            group = SurroundingRectangle(dots[i*5:i*5+5], color=GREEN, buff=0.2)
            groups.add(group)
        
        remaining = SurroundingRectangle(dots[20:22], color=RED, buff=0.2)
        
        # 逐步显示计算过程
        self.play(FadeIn(dots))
        self.wait(1)
        
        # 第一步：解释每组5个
        self.play(Write(calculation[0]))
        self.wait(1)
        
        # 第二步：显示4个完整组
        self.play(
            LaggedStart(*[Create(g) for g in groups], lag_ratio=0.3),
            run_time=3
        )
        self.wait(1)
        
        # 显示余数
        self.play(Write(calculation[1]))
        self.play(Create(remaining))
        self.wait(1)
        
        # 第三步：计算实际支付
        self.play(Write(calculation[2]))
        
        # 高亮需要支付的部分
        pay_dots = VGroup(*dots[:16], *dots[20:22])  # 4组×4个 + 余数2个
        self.play(
            pay_dots.animate.set_color(YELLOW),
            run_time=2
        )
        
        # 最终答案
        answer = Tex(r"\text{答案：需要支付}18\text{个的钱}", font_size=42, color=YELLOW)
        answer.next_to(calculation, DOWN, buff=1)
        self.play(Write(answer))
        self.wait(3)
        
        # 总结
        summary = VGroup(
            Text("总结：", font_size=36),
            Tex(r"\text{实际支付数量} = \left\lfloor\frac{\text{总数量}}{5}\right\rfloor \times 4 + \text{余数}", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(answer, DOWN, buff=1)
        
        self.play(Write(summary))
        self.wait(4)