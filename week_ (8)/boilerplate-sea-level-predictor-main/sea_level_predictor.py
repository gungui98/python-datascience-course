import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file

    fig, ax = plt.subplots(figsize=(16, 9))
    epa = pd.read_csv("epa-sea-level.csv")
    result = linregress(epa['Year'], epa['CSIRO Adjusted Sea Level'])

    # Create scatter plot
    epa.plot(kind='scatter', x='Year', y = 'CSIRO Adjusted Sea Level' )
  
    # Create first line of best fit
    min_year = epa['Year'].min()
    max_year = 2050
    best_fit_data = {
    "Year" : [],
    "prediction_value" : []
}

    best_fit_data['Year'] = [year for year in range(min_year, max_year +1)]
    best_fit_data["prediction_value"] = [result.slope*year + result.intercept for year in range(min_year, max_year + 1)]
    plt.plot( best_fit_data['Year'],  best_fit_data['prediction_value'])
   
    # Create second line of best fit
    start_year = 2000

    result = linregress(epa.loc[epa["Year"] >= start_year]["Year"], epa.loc[epa["Year"] >= start_year]["CSIRO Adjusted Sea Level"])
    b = [result.slope*year + result.intercept for year in range(2000, 2051)]
    
    plt.plot(  np.arange(2000, 2051),  b)
    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
