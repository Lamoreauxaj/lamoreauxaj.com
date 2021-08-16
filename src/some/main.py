import math
import random
from manim import *

class GPoint:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, o):
        return GPoint(self.x + o.x, self.y + o.y)

    def __truediv__(self, v):
        return GPoint(self.x / v, self.y / v)

    def __sub__(self, o):
        return GPoint(self.x - o.x, self.y - o.y)

    def norm(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

class GCircle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return "<{}, {}>".format(str(self.center), self.radius)

def dist(p, q):
    return (p - q).norm()

def in_circle(p, circle):
    if circle is None:
        return False
    return dist(p, circle.center) <= circle.radius

def from_manim_points(points):
    return [GPoint(point[0], point[1]) for point in points]

def to_manim_circle(circle):
    return Circle(arc_center=[circle.center.x, circle.center.y, 0], radius=circle.radius)

def circle(points):
    if len(points) == 1:
        return GCircle(points[0], radius=0)
    if len(points) == 2:
        center = (points[0] + points[1]) / 2
        radius = dist(points[0], points[1]) / 2
        return GCircle(center, radius)
    if len(points) == 3:
        ax, ay = points[0].x, points[0].y
        bx, by = points[1].x, points[1].y
        cx, cy = points[2].x, points[2].y
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
        uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
        center = GPoint(ux, uy)
        radius = dist(center, points[0])
        return GCircle(center, radius)
    return None

def minimum_enclosing_circle_helper(points, fixed, k):
    current_circle = circle(fixed)
    for i in range(k):
        point = points[i]
        if point in fixed:
            continue
        if not in_circle(point, current_circle):
            if len(fixed) == 3:
                return None
            current_circle = minimum_enclosing_circle_helper(points, fixed + [point], i + 1)
            if current_circle is None:
                break
    return current_circle

def minimum_enclosing_circle(points):
    return to_manim_circle(minimum_enclosing_circle_helper(from_manim_points(points), [], len(points)))

def worse_than_mec(points):
    mec = minimum_enclosing_circle_helper(from_manim_points(points), [], len(points))
    mec.radius += 3
    mec.center.x += random.random() * .5 - .25
    mec.center.y += random.random() * .5 - .25
    return to_manim_circle(mec)

EXAMPLE_POINTS = [[-3.5, 0.4, 0], [.5, 1, 0], [3, 0, 0], [2.2, 2, 0], [-1, -1.5, 0], [2.5, -1, 0], [-1.5, .5, 0]]
EXAMPLE_POINTS2 = [[.5, 1, 0], [2.2, 2, 0], [-1, -1.5, 0], [2.5, -1, 0], [-1.5, .5, 0], [1, 1, 0], [1, -.5, 0], [4, 0, 0]]
example_points_2 = [GPoint(point[0], point[1]) for point in EXAMPLE_POINTS2]

class Welcome(Scene):
    def construct(self):
        welcome_text = Tex("Welcome").scale(1.2)
        self.play(Write(welcome_text))
        self.wait(2)
        self.remove(welcome_text)
        self.wait()

        algo_text = Tex("Welzl's", " Minimum Enclosing Circle Algorithm").scale(1.2)
        algo_text.set_color_by_tex("Welzl", BLUE)
        self.play(Write(algo_text))
        self.wait(8)
        self.remove(algo_text)
        self.wait()

class Problem_statement(Scene):
    def construct(self):
        problem_name = Tex("Minimum Enclosing Circle", color=BLUE)
        problem_name.shift(UP)

        description = Tex(r"""Given $n$ points in the plane, \\
find the """, "minimum", """ radius of
a circle containing all of them.""").scale(.8)
        description.set_color_by_tex("minimum", color=YELLOW)

        self.play(Write(problem_name))
        self.wait()
        self.play(Write(description))
        self.wait(4)
        self.remove(problem_name)
        self.remove(description)
        self.wait()

class Example_points(Scene):
    def construct(self):
        points = []
        for location in EXAMPLE_POINTS:
            point = Dot(location)
            points.append(point)
        mec = minimum_enclosing_circle(EXAMPLE_POINTS)

        self.play(*[Create(point) for point in points])
        self.play(Create(mec))

class No_boundary_points(Scene):
    def construct(self):
        points = []
        for location in EXAMPLE_POINTS:
            point = Dot(location)
            points.append(point)
        circle = Circle(arc_center=[0, 0, 0], radius=6)
        radius = 0
        hit_dot = None
        hit_point = None
        i = 0
        for point in EXAMPLE_POINTS:
            next_radius = GPoint(point[0], point[1]).norm()
            if next_radius > radius:
                radius = next_radius
                hit_point = point
                hit_dot = points[i]
            i += 1
        smaller_circle = Circle(arc_center=[0, 0, 0], radius=radius)

        self.add(*points)
        self.add(circle)
        self.play(Transform(circle, smaller_circle, run_time=3))
        self.remove(hit_dot)
        self.add(Dot(hit_point, color=BLUE))
        self.wait(.1)


class One_boundary_point(Scene):
    def construct(self):
        points = [Dot(loc) for loc in EXAMPLE_POINTS]
        points[0] = Dot(EXAMPLE_POINTS[0], color=BLUE)
        fixed_point = GPoint(EXAMPLE_POINTS[0][0], EXAMPLE_POINTS[0][1])
        circle = Circle(arc_center=[0, 0, 0], radius=fixed_point.norm())
        x = -0.262307692308
        hit = 2
        smaller_circle = Circle(arc_center=[x, 0, 0], radius=3 - x)
        self.add(*points)
        self.add(circle)
        self.play(Transform(circle, smaller_circle, run_time=3))
        self.remove(points[hit])
        self.add(Dot(EXAMPLE_POINTS[hit], color=BLUE))
        self.wait(.1)


class Two_boundary_points(Scene):
    def construct(self):
        points = [Dot(loc) for loc in EXAMPLE_POINTS]
        points[0] = Dot(EXAMPLE_POINTS[0], color=BLUE)
        points[2] = Dot(EXAMPLE_POINTS[2], color=BLUE)
        x = -0.262307692308
        circle = Circle(arc_center=[x, 0, 0], radius=3 - x)
        smaller_circle = to_manim_circle(minimum_enclosing_circle_helper(from_manim_points(EXAMPLE_POINTS), from_manim_points([EXAMPLE_POINTS[0], EXAMPLE_POINTS[2]]), len(points)))
        self.add(*points)
        self.add(circle)
        self.play(Transform(circle, smaller_circle, run_time=3))
        self.wait(.1)


class Two_boundary_points_to_three(Scene):
    def construct(self):
        points = EXAMPLE_POINTS2
        dots = [Dot(point) for point in points]
        dots[2] = Dot(points[2], color=BLUE)
        dots[4] = Dot(points[4], color=BLUE)
        mec = minimum_enclosing_circle(points)
        gpoints = [GPoint(point[0], point[1]) for point in points]
        hit = [2, 4, 7]
        mid = (gpoints[2] + gpoints[4]) / 2
        theta = math.atan(.25)
        center = mid + GPoint(3.1 * math.cos(theta), 3.1 * math.sin(theta))
        center_dot = Dot([center.x, center.y, 0])
        circle = Circle(arc_center=[center.x, center.y, 0], radius=(center - gpoints[2]).norm())
        self.add(*dots)
        self.add(circle)
        self.play(Transform(circle, mec, run_time=3))
        self.remove(dots[7])
        self.add(Dot(points[7], color=BLUE))
        self.wait(.1)


class Adding_points_from_two_fixed(Scene):
    def construct(self):
        points = example_points_2
        manim_points = [Dot([point.x, point.y, 0]) for point in points]
        fixed_indices = [2, 4]
        for idx in fixed_indices:
            point = points[idx]
            manim_points[idx] = Dot([point.x, point.y, 0], color=BLUE)
        circle = minimum_enclosing_circle_helper(points, [points[2], points[4]], k=0)
        manim_circle = to_manim_circle(circle)
        for idx in fixed_indices:
            self.add(manim_points[idx])
        self.add(manim_circle)
        prev_idx = None
        for i in range(len(points)):
            if i in fixed_indices:
                continue
            point = points[i]
            if not in_circle(point, circle):
                manim_points[i].set_color(YELLOW)
                if prev_idx is not None:
                    manim_points[prev_idx].set_color(WHITE)
                prev_idx = i
                self.play(Create(manim_points[i]))
                circle = minimum_enclosing_circle_helper(points, [points[2], points[4]], k=i + 1)
                next_manim_circle = to_manim_circle(circle)
                self.play(Transform(manim_circle, next_manim_circle))
                self.add(next_manim_circle)
                self.remove(manim_circle)
                manim_circle = next_manim_circle
            else:
                self.play(Create(manim_points[i]))


class Justification(Scene):
    def construct(self):
        why = Tex("Why?").scale(1.2)
        why.set_color_by_tex("Why", color=RED)

        self.play(Write(why))
        self.wait(4)
        self.remove(why)
        self.wait()

