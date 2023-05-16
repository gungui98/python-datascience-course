import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df.loc[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(1 - 0.025))]
df["date"] = pd.to_datetime(df["date"])

def draw_line_plot():
    # Draw line plot
    
    fig, ax = plt.subplots(figsize=(32, 16))
    sns.lineplot(data=df, x="date", y="value")
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    df_bar = df_bar.groupby(pd.Grouper(key='date', axis=0, freq='M')).mean()
    df_bar['month'] = df_bar.index.strftime("%B")
    #df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.reset_index()
    df_bar['date'] = df_bar['date'].apply(lambda x: x.strftime('%Y-%m'))
    missing_data = {
        "year": [2016, 2016, 2016, 2016],
        "month": ['January', 'February', 'March', 'April'],
        "value": [0, 0, 0, 0]
    }
    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
    g = sns.catplot(
        data=df_bar, kind="bar",
        x="year", y="value", hue="month",
        ci=None, palette="dark", alpha=.6, height=6, legend="Months"
    )
    g.set_xlabels('Years') # not set_label
    g.set_ylabels('Average Page Views')
    g._legend.set_title("Months")

    fig = g.fig


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
    fig, axes = plt.subplots(1, 2, figsize=(32, 16))
    #yearly
    sns.boxplot(data=df_box, x="year", y="value", ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    #monthly
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
