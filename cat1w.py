#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:21:32 2024

@author: gsouza
"""

from pyomo.environ import *
from pyomo.opt import SolverFactory
model = AbstractModel()
H = 10
model.Tset = RangeSet(1,H)
model.c = Param()
model.cf = Param()
model.l = Param()
model.lf = Param()
model.tau = Param()
model.b = Param()
model.d = Param()
model.df = Param()
model.h = Param()
model.K = Param()
model.w = Param()
model.I0 = Param()
model.I0f = Param()
model.S = Var(model.Tset, domain = NonNegativeReals)
model.Sf = Var(model.Tset, domain = NonNegativeReals)
model.I = Var(model.Tset, domain = NonNegativeReals)
model.If = Var(model.Tset, domain = NonNegativeReals)
model.T = Var(model.Tset, domain = NonNegativeReals)

def obj(model):
    return sum(model.c*model.S[t] + model.h*model.I[t] + model.b*model.T[t]\
        +model.cf*model.Sf[t] + model.h*model.If[t] for t in model.Tset)
model.objfn = Objective(rule = obj, sense = minimize)

def invbalf(model, t):
    if t == 1:
        return model.If[t] - model.I0f + model.df + model.T[t] == 0
    elif t <= model.lf:
        return model.If[t] - model.If[t-1] + model.df + model.T[t] == 0
    else:
        return model.If[t] - model.If[t-1] - model.Sf[t - model.lf]\
               + model.df + model.T[t] == 0
model.ibalfcons = Constraint(model.Tset, rule = invbalf)
    
def invbali(model, t):
    if t == 1:
        return model.I[t] - model.I0 + model.d == 0
    elif t <= model.tau:
        return model.I[t] - model.I[t-1] + model.d == 0
    elif t <= model.l:
        return model.I[t] - model.I[t-1] - model.T[t-model.tau] + model.d == 0
    else: 
        return model.I[t] - model.I[t-1] - model.T[t-model.tau]\
                - model.S[t - model.l] + model.d == 0
model.ibalicons = Constraint(model.Tset, rule = invbali)

def transpcap(model, t):
    return model.w*model.T[t] <= model.K
model.transcapcons = Constraint(model.Tset, rule = transpcap)

def endinv(model):
    return model.If[H] == 0
model.endinvcons = Constraint(rule = endinv)


instance = model.create_instance("cat1w.dat")
instance.pprint()
opt = SolverFactory('glpk')
results = opt.solve(instance)
results.write()
instance.T.pprint()

    
    
    
    
    
    
    
    
    
    
    