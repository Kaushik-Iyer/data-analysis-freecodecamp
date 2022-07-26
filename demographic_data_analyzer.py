import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df =pd.read_csv('adult.data.csv',delimiter=',')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count =pd.Series(df['race'].value_counts())

    # What is the average age of men?
    average_age_men =np.average(df['age'])

    # What is the percentage of people who have a Bachelor's degree?
    degree=df[df['education']=='Bachelors'].size
    percentage_bachelors = (degree.size/df.size)*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    higher_fifty_above=advanced_education[advanced_education['salary']=='>50K']
    higher_education_rich = (higher_fifty_above.size/advanced_education.size)*100

    lower_fifty_above=lower_education[lower_education['salary']=='>50K']
    lower_education_rich =(lower_fifty_above.size/lower_education.size)*100 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_hours=df['hours-per-week']
    min_work_hours = min_hours.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hour_workers=df[df['hours-per-week']==min_hours.min()]
    num_min_workers = min_fifty_above=min_hour_workers[min_hour_workers['salary']=='>50K']

    rich_percentage = (min_fifty_above.size/num_min_workers.size)*100

    # What country has the highest percentage of people that earn >50K?
    
    perc_high_earn = 100*df[df.salary=='>50K']['native-country'].value_counts()/df['native-country'].value_counts()
    highest_earning_country = perc_high_earn.idxmax()
    highest_earning_country_percentage = round(perc_high_earn[highest_earning_country], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_occupation=df[df['native-country']=='India']
    top_IN_occupation = indian_occupation[indian_occupation['salary']=='>50K'].occupation.value_counts().idxmax()

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
