import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=[0], index_col=0)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025))
        & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
  # Draw line plot
  fig = plt.figure(figsize=(20, 6))
  fig = sns.lineplot(data=df.value)
  fig.set_xlabel("Date")
  fig.set_ylabel("Page Views")
  fig.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  # Save image and return fig (don't change this part)
  fig = fig.get_figure()
  fig.savefig('line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['year'] = df_bar.index.year
  df_bar['month'] = df_bar.index.month
  df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()

  # Draw bar plot
  ax = sns.barplot(data=df_bar, x='year', y='value', hue='month')
  ax.set_xlabel("Years")
  ax.set_ylabel("Average Page Views")
  ax.set_title("Months")
  legend_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  handles, labels = ax.get_legend_handles_labels()
  ax.legend(handles, legend_labels, title="Months")
  # Save image and return fig (don't change this part)
  fig = ax.get_figure()
  fig.savefig('bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box['year'] = df_box.index.year
  df_box['month'] = df_box.index.month_name()

  fig, axes = plt.subplots(1, 2, figsize=(20, 6))
  sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
  axes[0].set_xlabel("Year")
  axes[0].set_ylabel("Page Views")
  axes[0].set_title("Year-wise Box Plot (Trend)")

  sns.boxplot(data=df_box, x='month', y='value', ax=axes[1])
  axes[1].set_xlabel("Month")
  axes[1].set_ylabel("Page Views")
  axes[1].set_title("Month-wise Box Plot (Seasonality)")
  month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  axes[1].set_xticklabels(month_labels)
  # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig
