## TODO: import all necessary packages and functions
import csv
from collections import Counter, OrderedDict
import datetime
import time

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike
    share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or '
                 'Washington?\n')
    # TODO: handle raw input and complete function
    city = city.title()
    city_list = ['Chicago','New York','Washington']
    while(city not in city_list):
        city = input('\nSorry we don\'t have this city in our database.\n'
                     'Please choose one of these three cities: Chicago,'
                     'New York, or Washington\n')
        city = city.title()

    return city


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or '
                        'not at all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    time_period = time_period.lower()
    time_period_list = ['day','month','none']
    while(time_period not in time_period_list):
        time_period = input('\nSorry wrong input.\n'
                     'Please choose one of these three choices: month, day,'
                     ' none \n')
        time_period = time_period.lower()

    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or '
                 'June?\n')
    # TODO: handle raw input and complete function
    month = month.title()
    month_list = ['January', 'February', 'March', 'April', 'May', 'June']
    while(month not in month_list):
        month = input('\nSorry wrong input.\n'
                     'Please choose one of these six choices: January, '
                     'February, March, April, May, or June\n')
        month = month.title()

    return month


def get_day(month):
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    # TODO: handle raw input and complete function
    if month in ['January', 'March', 'May']:
        day_list = []
        for i in range(1,32):
            day_list.append(str(i))
        while(day not in day_list):
            day = input('\nSorry wrong input.\n'
                        'Please choose an integer between 1 - 31\n')
        day = day.title()

    elif month in ['April', 'June']:
        day_list = []
        for i in range(1,31):
            day_list.append(str(i))
        while(day not in day_list):
            day = input('\nSorry wrong input.\n'
                        'Please choose an integer between 1 - 30\n')
        day = day.title()

    elif month in ['February']:
        day_list = []
        for i in range(1,29):
            day_list.append(str(i))
        while(day not in day_list):
            day = input('\nSorry wrong input.\n'
                        'Please choose an integer between 1 - 28\n')
        day = day.title()

    return day


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        count_month_start = Counter()
        next(reader)

        for row in reader:
            count_month_start[row[0][5:7]] += 1

        return count_month_start.most_common(1)[0]


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for
    start time?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        count_day_start = Counter()
        next(reader)

        for row in reader:
            dt_str = row[0]
            dt_obj = datetime.datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
            weekday = dt_obj.weekday()
            count_day_start[weekday] += 1

        return count_day_start.most_common(1)[0]


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        count_hour_start = Counter()
        next(reader)

        for row in reader:
            count_hour_start[row[0][11:13]] += 1

        return count_hour_start.most_common(1)[0]


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        total = 0
        num_record = 0
        next(reader)

        for row in reader:
            total = total + float(row[2])
            num_record = num_record + 1

        average = total/num_record

        return (total,average)


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end
    station?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        count_start_station = Counter()
        count_end_station = Counter()
        next(reader)

        for row in reader:
            count_start_station[row[3]] += 1
            count_end_station[row[4]] += 1

        most_popular_start_station = count_start_station.most_common(1)[0]
        most_popular_end_station = count_end_station.most_common(1)[0]

        return (most_popular_start_station,most_popular_end_station)


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        count_trip = Counter()
        next(reader)

        for row in reader:
            trip = row[3] + ' to ' + row[4]
            count_trip[trip] += 1

        most_popular_trip = count_trip.most_common(1)[0]

        return (most_popular_trip)


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        count_user_type = Counter()
        next(reader)

        for row in reader:
            user_type = row[5]
            if user_type == '':
                user_type = 'Not Disclose'
            count_user_type[user_type] += 1

        return (count_user_type)


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    if city_file == 'washington.csv':
        return ''
    else:
        with open(city_file, newline='') as f:
            reader = csv.reader(f)
            count_gender = Counter()
            next(reader)

            for row in reader:
                gender = row[6]
                if gender == '':
                    gender = 'Not Disclose'
                    count_gender[gender] += 1

            return (count_gender)


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user),
    most recent (i.e. youngest user), and most popular birth years?
    '''
    # TODO: complete function
    if city_file == 'washington.csv':
        return ''

    else:
        with open(city_file, newline='') as f:
            reader = csv.reader(f)
            count_birth_year = Counter()
            next(reader)

            for row in reader:
                birth_year = row[7]
                if birth_year == '':
                    #birth_year = 'Not Disclose'
                    continue
                else:
                    birth_year = int(row[7][0:4])

                count_birth_year[birth_year] += 1

            od = sorted(count_birth_year.items())
            oldest_user = od[0]
            youngest_user = od[-1]
            most_popular_birth_year = count_birth_year.most_common(1)[0]

            return (oldest_user,youngest_user,most_popular_birth_year)


def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like
    to. After displaying five lines, ask the user if they would like to see
    five more, continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    display = display.lower()

    # TODO: handle raw input and complete function
    while(display not in ['yes', 'no']):
        display = input('\nSorry wrong input.\n'
                     'Please type \'yes\' or \'no\'.\n')
        display = display.lower()

    if display == 'no':
        print('OK, No data.')
        return display

    with open(city_file, newline='') as f:
        reader = csv.reader(f)
        i = 1
        next(reader)

        for row in reader:
            print(row)
            if i % 5 == 0:
                display2 = input('\nWant to see five more records?\n'
                                'Type \'yes\' or \'no\'.\n')
                display2 = display2.lower()
                while(display2 not in ['yes', 'no']):
                    display2 = input('\nSorry wrong input.\n'
                                 'Please type \'yes\' or \'no\'.\n')
                    display2 = display2.lower()
                if display2 == 'yes':
                    print('OK, five more are on the way ...')
                elif display2 == 'no':
                    print('OK, We stop here.')
                    break
            i += 1

        return (display)


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and
    time period specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    if city == 'Chicago':
        city_file = 'chicago.csv'
    elif city == 'New York':
        city_file = 'new_york_city.csv'
    elif city == 'Washington':
        city_file = 'washington.csv'

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        month_list = ['January', 'February', 'March', 'April', 'May', 'June']
        result = popular_month(city_file, time_period)
        month = month_list[int(result[0])-1]
        msg = 'The most popular month is '+ month
        msg = msg + ' with ' + str(result[1]) + ' records.'
        print(msg)

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.)
    # for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                     'Saturday', 'Sunday']
        result = popular_day(city_file, time_period)
        day = day_list[result[0]]
        msg = 'The most popular day of week is '+ day
        msg = msg + ' with ' + str(result[1]) + ' records.'
        print(msg)


        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
    result = popular_hour(city_file, time_period)
    hour = result[0]
    msg = 'The most popular hour of day is '+ hour
    msg = msg + ' with ' + str(result[1]) + ' records.'
    print(msg)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    result = trip_duration(city_file, time_period)
    msg = 'The total trip duration is '+ str(result[0]) + ' seconds'
    msg = msg + '\nAnd average trip duration is ' + str(result[1]) + ' seconds'
    print(msg)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    result = popular_stations(city_file, time_period)
    msg = 'The most popular start station is '+ result[0][0]
    msg = msg + ' with ' + str(result[0][1]) + ' records.'
    print(msg)
    msg = 'And the most popular end station is '+ result[1][0]
    msg = msg + ' with ' + str(result[1][1]) + ' records.'
    print(msg)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    result = popular_trip(city_file, time_period)
    msg = 'The most popular trip is '+ result[0]
    msg = msg + ' with ' + str(result[1]) + ' records.'
    print(msg)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    results = users(city_file, time_period)
    print('Counts for each user type:')
    for key,value in results.items():
        print(key + ' - ' + str(value))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    results = gender(city_file, time_period)
    if results == '':
        print('Sorry, no record for this city!')
    else:
        print('Counts for genders:')
        for key,value in results.items():
            print(key + ' - ' + str(value))

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user),
    # most recent (i.e. youngest user), and most popular birth years?
    # TODO: call birth_years function and print the results
    result = birth_years(city_file, time_period)
    if results == '':
        print('Sorry, no record for this city!')
    else:
        msg = 'The oldest users were born at '+ str(result[0][0])
        msg = msg + ' with ' + str(result[0][1]) + ' records.'
        print(msg)
        msg = 'The youngest users were born at '+ str(result[1][0])
        msg = msg + ' with ' + str(result[1][1]) + ' records.'
        print(msg)
        msg = 'The most popular birth year is '+ str(result[2][0])
        msg = msg + ' with ' + str(result[2][1]) + ' records.'
        print(msg)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that
    # they would like to
    display_data(city_file)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    while(restart.lower() not in ['yes','no']):
        restart = input('\nSorry, wrong input!\n'
        'Please type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
