import sympy as sp
from sympy import symbols, diff, factorial
def exact(a, b):
    x = sp.symbols('x')
    f = x ** 4 + 2 * x ** 2 + 1
    exact_result_integral = float(sp.integrate(f, (x, a, b)))
    print(f"Exact integral result of {exact_result_integral} in interval {a} to {b}")
    return exact_result_integral


exact_result_integral = exact(0, 1)

def Q_n_1(f, a, b, m, n):
    result = 0
    x = symbols('x')

    xi = [a + (i * (b - a) / m) for i in range(m + 1)]
    h = [(xi[i + 1] - xi[i]) for i in range(m)]
    xi_eta = [(xi[i] + xi[i + 1]) / 2 for i in range(m)]

    for k in range(n):
        term1 = 0
        term2 = 0

        for i in range(m):
            f_expr = f(x)

            f_xi_k = diff(f_expr, x, k).subs(x, xi[i])
            f_xi_next_k = diff(f_expr, x, k).subs(x, xi[i + 1])

            term1 += ((h[i]) / 6) ** (k + 1) * (f_xi_k + ((-1) ** k) * f_xi_next_k) / factorial(k + 1)
            term2 += ((-1) ** k) * (((xi_eta[i] - (xi[i] + 5 * xi[i + 1]) / 6) ** (k + 1)) -
                        ((xi_eta[i] - (5 * xi[i] + xi[i + 1]) / 6) ** (k + 1))) / factorial(k + 1) * f_xi_k

        result += term1 - term2

    return result

def f1(x):

    return x ** 4 + 2 * x ** 2 + 1

a = 0
b = 1


m_values_odds = list(range(1, 31, 2))  # 1'den 30'a kadar tek sayılar
n_values_odds = list(range(1, 31, 2))  # 1'den 30'a kadar tek sayılar

for m, n in zip(m_values_odds, n_values_odds):

    result_f1 = Q_n_1(f1, a, b, m, n)
    error_f_odds = abs(exact_result_integral - result_f1)

    print(f" E{m},{n}, Hata: {error_f_odds}")


m_values_evens = list(range(2, 31, 2))  # 1'den 30'a kadar tek sayılar
n_values_evens = list(range(2, 31, 2))  # 1'den 30'a kadar tek sayılar

for m, n in zip(m_values_evens, n_values_evens):

    result_f1 = Q_n_1(f1, a, b, m, n)
    error_f_evens = abs(exact_result_integral - result_f1)

    print(f" E{m},{n}, Hata: {error_f_evens}")

################################################################################################################

from sympy import symbols, diff, factorial

def Q_n_2(f, a, b, m, n):
    x = symbols('x')

    xi = [a + (i * (b - a) / m) for i in range(m + 1)]
    h = [(xi[i + 1] - xi[i]) for i in range(m)]
    xi_eta = [(xi[i] + xi[i + 1]) / 2 for i in range(m)]

    result = 0

    for k in range(n):
        term1 = 0
        term2 = 0

        for i in range(m):
            f_expr = f(x)

            f_xi_k = diff(f_expr, x, k).subs(x, xi_eta[i])
            f_xi_next_k = diff(f_expr, x, k).subs(x, xi[i]) if i != m - 1 else diff(f_expr, x, k).subs(x, xi[i + 1])

            term1 += ((h[i] / 3) ** (k + 1)) * ((1 + (-1) ** k) / factorial(k + 1)) * f_xi_k
            term2 += ((h[i] / 6) ** (k + 1)) * (1 / factorial(k + 1)) * (f_xi_k + ((-1) ** k) * f_xi_next_k)

        result += term1 + term2

    return result




def f1(x):

    return x ** 4 + 2 * x ** 2 + 1

a = 0
b = 1


m_values_odds = list(range(1, 31, 2))  # 1'den 30'a kadar tek sayılar
n_values_odds = list(range(1, 31, 2))  # 1'den 30'a kadar tek sayılar

for m, n in zip(m_values_odds, n_values_odds):

    result_f2 = Q_n_2(f1, a, b, m, n)
    error_f_odds = abs(exact_result_integral - result_f2)

    print(f" E{m},{n}, Hata: {error_f_odds}")


m_values_evens = list(range(2, 31, 2))  # 1'den 30'a kadar tek sayılar
n_values_evens = list(range(2, 31, 2))  # 1'den 30'a kadar tek sayılar

for m, n in zip(m_values_evens, n_values_evens):

    result_f2 = Q_n_2(f1, a, b, m, n)
    error_f_evens = abs(exact_result_integral - result_f2)

    print(f" E{m},{n}, Hata: {error_f_evens}")

#######################################################################################################################

from sympy import symbols, diff, factorial

def Q_n_3(f, a, b, m, n):
    x = symbols('x')

    xi = [a + (i * (b - a) / m) for i in range(m + 1)]
    h = [(xi[i + 1] - xi[i]) for i in range(m)]
    xi_eta = [(xi[i] + xi[i + 1]) / 2 for i in range(m)]

    result = 0

    for k in range(n):
        term1 = 0
        term2 = 0

        for i in range(m):
            f_expr = f(x)

            f_xi_k = diff(f_expr, x, k).subs(x, (xi[i] + 2 * xi[i + 1]) / 3)
            f_xi_next_k = diff(f_expr, x, k).subs(x, (2 * xi[i] + xi[i + 1]) / 3) if i != m - 1 else diff(f_expr, x, k).subs(x, xi[i + 1])

            term1 += (((-1) ** k) / (2 * factorial(k + 1))) * (((h[i] / 2) ** (k + 1)) + ((-1) ** k) * ((h[i] / 6) ** (k + 1))) * (f_xi_k + ((-1) ** k) * f_xi_next_k)
            term2 += ((h[i] / 6) ** (k + 1)) * (1 / factorial(k + 1)) * (f_xi_k + ((-1) ** k) * f_xi_next_k)

        result += term1 + term2

    return result

def f1(x):

    return x ** 4 + 2 * x ** 2 + 1

a = 0
b = 1


m_values_odds = list(range(1, 31, 2))  # 1'den 30'a kadar tek sayılar
n_values_odds = list(range(1, 31, 2))  # 1'den 30'a kadar tek sayılar

for m, n in zip(m_values_odds, n_values_odds):

    result_f3 = Q_n_3(f1, a, b, m, n)
    error_f_odds = abs(exact_result_integral - result_f3)

    print(f" E{m},{n}, Hata: {error_f_odds}")


m_values_evens = list(range(2, 31, 2))  # 1'den 30'a kadar tek sayılar
n_values_evens = list(range(2, 31, 2))  # 1'den 30'a kadar tek sayılar

for m, n in zip(m_values_evens, n_values_evens):

    result_f2 = Q_n_3(f1, a, b, m, n)
    error_f_evens = abs(exact_result_integral - result_f2)

    print(f" E{m},{n}, Hata: {error_f_evens}")