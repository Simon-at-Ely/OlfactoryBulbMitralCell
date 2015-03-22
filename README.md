OlfactoryBulbMitralCell
=======================

Area to develop a community olfactory bulb model implemented in Neuron using neuroConstruct

Discussion of the project can be found here:

https://github.com/Simon-at-Ely/OlfactoryBulbMitralCell/issues/7

If you are new to neuroConstruct and wish to particpate, neuroConstruct is hosted on Github and can be easily installed:

Linux

You first need to install Apache Ant if you don’t already have it, which should be available in the update program for your distro of Linux or the website is here: http://ant.apache.org/ 
 
git clone https://github.com/NeuralEnsemble/neuroConstruct.git neuroConstruct

cd ~/neuroConstruct

./updatenC.sh 

ant run
 
to add the mitral cell model:
git clone https://github.com/Simon-at-Ely/OlfactoryBulbMitralCell.git OlfactoryBulbMitralCell
 
then to run neuroConstruct:
 
cd ~/neuroConstruct

./nC.sh
 
neuroConstruct is Gui based so you can click open project and navigate to model to open it. When you have opened it to run the model in Neuron (you will need Neuron installed on your computer):
 
Pick the ‘generate’ tab and move to the bottom of the screen and click the choose network button.

Choose the stored network and the design of the model will be generated.

Next go to the ‘export’ tab and choose the ‘Neuron’ tab on that page.

Click on the generate hoc code button.

When the run hoc code button becomes active, clicking on it should launch Neuron and run the model. If nothing happens you will need to edit the path for Neuron in the neuroConstruct user setting that can be accessed through the menu at the top of the window.


See also http://www.opensourcebrain.org/projects/olfactory-bulb-network-model-o-connor-angelo-and-jacob-2012

