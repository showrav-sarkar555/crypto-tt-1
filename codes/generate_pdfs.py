from fpdf import FPDF
import os

output_dir = r"c:\Users\USER\Desktop\vs cod\m"

codes = {}

codes["Exp1_Bisection_Method"] = {
    "title": "Experiment 1: Bisection Method",
    "subtitle": "Study of Bisection Method for finding solutions to equations with a single unknown variable",
    "code": r"""clc;
clear all;

fx = input('Enter the function f(x): ', 's');
f = eval(['@(x)', fx]);

a = input('Enter a = ');
b = input('Enter b = ');

if f(a)*f(b) > 0
    disp('Invalid interval. Root does not lie between a and b.');
    return;
end

for k = 1:100
    x = (a + b) / 2;
    fx_val = f(x);

    if k > 1
        error = abs((x - x_prev) / x) * 100;
    else
        error = 100;
    end

    if fx_val == 0 || error <= 0.01
        break;
    end

    if f(a) * fx_val < 0
        b = x;
    else
        a = x;
    end
    x_prev = x;
end

fprintf('The root is %f\n', x);"""
}

codes["Exp2_False_Position_Method"] = {
    "title": "Experiment 2: Method of False Position (Regula Falsi)",
    "subtitle": "Study of Method of False Position for finding solutions to equations with a single unknown variable",
    "code": r"""clc;
clear;

eqn = input('Enter the function f(x): ','s');
f = @(x) eval(eqn);

a = input('Enter value of a: ');
b = input('Enter value of b: ');

if f(a)*f(b) > 0
    disp('Invalid interval. Root does not lie between a and b.');
    return;
end

tol = 1e-4;
max_iter = 100;

for i = 1:max_iter
    xs = (a*f(b) - b*f(a)) / (f(b) - f(a));

    if abs(f(xs)) < tol
        break;
    end

    if f(a)*f(xs) < 0
        b = xs;
    else
        a = xs;
    end
end

fprintf('Approximate root = %.6f\n', xs);"""
}

codes["Exp3_Secant_Method"] = {
    "title": "Experiment 3: Secant Method",
    "subtitle": "Study of Secant Method for finding solutions to equations with a single unknown variable",
    "code": r"""clc;
clear all;

fx = input('Enter the function f(x): ', 's');
f = str2func(['@(x)', fx]);

x0 = input('Enter first guess x0 = ');
x1 = input('Enter second guess x1 = ');

k = 1;

while true
    x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0));

    if abs(f(x2)) < 1e-6
        break;
    end

    x0 = x1;
    x1 = x2;
    k = k + 1;
end

fprintf('The root is %f\n', x2);"""
}

codes["Exp4_Newton_Raphson_Method"] = {
    "title": "Experiment 4: Newton-Raphson Method",
    "subtitle": "Study of Newton-Raphson Method for finding solutions to equations with a single unknown variable",
    "code": r"""clc;
clear all;

fx = input('Enter the function f(x): ', 's');
f = str2func(['@(x)', fx]);

dfx = input('Enter the derivative f''(x): ', 's');
df = str2func(['@(x)', dfx]);

x0 = input('Enter initial guess x0 = ');

while true
    x1 = x0 - f(x0)/df(x0);

    if abs(f(x1)) < 1e-6
        break;
    end

    x0 = x1;
end

fprintf('The root is %f\n', x1);"""
}

codes["Exp5_Trapezoidal_Rule"] = {
    "title": "Experiment 5: Trapezoidal Rule",
    "subtitle": "Study of Trapezoidal Rule for Numerical Integration",
    "code": r"""clc;
clear all;

fx = input('Enter the function f(x): ', 's');
f = str2func(['@(x)', fx]);

a = input('Enter lower limit a = ');
b = input('Enter upper limit b = ');
n = input('Enter number of subintervals n = ');

h = (b - a) / n;

sum = f(a) + f(b);

for i = 1:n-1
    x = a + i*h;
    sum = sum + 2*f(x);
end

I = (h/2) * sum;

fprintf('The approximate value of the integral is: %f\n', I);"""
}

codes["Exp6_Simpsons_One_Third_Rule"] = {
    "title": "Experiment 6: Simpson's 1/3 Rule",
    "subtitle": "Study of Simpson's 1/3 Rule for Numerical Integration",
    "code": r"""clc;
clear all;

fx = input('Enter the function f(x): ', 's');
f = str2func(['@(x)', fx]);

a = input('Enter lower limit a = ');
b = input('Enter upper limit b = ');
n = input('Enter number of subintervals n (even) = ');

if mod(n,2) ~= 0
    disp('n must be an even number for Simpson''s 1/3 Rule.');
    return;
end

h = (b - a) / n;
sum = f(a) + f(b);

for i = 1:n-1
    x = a + i*h;
    if mod(i,2) == 0
        sum = sum + 2*f(x);
    else
        sum = sum + 4*f(x);
    end
end

I = (h/3) * sum;

fprintf('The approximate value of the integral is: %f\n', I);"""
}

