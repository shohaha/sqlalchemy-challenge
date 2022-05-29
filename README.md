# sqlalchemy-challenge

# SQLAlchemy Bootcamp Asssignment - Surf’s Up

## Background

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following sections outline the steps you must take to accomplish this task.

### Part 1: Climate Analysis and Exploration

In this section, I will use Python and SQLAlchemy to perform basic climate analysis and data exploration of a climate database by completing the following tasks using SQLAlchemy ORM queries, Pandas, and Matplotlib.

#### Precipitation Analysis

Perform an analysis of precipitation in the area, to do the following:

* Find the most recent date in the dataset.

* Using this date, retrieve the previous 12 months of precipitation data by querying the 12 previous months of data. **Note:** Do not pass in the date as a variable to your query.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame, and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results by using the DataFrame `plot` method, as shown in the following image:

* Use Pandas to print the summary statistics for the precipitation data.

#### Station Analysis

Perform an analysis of stations in the area, to do the following:

* Design a query to calculate the total number of stations in the dataset.

* Design a query to find the most active stations (the stations with the most rows).

    * List the stations and observation counts in descending order.

    * Which station id has the highest number of observations?

    * Using the most active station id, calculate the lowest, highest, and average temperatures.

    * Use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in queries.

* Design a query to retrieve the previous 12 months of temperature observation data (TOBS).

    * Filter by the station with the highest number of observations.

    * Query the previous 12 months of temperature observation data for this station.

    * Plot the results as a histogram with `bins=12`

* Close out session.

- - -

### Part 2: Design Your Climate App

Design a Flask API based on queries.

Use Flask to create routes, as follows:

* `/`

    * Homepage.

    * List all available routes.

* `/api/v1.0/precipitation`

    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

    * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

    * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

    * Query the dates and temperature observations of the most active station for the previous year of data.

    * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.

    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).

* Join the station and measurement tables for some of the queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.

### Bonus: Other Analyses

#### Temperature Analysis 1

Conduct an analysis to answer the following question: Hawaii is reputed to enjoy mild weather all year round. Is there a meaningful difference between the temperatures in, for example, June and December?

* Use Pandas to perform the following steps:

    * Convert the date column format from `string` to `datetime`.

    * Set the date column as the DataFrame index.

    * Drop the date column.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for the temperature in December.

* Use the t-test to determine whether the difference in means, if any, is statistically significant. 

#### Temperature Analysis 2

### Background

You want to take a trip from August 1 to August 7 of this year, but you are worried that the weather will be less than ideal. Using historical data in the dataset, find out what the temperature has previously been for this timeframe.

* Use a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

**Complete the following steps:**

* Use the `calc_temps` function to calculate the minimum, average, and maximum temperatures for your trip using the matching dates from a previous year (for example, use "2017-08-01").

* Plot the minimum, average, and maximum temperature from your previous query as a bar chart, as captured in the following steps and image:

    * Use "Trip Avg Temp" as the title.

    * Use the average temperature as the bar height (_y_ value).

    * Use the peak-to-peak (TMAX-TMIN) value as the _y_ error bar (YERR).

#### Daily Rainfall Average

### Background
Now that you have an idea of the temperature, let’s find out what the rainfall has been. You don't want to visit if it rains the whole time! 

**Complete these following steps:**

* Calculate the rainfall per weather station using the previous year's matching dates.

    * Sort this in descending order by precipitation amount, and list the station, name, latitude, longitude, and elevation.

### Daily Temperature Normals

Calculate the daily normals for the duration of your trip. Normals are the averages for the minimum, average, and maximum temperatures.

You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Make sure to use all historic TOBS that match that date string.

**Complete the following steps:**

* Set the start and end date of the trip.

* Use the date to create a range of dates.

* Strip off the year, and save a list of strings in the format `%m-%d`.

* Use the `daily_normals` function to calculate the normals for each date string, and append the results to a list called `normals`.

* Load the list of daily normals into a Pandas DataFrame, and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals, as shown in the following image:

* Close out session.
