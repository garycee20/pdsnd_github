import sys
import pandas as pd

# Define a function to input a specified city
def input_city():
    """
    Users input a city and function tests to ensure name is within CITY_INDEX

    Args:
        Nil
    Returns:
        str (city) - name of the specified city
    """
    # Define a dictionary CITY_SELECT with number key for value city
    CITY_SELECT={1:'Chicago',
             2:'New York City',
             3:'Washington'}

    # Print CITY_SELECT and ask user to input a number for city to load
    print('\nAvailable cities to select from:\n')
    for i in CITY_SELECT.keys():
        print('{}: {}\n'.format(i,CITY_SELECT[i]))
    while True:
        try:
            city=CITY_SELECT[int\
            (input('Enter the number of the city you wish to analyse: '))]\
            .lower()
            break
        except:
            print('\nPlease try again!!\n')
            print('Specify the number of the city you wish to analyse: ')
    return city

# Define a function to input month and day to filer data
def input_month_day(month_check,day_check):
    """
    Users input a month and day to filter DataFrame

    Args:
        list (month_check) - list of months in dataset to check selection
        against
        list (day_check) - list of days in dataset to check selection against
    Returns:
        str (month) - the name of the specified month
        str (day) - name of the specified day of the week
    """
    # Ask user to input month
    month=input('\nIf you wish to filter by a month please enter the \
month name (for no filtering write \'all\'): ').title()
    while month not in month_check:
        print('\nInput error! Please try again\n')
        print('Only the following months are available:\n')
        for month in month_check:
            print(month)
        month=input('\nIf you wish to filter by a month please enter \
the month name (for no filtering write \'all\'): ').title()

    # Ask user to input the day of the week
    day=input('\nIf you wish to filter by a day of the week please enter \
the day\'s name (for no filtering write \'all\'): ').title()
    while day not in day_check:
        print('\nInput error! Please try again\n')
        print('Only the following days are available:\n')
        for day in day_check:
            print(day)
        day=input('\nIf you wish to filter by a day of the week please enter \
the day\'s name (for no filtering write \'all\'): ').title()

    return month,day

# Define a function to load specified dataset
def load_data():
    """
    loads data for the specified city.

    Args:
        nil
    Returns:
        df-pandas DataFrame containing city data filtered by month and day
        str (city) - name of the city dataset is from
        str (month) - name of the month the dataset is filtered on
        str (day) - name of the day the dataset is filtered on
    """
    # Call input_city function to define city to load
    city=input_city()

    # Define dictionary CITY_INDEX to index the specified city with a file name
    CITY_INDEX={'chicago':'chicago.csv',
            'new york city':'new_york_city.csv',
            'washington':'washington.csv'}

    # load data file into dataframe
    df=pd.read_csv(CITY_INDEX[city])

    # Convert column Start Time to date_time dtype
    df['Start Time']=pd.to_datetime(df['Start Time'])

    # Create a column in DataFrame df for the month
    df['Month']=pd.DatetimeIndex(df['Start Time']).month_name()

    # Create a column in DataFrame df for the day
    df['Day']=pd.DatetimeIndex(df['Start Time']).day_name()

    # Create a column in DataFrame df for the day
    df['Hour']=pd.DatetimeIndex(df['Start Time']).hour

    # Create list month_check of all months in loaded dataset
    month_check=list((df.sort_values(by=['Start Time']))['Month'].unique())
    month_check.append('All')

    # Create list day_check of all days in loaded dataset
    day_check=list((df.sort_values(by=['Start Time']))['Day'].unique())
    day_check.append('All')

    # Call input_month_day function to define month and day to filter on
    month,day=input_month_day(month_check,day_check)

    # Filter for input month
    if month!= 'All':
        df=df.loc[df['Month']==month]

    # Filter for input day
    if day!= 'All':
        df=df.loc[df['Day']==day]

    # Print success message
    print('-'*43)
    print('\nBikeshare data loaded for {} filtered by month: {} & day: {}\n'
          .format(city.title(),month.title(),day.title()))
    print('-'*43)

    return df,city,month,day

# Define a function to calculate all popular times
def pop_time(df):
    """
    Function to calculate and print the most popular times for bikeshare

    Arg:
        (DataFrame) df - the bikeshare data in a pandas DataFrame
    Return:
        Nil
    """
    # Define a set of column names in df
    col_name=['Month','Day','Hour']

    # Print title of calculation block
    print('\nPOPULAR BIKE SHARE TIMES IN {}'.format(city.upper()))
    print('NOTE: Only unfiltered time periods will be displayed\n')

    # Test for month filtered on all and calculate most popular
    if month=='All':
        pop_month=(df['Month'].mode(dropna=True))[0]
        print('The most popular month is {}'.format(pop_month))

    # Test for day filtered on all and calculate most popular
    if day=='All':
        pop_day=(df['Day'].mode(dropna=True))[0]
        print('The most popular day is {}'.format(pop_day))

    # Calculate and print most popular hour
    pop_hour=(df['Hour'].mode(dropna=True))[0]
    print('The most popular hour is {}'.format(pop_hour))
    print('-'*43)

