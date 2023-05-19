import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    df.rename(columns={'CSIRO Adjusted Sea Level':'Sea Level (inches)'}, inplace=True)

    def predict_linregress(df, kind):
        lineA = linregress(x= df.Year, y = df['Sea Level (inches)'])
        xa = np.arange(df.Year.min(), 2051, 1 )
        ya = lineA.intercept + lineA.slope*xa
        df_lineA = pd.DataFrame({'Year' : xa , 'predict_sea_level' : ya, 'kind': [kind]*len(xa)})
        return df_lineA

    sns.scatterplot(data = df , x = 'Year' , y ='Sea Level (inches)',color='c', label = "past sea level")

    df_predict = pd.concat([
        predict_linregress(df, 'prediction with all values'),
        predict_linregress(df[df.Year >= 2000], 'prediction with after 2000 values')
    ])
    sns.lineplot(data=df_predict, x='Year', y='predict_sea_level', hue='kind')
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()