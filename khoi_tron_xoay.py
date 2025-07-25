from manim import *

class KhoiTronXoay(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 5],
            y_range=[0, 5],
            x_length=7,
            y_length=4,
            axis_config={"include_numbers": True}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        graph = axes.plot(lambda x: x**0.5, color=YELLOW)
        graph_label = MathTex("y = f(x)").next_to(graph, UP + RIGHT)

        a = 1
        b = 4
        area = axes.get_area(graph, x_range=(a, b), color=RED_B, opacity=0.4)

        x0 = 2.5
        x0_dot = Dot(axes.c2p(x0, 0), color=ORANGE)
        x0_line = DashedLine(axes.c2p(x0, 0), axes.c2p(x0, x0**0.5), color=GREEN)
        r_label = MathTex("r = |f(x_0)|", color=GREEN).next_to(x0_line, RIGHT)

        formula1 = MathTex(
            "S(x_0) = \\pi r^2 = \\pi [f(x_0)]^2"
        ).scale(0.8).to_edge(UP)
        formula2 = MathTex(
            "V = \\pi \\int_a^b [f(x)]^2 dx"
        ).scale(0.8).next_to(formula1, DOWN)

        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.play(Create(area))
        self.play(Create(x0_line), FadeIn(x0_dot), Write(r_label))
        self.wait(1)
        self.play(Write(formula1))
        self.play(Write(formula2))
        self.wait(2)
