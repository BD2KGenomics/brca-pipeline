import pulp as pp
import numpy as np

def main():
    vector_solver()



def vector_solver():
    d = pp.LpVariable.dicts("x", range(2), 0, 1)
    prob = pp.LpProblem("myV", pp.LpMinimize)
    prob += d[0] + d[1] == 1
    print pp.LpStatus[prob.solve()]
    print pp.value(d[0])
    print pp.value(d[1])

def basic_pulp_solver():
    x = pp.LpVariable("x", 0, 3)
    y = pp.LpVariable("y", 0, 1)
    prob = pp.LpProblem("myP", pp.LpMinimize)
    prob += x + y <= 2
    prob += -4*x + y
    status = prob.solve()
    print pp.LpStatus[status]
    print pp.value(x), pp.value(y)



if __name__ == '__main__':
    main()