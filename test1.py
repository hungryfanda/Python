# code
import sys, platform
import time

l=list(range(100000001))
t=tuple(range(100000001))

start = (time.time_ns()/(10^9))
for i in range(len(t)):
    a = t[i]
end = (time.time_ns()/(10^9))
print("Total lookup time for Tuple: ", end - start)

start = (time.time_ns()/(10^9))
for i in range(len(l)):
    a = l[i]
end = (time.time_ns()/(10^9))
print("Total lookup time for LIST: ", end - start)