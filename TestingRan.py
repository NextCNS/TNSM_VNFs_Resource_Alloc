import AlgorithmOne as algoOne
import AlgorithmTwo as algoTwo
import AlgorithmThree as algoThree
from graph_tool.all import *
import random
import TotalNetwork as tn
import matplotlib.pyplot as plt

intervalFactor = 2

# (1) No. of vnf vs No. of succesfull mappings

def testSuccMappings(algoType):

    noRanSlices = tn.numRnSlices

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)

    for ctrVar in range(5):

        ranSlices = tn.createRANSlice(noRanSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
        
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        xOne.append(noRanSlices)
        yOne.append(numMappings)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noRanSlices += intervalFactor

    returnData = [xOne, yOne]

    return returnData;
    

# (2) No. of vnf vs No. of unsuccesfull mappings

def testUnsuccMappings(algoType):

    noRanSlices = tn.numRnSlices

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)

    for ctrVar in range(5):
        
        ranSlices = tn.createRANSlice(noRanSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        xOne.append(noRanSlices)
        yOne.append(tn.numVnfFunctions - numMappings)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noRanSlices += intervalFactor

    returnData = [xOne, yOne]

    return returnData;


# (3) No. of vnf vs No. of Available Substrate Resources

def testAvailRes(algoType):

    noRanSlices = tn.numRnSlices

    xOne = []
    yOne = []
    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)

    for ctrVar in range(5):
        
        ranSlices = tn.createRANSlice(noRanSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        xOne.append(noRanSlices)
        resAvail = tn.sbsAvailableRes(totalNetwork)
        yOne.append(resAvail)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noRanSlices += intervalFactor

    returnData = [xOne, yOne]

    return returnData;

# (4) No. of vnf vs Amount of Exhausted Substrate Resources

def testExhaustRes(algoType):

    noRanSlices = tn.numRnSlices

    xOne = []
    yOne = []

    substrateNetwork = tn.createSbsNetwork(tn.numSubsNodes, tn.resCapList, tn.resCtPerSbs, 2)

    for ctrVar in range(5):
        
        # One
        ranSlices = tn.createRANSlice(noRanSlices, tn.numVnfFunctions, tn.resList, tn.resCtPerVnf, 3)
        totalNetwork  = tn.createTotalNetwork(substrateNetwork, ranSlices, tn.vnfCncList, tn.vnfTotalAccList)
            
        if algoType == 1:
            numMappings = tn.algoOneTest(totalNetwork, substrateNetwork, ranSlices, tn.resList, tn.resCapList)
        elif algoType == 2:
            numMappings = tn.algoTwoTest(totalNetwork, tn.vnfCncList)
        elif algoType == 3:
            numMappings = tn.algoThreeTest(totalNetwork, tn.vnfTotalAccList)
        else:
            numMappings = tn.algoFourTest(totalNetwork, substrateNetwork, ranSlices, tn.resCapList, tn.vnfCncList)
        
        
        xOne.append(noRanSlices)
        resAvail = tn.sbsAvailableRes(totalNetwork)
        yOne.append(tn.numSubsNodes*tn.resCtPerSbs - resAvail)

        ranSlices.clear()
        totalNetwork.clear()
        tn.resList.clear()
        tn.vnfCncList.clear()
        tn.vnfTotalAccList.clear()
        
        noRanSlices += intervalFactor

    returnData = [xOne, yOne]

    return returnData;