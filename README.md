# Impact of Content Personalization Algorithms in Social Media
This repository is for the final Project of COMPSCI 690F. Our work focusses on how the implementation of a global recommender model affects polarization in a simulation of a social network.

## Prerequisite Commands
Please do the following to be able to run our code.

1. Setup a venv and run 
`pip install -r requirements.txt`

2. Set python path for successful imports
`export PYTHONPATH='.'`

## Running the simulation
The functioning of the recommender system is dependent on two parameters: SIGMA and GLOBAL_RECOMMENDER which range between 0 to 1. These parameter values can be adjusted in the src/main/utils/constants.py file.

As of now, creating a network with a configurable set of parameters is done. The actual simulation needs to be done. Run the following to create the network.

To run the threshold model, use 
`python3 src/main/simulation/simulator_main.py --algoType threshold`

To run the baseline, use
`python3 src/main/simulation/simulator_main.py --algoType baseline`

The results are generated in data_simulation folder with a timestamp. All the graphs presented in the paper get generated in the respective folders.
