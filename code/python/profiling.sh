#!/bin/bash
# Number of calls, time per call excluding and including subfunctions
#python -m profile type.py
python -m cProfile type.py

# Memory
# conda install -c conda-forge filprofiler
fil-profile run function.py

# Timing a statement
python -m timeit "l1=[pow(i,3) for i in range(1000)]"