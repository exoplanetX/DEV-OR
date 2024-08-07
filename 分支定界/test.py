from gurobipy import *
import numpy as np
import copy
import matplotlib.pyplot as plt
RLP = Model('relaxed MIP')
x={}
for i in range(2):
    x[i] = RLP.addVar(lb=0,ub=GRB.INFINITY,vtype=GRB.CONTINUOUS, name='x_'+str(i))
RLP.setObjective(100*x[0]+150*x[1],GRB.MAXIMIZE)
RLP.addConstr(2*x[0]+x[1]<=10,name='c_1')
RLP.addConstr(3*x[0]+6*x[1]<=40,name='c_2')
RLP.optimize()

Queue=[]
