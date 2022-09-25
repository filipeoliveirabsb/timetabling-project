import pulp

prob = pulp.LpProblem("Employee Timetabling", pulp.LpMinimize)

# Variables to represent the number of nurses working each shift

shift1=pulp.LpVariable("Shift1",0,None,pulp.LpInteger)

shift2=pulp.LpVariable("Shift2",0,None,pulp.LpInteger)

shift3=pulp.LpVariable("Shift3",0,None,pulp.LpInteger)

shift4=pulp.LpVariable("Shift4",0,None,pulp.LpInteger)

shift5=pulp.LpVariable("Shift5",0,None,pulp.LpInteger)

shift6=pulp.LpVariable("Shift6",0,None,pulp.LpInteger)


# The objective function is added to 'prob' first

prob += shift1 + shift2 + shift3 + shift4 + shift5 + shift6, "Total Nurses"


# The six constraints to ensure there are enough nurses for each time period

prob += shift6 + shift1 >= 70, "MimimumNurses06amTo10am"

prob += shift1 + shift2 >= 170, "MimimumNurses10amTo2pm"

prob += shift2 + shift3 >= 200, "MimimumNurses02pmTo6pm"

prob += shift3 + shift4 >= 85, "MimimumNurses06pmTo10pm"

prob += shift4 + shift5 >= 25, "MimimumNurses10pmTo2am"

prob += shift5 + shift6 >= 40, "MimimumNurses02amTo06am"

# Solve the problem using PuLP's choice of Solver

prob.solve()


# The status of the solution is printed to the screen

print("Status:", pulp.LpStatus[prob.status])


# Each of the variables is printed with it's resolved optimum value

for v in prob.variables():

  print(v.name, "=", v.varValue)


# The optimized objective function value is printed to the screen

print("Total number of nurses = ", pulp.value(prob.objective))