# The entry point for the simulation.

import json
import os
import sys

myDir = os.getcwd()
sys.path.append(myDir)

import src.main.utils.constants as consts

from src.main.network.uniformNetwork import generateNetwork
from src.main.newsArticles.articleGenerator import generateArticles
from src.main.network.articleSampler import sameInclinationSampler, staggeredInclinationSampler
from src.main.simulation.simulate_rounds import roundsSimulator
from src.main.simulation.simulate_rounds_baseline import roundsSimulatorBaseline
from src.main.simulation.simulate_rounds_weighted_threshold import roundsSimulatorWeightedThreshold
from src.main.analysis.endOfRoundAnalysis import analyzeHistograms, analyzeNetworkDynamics, analyzeHistogramsAggregated, plotBoxPlotOfActivations  
import networkx as nx
import matplotlib.pyplot as plt
import datetime
import argparse

NUMBER_OF_RUNS = 1

def networkCreator(args):
    # generate network
    dateString = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    #quit(1)
    config = [[item, vars(consts)[item]] for item in dir(consts) if not item.startswith("__")]
    if not os.path.exists(consts.DATA_SIMULATION_FOLDER):
        os.mkdir(consts.DATA_SIMULATION_FOLDER)
    
    if not os.path.exists(os.path.join(consts.DATA_SIMULATION_FOLDER, dateString)):
        os.mkdir(os.path.join(consts.DATA_SIMULATION_FOLDER, dateString))

    with open(os.path.join(consts.DATA_SIMULATION_FOLDER, dateString, "config.json"), "w") as f:
        json.dump(config, f, indent=4)

    activationStatsAll = []
    activationDynamicsStatsAll = []
    p_avgsAll = []
    p_listsAll = []
    for i in range(NUMBER_OF_RUNS):
        print(f"************************ RUN {i} of {NUMBER_OF_RUNS}*********************")
        networkFolder, nodeGraph = generateNetwork(
            consts.HOMOPHILY_INDEX,
            consts.NODE_COUNT,
            consts.EDGE_COUNT_MEAN,
            consts.EDGE_COUNT_VAR,
            dateString,
            i
        )
        
        articleList = generateArticles(
            consts.ARTICLE_ATTRACTIVENESS_RANGE,
            consts.ARTICLE_ATTRACTIVENESS_MEAN,
            consts.ARTICLE_ATTRACTIVENESS_VAR,
            consts.ARTICLE_POLARITY_RANGE,
            consts.ARTICLE_POLARITY_MEAN,
            consts.ARTICLE_POLARITY_VAR,
            consts.ARTICLE_COUNT,
            networkFolder
        )

        samplers = sameInclinationSampler(nodeGraph, articleList)

        print(samplers[0])

        

        if args.algoType == "baseline":
            activationDynamicsStats, activationStats, p_avgs, p_lists  = roundsSimulatorBaseline(
                nodeGraph,
                articleList,
                samplers
            )

        elif args.algoType == "threshold":
            activationDynamicsStats, activationStats, p_avgs, p_lists  = roundsSimulator(
                nodeGraph,
                articleList,
                samplers
            )
        
        elif args.algoType == "weighted_threshold":
            activationDynamicsStats, activationStats, p_avgs, p_lists  = roundsSimulatorWeightedThreshold(
                nodeGraph,
                articleList,
                samplers
            )


        p_avgsAll.append(p_avgs)
        p_listsAll += p_lists
        activationStatsAll.append(activationStats)
        activationDynamicsStatsAll += activationDynamicsStats
    

    print("Averages")
    print(p_avgsAll)
    plotBoxPlotOfActivations(p_listsAll)
    #analyzeHistograms(activationStatsAll[0])

    analyzeHistogramsAggregated(activationStatsAll, consts.HOMOPHILY_INDEX,  os.path.join(consts.DATA_SIMULATION_FOLDER, dateString))
    analyzeNetworkDynamics(activationDynamicsStatsAll, consts.HOMOPHILY_INDEX, os.path.join(consts.DATA_SIMULATION_FOLDER, dateString))
    return networkFolder, articleList

def visualize_network(network_path):
    G = nx.read_gml(network_path)
    political_map = nx.get_node_attributes(G, "polInc")
    colors = [consts.COLOR_MAP[political_inclination] for node, political_inclination in political_map.items()]
    nx.draw_networkx(G, node_color=colors, with_labels=True)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--algoType', choices={"baseline", "threshold", "weighted_threshold"}, type=str, default="threshold", metavar='N', help='the options with which simulate rounds needs to run')
    
    args = parser.parse_args()

    networkFolder,  article_list = networkCreator(args)
    # visualize graph
    visualize_network(os.path.join(networkFolder, consts.NETWORK_ORIGINAL_FILENAME))
