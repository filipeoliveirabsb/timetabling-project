"""Example of a simple employee scheduling problem."""
from ortools.sat.python import cp_model


def main():
    # Data.
    employees = 4
    num_shifts = 1
    num_days = 30
    all_employees = range(employees)
    all_shifts = range(num_shifts)
    all_days = range(num_days)

    #print(employees)
    #print(all_employees)

    # Creates the model.
    model = cp_model.CpModel()

    # Creates shift variables.
    # shifts[(n, d, s)]: employee 'n' works shift 's' on day 'd'.
    shifts = {}
    for n in all_employees:
        for d in all_days:
            for s in all_shifts:
                shifts[(n, d,
                        s)] = model.NewBoolVar('shift_n%id%is%i' % (n, d, s))

    # Each shift is assigned to exactly one employee in the schedule period.
    for d in all_days:
        for s in all_shifts:
            model.AddAtMostOne(shifts[(n, d, s)] for n in all_employees)
            #model.AddExactlyOne(shifts[(n, d, s)] for n in all_employees)

    # Each employee works at most one shift per day.
    for n in all_employees:
        for d in all_days:
            model.AddAtMostOne(shifts[(n, d, s)] for s in all_shifts)

    # Try to distribute the shifts evenly, so that each employee works
    # min_shifts_per_employee shifts. If this is not possible, because the total
    # number of shifts is not divisible by the number of employees, some employees will
    # be assigned one more shift.
    min_shifts_per_employee = (num_shifts * num_days) // employees
    if num_shifts * num_days % employees == 0:
        max_shifts_per_employee = min_shifts_per_employee
    else:
        max_shifts_per_employee = min_shifts_per_employee + 1
    for n in all_employees:
        num_shifts_worked = []
        for d in all_days:
            for s in all_shifts:
                num_shifts_worked.append(shifts[(n, d, s)])
        model.Add(min_shifts_per_employee <= sum(num_shifts_worked))
        model.Add(sum(num_shifts_worked) <= max_shifts_per_employee)

    # Creates the solver and solve.
    solver = cp_model.CpSolver()
    solver.parameters.linearization_level = 0
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True


    class employeesPartialSolutionPrinter(cp_model.CpSolverSolutionCallback):
        """Print intermediate solutions."""

        def __init__(self, shifts, employees, num_days, num_shifts, limit):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self._shifts = shifts
            self._employees = employees
            self._num_days = num_days
            self._num_shifts = num_shifts
            self._solution_count = 0
            self._solution_limit = limit

        def on_solution_callback(self):
            self._solution_count += 1
            print('Solution %i' % self._solution_count)
            for d in range(self._num_days):
                print('Day %i' % d)
                for n in range(self._employees):
                    is_working = False
                    for s in range(self._num_shifts):
                        if self.Value(self._shifts[(n, d, s)]):
                            is_working = True
                            print('  employee %i works shift %i' % (n, s))
                    if not is_working:
                        print('  employee {} does not work'.format(n))
            if self._solution_count >= self._solution_limit:
                print('Stop search after %i solutions' % self._solution_limit)
                self.StopSearch()

        def solution_count(self):
            return self._solution_count

    # Display the first five solutions.
    solution_limit = 18
    solution_printer = employeesPartialSolutionPrinter(shifts, employees,
                                                    num_days, num_shifts,
                                                    solution_limit)

    solver.Solve(model, solution_printer)

    # Statistics.
    print('\nStatistics')
    print('  - conflicts      : %i' % solver.NumConflicts())
    print('  - branches       : %i' % solver.NumBranches())
    print('  - wall time      : %f s' % solver.WallTime())
    print('  - solutions found: %i' % solution_printer.solution_count())


if __name__ == '__main__':
    main()