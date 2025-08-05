from manim import *

class ShiftExample(Scene):
    def construct(self):
        square = Square()  # 创建一个正方形
        self.play(Create(square))  # 创建动画显示正方形
        square.shift(UP + 2 * RIGHT)  # 将正方形向上和向右移动
        self.play(Create(square))  # 创建动画显示正方形
        # self.play(square.shift, UP + 2 * RIGHT)  # 将正方形向上和向右移动
        # self.wait()