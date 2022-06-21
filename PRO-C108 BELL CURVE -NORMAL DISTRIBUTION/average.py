import csv
import plotly.figure_factory as ff
import pandas as px

df=px.read_csv("average.csv")
fig=ff.create_distplot([df["Avg Rating"].to_list()],["AVERAGE RATING"])
fig.show()