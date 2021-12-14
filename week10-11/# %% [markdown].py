# %% [markdown]
# # Project 4: Can you predict that?

# %% [markdown]
# ### Details
# #### The state of Colorado has a large portion of their residential dwelling data that is  missing the year built and this document has a prediction model that can classify if a house is built pre 1980. It also predicts (regression) the actual age of each home.
# 

# %%
import pandas as pd
import altair as alt
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
# %%
# Load modules
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# %%
# load data
dwellings_denver = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_denver/dwellings_denver.csv")
dwellings_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_ml/dwellings_ml.csv")
dwellings_neighborhoods_ml = pd.read_csv("https://github.com/byuidatascience/data4dwellings/raw/master/data-raw/dwellings_neighborhoods_ml/dwellings_neighborhoods_ml.csv")   

# alt.data_transformers.enable('json') Altair no longer supports JSON
alt.data_transformers.enable('data_server')

# %% [markdown]
# ## GRAND QUESTION 1
# ### Create 2-3 charts that evaluate potential relationships between the home variables and before 1980

# %% [markdown]
# Price is affected  by living area

# %%
chart = (alt.Chart(dwellings_denver, title="Selling Price vs Square Feet")
    .encode(
        alt.X("livearea:Q", title = "Sqf per area"),
        alt.Y('sprice:Q',title="Selling Price")
    )
    .mark_point().properties(width=400,height=350)
)
chart

# %% [markdown]
# Second Chart: Selling Price vs Deduction

# %%
chart = (alt.Chart(dwellings_denver, title="Selling Price vs Deduction")
    .encode(
        alt.X("sprice:Q", title = "Selling price"),
        alt.Y('deduct:Q',title="Deduction from the selling price")
    )
    .mark_bar().properties(width=400,height=350)
)
chart
# chart.save("price.png")

# %% [markdown]
# 2 bedroom houses are most commonly sold followed by 3 bedroom

# %%
dwellings_denver['numbdrm'].value_counts().plot(kind='bar')
plt.title(' 2 bedroom houses are most commonly sold followed by 3 bedroom')
plt.xlabel('Bedrooms')
plt.ylabel('Count')
sns.despine


# %% [markdown]
# ## GRAND QUESTION 2
# ### Can you build a classification model (before or after 1980) that has at least 90% accuracy for the state of Colorado to use (explain your model choice and which models you tried)?

# %% [markdown]
# Yes, I can build a clasiffication model. I tried using other models but this is the only one I got working. I found that decision trees are easy to interpret and visualize.  It requires fewer data preprocessing from the user, for example, there is no need to normalize columns.

# %%
# Removes the target and keeps all features
#split dataset in features and target variable

X_pred = dwellings_ml.drop(dwellings_ml.filter(regex = 'before1980|yrbuilt|parcel').columns, axis = 1)
# Selects the target column
y_pred = dwellings_ml.filter(regex = "before1980")
# Splitting X and y variables into train and test sets using stratified sampling
X_train, X_test, y_train, y_test = train_test_split(
    X_pred, y_pred, test_size = .34, random_state = 76)  

# clf stands for classifier model.
clf = tree.DecisionTreeClassifier()
# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)
#  Using the features in the test set to make predictions
y_pred = clf.predict(X_test)
y_probs = clf.predict_proba(X_test)

# %% [markdown]
# ## GRAND QUESTION 3
# ### Will you justify your classification model by detailing the most important features in your model (a chart and a description are a must)?

# %%
df_features = pd.DataFrame(
    {'f_names': X_train.columns, 
    'f_values': clf.feature_importances_}).sort_values('f_values', ascending = False)

# %%
metrics.plot_roc_curve(clf, X_test, y_test)

# %% [markdown]
# ## GRAND QUESTION 4
# ### Can you describe the quality of your classification model using 2-3 evaluation metrics? You need to provide an interpretation of each evaluation metric when you provide the value.
# 

# %%
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# %%
print(metrics.classification_report(y_pred, y_test))


