import pandas as pd

<<<<<<< HEAD
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
  
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts().tolist()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors'].shape[0]/df['education'].shape[0] * 100, 1)
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
>>>>>>> 5d6a076483c1944b3a098e2c5e8539249fc82459

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
<<<<<<< HEAD
    higher_education = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))
  
    lower_education = ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'))

    # percentage with salary >50K
    higher_education_rich = round(df.loc[higher_education & (df['salary'] == '>50K')].shape[0]/df.loc[higher_education].shape[0] * 100, 1)
    lower_education_rich = round(df.loc[lower_education & (df['salary'] == '>50K')].shape[0]/df.loc[lower_education].shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = (df['hours-per-week'] == (df['hours-per-week'].min()))
  
    rich_percentage = round(df.loc[num_min_workers & (df['salary'] == '>50K')].shape[0]/df.loc[num_min_workers].shape[0] * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country = (df.loc[(df['salary'] == '>50K'), 'native-country'].value_counts()/df['native-country'].value_counts()).sort_values(ascending = False)
    highest_earning_country = country.index[0]
    
    highest_earning_country_percentage =  round(country['Iran']*100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    res = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India'), 'occupation'].value_counts()
    top_IN_occupation = res.index[0]
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
>>>>>>> 5d6a076483c1944b3a098e2c5e8539249fc82459

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
    }
