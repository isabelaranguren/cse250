# Client Report - Introduction
__Course CSE 250__
__Isabel Aranguren__

## Elevator pitch

_The purpose of this assignment is to teach you how to visualise  data using Altair_

### GRAND QUESTION 1
#### Finish the readings and come to class prepared with any questions to get your environment working smoothly.

##### Yes, I finished the readings 

### GRAND QUESTION 2

#### Create a python script and use VS Code to create the example Altair chart in the assigned readings (note that you have to type chart to see the Altair chart after you run the code). Save your Altair chart for submission

####  TECHNICAL DETAILS

Example:
![](chart.png)

### Include the Markdown table created from the following code in your report (assuming you have mpg from question 2)


```python
print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))
```

| manufacturer   | model   |   year |   hwy |
|:---------------|:--------|-------:|------:|
| audi           | a4      |   1999 |    29 |
| audi           | a4      |   1999 |    29 |
| audi           | a4      |   2008 |    31 |
| audi           | a4      |   2008 |    30 |
| audi           | a4      |   1999 |    26 |


## APPENDIX A (PYTHON SCRIPT)

```python
#%%
import pandas as pd 
import altair as alt

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

# alt.data_transformers.enable('json')

chart = (alt.Chart(mpg)
  .encode(
    x = "displ",
    y = "hwy",
    color = "class"
    )
  .mark_circle())
chart.save('chart.png')

print(mpg
    .head(5)
    .filter(["manufacturer", "model","year", "hwy"])
    .to_markdown(index=False))


```

