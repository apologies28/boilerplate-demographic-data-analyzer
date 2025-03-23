import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    # Filtering the DataFrame for the Male sex
    df_male = df[df["sex"] == "Male"]

    # Calculate the average age of men
    average_age_men = df_male["age"].mean()

    # Typecasting as a float data
    average_age_men = round(float(average_age_men), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # Filtering the DataFrame for people with a Bachelors degree
    df_bachelors_degree = df[df["education"] == "Bachelors"]

    # Calculate percentage
    percentage_bachelors = round((len(df_bachelors_degree) / len(df)) * 100, 1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # Filtering the DataFrame for people with advanced education
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Filtering the DataFrame for people with advanced education who make more than 50K
    advanced_education_over_50k = advanced_education[advanced_education['salary'] == '>50K']

    # Calculate the percentage
    adv_e_percentage_over_50k = (len(advanced_education_over_50k) / len(advanced_education)) * 100

    
    # What percentage of people without advanced education make more than 50K?
    # Filtering the DataFrame for people with advanced education
    no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Filtering the DataFrame for people with advanced education who make more than 50K
    no_advanced_education_over_50k = no_advanced_education[no_advanced_education['salary'] == '>50K']

    # Calculate the percentage
    no_advanced_education_percentage = (len(no_advanced_education_over_50k) / len(no_advanced_education)) * 100


    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = round(adv_e_percentage_over_50k, 1)
    lower_education_rich = round(no_advanced_education_percentage, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = int(df["hours-per-week"].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    # Filtering the Dataframe for people who work the minimum hours
    df_min_hours = df.loc[df["hours-per-week"] == 1]

    # Filtering the DataFrame for people who earn aboove 50K
    min_hours_over_50k = df_min_hours[df_min_hours["salary"] == ">50K"]

    # Calculate the percentage
    min_hours_percentage_over_50k = (len(min_hours_over_50k) / len(df_min_hours)) * 100

    num_min_workers = len(min_hours_over_50k)

    rich_percentage = min_hours_percentage_over_50k

    # What country has the highest percentage of people that earn >50K?

    # Create a list of the unique values in the series "native-country" and an empty list to store the percentage of people who earn above 50k in each country.
    list_of_countries = df["native-country"].value_counts().index.tolist()
    percentages = []

    # Iterate over list of countries and calculate the percentage of people who earn above 50k in each country and append them to the list "percentages"
    for countries in list_of_countries:
        df_country = df[df["native-country"] == countries]
        df_country_over_50 = df_country[df_country["salary"] == ">50K"]

        percentage = (len(df_country_over_50) / len(df_country)) * 100
        percentages.append(percentage)

    # Zipping the list of countries and the list of percentages together to sort them
    zipped = zip(percentages, list_of_countries)

    sorted_zipped = sorted(zipped, key=lambda x:x[0], reverse=True)
     
    highest_earning_country = sorted_zipped[0][1]

    highest_earning_country_percentage = round(sorted_zipped[0][0], 1)

    # Identify the most popular occupation for those who earn >50K in India.
    over_50k = df[df["salary"] == ">50K"]
    
    # Filtering the over_50K DataFrame for those in India
    over_50k_india = over_50k[over_50k["native-country"] == "India"]

    # Calculating the most popular occupation
    top_IN_occupation =  over_50k_india["occupation"].value_counts().index[0]    # .value_counts returns a series in descending order so that the first element is the most frequently-occurring element.

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


calculate_demographic_data(print_data=True)