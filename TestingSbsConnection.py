import Algorithms.RBA as algoOne
import Algorithms.GCBA as algoTwo
import Algorithms.GBA as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------------------------

# (1) No. of Connections Sbs vs No. of Succesfull Mapings 
intervalFactor = -1

def testSuccMappings(algoType,  connectivitySbs = tn.sbsDegree, intervalFactor = tn.intervalFactor, iterations = tn.iterCount):

    connectivity = tn.sbsDegree

    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity=tn.vnfDegree, random_range=0)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity, random_range=tn.randUpBoundSbs)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)

        xOne.append(connectivity)
        yOne.append(numMappings)

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+= intervalFactor

    returnData = [xOne, yOne]
    return returnData;


# (2) No. of Connections Sbs vs No. of UnSuccesfull Mapings 

def testUnsuccMappings(algoType, connectivitySbs = tn.sbsDegree, intervalFactor = tn.intervalFactor, iterations = tn.iterCount):

    connectivity = tn.sbsDegree

    xOne = []
    yOne = []
    
    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity = tn.vnfDegree, random_range=0)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity, random_range=tn.randUpBoundSbs)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)

        xOne.append(connectivity)
        yOne.append(tn.numVnfFunctions - numMappings)

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+=intervalFactor
    
    returnData = [xOne, yOne]
    return returnData;

# (3) No. of Connections Sbs vs Amount of Sbs. Resouces Unused.

def testAvailRes(algoType,  connectivitySbs = tn.sbsDegree, intervalFactor = tn.intervalFactor, iterations = tn.iterCount):

    connectivity = tn.sbsDegree

    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity = tn.vnfDegree, random_range=0)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity, random_range=tn.randUpBoundSbs)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)

        avRes = tn.sbsAvailableRes(totalNetwork)
        xOne.append(connectivity)
        yOne.append(avRes)

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        connectivity+= intervalFactor

    returnData = [xOne, yOne]
    return returnData;
        

# (4) No. of Connections Sbs vs Amount of Sbs. Resouces Exhausted

def testExhaustRes(algoType,  connectivitySbs = tn.sbsDegree, intervalFactor = tn.intervalFactor, iterations = tn.iterCount):

    connectivity = tn.sbsDegree

    xOne = []
    yOne = []

    ranSlices = tn.createRANSlice(tn.numRnSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, connectivity =tn.vnfDegree, random_range=0)

    for ctrVar in range(iterations):
        
        # One
        
        substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, connectivity, random_range=tn.randUpBoundSbs)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork)
        else:
            numMappings = tn.algoFourTest(totalNetwork)

        avRes = tn.sbsAvailableRes(totalNetwork)
        xOne.append(connectivity)
        yOne.append(tn.numSubsNodes*tn.resCtPerSbs - avRes)

        substrateNetwork.clear()
        totalNetwork.clear()
        tn.resCapList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
    
        connectivity+= intervalFactor
    
    returnData = [xOne, yOne]
    return returnData;
    