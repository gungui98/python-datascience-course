import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    start_year = df["Year"].min()
    end_year = 2050
    best_fit_data = {
        "Year": [],
        "y_value": []
    }
    for year in range(start_year, end_year):
        best_fit_data["Year"] = [year for year in range(start_year, end_year)]
        best_fit_data["y_value"] = [result.slope * year + result.intercept for year in range(start_year, end_year)]
    
    plt.plot(best_fit_data["Year"], best_fit_data["y_value"], 'r')

    # Create second line of best fit
    start_year = 2000
    end_year = 2050
    result = linregress(df.loc[df["Year"] >= start_year]["Year"], df.loc[df["Year"] >= start_year]["CSIRO Adjusted Sea Level"])
    for year in range(start_year, end_year):
        best_fit_data["Year"] = [year for year in range(start_year, end_year)]
        best_fit_data["y_value"] = [result.slope * year + result.intercept for year in range(start_year, end_year)]
    
    plt.plot(best_fit_data["Year"], best_fit_data["y_value"], 'g')
    

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
