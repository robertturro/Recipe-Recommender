import pandas as pd
import numpy as np
import os
import kaggle
import ast
from sklearn.cluster import KMeans
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import pickle
from scipy import spatial
import operator
from ast import literal_eval



def Similarity(user_input, row1):

    ingreds_A = row1['ingredients_bin']
    ingreds_B = user_input['ingredients_bin'][user_input.index[0]]

    IngredDistance = spatial.distance.cosine(ingreds_A, ingreds_B)
    
    nutrition_A = row1['nutrition']
    nutrition_B = user_input['nutrition'][user_input.index[0]]

    NutDistance = spatial.distance.cosine(nutrition_A, nutrition_B)

    return IngredDistance + NutDistance 


def filter_df(df,time_filter, dietary_restriction, ethnicity, type_of_food, holiday):

    if time_filter == "Less than 5 Hours":
        df = df[df['minutes'] < 300]
    if time_filter == "Less than 3 Hours":
        df = df[df['minutes'] < 180]
    if time_filter == "Less than 1 Hour":
        df = df[df['minutes'] < 60]
    if time_filter == "Any Time":
        df = df

    if dietary_restriction != "None":
        df = df.explode('dietary_restriction')
        df = df[df['dietary_restriction'].isin(dietary_restriction)]

    if ethnicity != "Any":
        df = df.explode('ethnicity')
        df = df[df['ethnicity'] == ethnicity]

    if type_of_food != "Any":
        df = df.explode('type_of_food')
        df = df[df['type_of_food'] == type_of_food]

    if holiday != "No":
        df = df.explode('holiday')
        df = df[df['holiday'] == holiday]

    return df


def getNeighbors(user_input, df, K, name_df):
    distances = []
    
    for index, recipe in df.iterrows():
        
        dist = Similarity(user_input, recipe)
        name = name_df[name_df['id'] == index]['name']
        steps = name_df[name_df['id'] == index]['steps']
        distances.append((name,steps, dist))

    distances.sort(key=operator.itemgetter(2))
    neighbors = []

    for x in range(K):
        neighbors.append(distances[x])
    return neighbors


