import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True,   index_col='date')

# Clean data
df = df.loc[(df.value > df.value.quantile(0.025) ) & (df.value < df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
  #fig, ax = plt.subplots(figsize=(14,8))
  ax = df.plot(kind='line', figsize=(20, 5), legend=False, color = "firebrick")
  #plt.title/ plt,ylabel/ plt.xlabel
  ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
  ax.set_ylabel('Page Views')
  ax.set_xlabel("Date")
  fig = ax.figure





    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()
    df_bar['Months_int'] = df_bar.index.month
    df_bar = df_bar.reset_index()
    df_bar.drop(columns='date', inplace=True)
    df_bar = df_bar.groupby(by=['Months_int', 'Years', 'Months'], as_index=False).mean()
    df_bar['value'] = df_bar['value'].round().astype(int)
    # Draw bar plot
    fig, ax = plt.subplots()

  
    chartbar = sns.barplot(data = df_bar, x = 'Years', y = 'value',hue='Months', palette='tab10' )
    chartbar.set_xticklabels( chartbar.get_xticklabels() ,rotation = 90);
    ax.legend(loc=2)
    chartbar.set_xticklabels(chartbar.get_xticklabels(), rotation = 90, horizontalalignment= 'center')
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")
    ax.set_xlabel('Years')

    ax.set_ylabel("Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box['Months'] = df.index.month_name()
    df_box['Months_int'] = df.index.month
    df_box['Year'] = df.index.year
    df_box.reset_index(inplace=True)
    df_box.drop(columns='date', inplace= True)
    df_box = df_box.sort_values(by=['Months_int'])
    month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                  7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    df_box.replace({'Months_int': month_dict}, inplace=True)
    # Draw box plots (using Seaborn)
    
    fig, ax = plt.subplots(1,2, figsize=(18, 8))
    sns.boxplot(x="Year", y="value", data=df_box, ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    sns.boxplot(x="Months_int", y="value", data=df_box, ax=ax[1])
    ax[0].set_ylabel("Page Views")
    ax[1].set_ylabel("Page Views")
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel('Month')
    




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
