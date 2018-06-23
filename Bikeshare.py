import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    print('Enter the city for which you want to explore the bikeshare data')
    city = ''
    while(city != 'ch' and city != 'nyc' and city != 'wa'):
        city = input('Enter ch for Chicago, nyc for New York City, wa for Washington : ')
    if(city == 'ch'):
        city = 'chicago'
    elif(city == 'nyc'):
        city = 'new york city'
    else:
        city = 'washington'
    choice = input('Do you wish to apply month/day filter. Enter month/day/both.Enter all for no filter : ').lower()
    if(choice == 'month'):
        print('Enter month for which you want to explore data')
        month = input().lower()
        day = 'none'
    elif(choice == 'day'):
        print('Enter the day for which you want to explore data')
        day = input().lower()
        month = 'none'
    elif(choice == 'both'):
        print('Enter month for which you want to explore data')
        month = input().lower()
        print('Enter the day for which you want to explore data')
        day = input().lower()
    else:
        month = 'all'
        day = 'all'
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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all' and month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month)
        df = df[df['month'] == month + 1]
        print(months[month])
    if day != 'all' and day != 'none':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    common_month = months[month - 1]
    print('The most common month is {}'.format(common_month))

    common_day = df['day_of_week'].mode()[0]
    print('The most common day is {}'.format(common_day))

    df['hour'] = df['Start Time'].dt.hour
    frequent_hour = df['hour'].mode()[0]
    print('The most common hour is {}'.format(frequent_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(commonly_used_start_station))

    commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(commonly_used_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travelling time is {}'.format(total_travel_time))

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travelling time is {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_type_count = df['User Type'].value_counts()
    print(user_type_count)

    gender_count = df['Gender'].value_counts()
    print(gender_count)

    earliest_birth_year = df['Birth Year'].min()
    print('Earliest Birth year is {}'.format(earliest_birth_year))

    most_common_birth_year = df['Birth Year'].mode()[0]
    print('Most common Birth year is {}'.format(most_common_birth_year))

    recent_birth_year = df['Birth Year'].max()
    print('Most recent Birth year is {}'.format(recent_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):

    print(df.sample(n=5))

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if(city == 'chicago' or city == 'new york city'):
            user_stats(df)
        while True:
            choice = input('Want to see raw data. Enter y/n  : ')
            if(choice == 'y'):
                raw_data(df)
            else:
                break
        restart = input('\nWould you like to restart? Enter yes or no : ')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
