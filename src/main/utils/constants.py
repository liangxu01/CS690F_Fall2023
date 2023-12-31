INCLINATIONS = [-1,1]
NETWORK_ORIGINAL_FILENAME = "startOfNetwork.gml"
DATA_SIMULATION_FOLDER = "data_simulation"
ARTICLES_FILENAME = "articlesInfo.json"
# config constants
HOMOPHILY_INDEX = 0.2
NODE_COUNT = 250

EDGE_COUNT_MEAN = 15
EDGE_COUNT_VAR = 2
EDGE_COUNT_LOWER_BOUND = 1
EDGE_COUNT_UPPER_BOUND = min(int(0.9*NODE_COUNT), NODE_COUNT-1)

#article level constants
ARTICLE_POLARITY_RANGE = [0.5,1]
ARTICLE_POLARITY_MEAN = 0.75
ARTICLE_POLARITY_VAR = 0.1

ARTICLE_ATTRACTIVENESS_RANGE = [0,1]
ARTICLE_ATTRACTIVENESS_MEAN = 0.5
ARTICLE_ATTRACTIVENESS_VAR = 0.005

ARTICLE_COUNT = 100 # this corresponds to the number of rounds which the article will go through.

ARTICLE_SAMPLER_COUNT = 10
ARTICLE_SAMPLER_COUNT_OFFSET = 1

#user level constants
COLOR_MAP = {-1: 'blue', 1: 'red'}
WEIGHTAGE_CONGRUENT_MEAN = 0.7
WEIGHTAGE_CONGRUENT_VAR = 0.1
WEIGHTAGE_CONGRUENT_UPPER_BOUND = 1
WEIGHTAGE_CONGRUENT_LOWER_BOUND = 0.5
#0.18 was last tested wiwth 100 nodes
# for thresh model
THRESH_ALPHA_MEAN = 0.06
# for weighted thresh model
# THRESH_ALPHA_MEAN = 0.48
THRESH_ALPHA_VAR = 0.03
THRESH_ALPHA_LOWER_BOUND = 0
THRESH_ALPHA_UPPER_BOUND = 1

USER_ARTICLE_OFFSET_FACTOR = 0.1
USER_ARTICLE_VAR = 0.05

#USER_ARTICLE_LOWER_BOUND = 0.1
#USER_ARTICLE_UPPER_BOUND = 0.9

WEIGHT_P_N = 0.6
WEIGHT_P_P = 0.4

SIGMA = 0.5
GLOBAL_RECOMMENDER = 0.06
