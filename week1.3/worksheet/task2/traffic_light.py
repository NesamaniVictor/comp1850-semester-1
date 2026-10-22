"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Nesamani Victor
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 } #dictionary

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
state = "red"

print(f"Time {systime:03} State {state}")

for systime in range(1, maxtime + 1):
    cycle_time = systime % 15

    if cycle_time < states["red"]:
        state = "red"
    elif cycle_time < states["red"] + states["red_amber"]:
        state = "red_amber"
    elif cycle_time < states["red"] + states["red_amber"] + states["green"]:
        state = "green"
    else:
        state = "amber"

#Print the time and state using the required format
    print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14