# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import datadotworld as dw
import pandas as pd
import altair as alt

# %% [markdown]
# ## GRAND QUESTION 1
# ### Write an SQL query to create a new dataframe about baseball players who attended BYU-Idaho. The new table should contain five columns: playerID, schoolID, salary, and the yearID/teamID associated with each salary. Order the table by salary (highest to lowest) and print out the table in your report.

# %%
#  The WHERE keyword allows us to filter down the table horizontally (fewer rows).
result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT *
    FROM batting
    LIMIT 2;
    ''')
result

# %%
table = result.dataframe
print(table.head(3).to_markdown())

# %% [markdown]
# ## GRAND QUESTION 2
# # This three-part question requires you to calculate batting average (number of hits divided by the number of at-bats)
# %% [markdown]
#  a. Write an SQL query that provides playerID, yearID, and batting average for players with at least one at bat. Sort the table from highest batting average to lowest, and show the top 5 results in your report.
# 

# %%
result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT 
    playerid
    , yearid
    , h/ab AS batting_average
    FROM batting
    WHERE h >= 1
    ORDER BY batting_average DESC
    LIMIT 5
    ;
    ''')

table = result.dataframe
print(table.head(5).to_markdown())

# %% [markdown]
# b. Use the same query as above, but only include players with more than 10 “at bats” that year. Print the top 5 results.
# 

# %%
result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT 
    playerid
    , yearid
    , h/ab AS batting_average
    FROM batting
    WHERE ab >= 1
    ORDER BY batting_average DESC
    LIMIT 5
    ;
    ''')

table = result.dataframe
print(table.head(5).to_markdown())

# %% [markdown]
# c. Now calculate the batting average for players over their entire careers (all years combined). Only include players with more than 100 at bats, and print the top 5 results.

# %%
result = dw.query('byuidss/cse-250-baseball-database', 
    '''
    SELECT p.namefirst, p.namelast, SUM(b.h) as hits, SUM(b.ab) AS at_bat, SUM(b.h)/SUM(b.ab) AS bat_avg
    FROM people p
    JOIN batting b ON p.playerid = b.playerid
    WHERE b.ab > 100
    GROUP BY p.playerid
    ORDER BY bat_avg DESC
    LIMIT 5
    ;    
   ''')

table = result.dataframe
print(table.head(5).to_markdown())

# %% [markdown]
# ## GRAND QUESTION 3
# ### Pick any two baseball teams and compare them using a metric of your choice (average salary, home runs, number of wins, etc.). Write an SQL query to get the data you need. Use Python if additional data wrangling is needed, then make a graph in Altair to visualize the comparison. Provide the visualization and its description.

# %%
result = dw.query('byuidss/cse-250-baseball-database', 
 '''
    SELECT    f.franchname AS Team
            , t.teamid
            , t.ab AS at_bat
            , t.2b AS doubles
            , t.r AS runs_scored
            , t.2b/t.ab AS doubles_by_at_bat
            , t.r/t.2b AS runs_per_double
    FROM teams t
    JOIN teamsfranchises f ON t.franchid = f.franchid
    WHERE f.active = "Y" AND t.teamid = "WAS" OR t.teamid = "BOS"
    GROUP BY f.franchname
    ORDER BY runs_scored DESC
    ;
   ''')

table = result.dataframe
print(table.head().to_markdown())


# %%
# Chart
chart = (
    alt.Chart(table)
    .encode(
        alt.X('Team'),
        alt.Y('runs_per_double'))
    .mark_bar()
    .properties(width=400, title="Boston Score More Runs Than Washington From Doubles")
)
chart.save('chart.png')


