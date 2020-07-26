from sympy import Eq, S, sqrt
from sympy.abc import x, y, z, s, t
from sympy.sets import FiniteSet, EmptySet
from sympy.geometry import Point
from sympy.vector import ImplicitRegion
from sympy.testing.pytest import raises


def test_ImplicitRegion():
    ellipse = ImplicitRegion((x, y), (x**2/4 + y**2/16 - 1))
    assert ellipse.equation == x**2/4 + y**2/16 - 1
    assert ellipse.variables == (x, y)
    assert ellipse.degree == 2
    r = ImplicitRegion((x, y, z), Eq(x**4 + y**2 - x*y, 6))
    assert r.equation == x**4 + y**2 - x*y - 6
    assert r.variables == (x, y, z)
    assert r.degree == 4


def test_regular_point():
    r1 = ImplicitRegion((x,), x**2 - 16)
    r1.regular_point() == (-4,)
    c = ImplicitRegion((x, y), x**2 + y**2 - 4)
    c.regular_point() == (-2, 0)
    r2 = ImplicitRegion((x, y), (x - S(5)/2)**2 + y**2 - (S(1)/4)**2)
    raises(NotImplementedError, lambda: r2.regular_point())


def test_singular_points_and_multiplicty():
    r1 = ImplicitRegion((x, y, z), Eq(x + y + z, 0))
    assert r1.singular_points() == FiniteSet((-y - z, y, z))
    assert r1.multiplicity((0, 0, 0)) == 1
    assert r1.multiplicity((-y - z, y, z)) == 1
    r2 = ImplicitRegion((x, y, z), x*y*z + y**4 -x**2*z**2)
    assert r2.singular_points() == FiniteSet((0, 0, z), ((-y*sqrt(4*y**2 + 1)/2 + y/2)/z, y, z),\
                            ((y*sqrt(4*y**2 + 1)/2 + y/2)/z, y, z))
    assert r2.multiplicity((0, 0, 0)) == 3
    assert r2.multiplicity((0, 0, 6)) == 2
    r3 = ImplicitRegion((x, y, z), z**2 - x**2 - y**2)
    assert r3.singular_points() == FiniteSet((0, 0, 0))
    assert r3.multiplicity((0, 0, 0)) == 2
    r4 = ImplicitRegion((x, y), x**2 + y**2 - 2*x)
    assert r4.singular_points() == EmptySet
    assert r4.multiplicity(Point(1, 3)) == 0


def test_rational_parametrization():
    p = ImplicitRegion((x,), x - 2)
    assert p.rational_parametrization() == (x - 2,)

    line = ImplicitRegion((x, y), Eq(y, 3*x + 2))
    assert line.rational_parametrization() == (x, 3*x + 2)

    circle1 = ImplicitRegion((x, y), ((x-2)**2 + (y+3)**2 - 4))
    assert circle1.rational_parametrization(parameters=t) == (4/(t**2 + 1), 4*t/(t**2 + 1) - 3)
    circle2 = ImplicitRegion((x, y), (x - 1/2)**2 + y**2 - (1/4)**2 )
    raises(NotImplementedError, lambda: circle2.rational_parametrization())
    circle2.rational_parametrization(t, reg_point=Point(0.75, 0)) == (3/4 - 0.5/(t**2 + 1), -0.5*t/(t**2 + 1))
    circle3 = ImplicitRegion((x, y), Eq(x**2 + y**2, 2*x))
    assert circle3.rational_parametrization(parameters=(t,)) == (2/(t**2 + 1), 2*t/(t**2 + 1))

    parabola = ImplicitRegion((x, y), (y - 3)**2 - 4*(x + 6))
    assert parabola.rational_parametrization(t) == (-6 + 4/t**2, 3 + 4/t)

    rect_hyperbola = ImplicitRegion((x, y), x*y - 1)
    assert rect_hyperbola.rational_parametrization(t) == (-100 + (100*t + S(1)/100)/t, 100*t)

    cubic_curve = ImplicitRegion((x, y), x**3 + x**2 - y**2)
    assert cubic_curve.rational_parametrization(parameters=(t)) == (t**2 - 1, t*(t**2 - 1))
    cuspidal = ImplicitRegion((x, y), (x**3 - y**2))
    assert cuspidal.rational_parametrization(t) == (t**2, t**3)

    I= ImplicitRegion((x, y), x**3 + x**2 - y**2)
    assert I.rational_parametrization(t) == (t**2 - 1, t*(t**2 - 1))

    sphere = ImplicitRegion((x, y, z), Eq(x**2 + y**2 + z**2, 2*x))
    assert sphere.rational_parametrization(parameters=(s, t)) == (2/(s**2 + t**2 + 1), 2*t/(s**2 + t**2 + 1), 2*s/(s**2 + t**2 + 1))

    conic = ImplicitRegion((x, y), Eq(x**2 + 4*x*y + 3*y**2 + x - y + 10, 0))
    conic.rational_parametrization(t) == (-100 - 205/(3*(3*t**2 - sqrt(41881)*t + 4*t - 2*sqrt(41881)/3 + 1)),\
                                -205*t/(3*(3*t**2 - sqrt(41881)*t + 4*t - 2*sqrt(41881)/3 + 1)) - sqrt(41881)/6 + 401/6)

    r1 = ImplicitRegion((x, y), y**2 - x**3 + x)
    raises(NotImplementedError, lambda: r1.rational_parametrization())
    r2 = ImplicitRegion((x, y), y**2 - x**3 - x**2 + 1)
    raises(NotImplementedError, lambda: r2.rational_parametrization())
