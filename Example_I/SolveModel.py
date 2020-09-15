#! /usr/bin/env python

from gurobipy import *

if (len(sys.argv) != 2):
    print("Usage: gurobi.sh SolveModel.py model.lp")
    exit()

modelFile = sys.argv[1]


# The number of threads, 48 or 1
Threads = 48

print("Test Using %i threads ...\n\n\n" %Threads)

m = read(modelFile)

m.setParam("LogToConsole", 0)
m.setParam("LogFile", "Log%i_cores.log" %Threads)

# Set the number of threads
m.setParam("Threads", Threads)

# Set LazyConstraints = 1
m.setParam("LazyConstraints", 1)

m.optimize()

if m.Status == 2:
    print("\n\n\nFind Solution\n\n\n")
    m.write('solution_%i_cores.sol' %Threads)
elif m.Status == 3:
    print("\n\n\nthe model is infeasible\n\n\n")
else:
    print("Unkown Error")


##########################################

# The number of threads, 48 or 1
Threads = 1

print("Test Using %i threads ...\n\n\n" %Threads)

m = read(modelFile)

m.setParam("LogToConsole", 0)
m.setParam("LogFile", "Log%i_cores.log" %Threads)

# Set the number of threads
m.setParam("Threads", Threads)

# Set LazyConstraints = 1
m.setParam("LazyConstraints", 1)

m.optimize()

if m.Status == 2:
    print("\n\n\nFind Solution\n\n\n")
    m.write('solution_%i_cores.sol' %Threads)
elif m.Status == 3:
    print("\n\n\nthe model is infeasible\n\n\n")
else:
    print("Unkown Error")