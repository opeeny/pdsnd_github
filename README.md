### Date created
04/12/2019

### Project Title
Bikeshare Data *Python* Script

### Python Script to Explore US Bikeshare Data 
A Python script written for Project 2 of Nanodegree data science program at Udacity, sponsered by **AAL**(Africa). 
Its used to explore data related to bike share systems for the three cities including Chicago, New York City, and Washington. It imports data from csv files and compute descriptive statistics from the data. It also takes in users' raw input to create an interactive experience in the terminal to present these statistics.
### How to run the script
You can run the script by install Python Anaconda, you will need to [download the Anaconda installer](https://www.anaconda.com/download/). This script is written in Python 3, so you will need the Python 3.x version of the installer. After downloading and installing **Anaconda**.
### Datasets
The datasets used for this script contain bike share data for the three cities of chicago, New york and Washington. . Some data wrangling has been performed by Udacity's staff before being provided to the students. I downloaded this files from the udacity project workspace. The file sizes are too big to be loaded at once, so on requesting to view the city data, i specified 7 columns each time a user requests to see the data.

The data is provided by [*Motivate*](https://www.motivateco.com/), which is a bike share system provider for many cities in the United States. The data files for all three cities contain the same six columns:
* Start Time
* End Time
* Trip Duration (in seconds)
* Start Station
* End Station
* User Type (Subscriber or Customer)

The Chicago and New York City files also contain the following two columns:
* Gender
* Birth Year
### Questions explored
The script answers the following questions about the bike share data:
* What is the most popular month for start time?
* What is the most popular day of week (Monday, Tuesday, etc.) for start time?
* What is the most popular hour of day for start time?
* What is the total trip duration and average trip duration?
* What is the most popular start station and most popular end station?
* What is the most popular trip?
* What are the counts of each user type?
* What are the counts of gender?
* What are the earliest (i.e. oldest person), most recent (i.e. youngest person), and most popular birth years?
### Future scope
In the future, more functions that compute statistics will be added to answer more questions about the data, meanwhile the terminal is the way for user to interact with the script. The possibilities of improving the interactive experience (e.g turning this script into a web application) shall be explored.
### Resources referred to complete this project
###### Use parse_dates to recognize datetime columns:
* https://stackoverflow.com/questions/21269399/datetime-dtypes-in-pandas-read-csv
* https://stackoverflow.com/questions/17465045/can-pandas-automatically-recognize-dates
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
###### Converting pandas series or dataframes to string:
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.to_string.html
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_string.html

###### Assessing datetime series:
*https://stackoverflow.com/questions/42977395/pandas-dt-hour-formatting by godfreyopeeny
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html
* https://stackoverflow.com/questions/29366572/pandas-how-to-filter-most-frequent-datetime-objects

###### The filtering of the date:
* https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates

###### Checking the validity of the date:
* https://stackoverflow.com/questions/9987818/in-python-how-to-check-if-a-date-is-valid/9987935

###### Adding a day to a date:
* http://www.pressthered.com/adding_dates_and_times_in_python/

###### Read day of week, month, hour etc.:
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.html
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.dt.dayofweek.html

###### Convert seconds to hours, minutes and seconds:
* https://stackoverflow.com/questions/775049/how-to-convert-seconds-to-hours-minutes-and-seconds
* https://docs.python.org/3/library/functions.html#divmod

###### Concatenate strings of two columns:
* https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
* http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.str.cat.html#pandas.Series.str.cat

###### Set column widths:
* https://pandas.pydata.org/pandas-docs/stable/options.html
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.set_option.html

###### Other pandas and numpy functions:
* Lessons in the Introduction to Data Analysis section of Udacity's Data Aanalyst Nanodegree
