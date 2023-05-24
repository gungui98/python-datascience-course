import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                 index_col=['date'],
                 parse_dates=True)

# Clean data
mask = (df['value'] >= df['value'].quantile(0.025)) & (
  df['value'] <= df['value'].quantile(0.975))
df = df[mask]


def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(30, 10))
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_xlabel("Date")
  ax.set_ylabel("Page Views")
  sns.lineplot(data=df, legend=False)
  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['Years'] = df.index.year
  df_bar["Months"] = df_bar.index.month_name()
  # Draw bar plot
  fig, ax = plt.subplots(figsize=(20, 15))
  ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
  df_bar["month_number"] = df_bar.index.month
  df_bar = pd.DataFrame(
    df_bar.groupby([
      "Years", "Months", "month_number"
    ])["value"].mean().round().astype(int)).sort_values(["month_number"])
  df_bar = df_bar.rename(columns={"value": "Average Page Views"})
  df_bar = df_bar.reset_index()
  chart = sns.barplot(data=df_bar,
                      x="Years",
                      y="Average Page Views",
                      hue="Months",
                      palette="tab10")
  chart.set_xticklabels(chart.get_xticklabels(),
                        rotation=90,
                        horizontalalignment='center')
  plt.legend(loc='upper left')
  # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2, figsize=(20, 10.5))
  sns.boxplot(df_box, x="year", y="value", ax=axes[0])
  axes[0].set_title("Year-wise Box Plot (Trend)")
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")

  month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  sns.boxplot(df_box, x="month", y="value", order=month_order, ax=axes[1])
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")
  

  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
