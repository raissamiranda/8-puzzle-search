# 8 puzzle search

## Instructions for execution

To execute the program, it is necessary to unzip the TP1.zip file. Once unzipped, simply access the directory where the program is stored:

```
$   cd <destdirectory>
```

Now, it is necessary to run the problem with the information in the command line. The first parameter should be a letter representing the algorithm used, followed by the configuration of the input (the 3 lines of the 8-puzzle in sequence, using the number 0 to represent the empty space). Optionally, a last parameter (PRINT) indicating whether the steps to the solution should be printed.

Below is the acronym used for each algorithm:

* A -> A* search
* B -> Breadth-first search
* G -> Greedy best-first search
* H -> Hill Climbing
* I -> Iterative deepening search
* U -> Uniform-cost search

Here is the execution instruction:
```
$   python3 TP1.py <algorithm <initConfig> <PRINT-optional>
```

An example call for the Hill Climbing algorithm:
```
$   python3 TP1.py H 1 2 3 4 5 6 7 8 0 PRINT
```

The program will return the number of states traversed until a solution is found, if any. If the PRINT parameter is used, it will then display all these intermediate states.
