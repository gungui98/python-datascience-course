import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = True, index_col = 'date')
df = df[(df['value'].quantile(0.025) <= df['value']) & (df['value'].quantile(0.975) >= df['value'])]
print(df.count(numeric_only=True))

# Clean data


def draw_line_plot():
  # print(df_line)
  # print(df_line.columns)
  fig = plt.figure(figsize = (32, 9))
  ax = fig.add_subplot()
  
  sns.lineplot(x = "date", y = "value", ax = ax, data = df, color='red')
  
  # Add title and labels
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  # plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  # plt.xlabel('Date')
  # plt.ylabel('Page Views')

  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df;
  df_bar['month'] = df.index.month
  df_bar['year'] = df.index.year
  df_bar = df_bar.groupby(['year', 'month']).mean()
  df_bar = df_bar.reset_index()
  df_bar = pd.pivot_table(df_bar, values='value', index='year', columns='month', dropna=False)
  df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
  # print(df_bar)  
  ax = df_bar.plot(kind='bar', figsize = (16,9), xlabel = 'Years', ylabel = 'Average Page Views')
  fig = ax.get_figure()
  # Draw bar plot





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

    fig,(ax1, ax2) = plt.subplots(1, 2, figsize = (16, 9))
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1).set(title = "Year-wise Box Plot (Trend)", xlabel = 'Year', ylabel = 'Page Views')
    sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct','Nov', 'Dec']).set(title = "Month-wise Box Plot (Seasonality)", xlabel = 'Month', ylabel = 'Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
if __name__ == '__main__':
  draw_box_plot()
