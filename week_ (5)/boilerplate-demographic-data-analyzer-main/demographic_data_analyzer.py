import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df.head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    filter1 = df['sex'] == 'Male'
    df_male_age = df['age'].where(filter1)
    average_age_men = round(float(df_male_age.mean()),1)

    # What is the percentage of people who have a Bachelor's degree?
    filter2 = df['education'] == 'Bachelors'
    suma2 = df['education'].where(filter2).dropna().count()
    percentage_bachelors = round((suma2 / df['education'].count()) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    filter3 = df['salary'] == '>50K' 
    
    filter3a = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    
    filter3b = ~(df['education'] == 'Bachelors') & ~(df['education'] == 'Masters') & ~(df['education'] == 'Doctorate')

    higher_education = df['education'].where(filter3a).dropna().count()
    lower_education = df['education'].where(filter3b).dropna().count() 

    # percentage with salary >50K
    higher_education_rich = round(df['education'].where(filter3 & filter3a).dropna().count() / higher_education * 100,1)
    lower_education_rich = round(df['education'].where(filter3 & filter3b).dropna().count() / lower_education * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    min_work_h_salary = df[(df['hours-per-week'] == min_work_hours) & filter3]

    haves = len(min_work_h_salary.index)
    have_nots = len(df[(df['hours-per-week'] == min_work_hours)].index)

    rich_percentage = haves / have_nots * 100

    # What country has the highest percentage of people that earn >50K?
    country_list = pd.DataFrame(data=df['native-country'].unique(), columns = ["native-country"])
    country_list['High_Earners'] = 0
    country_list['High_Earners_Ratio'] = 0

    country_list.set_index('native-country')

    filter3 = df['salary'] == '>50K' 

    for i, row in country_list.iterrows():
        filter6 = df['native-country'] == row['native-country']
        country_list.iloc[i, 1] = df['native-country'].where(filter3 & filter6).dropna().count()
        country_list.iloc[i, 2] = country_list.iloc[i, 1] / df['native-country'].where(filter6).dropna().count() * 100

    country_list.loc[country_list['High_Earners'].idxmax()]
    country_list.loc[country_list['High_Earners_Ratio'].idxmax()]


    highest_earning_country = country_list.loc[country_list['High_Earners_Ratio'].idxmax(), 'native-country']
    highest_earning_country_percentage = round(country_list.loc[country_list['High_Earners_Ratio'].idxmax(), 'High_Earners_Ratio'],1)

    # Identify the most popular occupation for those who earn >50K in India.
    df_filtered = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = df_filtered['occupation'].value_counts().idxmax()

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