codes["Exp7_Simpsons_Three_Eighth_Rule"] = {
    "title": "Experiment 7: Simpson's 3/8 Rule",
    "subtitle": "Study of Simpson's 3/8 Rule for Numerical Integration",
    "code": r"""clc;
clear all;

fx = input('Enter the function f(x): ', 's');
f = str2func(['@(x)', fx]);

a = input('Enter lower limit a = ');
b = input('Enter upper limit b = ');
n = input('Enter number of subintervals n (multiple of 3) = ');

if mod(n,3) ~= 0
    disp('Number of subintervals must be a multiple of 3.');
    return;
end

h = (b - a) / n;

sum = f(a) + f(b);
for i = 1:n-1
    x = a + i*h;
    if mod(i,3) == 0
        sum = sum + 2*f(x);
    else
        sum = sum + 3*f(x);
    end
end

I = (3*h/8) * sum;

fprintf('The approximate value of the integral is: %f\n', I);"""
}

codes["Exp8_Newton_Forward_Interpolation"] = {
    "title": "Experiment 8: Newton's Forward Interpolation",
    "subtitle": "Study of Newton's Forward Interpolation Formula",
    "code": r"""clc;
clear all;

n = input('Enter number of data points: ');

x = zeros(1, n);
y = zeros(1, n);

fprintf('Enter the data points:\n');
for i = 1:n
    x(i) = input(['x(' num2str(i) ') = ']);
    y(i) = input(['y(' num2str(i) ') = ']);
end

xp = input('Enter the value of x to interpolate: ');

h = x(2) - x(1);

% Build forward difference table
d = zeros(n, n);
d(:,1) = y';

for j = 2:n
    for i = 1:n-j+1
        d(i,j) = d(i+1,j-1) - d(i,j-1);
    end
end

% Apply Newton's Forward formula
u = (xp - x(1)) / h;
result = d(1,1);
u_term = 1;

for j = 2:n
    u_term = u_term * (u - (j-2)) / (j-1);
    result = result + u_term * d(1,j);
end

fprintf('The interpolated value at x = %.4f is: %.6f\n', xp, result);"""
}

codes["Exp9_Newton_Backward_Interpolation"] = {
    "title": "Experiment 9: Newton's Backward Interpolation",
    "subtitle": "Study of Newton's Backward Interpolation Formula",
    "code": r"""clc;
clear all;

n = input('Enter number of data points: ');

x = zeros(1, n);
y = zeros(1, n);

fprintf('Enter the data points:\n');
for i = 1:n
    x(i) = input(['x(' num2str(i) ') = ']);
    y(i) = input(['y(' num2str(i) ') = ']);
end

xp = input('Enter the value of x to interpolate: ');

h = x(2) - x(1);

% Build backward difference table
d = zeros(n, n);
d(:,1) = y';

for j = 2:n
    for i = n:-1:j
        d(i,j) = d(i,j-1) - d(i-1,j-1);
    end
end

% Apply Newton's Backward formula
u = (xp - x(n)) / h;
result = d(n,1);
u_term = 1;

for j = 2:n
    u_term = u_term * (u + (j-2)) / (j-1);
    result = result + u_term * d(n,j);
end

fprintf('The interpolated value at x = %.4f is: %.6f\n', xp, result);"""
}

codes["Exp10_Lagrange_Interpolation"] = {
    "title": "Experiment 10: Lagrange Interpolation",
    "subtitle": "Study of Lagrange Interpolation Formula",
    "code": r"""clc;
clear all;

n = input('Enter number of data points: ');

x = zeros(1, n);
y = zeros(1, n);

fprintf('Enter the data points:\n');
for i = 1:n
    x(i) = input(['x(' num2str(i) ') = ']);
    y(i) = input(['y(' num2str(i) ') = ']);
end

xp = input('Enter the value of x to interpolate: ');

% Apply Lagrange Interpolation formula
result = 0;

for i = 1:n
    L = 1;
    for j = 1:n
        if j ~= i
            L = L * (xp - x(j)) / (x(i) - x(j));
        end
    end
    result = result + L * y(i);
end

fprintf('The interpolated value at x = %.4f is: %.6f\n', xp, result);"""
}


for name, data in codes.items():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 12, data["title"], ln=True, align="C")
    pdf.ln(3)

    # Subtitle
    pdf.set_font("Helvetica", "I", 11)
    pdf.multi_cell(0, 7, data["subtitle"], align="C")
    pdf.ln(5)

    # Separator line
    pdf.set_draw_color(0, 0, 0)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # Program heading
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(0, 10, "Program:", ln=True)
    pdf.ln(2)

    # Code block with background
    pdf.set_fill_color(245, 245, 245)
    pdf.set_font("Courier", "", 10)

    for line in data["code"].strip().split("\n"):
        pdf.cell(0, 5.5, "  " + line, ln=True, fill=True)

    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    filepath = os.path.join(output_dir, f"{name}.pdf")
    pdf.output(filepath)
    print(f"Created: {filepath}")

print("\nAll 10 PDFs generated successfully!")
