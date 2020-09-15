#! /usr/bin/env python

from gurobipy import *

if (len(sys.argv) != 3):
    print("Usage: gurobi.sh SolveModel.py model.lp model_reordered.lp")
    exit()

modelFile = sys.argv[1]
modelReorderedFile = sys.argv[2]


# The number of threads, 80
Threads = 80

print("Test Using %i threads ...\n\n\n" %Threads)

m = read(modelFile)

m.setParam("LogToConsole", 0)
m.setParam("LogFile", "Log%i_cores.log" %Threads)

# Set the number of threads
m.setParam("Threads", Threads)

m.optimize()

if m.Status == 2:
    print("\n\n\nFind Solution\n\n\n")
    m.write('solution_%i_cores.sol' %Threads)
elif m.Status == 3:
    print("\n\n\nthe model is infeasible\n\n\n")
else:
    print("Unkown Error")


##########################################

# The number of threads, 80
Threads = 80

print("Test Using %i threads ...\n\n\n" %Threads)

m = read(modelReorderedFile)

m.setParam("LogToConsole", 0)
m.setParam("LogFile", "reoredered_Log%i_cores.log" %Threads)

# Set the number of threads
m.setParam("Threads", Threads)


m.optimize()

if m.Status == 2:
    print("\n\n\nFind Solution\n\n\n")
    m.write('reoredered_solution_%i_cores.sol' %Threads)
elif m.Status == 3:
    print("\n\n\nthe model is infeasible\n\n\n")
else:
    print("Unkown Error")