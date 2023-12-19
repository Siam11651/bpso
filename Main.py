import pickle
import random_starter as rs
from PSOProblems import *

if __name__ == "__main__":
    # problem = CPSOProblem("lbest")
    # problem = CPSOProblem("gbest")
    # problem = CBPSOProblem("lbest")
    # problem = BPSOKnapsackProblem()
    # problem = TVBPSOKnapsackProblem()
    # problem = BPSOTSPProblem()

    # problem.plotResults()
    file = open("dataset", mode="rb")
    data = pickle.loads(file.read())

    file.close()
    rs.random_starter.start(len(data[1]))

    print("time invariant:")
    BPSOKnapsackProblem(data)
    print()
    print("time variant:")
    TVBPSOKnapsackProblem(data)