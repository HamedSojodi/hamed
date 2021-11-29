# Student grade script using module of sys
import sys
Sum=0
for i in range(1, len(sys.argv)):
    Sum+=int(sys.argv[i])
print(Sum / len(sys.argv[1::]))