# Define a function to calculate most common stations and trip
def common_stat_trip(df):
    """
    Function to find and print the most common start/end station and trip

    Arg:
        (DataFrame) df - the bikeshare data in a pandas DataFrame
    Return:
         Nil
    """
    # Print title of calculation block
    print('\nBIKESHARE COMMON STATIONS AND TRIPS IN {}\n'.format(city.upper()))

    # Create a new column in df concatenating start and end station
    df['Trip']=df['Start Station']+' to '+df['End Station']

    # Create a set of column names in df
    col_name=['Start Station','End Station','Trip']

    # Iterate through each object in col_name to determine the most popular
    for i in col_name:
        print('The most popular {} for bikeshare is {}'\
              .format(i.lower(),(df[i].mode(dropna=True))[0]))
    print('-'*43)

# Define a function to calculate trip duration statistics
def trip_duration(df):
    """
    Function to calculate and print total and average trip duration

    Arg:
        (DataFrame) df - the bikeshare data in a pandas DataFrame
    Return:
         Nil
    """
    # Print title of calculation block
    print('\nBIKESHARE TRIP DURATIONS IN {}\n'.format(city.upper()))

    # Calculate total travel time
    tot_trip=round((df['Trip Duration'].sum())/3600,2)
    print('The total travel time is {} hours'.format(tot_trip))

    # Calculate the average trip time
    avg_trip=round((df['Trip Duration'].mean())/60,2)
    print('The average trip duration is {} minutes'.format(avg_trip))
    print('-'*43)

# Define a function to calculate user info
def user_info(df):
    """
    Function to calculate total and average trip duration

    Arg:
        (DataFrame) df - the bikeshare data in a pandas DataFrame
    Return:
         Nil
    """
    # Print title of calculation block
    print('\nBIKESHARE USER INFORMATION IN {}\n'.format(city.upper()))

    # Generate a set of column names
    col_names=['User Type','Gender']

    #Check if city is NYC or chicago
    if city in ['chicago','new york city']:
        # Iterate through each column name in col_names
        for col_name in col_names:

            # Generate a series for col_name counts
            col_name_count=df[col_name].value_counts()

            # Print col_name_count series
            print('Count of {}:\n'.format(col_name.lower()))
            for i in col_name_count.keys():
                print('{}'.format(i),(' '*(15-len(i))),
                      '{}'.format(col_name_count[i]))
            print('-'*15,'\n')

            # Print results
            print('The earliest birth year is {}'.format(earliest))
            print('The most recent birth year is {}'.format(latest))
            print('The most common birth year is {}'.format(int(common[0])))
            print('-'*43)
    else:
        # Calculate a count of user type
        col_name_count=df['User Type'].value_counts()

        # Print a count of user type series
        print('Count of user type:\n')
        for i in col_name_count.keys():
            print('{}'.format(i),(' '*(15-len(i))),
                  '{}'.format(col_name_count[i]))
        print('-'*43,'\n')

# Define function to run all calculation functions
def summarise_all(df):
    """
    Runs all of the calculation functions

    Args:
        (DataFrame) df - the bikeshare data in a pandas DataFrame
    Returns:
        nil
    """
    # Call all functions
    pop_time(df)
    common_stat_trip(df)
    trip_duration(df)
    user_info(df)

# Define a function to end the Program
def end():
    """
    exits the program

    Args:
        nil
    Returns:
        nil
    """
    sys.exit()

# Define a function for a menu of options
def select_menu():
    """
    Function to print a menu of possible functions to select from and
    ask for user to input select
    Arg:
        Nil
    Return:
         int (num_select) - the selected number of functions to run
    """

    # Define a dictionary to produce a functions menu
    func_menu={1:'Popular times',
               2:'Popular stations and trips',
               3:'Trip durations',
               4:'User information',
               5:'Summarise all statistics',
               6:'Restart and load a new dataset',
               7:'Quit'}

    # Print selection menu from functions dictionary
    print('\nSELECTION MENU\n')
    print('Available statistics to select from:\n')
    for i in func_menu.keys():
        print('{}: {}\n'.format(i,func_menu[i]))

    # Ask user to input selection of which function to run and test
    num_select=int(input('Enter the number of your selection: '))
    while num_select not in func_menu.keys():
        print('\nPlease try again!!\n')
        num_select=int(input('Specify a number from 1-7 for your selection: '))

    return num_select

# Program welcome message
print('-'*43)
print('| WELCOME TO THE BIKE SHARE DATA EXPLORER |')
print('-'*43)

# Run the load_data function
df,city,month,day=load_data()

# Run selection menu function again an pasue between functions
# Pause function from stackoverflow
while True:
    input("\nPress Enter to continue...")
    num_select=select_menu()

    # Define a dictionary to call functions
    functions={1:pop_time,
               2:common_stat_trip,
               3:trip_duration,
               4:user_info,
               5:summarise_all,
               6:load_data,
               7:end}

    # Run selected function
    if num_select<=5:
        functions[num_select](df)
    elif num_select==6:
        df,city,month,day=functions[num_select]()
    else:
        functions[num_select]()
