import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
import time

#CITY_DATA = {'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def specify_city():
    '''This introduces the script and asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nType city name\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago':
            print('Looks like youre interested in Chicago data')
            return 'chicago.csv'
        elif city.lower() == 'new york':
            print('Looks like you are interested in New York data')
            return 'new_york_city.csv'
        elif city.lower() == 'washington':
            print('Looks like youre interested in Washington data')
            return 'washington.csv'
        else:
            print('Sorry, I do not understand your input. Please input either '
                  'Chicago, New York, or Washington.')

def provide_time_frame():
    '''This Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) Time filter for the bikeshare data.
    '''
    time_frame = ''
    while time_frame.lower() not in ['month', 'day', 'none']:   
        time_frame = input('\nWould you like to filter the data by month, day,'
                            ' or not at all? Type "month", "day", or "none" for no time filter: ')
        if time_frame.lower() not in ['month', 'day', 'none']:
            print('Sorry, I do not understand that input.')
    return time_frame

def specify_month():
    '''This asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of month for the bikeshare data.
    '''
    month_input = ''
    dict_of_months = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while month_input.lower() not in dict_of_months.keys():
        month_input = input('\nOn which month? January, February, March, April,'
                            ' May, or June?\n')
        if month_input.lower() not in dict_of_months.keys():
            print('Sorry, I do not understand your input. Please type in a '
                  'month between January and June')
    month = dict_of_months[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))

def specify_day():
    '''This asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (tuple) Lower limit, upper limit of date for the bikeshare data.
    '''
    this_month = specify_month()[0]
    month = int(this_month[5:])
    valid_date = False
    while valid_date == False:    
        is_int = False
        day = input('\nOn which day? Please type an integer as your response.\n')
        while is_int == False:
            try:
                day = int(day)  
                is_int = True
            except ValueError:
                print('Sorry, I do not understand your input. Please type your'
                      ' response as an integer.')
                day = input('\nWhich day? Please type an integer as your response e.g 1 for Sun, 2 for Mon, etc\n')
        try:
            start_date = dt(2017, month, day)
            valid_date = True
        except ValueError as ve:
            print(str(ve).capitalize())
    end_date = start_date + timedelta(days=1)
    return (str(start_date), str(end_date))

def popular_month(df):
    '''Calculates and prints the most popular month for start time.
    Args:
        bikeshare dataframe
        mode() returns the common or mode
    Returns:
        none
    '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))

def popular_day(df):
    '''This calculates and prints the most popular day of week (Monday, Tuesday, etc.) for start time.
    Args: 
        bikeshare dataframe(df)
    Returns: 
        none
    '''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

def popular_hour(df):
    '''Calculates and prints the most popular hour of day for start time.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_hour = int(df['start_time'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular hour of day for start time is {}{}.'.format(pop_hour_readable, am_pm))

def trip_duration(df):
    '''Finds and prints the total trip duration and average trip duration in
       hours, minutes, and seconds.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    total_duration = df['trip_duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(hour, minute, second))
    average_duration = round(df['trip_duration'].mean())
    m, s = divmod(average_duration, 60)
    if m > 60:
        h, m = divmod(m, 60)
        print('The average trip duration is {} hours, {} minutes and {}'
              ' seconds.'.format(h, m, s))
    else:
        print('The average trip duration is {} minutes and {} seconds.'.format(m, s))

def popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    pop_start = df['start_station'].mode().to_string(index = False)
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    print('The most popular end station is {}.'.format(pop_end))

def popular_trip(df):
    '''Finds and prints the most popular trip.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    most_pop_trip = df['journey'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))

def users(df):
    '''Finds and prints the counts of each user type.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))

def gender(df):
    '''This queries and prints the counts of gender.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))

def birth_years(df):
    ''' Here is  the earliest/ oldest user, most recent or 
        youngest user, and most popular birth years.
    Args:
        bikeshare dataframe
    Returns:
        none
    '''
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        data frame
    Returns:
        none
    '''
    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    #display the last seven rows
    tail = 7
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, Your input is not understood. Please type 'yes' or"
                  " 'no'.")
    if display.lower() == 'yes':
    #This prints every column except the 'journey' column created in the descriptive_stats()
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual'
                                     ' trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type "
                          "'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def descriptive_stats():
    '''Calculates and prints out the descriptive statistics about a city and
    time duration specified by the user throught the input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = specify_city()
    print('Wait, your city data is loading...')
    df = pd.read_csv(city, parse_dates = ['Start Time', 'End Time'])
    
    # change all column names to lowercase letters and replace spaces with underscores
    new_labels = []
    for col in df.columns:
        new_labels.append(col.replace(' ', '_').lower())
    df.columns = new_labels
    
    # increases the column width so that the long strings in the 'journey'#column can be displayed fully
    pd.set_option('max_colwidth', 100)
    
    # creates a 'journey' column that concatenates 'start_station' with 
    # 'end_station' for the use popular_trip() function
    df['journey'] = df['start_station'].str.cat(df['end_station'], sep=' to ')

    # Filter by time period (month, day, both, none)
    time_frame = provide_time_frame()
    if time_frame == 'none':
        df_filtered = df
    elif time_frame == 'month' or time_frame == 'day':
        if time_frame == 'month':
            filter_lower, filter_upper = specify_month()
        elif time_frame == 'day':
            filter_lower, filter_upper = specify_day()
        print('Filtering data...')
        df_filtered = df[(df['start_time'] >= filter_lower) & (df['start_time'] < filter_upper)]
    print('\nworking on the first statistic...')

    if time_frame == 'none':
        start_time = time.time()
        # What is the most popular month for start time?
        popular_month(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nNow calculating the next statistic...")
    
    if time_frame == 'none' or time_frame == 'month':
        start_time = time.time()
     
        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        popular_day(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")    
        start_time = time.time()
    # What is the most popular hour of day for start time?
    popular_hour(df_filtered)
    #print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    popular_stations(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    print("\nCalculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(df_filtered)
    print("That took %s seconds." % (time.time() - start_time))
    
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        print("\nCalculating the next statistic...")
        start_time = time.time()
        
        # What are the counts of gender?
        gender(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))
        print("\nCalculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest
        # user), and most popular birth years?
        birth_years(df_filtered)
        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(df_filtered)

    # This asks fr the raw input for a user to restart the script, would like to restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while restart.lower() not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        descriptive_stats()

if __name__ == "__main__":
	descriptive_stats()