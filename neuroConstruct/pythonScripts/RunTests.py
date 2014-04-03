#
#
#   File to test current configuration of GranuleCell project.
#
#   To execute this type of file, type '..\..\..\nC.bat -python XXX.py' (Windows)
#   or '../../../nC.sh -python XXX.py' (Linux/Mac). Note: you may have to update the
#   NC_HOME and NC_MAX_MEMORY variables in nC.bat/nC.sh
#
#   Author: Padraig Gleeson
#
#   This file has been developed as part of the neuroConstruct project
#   This work has been funded by the Medical Research Council and the
#   Wellcome Trust
#
#

import sys
import os

try:
    from java.io import File
except ImportError:
    print "Note: this file should be run using ..\\..\\..\\nC.bat -python XXX.py' or '../../../nC.sh -python XXX.py'"
    print "See http://www.neuroconstruct.org/docs/python.html for more details"
    quit()

sys.path.append(os.environ["NC_HOME"]+"/pythonNeuroML/nCUtils")

import ncutils as nc # Many useful functions such as SimManager.runMultipleSims found here

projFile = File(os.getcwd(), "../Mitral_Cell_Simple_Gap_Network.ncx")


##############  Main settings  ##################

simConfigs = []

#simConfigs.append("Default Simulation Configuration")
simConfigs.append("TestSimConfig")

simDt =                 0.001
simDtOverride =         {"LEMS":0.00025}

#simulators =            ["NEURON", "GENESIS_PHYS", "GENESIS_SI", "MOOSE_PHYS", "MOOSE_SI", "LEMS"]
simulators =            ["NEURON", "GENESIS_PHYS", "GENESIS_SI", "MOOSE_PHYS", "MOOSE_SI"]

varTimestepNeuron =     True
varTimestepTolerance =  0.00001

plotSims =              True
plotVoltageOnly =       True
runInBackground =       True
analyseSims =           True
verbose =               False
numConcurrentSims =     3

#############################################


def testAll(argv=None):
    if argv is None:
        argv = sys.argv

    print "Loading a project from "+ projFile.getCanonicalPath()

    simManager = nc.SimulationManager(projFile,
                                      verbose = verbose,
                                      numConcurrentSims = numConcurrentSims)

    simManager.runMultipleSims(simConfigs =           simConfigs,
                               simDt =                simDt,
                               simDtOverride =        simDtOverride,
                               simulators =           simulators,
                               runInBackground =      runInBackground,
                               varTimestepNeuron =    varTimestepNeuron,
                               varTimestepTolerance = varTimestepTolerance)

    simManager.reloadSims(plotVoltageOnly =   plotVoltageOnly,
                          plotSims =          plotSims,
                          analyseSims =       analyseSims)

    # These were discovered using analyseSims = True above.
    # They need to hold for all simulators
    spikeTimesToCheck = {'CellGroup_Test_0': [107.0, 123.3, 139.7, 156.0, 172.2, 188.4]}

    #spikeTimeAccuracy = 1.1 # Too long!! Lems's fault...
    spikeTimeAccuracy = 0.1 

    report = simManager.checkSims(spikeTimesToCheck = spikeTimesToCheck,
                                  spikeTimeAccuracy = spikeTimeAccuracy)

    print report

    return report


if __name__ == "__main__":
    testAll()


