# package import
#%%
import pandas as pd
import altair as alt
import numpy as np
# data import
url = "https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv"
names = pd.read_csv(url)

#%%
names.head()
names.year = pd.to_datetime(names.year, format='%Y')