# Flight Delays Exploration
## by Julia Kinday


## Dataset

The dataset reports flights in the United States from 1987 to 2008, including carriers, arrival and departure delays, and reasons for delays. Original dataset consists of 22 separate  compressed CSV files with US domestic flight data from 1 year in each file. Since the total amount of rows exceeds 120M I've decided to collect samples of 1000 rows for each year and combine them into one dataset. I attach the combined CSV file and Python script to my submission in case you don't want to resample so much data or would like to look at the script. I used conditional sampling to get rows where Departure Delay is both non-NaN and greater than 0 because it is the primary feature I want to investigate. 

During exploration I droped outliers in Departure Delays and Arrival Delays to get better picture. While ploting data I used [this source](https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat) to get airline names to replace their codes on plots. 

## Summary of Findings

I began exploration from looking into the main feature: departure delay. On histogram and box plot it showed a wide range of values from 0 to 1433 with the most of flights delay not more than on 1 hour. Log transformation didn't give any additional insights. Delay was slowly increasing over the years with a bump at 2003 when the new report system was implemented.

I looked into fewer features than I used in summary, because some of them didn't present anything worth looking further. While looking into carriers, I looked not only on the count of delays but also at the proportions and means using histograms and countplots. As the result it showed that 5 of 29 carriers are responsible for more than 60% of delays but their mean departure delays are relatively low. On the timeline plot Southwest Airlines had interesting change of mean delay: first 10 years of observation it was higher that others then in 2005 we see constant decrease. Other 4 carriers were slowly increasing their departure delay means with a sharp increase of mean delay at 2003, probably because the new report system was implemented and data became more accurate.

The delay reasons had less data than other features, airlines began to report them only from 2003. Ploted on the heatmap and scatter plots these variables gave some interesting insides: 'CarrierDelay' and 'LateAircraftDelay' have stronger correlation with departure delays, while 'WeatherDelay' and 'NASDelay' have stronger correlation with arrival delays. On the combined barplot Weather shows to have not so huge impact on delay average, LateAircraftDelay tends to be longer at the beginning of the year and CarrierDelay shows that avialines perform evenly with small decrease in November.

Airport exploration with countplots showed small difference between airport of origin and destination airport, probably because 6 airports that have most of the delays – Atlanta International Airport, O'Hare Airport, Dallas/Fort Worth International Airport, Los Angeles International Airport, Denver International Airport – are in top 10 busiest airports in USA so there is no surprise they have a bigger part of delays.
