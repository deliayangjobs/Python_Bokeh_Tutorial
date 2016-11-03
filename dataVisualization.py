from bokeh.charts import Scatter, output_file, show
import pandas


df=pandas.DataFrame(columns=["X","Y"])
df["X"]=[1,2,3,4,5]
df["Y"]=[5,6,4,5,3]
p=Scatter(df, x="X", y="Y", title="Temperature Observation", xlabel="Day of Observations", ylabel="Temperature")

output_file("Scatter_charts.html")

show(p)
