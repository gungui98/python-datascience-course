import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
       # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    cond1 = df['sex'] == 'Male'
    sum_age_men = df[cond1].age.sum()
    ave = sum_age_men/cond1.sum()
    average_age_men = round(ave,1)

    # What is the percentage of people who have a Bachelor's degree?
    cond2 = df['education'] == 'Bachelors'
    percentage_bachelors = cond2.sum()/df.education.shape[0]
    percentage_bachelors = round(percentage_bachelors*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    cond3 = np.isin(df.education, (['Bachelors', 'Masters', 'Doctorate']))
    cond4 = df['salary'] == '>50K'
    sumnew1 = df[cond3 & cond4].shape[0]
    sumnew2 = df[cond3].shape[0]
    higher_education_rich = sumnew1/sumnew2
    higher_education_rich = np.round(higher_education_rich*100, 1)
    lower_education_rich =  df[(~cond3) & cond4].shape[0]/ df[~cond3].shape[0]
    lower_education_rich = np.round(lower_education_rich*100, 1)

    # percentage with salary >50K
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    cond5 = df['hours-per-week'] == df['hours-per-week'].min()
    amin = df[cond5].shape[0]
    min_work_hours = df['hours-per-week'].min()
  
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    num_min_workers =  df[cond5 & cond4].shape[0]/amin
    rich_percentage = int(num_min_workers*100)

    # What country has the highest percentage of people that earn >50K?
    salary_gt50 = df[cond4]['native-country'].value_counts()
    eachpopu_country = df['native-country'].value_counts()
    #highest_earning_country_percentage = a[-1]
    #highest_earning_country =
    m = (salary_gt50/eachpopu_country).sort_values(ascending=False)
    highest_earning_country = m.index[0]
    highest_earning_country_percentage = m[0]
    highest_earning_country_percentage = round(highest_earning_country_percentage*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    salary_gt50india = df[cond4 & (df['native-country'] == 'India')]['occupation'].value_counts()
    top_IN_occupation = salary_gt50india.index[0]

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
