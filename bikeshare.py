import time
import pandas as pd
import numpy as np

CITY_DATA = { 'c': 'chicago.csv',
              'n': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city=input("Would you like to see data for Chicago Type c , New York city Type n , or Washington Type w?").lower()
            if city.lower() not in ('c','n','w'):
                print("City input was invalid, please re-enter city")
            else:
                break
        except Exception as e:
            print()
            continue





    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input("Which month? January, February, March, April, May, June, or all ?").lower()
            if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                print("Month input was invalid, please re-enter month")
            else:
                break

        except Exception as e:
            print()
            continue


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while  True:
        try:
            day=input("Which day? Please type your response as an integer (1 = Sunday, 2= Monday , 3= Tuesday, 4=Wednesday, 5= Thursday, 6= Friday, 7= Friday, all)")
            if day not in ('1','2','3','4','5','6','7','all'):
                print("Day input was invalid ,please re-enter day")
            else:
                break
        except Exception as e:
            print()
            continue




    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

       # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])



       # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

       # filter by month if applicable
    if month != 'all':
           # use the index of the months list to get the corresponding int
         months = ['january', 'february', 'march', 'april', 'may', 'june']
         month = months.index(month) + 1

           # filter by month to create the new dataframe
         df = df[df['month'] == month]

       # filter by day of week if applicable
    if day != 'all':
           # filter by day of week to create the new dataframe
            # use the dictionary to get the corresponding day
            days = { '1': 'Sunday','2': 'Monday','3': 'Tuesday','4':'Wednesday','5':'Thursday','6':'Friday','7':'Saturday' }
            day = days[day]
            df = df[df['day_of_week'] == day]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Frequent month:', popular_month)

    # display the most common day of week
    popular_dow = df['day_of_week'].mode()[0]

    print('Most common day of week:', popular_dow)

    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] =df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]

    print('Most commonly used start station:', popular_start_st)


    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]

    print('Most commonly used end station:', popular_end_st)



    # display most frequent combination of start station and end station trip
    df['station_com'] = ('Start: '+ df['Start Station'] +'- End: '+ df['End Station'])

    print('The most commonly used start station and end station \n')
    print(df['station_com'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('Total travel time :', total_travel_time)
    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean travel time :', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()

    print(count_user_type)


    # Display counts of gender
    if city == "n"  or city=="c":
        count_gender = df['Gender'].value_counts()
        print(count_gender)

    # Display earliest, most recent, and most common year of birth
    if city == "n"  or city=="c":
        earliest_year_of_birth=df['Birth Year'].min()
        print('Earliest year of birth :', earliest_year_of_birth)

        recent_year_of_birth=df['Birth Year'].max()
        print('Most recent year of birth :', recent_year_of_birth)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
def raw_data(df):


        # creating iterator to display 5 lines of raw data
        n=5
        while True:
            raw=input("Would you like to see raw data? y or n \n").lower()
            if raw =="y":
                for i in range(0,n-1,1):
                    print(df.iloc[i])
                    n +=5
            elif raw=="n":
                break

            else:
                print("not  a valid input.")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)



        restart = input('\nWould you like to restart? Enter y or n\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
