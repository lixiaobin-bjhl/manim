from manim import *

config.tex_template = TexTemplateLibrary.ctex

class TestChinese(Scene):
    def construct(self):
        text = MathTex(r"\text{这是中文}")
        self.play(Write(text))
        self.wait()