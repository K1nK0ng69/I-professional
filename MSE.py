from sympy import symbols, Function, integrate, solve, Eq

# Define variables
X = symbols('X')
w1, w2 = symbols('w1 w2')
Y = X**3  # Target variable
Y1 = X  # Feature 1
Y2 = X**2 - X  # Feature 2
Y_hat = w1*Y1 + w2*Y2  # Linear model

# MSE expression
MSE = (Y - Y_hat)**2

# Expectation over X in range [0, 1]
MSE_expectation = integrate(MSE, (X, 0, 1))

# Partial derivatives for w1 and w2
dMSE_dw1 = MSE_expectation.diff(w1)
dMSE_dw2 = MSE_expectation.diff(w2)

# Solve the system of equations to find optimal w1 and w2
optimal_params = solve((Eq(dMSE_dw1, 0), Eq(dMSE_dw2, 0)), (w1, w2))

# Substitute optimal parameters back into the MSE to find the minimum MSE
min_MSE = MSE_expectation.subs(optimal_params)
print(optimal_params, min_MSE.simplify())
