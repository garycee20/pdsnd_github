### Date created
29/03/2020

### Project Title
Bikeshare data exploration tool

### Description
bikeshare.py is a program to explore bikeshare data from three different US
cities. These cities are:
1. Chicago
2. New York City
3. Washington
The program loads data for a selected city from a csv file. Output can be filtered by a user selected month or day.

The main program interface is a selection menu with the following options:

1. Popular times - Calculate the most popular month, day and hour for the
specified dataset. Note: month and day will be excluded if you have chosen
to filter on either of these.

2. Popular stations and trips - Determines the most popular start and end
station and trip.

3. Trip durations - Calculates the total and average trip duration.

4. User information - Returns counts of User Types and Gender as well as
statistics of birth year. Note: gender and birth year statistics are not
available for Washington.

5. Summarise all statistics - Print a summary of all the above statistics.

6. Restart and load a new dataset - Restart and load a new city, again with
options to filter by month and day.

7. Quit - exit the program.

### Files used
bikeshare.py - bike exploration program
chicago.csv - Chicago bikeshare dataset
new_york_city.csv - New York City bikeshare dataset
washington.csv - Washington bikeshare dataset

### Credits
After running selected options there is a pause where the user is asked to
press 'Enter' to continue, this was taken from Stackoverflow:
https://stackoverflow.com/questions/983354/how-do-i-make-python-wait-for-a-pressed-key
