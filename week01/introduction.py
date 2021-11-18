#%%
import pandas as pd 
import altair as alt

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

alt.data_transformers.enable('json')

chart = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    color = "class"
    )
  .properties(width=700,height=450, title="Cars with big engines use more fuel")
  .mark_circle())
chart.save('chart.png')

print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))

# %%
