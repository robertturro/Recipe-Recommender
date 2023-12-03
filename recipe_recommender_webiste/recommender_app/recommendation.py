import pandas as pd
import numpy as np
import os  
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
from fuzzywuzzy import fuzz
from .models import Recipe_Data
from .models import Liked_Recipes, Recipe_Data

# When a user searches for recipes this function is called and filters the Recipe_Data model based on the user input from the recipe search form.
def filter_df(user_input):
    
    with open(r'D:\recipe_recommender\recipe_recommender_webiste\recommender_app\static\ingredients2.pickle','rb') as f:
        ingreds = pickle.load(f)

    with open(r'D:\recipe_recommender\recipe_recommender_webiste\recommender_app\static\ingredient_map.pkl','rb') as f2:
        ingred_map = pickle.load(f2)

    with open(r'D:\recipe_recommender\recipe_recommender_webiste\recommender_app\static\ethnicity_map.pkl','rb') as f2:
        eth_map = pickle.load(f2)

    with open(r'D:\recipe_recommender\recipe_recommender_webiste\recommender_app\static\dr_map.pkl','rb') as f2:
        dr_map = pickle.load(f2)

    initial_ingreds = user_input['ingredients_selected'][0]
    time_filter = user_input['time'][0]
    dietary_restriction = user_input['dietary'][0]
    ethnicity = user_input['ethnicity'][0]
    calories = user_input['calories'][0]
    protein = user_input['protein'][0]
    carbs = user_input['carbs'][0]
    sugar = user_input['sugar'][0]

    ingredients = []

    for i in range(len(ingreds)):
        for j in range(len(initial_ingreds)):
            if fuzz.ratio(initial_ingreds[j],ingreds[i]) > 75:
                ingredients.append(ingreds[i])


    ingredients.extend(initial_ingreds)

    df = Recipe_Data.objects.all()
    recipe_ids1 = []
    
    if "Any" not in initial_ingreds:
        for i in ingredients:
            recipe_ids1.extend(ingred_map[i])

        df = df.filter(recipe__in=recipe_ids1)

    recipe_ids2 = []

    if "None" not in dietary_restriction:
        print("Dietary Restriction")
        for j in dietary_restriction:
            recipe_ids2.extend(dr_map[j])

        df = df.filter(recipe__in=recipe_ids2)

    recipe_ids3 = []

    if "Any" not in ethnicity: 
        for k in ethnicity:
            recipe_ids3.extend(eth_map[k])

        df = df.filter(recipe__in=recipe_ids3)
        
    if time_filter == "Less than 5 Hours": 
        df = df.filter(minutes__lte=300)
    if time_filter == "Less than 3 Hours":
        df = df.filter(minutes__lte=180)
    if time_filter == "Less than 1 Hour":
        df = df.filter(minutes__lte=60)
    
    
    # All values precomputed in data_preprocessing.ipynb
    if calories == "Low Calorie":
        df = df.filter(calories__lte=200)

    if calories == "High Calorie": 
        df = df.filter(minutes__gte=556.5)

    if protein == "High Protein": 
        df = df.filter(minutes__gte=40)

    if protein == "Low Protein":
        df = df.filter(minutes__lte=5)

    if sugar == "High Sugar":  
        df = df.filter(minutes__gte=40)

    if sugar == "Low Sugar": 
        df = df.filter(minutes__lte=7)

    if carbs == "High Carbs": 
        df = df.filter(minutes__gte=17)

    if carbs == "Low Carbs":
        df = df.filter(minutes__lte=5)

    return df

# Small function used to handle the number of recipes which are shown at once after a search
def prepare_df(df,num1,num2):
    try:
        df = df.all()[num1:num2]
    except:
        df = df.all()[num1:]
        
    return df
 
# This is the main recommendation algorithm which uses the cosine distance between two arrays to determine their similarity. 
# The arrays used are the tag bins for each row of of the
def Similarity(liked_recipe, data_row):

    recipe_A = ast.literal_eval(data_row['tag_bins'])
    recipe_B = ast.literal_eval(liked_recipe['tag_bins'])

    Recipe_Distance = spatial.distance.cosine(recipe_A, recipe_B)
    
    return Recipe_Distance

# This function loops through each liked recipe a user has and first checks if the liked recipe already had a value for the most_similar column.
# The most_similar column is filled whenever a user likes that recipe and the most similar recipe is calculated. If any user has liked a certain recipe, the 
# recipe will therefore have a most similar value and will not need to be computed again. If a certain recipe has never been liked before, or if the most similar 
# recipe is already in a user's liked recipes, then a new most similar value must be computed.
def getNeighbors(liked):
    with open(r'D:\recipe_recommender\recipe_recommender_webiste\recommender_app\static\ingredients2.pickle','rb') as f:
        ingreds = pickle.load(f)

    with open(r'D:\recipe_recommender\recipe_recommender_webiste\recommender_app\static\ingredient_map.pkl','rb') as f2:
        ingred_map = pickle.load(f2)

    ingreds = ingreds[50:]
    liked_df = pd.DataFrame(list(liked.values()))
    full_data = pd.DataFrame(list(Recipe_Data.objects.all().values()))
    recommended = []

    for k in range(len(liked_df)):
        r = liked_df.iloc[k]['recipe']
        ing = liked_df.iloc[k]['ingredients']
        # Getting the most similar recipe
        recipe_data = Recipe_Data.objects.filter(recipe=r).values_list('most_similar')[0][0]

        # Checking if recipe_data is none or aleady in the user's liked recipes
        if (recipe_data is not None) and (str(recipe_data) not in list(liked_df['recipe'])):
            recommended.append(Recipe_Data.objects.filter(recipe=r).values_list('most_similar')[0][0])
            continue

        else:
            initial_ingreds = ing.split(",")
            initial_ingreds = [i.strip() for i in initial_ingreds]
            ingredients = []

            # Filtering the full recipe data to only include recipes with the ingredients of the liked recipe in order to improve
            # recommendation results
            for i in range(len(ingreds)):
                for j in range(len(initial_ingreds)):
                    if fuzz.ratio(initial_ingreds[j],ingreds[i]) > 75:
                        ingredients.append(ingreds[i])

            recipe_ids1 = []
            for i in ingredients:
                recipe_ids1.extend(ingred_map[i])
                
            filtered_data = full_data[full_data['recipe'].isin(recipe_ids1)]
            data = filtered_data[filtered_data['recipe'] != int(r)].reset_index()
            distances = []

            # Looping through the filtered data and computing the similarity of each recipe to the liked recipe
            for j in range(len(data)):
                
                dist = Similarity(liked_df.iloc[k], data.iloc[j])
                recipe_id = data[data.index == j]['recipe']
                recipe_name = data[data.index ==j]['recipe_name']
                distances.append((recipe_id,recipe_name, dist))

            # Getting the recipe with the smallest cosine distance
            distances.sort(key=operator.itemgetter(2))
            x = distances[0][0].reset_index()['recipe'][0]

            # If the recipe with the smallest distance is in the user's liked recipes loop through the rest of the recipes
            # until a new recipe is reached. 
            if str(x) in list(liked_df['recipe']):
                i=1
                while str(x) in list(liked_df['recipe']):
                    try:
                        x = distances[i][0].reset_index()['recipe'][0]
                        i+=1
                    except:
                        continue

            recommended.append(x)

            # Only change the value of most_similar if it is None
            if recipe_data is None:
                recipe_update = Recipe_Data.objects.get(recipe=r)
                recipe_update.most_similar = x
                recipe_update.save() 
        

    return recommended




