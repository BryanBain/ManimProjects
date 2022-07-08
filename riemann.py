from manim import *
import scipy.integrate as integrate

class Riemann4(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-1,6], y_range=[-1,26,2], y_length = 7, 
                        x_length = 6
    ).add_coordinates().to_edge(LEFT)

    f = lambda x: x**2
    f_graph = plane.plot(f, x_range = [-1,5.1])

    x_min = 1
    x_max = 5
    num_rects = 4
    dx = (x_max - x_min) / num_rects

    left_rects = plane.get_riemann_rectangles(
        f_graph, 
        x_range = [x_min, x_max], 
        dx = dx, 
        input_sample_type = "left"
    )

    self.add(plane)
    self.play(Create(f_graph))
    self.wait()
    for i in range(num_rects):
      self.play(Create(left_rects[i]), run_time = 0.5)
    self.wait(2)

    self.play(Uncreate(left_rects))

    right_rects = plane.get_riemann_rectangles(
        f_graph, 
        x_range = [x_min, x_max], 
        dx = dx, 
        input_sample_type = "right",
        fill_opacity = 0.6
    )

    self.wait()
    for i in range(num_rects):
      self.play(Create(right_rects[i]), run_time = 0.5)
    self.wait(2)

    self.play(Uncreate(right_rects))

    center_rects = plane.get_riemann_rectangles(
        f_graph, 
        x_range = [x_min, x_max], 
        dx = dx, 
        input_sample_type = "center",
        fill_opacity = 0.7
    )
    
    self.wait()
    for i in range(num_rects):
      self.play(Create(center_rects[i]), run_time = 0.5)
    self.wait(2)

class Riemann8(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-1,6], y_range=[-1,26,2], y_length = 7, 
                        x_length = 6
    ).add_coordinates().to_edge(LEFT)

    f = lambda x: x**2
    f_graph = plane.plot(f, x_range = [-1,5.1])

    x_min = 1
    x_max = 5
    num_rects = 8
    dx = (x_max - x_min) / num_rects

    left_rects = plane.get_riemann_rectangles(
        f_graph, 
        x_range = [x_min, x_max], 
        dx = dx, 
        input_sample_type = "left"
    )

    self.add(plane)
    self.play(Create(f_graph))
    self.wait()
    for i in range(num_rects):
      self.play(Create(left_rects[i]), run_time = 0.5)
    self.wait(2)

    self.play(Uncreate(left_rects))

    right_rects = plane.get_riemann_rectangles(
        f_graph, 
        x_range = [x_min, x_max], 
        dx = dx, 
        input_sample_type = "right",
        fill_opacity = 0.6
    )

    self.wait()
    for i in range(num_rects):
      self.play(Create(right_rects[i]), run_time = 0.5)
    self.wait(2)

    self.play(Uncreate(right_rects))

    center_rects = plane.get_riemann_rectangles(
        f_graph, 
        x_range = [x_min, x_max], 
        dx = dx, 
        input_sample_type = "center",
        fill_opacity = 0.7
    )
    
    self.wait()
    for i in range(num_rects):
      self.play(Create(center_rects[i]), run_time = 0.5)
    self.wait(2)

class RiemannArea(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-1,6], y_range=[-1,26,2], y_length = 7, 
                        x_length = 6
    ).add_coordinates().to_edge(LEFT)

    f = lambda x: x**2
    f_graph = plane.plot(f, x_range = [-1,5.1])

    self.add(plane)
    self.wait()
    self.play(Create(f_graph), run_time=2)
    self.wait()

    x_min = 1
    x_max = 5

    dx_list = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125]

    rectangles = VGroup(
        *[plane.get_riemann_rectangles(
            graph = f_graph, 
            x_range = [x_min, x_max],
            dx = dx,
            stroke_width = 0.1,
            stroke_color = WHITE
        )
        for dx in dx_list
        ]
    )

    first_area = rectangles[0]
    self.play(Create(first_area), run_time=2)
    self.wait(0.5)
    for i in range(1,len(dx_list)):
      new_area = rectangles[i]
      self.play(Transform(first_area, new_area), run_time = 1)
      self.wait(0.5)

    area = integrate.quad(f, x_min, x_max)
    text = Tex("Area: $\int_{1}^{5}x^2$", round(area[0], 6)).to_edge(RIGHT, buff=1)

    self.play(Write(text))
    self.wait()

class RiemannLeft(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-1,6], y_range=[-1,26,2], y_length = 7, 
                        x_length = 6
    ).add_coordinates().to_edge(LEFT)

    f = lambda x: x**2
    f_graph = plane.plot(f, x_range = [-1,5.1])

    x_min = 1
    x_max = 5

    self.add(plane)
    self.play(Create(f_graph))
    self.wait()

    # self.play(Uncreate(left_rects))
    dx_list = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625]

    rectangles = VGroup(
        *[plane.get_riemann_rectangles(
            graph = f_graph, 
            x_range = [x_min, x_max],
            dx = dx,
            stroke_width = 0.2,
            stroke_color = WHITE
        )
        for dx in dx_list
        ]
    )

    first_area = rectangles[0]
    self.play(Create(first_area), run_time=2)
    self.wait(0.5)
    for i in range(1,len(dx_list)):
      new_area = rectangles[i]
      self.play(Transform(first_area, new_area), run_time = 1)
      self.wait(0.5)

    area = integrate.quad(f, x_min, x_max)
    text = Tex("Area: \n $\displaystyle \int_{1}^{5}x^2 \, \mathrm{d}x = \\frac{124}{3} $").to_edge(RIGHT, buff=1)

    self.play(Write(text))
    self.wait()

class RiemannRight(Scene):
  def construct(self):
    plane = NumberPlane(x_range=[-1,6], y_range=[-1,26,2], y_length = 7, 
                        x_length = 6
    ).add_coordinates().to_edge(LEFT)

    f = lambda x: x**2
    f_graph = plane.plot(f, x_range = [-1,5.1])

    x_min = 1
    x_max = 5

    self.add(plane)
    self.play(Create(f_graph))
    self.wait()

    # self.play(Uncreate(left_rects))
    dx_list = [1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125]

    rectangles = VGroup(
        *[plane.get_riemann_rectangles(
            graph = f_graph, 
            x_range = [x_min, x_max],
            dx = dx,
            stroke_width = 0.2,
            stroke_color = WHITE,
            input_sample_type = "right",
            fill_opacity = 0.6
        )
        for dx in dx_list
        ]
    )

    first_area = rectangles[0]
    self.play(Create(first_area), run_time=2)
    self.wait(0.5)
    for i in range(1,len(dx_list)):
      new_area = rectangles[i]
      self.play(Transform(first_area, new_area), run_time = 1)
      self.wait(0.5)

    area = integrate.quad(f, x_min, x_max)
    text = Tex("Area: \n $\displaystyle \int_{1}^{5}x^2 \, \mathrm{d}x = \\frac{124}{3} $").to_edge(RIGHT, buff=1)

    self.play(Write(text))
    self.wait()
