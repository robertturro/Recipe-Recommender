# Recipe Recommender Website Using Django

The goal of this project was to create a website that allows a user to search for recipes by ingredient, nutritional information, time to cook, dietary restriction, and ethnicity (Italian, Mexican, Japanese, etc). After searching for recipes a user can scroll through all the options that are presented and can like any desired recipes. After searching for recipes a user can then go to a personalized dashboard which presents all previously liked recipes plus recommended recipes which are based off of the recipes that the user liked. 

The recipe data that was used was taken from the following Kaggle dataset: https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions 
The datasets that were used were PP_recipes.csv, PP_users.csv, and RAW_recipes.csv. These three datasets were combined to make the final dataset which consisted of the most rated recipes with an average rating of three or more. The final recipe data as well as all of the datasets used to make the final dataset are too large to keep in this repository, but the entire process of building the final dataset can be seen in the data_preprocessing.ipynb file. 

The web framework used was python's Django. The final dataset made in the data_preprocessing.ipynb file was loaded into a Django model by uploading an excel extract. That entire process was done through the import_from_excel function in views.py which renders the templates named import_form.html and import_sucess.html. By uploaded the recipe dataset into a model, the process of having to upload a data extract every time a view function is called was able to be avoided. The process of uploading a data extract took about 10-15 seconds and extracting data from a Django model is instantaneous so a significant amount of time was saved by uploading the data to a Django model. 


The recommendation algorithm follows a Content-Based Filtering recommendation system in which the recipes that get recommended are the recipes that are most similar to recipes that the user has recently liked. 
