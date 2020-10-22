#!/usr/bin/env python3

# Script to generate OpenFOAM table used for varying inlet velocity

# Min and max velocity in m/s
# Speed of sound a = 310.213 m/s
minU = 0
maxU = 372.2556 # Ma = 1.2

# Number of steps to perform
nSteps = 20

# The duration of transitions between steps and steps themselves is calculated
# as a function of step velocity, such that airflow covers a certain distance
# within a step. If using CFL-regulated timesteps, this ensures the same number
# of timesteps per velocity step.
transitionLength = 7 #6
stepLength = 60 #20 # 12

# Output table
print(f"\tuniformValue table\n\t(\n\t\t(0 (0 0 -{minU}))")
curT = 0
curU = minU
for n in range(nSteps):
    curU += (maxU - minU) / (nSteps * 1.0)
    curT += transitionLength / curU
    print(f"\t\t({curT} (0 0 -{curU}))")
    curT += stepLength / curU
    print(f"\t\t({curT} (0 0 -{curU}))")

print("\t);\n\n")
print(f"Shortest transition: {transitionLength / (maxU*1.0)}")
print(f"Shortest step: {stepLength / (maxU*1.0)}")
