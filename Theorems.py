import sympy as sp
import math

def result_of_integral(a, b, f):
    x = sp.symbols('x')

    # Define the function
    function = sp.sympify(f)

    # Calculate the definite integral
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

def calculate_expression_Q_1(a, b, n, f):
    result_list = []  # Ara sonuçları saklamak için bir liste oluşturalım
    x = sp.symbols('x')  # x sembolünü tanımlayalım

    for k in range(0, n):  # Her bir x = k için işlem yapacağız
        x_val = k  # x = k değerini kullanacağız
        term1 = (1 / math.factorial(k + 1)) * ((b - a) / 6) ** (k + 1) * (f.subs(x, a).diff(x, k).doit() + (-1) ** k * f.subs(x, b).diff(x, k).doit())
        term2 = (-1) ** k / math.factorial(k + 1) * (
                    (x-(a + 5 * b) / 6 ) ** (k + 1) - (x-((5 * a + b) / 6) ) ** (k + 1)) * f.diff(x, k)

        result_list.append(term1 + term2.subs(x, x_val).evalf())  # Her iterasyonda ara sonucu listeye ekleyelim

    return result_list

f = get_user_function()
a_val = float(input("Enter the lower limit: "))
b_val = float(input("Enter the upper limit: "))
n_val = int(input("Enter the value for 'n': "))

definite_integral = result_of_integral(a_val, b_val, f)
results = calculate_expression_Q_1(a_val, b_val, n_val, sp.exp(sp.symbols('x')))
final_result = sum(results)

print(" iteration Q1:", final_result)


#######################################################################################################################
# Q2 Iteration

def result_of_integral(a, b, f):
    x = sp.symbols('x')

    # Define the function
    function = sp.sympify(f)

    # Calculate the definite integral
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

def calculate_expression_Q_1(a, b, n, f):
    result_list = []  # Ara sonuçları saklamak için bir liste oluşturalım
    x = sp.symbols('x')  # x sembolünü tanımlayalım

    for k in range(0, n):  # Her bir x = k için işlem yapacağız
        x_val = k  # x = k değerini kullanacağız
        term1 = (1 / math.factorial(k + 1)) * ((b - a) / 6) ** (k + 1) * (f.subs(x, a).diff(x, k).doit() + (-1) ** k * f.subs(x, b).diff(x, k).doit())
        term2 = (-1) ** k / math.factorial(k + 1) * (
                    (x-(a + 5 * b) / 6 ) ** (k + 1) - (x-((5 * a + b) / 6) ) ** (k + 1)) * f.diff(x, k)

        result_list.append(term1 + term2.subs(x, x_val).evalf())  # Her iterasyonda ara sonucu listeye ekleyelim

    return result_list
f = get_user_function()

a_val = float(input("Enter the lower limit: "))
b_val = float(input("Enter the upper limit: "))
n_val = int(input("Enter the value for 'n': "))

x_val = (a_val + b_val) / 2
definite_integral = result_of_integral(a_val, b_val, f)
results = calculate_expression_Q_1(a_val, b_val, n_val, sp.exp(sp.symbols('x')))

final_result = sum(results)
print("Iteration Q2:", final_result)

########################################################################################################################
# Q3 Iteration
def result_of_integral(a, b, f):
    x = sp.symbols('x')

    # Define the function
    function = sp.sympify(f)

    # Calculate the definite integral
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

def calculate_expression_Q_1(a, b, n, f):
    result_list = []  # Ara sonuçları saklamak için bir liste oluşturalım
    x = sp.symbols('x')  # x sembolünü tanımlayalım

    for k in range(0, n):  # Her bir x = k için işlem yapacağız
        x_val = k  # x = k değerini kullanacağız
        term1 = (1 / math.factorial(k + 1)) * ((b - a) / 6) ** (k + 1) * (f.subs(x, a).diff(x, k).doit() + (-1) ** k * f.subs(x, b).diff(x, k).doit())
        term2 = (-1) ** k / math.factorial(k + 1) * (
                    (x-(a + 5 * b) / 6 ) ** (k + 1) - (x-((5 * a + b) / 6) ) ** (k + 1)) * f.diff(x, k)

        result_list.append(term1 + term2.subs(x, x_val).evalf())  # Her iterasyonda ara sonucu listeye ekleyelim

    return result_list
f = get_user_function()

a_val = float(input("Enter the lower limit: "))
b_val = float(input("Enter the upper limit: "))
n_val = int(input("Enter the value for 'n': "))

x_val = (a_val + (b_val / 2))
definite_integral = result_of_integral(a_val, b_val, f)
results = calculate_expression_Q_1(a_val, b_val, n_val, sp.exp(sp.symbols('x')))

final_result = sum(results)
print("Iteration Q3:", final_result)

########################################################################################################################
# Error Calculation for Qi's

