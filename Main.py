from PSOProblems import *

if __name__ == "__main__":
    # problem = CPSOProblem("lbest")
    # problem = CPSOProblem("gbest")
    # problem = CBPSOProblem("lbest")
    # problem = BPSOKnapsackProblem()
    # problem = TVBPSOKnapsackProblem()
    # problem = BPSOTSPProblem()

    # problem.plotResults()
    print("time invariant:")
    BPSOKnapsackProblem()
    print("time variant:")
    TVBPSOKnapsackProblem()