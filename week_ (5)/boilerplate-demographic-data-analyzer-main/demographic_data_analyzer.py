import pandas as pd

<<<<<<< HEAD
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    condition = df["sex"] == "Male"
    average_age_men = round(df.loc[condition, "age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    condition = df["education"] == "Bachelors"
    percentage_bachelors = round(len(df.loc[condition]) / len(df) * 100, 1)
=======

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = None

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None

    # What is the average age of men?
    average_age_men = None

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None
>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
<<<<<<< HEAD
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"]) == False

    # percentage with salary >50K
    higher_education_rich = round(len(df.loc[(higher_education) & (df["salary"] == '>50K')]) / len(df.loc[higher_education]) * 100, 1)
    lower_education_rich = round(len(df.loc[(lower_education) & (df["salary"] == '>50K')]) / len(df.loc[lower_education]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    condition = df["hours-per-week"] == min_work_hours
    num_min_workers = len(df.loc[condition])
  
    rich_percentage = round(len(df.loc[(condition) & (df["salary"] == ">50K")]) / num_min_workers * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    riches = df.loc[df["salary"] == ">50K", "native-country"].value_counts() 
    riches_percentage = (round(riches / df["native-country"].value_counts() * 100, 1)).sort_values(ascending=False)
    highest_earning_country = riches_percentage.head(1).keys()[0]
    highest_earning_country_percentage = riches_percentage.head(1)[0]

    # Identify the most popular occupation for those who earn >50K in India.
    condition = (df["native-country"] == "India") & (df["salary"] == ">50K")
    top_IN_occupation = df.loc[condition, "occupation"].value_counts().sort_values(ascending=False).head(1).keys()[0]
=======
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f

    # DO NOT MODIFY BELOW THIS LINE

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
<<<<<<< HEAD
    }
=======
    }
>>>>>>> 525d56702a5550e7e07345bed05263e073c0727f
