import pyomo.environ as pyo
# Create a model
model = pyo.ConcreteModel()

# Define decision variables
model.price = pyo.Var(domain=pyo.NonNegativeReals)
model.quantity = pyo.Var(domain=pyo.NonNegativeIntegers)

# Define objective function
model.profit = pyo.Objective(expr = (model.price - 10) * model.quantity, sense=pyo.maximize)

# Define constraints
model.constraints = pyo.ConstraintList()
model.constraints.add(model.quantity <= 100)
model.constraints.add(model.quantity >= 0)

# Solve the model
solver = pyo.SolverFactory('glpk')
results = solver.solve(model)

# Get the results
price = model.price()
quantity = model.quantity()
profit = model.profit()