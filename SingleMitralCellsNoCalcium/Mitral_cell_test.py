#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Mitral_cell_test.py - test of the Mitralcell model

    Basic Python script to load a cell model NDF file, provide current
    injection to the Apical Tuft, and run the simulation, writing the soma Vm to
    a specified file.
"""
import pdb   # the Python debugger
import os
import sys

# This sets an environment to find the libraries needed for running SSPy
# It will likely not be required in later versions of G-3

sys.path.append( os.path.join(os.environ['HOME'],
    'neurospaces_project/sspy/source/snapshots/0/tests/python'))

# The location of model files to be loaded
os.environ['NEUROSPACES_NMC_MODELS']= '/home/Simon/OlfactoryBulbMitralCell/SingleMitralCellsNoCalcium'

# The following four commands set up SSPy as the scheduler component

#from test_library import add_sspy_path
#add_sspy_path()
from sspy import SSPy 
scheduler = SSPy(verbose=True)


# Create a model container service and load an ndf file
my_model_container = scheduler.CreateService(name="My Model Container",
    type="model_container", verbose=True)

# The commands above are common to most G-3 Python simulation scripts

# load a particular NDF cell model file
my_model_container.Load('Mitral_Cells_noCa_nolib.ndf')

# set a model parameter, the INJECT field to provide constant current injection

input_CG1 = 0.01e-09
compartmentnumber_list_1 = [ "88", "96", "100", "26", "12", "18", "11", "45", "29", "30", "43", "48", "37", "81", "70", "93", "76", "59", "43", "47"]

for index in range(20):
  my_model_container.SetParameter( "/cells/CellGroup_1/CellGroup_1_0/Seg1_apic_%s" % compartmentnumber_list_1[index], 'INJECT', input_CG1)

# input_CG2 = 0.01e-09
# compartmentnumber_list_2 = [ "105", "98", "93", "117", "116", "115", "111", "35", "76", "77", "112", "73", "45", "84", "66", "49", "48", "18", "43", "42"]

# for index in range(20):
#  my_model_container.SetParameter( "/cells/CellGroup_2/CellGroup_2_0/Seg1_apic_%s" % compartmentnumber_list_2[index], 'INJECT', input_CG2)

# input_CG3 = 0.01e-09
# compartmentnumber_list_3 = [ "32", "31", "37", "23", "22", "24", "20", "21", "28", "18", "17", "16", "14", "13", "29", "36", "35", "33", "34", "27"]

# for index in range(20):
#  my_model_container.SetParameter( "/cells/CellGroup_3/CellGroup_3_0/Seg1_apic_%s" % compartmentnumber_list_3[index], 'INJECT', input_CG3)

# input_CG4 = 0.01e-09
# compartmentnumber_list_4 = [ "24", "12", "13", "17", "18", "15", "7", "8", "6", "9", "27", "26", "25", "23", "22", "21", "20", "19", "28", "16"]

# for index in range(20):
#  my_model_container.SetParameter( "/cells/CellGroup_4/CellGroup_4_0/Seg1_apic_%s" % compartmentnumber_list_4[index], 'INJECT', input_CG4)

# input_CG5 = 0.01e-09
# compartmentnumber_list_5 = [ "38", "36", "6", "4", "34", "5", "18", "19", "11", "12", "13", "8", "21", "26", "24", "23", "27", "32", "30", "17"]

# for index in range(20):
#  my_model_container.SetParameter( "/cells/CellGroup_5/CellGroup_5_0/Seg1_apic_%s" % compartmentnumber_list_5[index], 'INJECT', input_CG5)

# input_CG6 = 0.01e-09
# compartmentnumber_list_6 = [ "3", "20", "16", "22", "17", "21", "19", "18", "4", "5", "6", "7", "10", "9", "8", "11", "12", "13", "14", "15"]

# for index in range(20):
#  my_model_container.SetParameter( "/cells/CellGroup_6/CellGroup_6_0/Seg1_apic_%s" % compartmentnumber_list_6[index], 'INJECT', input_CG6)


# Create a solver, in this case heccer
my_heccer = scheduler.CreateSolver('My solver', 'heccer', verbose=False)

# Sets the element of the model to run from
# my_heccer.SetModelName('/cells')
my_heccer.SetModelName('/cells/CellGroup_1/CellGroup_1_0')
# my_heccer.SetModelName('/cells/CellGroup_2/CellGroup_2_0')
# my_heccer.SetModelName('/cells/CellGroup_3/CellGroup_3_0')
# my_heccer.SetModelName('/cells/CellGroup_4/CellGroup_4_0')
# my_heccer.SetModelName('/cells/CellGroup_5/CellGroup_5_0')
# my_heccer.SetModelName('/cells/CellGroup_6/CellGroup_6_0')

# set the timestep for the entire scheduler (solvers, inputs and outputs)
my_heccer.SetTimeStep(2e-05)


#
# Create Outputs
#
my_output = scheduler.CreateOutput('My output object', 'double_2_ascii')

my_output.SetFilename('CG1_Mitral_soma_Vm.txt')

# my_output.SetHeader("# time CGR1 CGR2 CGR3 CGR4 CGR5 CGR6")

# this adds to output to the output object
my_output.NoTimeStep(1)
my_output.AddOutput('/cells/CellGroup_1/CellGroup_1_0/Seg0_soma', 'Vm')
# my_output.AddOutput('/cells/CellGroup_2/CellGroup_2_0/Seg0_soma', 'Vm')
# my_output.AddOutput('/cells/CellGroup_3/CellGroup_3_0/Seg0_soma', 'Vm')
# my_output.AddOutput('/cells/CellGroup_4/CellGroup_4_0/Seg0_soma', 'Vm')
# my_output.AddOutput('/cells/CellGroup_5/CellGroup_5_0/Seg0_soma', 'Vm')
# my_output.AddOutput('/cells/CellGroup_6/CellGroup_6_0/Seg0_soma', 'Vm')

# an alternate way is to add output to the top level SPPy object
# This is useful when interfacing with a GUI
# scheduler.AddOutput('/cell/soma', 'Vm')

# to apply this to a particular output object, one would use
# scheduler.AddOutput('/cell/soma', 'Vm', 'output1')

# Optionally, provide output a multiple of the simulation time step
my_output.SetResolution(5)

# finally run the simulation for a specified time or number of steps
scheduler.Run(time=0.5)
# scheduler.Run(steps=25000)

print "Done!"
