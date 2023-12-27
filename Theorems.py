import sympy as sp
import math
def result_of_integral(a, b, f):
    x = sp.symbols('x')
    function = sp.sympify(f)
    definite_integral = sp.integrate(function, (x, a, b))
    print(f"The definite integral of the function from {a} to {b} is: {definite_integral}")
    return definite_integral

def get_user_function():
    user_input = input("Enter the function in terms of 'x': ")
    try:
        function = sp.sympify(user_input)
    except sp.SympifyError:
        print("Please enter a valid symbolic expression.")
        return get_user_function()
    return function

def calculate_expression(a, b, n, x_val, f):
    result_list = []
    x = sp.symbols('x')

    for k in range(0, n):
        term1 = (1 / math.factorial(k + 1)) * ((b - a) / 6) ** (k + 1) * (f.subs(x, a).diff(x, k).doit() + (-1) ** k * f.subs(x, b).diff(x, k).doit())
        term2 = (-1) ** k / math.factorial(k + 1) * ((x-(a + 5 * b) / 6 ) ** (k + 1) - (x-((5 * a + b) / 6) ) ** (k + 1)) * f.diff(x, k)

        result_list.append(term1 + term2.subs(x, x_val).evalf())

    return result_list

f = get_user_function()
a_val = float(input("Enter the lower limit 'a': "))
b_val = float(input("Enter the upper limit 'b': "))
n_val = int(input("Enter the value for 'n': "))

x_values = [(a_val + b_val) / 2, (a_val + b_val) / 2, a_val + b_val / 2]  # Farklı x değerleri

definite_integral = result_of_integral(a_val, b_val, f)

for i, x_val in enumerate(x_values, start=1):
    results = calculate_expression(a_val, b_val, n_val, x_val, f)
    final_result = sum(results)
    error = (definite_integral - final_result)
    print(f"Error between definite integral and iteration Q{i}:", error)

