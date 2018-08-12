from . import DefaultParameters as dp

def Solve(antCls, numIterations = dp.numIterations, numAnts = dp.numAnts, **kwargs):
    try:
        globalBest = None
        for k in range(numIterations):
            ants = [antCls(**kwargs) for _ in range(numAnts)]
            ants[0].makeLeader()

            for ant in ants:
                ants[0].sharePheromoneStructure(ant)
                ant.constructSolution()
                ant.localSearch()

            iterBest = min(ants, key = lambda a: a.getSolutionValue())
            if globalBest==None or iterBest.getSolutionValue() < globalBest.getSolutionValue():
                globalBest = iterBest 
            print(iterBest.getSolutionValue(), globalBest.getSolutionValue())

            for ant in set(ants + [iterBest, globalBest]):
                ant.setIterBest(iterBest)
                ant.setGlobalBest(globalBest)
                ant.updatePheromones()

        return globalBest.getSolutionValue(), list(globalBest.getSolutionComponents())
    except TypeError as err:
        print('Error: some parameters are not supported by the selected algorithm type')
