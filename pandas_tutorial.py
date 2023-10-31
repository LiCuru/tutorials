# --- tutorial for pandas.DataFrame.resample() ---

# --- installing Python ---
# for this tutorial, you'll need to have Python installed on your system
# the proper version of python is a python3 version.
# Python3 is the up to date version

# if you are using linux Ubuntu, Python is installed by default
# you can check the Python version by typing
# 'python3 --version'
# in the command line (accessed with CTRL + SHIFT + T)

# if you are using linux Debian, follow the 'Step 1 - Setting Up Python3' section in the tutorial at this website:
# https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-debian-11

# --- setting up the development environment ---
# for the development environment, install Qt
# access https://www.qt.io/download-open-source
# and click on 'Download the Qt Online Installer'
# run the installer. It's gonna install Qt
# installing Qt for development is gonna take some time
# when in the 'Installation Folder' phase, select the 'personalized installation' option
# then, in the 'Select Components' phase, select the 3 'Qt Creator' options and
# the 'Developer and Designer Tools', under the 'Qt' option
# then just keep going on and install it
# it's gonna take some time

# after installing Qt for development, create a new project
# click on 'File' > 'New Project' > 'Application (Qt for Python)' > 'Qt Quick Application - Empty'
# then, click on 'next' > 'next' > 'finish'
# the project will be created

# after creating the project, go to the main.py file in the Left Sidebar
# delete all of its contents
# it's done.

# to set up a new shortcut for running the code
# go for 'Edit' > 'Preferences' > 'Environment'
# select the 'keyboard' tab
# on 'Filter', write 'run'
# select 'run'
# Under 'Project Explorer', select 'run'
# in the 'key sequence' field, type 'F8'
# now, the 'F8' key will be the keyboard shortcut for running the code



# --- the pandas.DataFrame.resample tutorial ---

# first, a dataframe, that is, a table, will be created
# then, it's gonna be changed with the 'resample' method
# (a 'method' is an action, the 'resample' action will be applied on the table)

# The 'resample' method changes the time units from which the table has
# its counts. It cannot be applied in another type of data that is not a 'time-series'

# Notice that 'time-series' is n-o-t a 'series' object. You'll understand the meaning
# of this difference by the end of this text

# So, the 'resample' method changes the time units from which the table has
# its counts. It cannot be applied in another type of data that is not a 'time-series'
# As it changes the 'time-series', and the number of rows (lines) in a column, it can
# gather bigger "chunks of time" per row, creating a table with less rows. Or ir can
# split the time-series into 'smaller pieces of time', generating more rows.
# it applies a method (an action) for filling the new set of rows. It can be a sum
# when gathering rows into a lesser amount of rows, for instance. Or it can,
# for instance, just repeat the last or the next value on the new rows, if more
# rows are created. Many different actions, that is, methods, can be applied
# when 'resampling' a dataframe.

# Pandas documentation describes these methods
# and all of the other methods given by pandas.
# it can be found at the https://pandas.pydata.org/ website
# in the 'documentation' section

# First, we have to import pandas, it's not in python by default,
# even though it's a python library
# Installing python won't install pandas
# pandas is a library, a library written with python
# a library from which tables, series and other things are created
# studied and manipulated. Pandas library is meant for working with data.
# it has to be installed the same way python has to be installed
# if not installed, calling pandas just won't work, cus it won't be there.
# Instructions on how to install it can be found
# in the 'getting started' section
# at the same https://pandas.pydata.org/ website


#After that, it can be imported:

import pandas as pd


# everytime we need to use pandas, we don't write 'pandas',
# it's abreviated to 'pd' when it's written 'pandas as pd'
# when we say 'pandas.DataFrame()', for instance
# we mean to write 'pd.DataFrame()', even though we are still calling the pandas library
# the '.DataFrame()'  after 'pd' means that, from 'pd' (pandas), we are calling the
# 'DataFrame()' method. It's as if the dot was the point from which the option is taken.
# I mean, from 'pd', use the 'DataFrame()' option. Look --> 'pd.DataFrame()'



# in pandas:
# dataframes are tables
# tables are dataframes


# in cooking:

#                       cake pan ------------------------------------>  cake
#                                                      generates



#                   donut cake pan ------------------------------------>  donut cake
#                                                           generates



#                   heart cake pan ------------------------------------>  heart cake
#                                                           generates



# in object oriented programming (OOP):

#                                 class  -------------------------------------->  object
#                                                             generates



#            pd.DataFrame() class  ------------------------------->  dataframe object
#                                                               generates



#                      pd.Series() class  ------------------------------->  series object
#                                                                  generates



# 'objects' have their own methods (actions) and attributes (characteristics)

# the tables in the pandas library are objects called 'dataframes'
# each 'row' (each line) of the table has an index value to it
# that is, there is a "column" called 'index'. Even though you visualize it as a
# "column'"on the dataframe it's not even called 'column' by pandas.
# it's an object of its own, and this "column" is called 'index'.
# It's filled with values that identify the 'rows' (the lines of the dataframe)
# the 'index' is at the left end of the dataframe

# 'series' objects are as if they were a 1 column table, but they are not a table.
# they are a single list (a single "column")
# with an 'index' for each value (for each 'row', that is, for each line)
# the 'index' is at the left end of the series

# there are dataframes with only one column though.
# A dataframe object (a table) with
# one single column is not the same thing as a series.
# They are different kind of objects.

# a series is a pd.Series() created object
# a dataframe is a pd.DataFrame() created object
# each of these kind of objects have their own set of object methods (actions)
# and their own set of attributes (characteristics)
# they are different kind of objects
# calling a method (action), or an attribute(characteristic) that only
# a dataframe object has on a rather series object will raise an error
# the error message, in red, will say something like
# "this series object does not have this method, or action"


# the pandas documentation (found in https://pandas.pydata.org/) describes the
# classes
# objects
# object methods, that is, object actions
# object attributes, that is, object characteristics

#(classes are a sort of object though. But that is not important for now)

# A dataframe has one or more columns and it has an index.
# Indexes, for instance, are objects too

# A series has one "column", and it has an index too.


# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#
# this link from the documentation, pointing to the sort of chapter called
# '10 minutes to pandas' in the user guide section of the documentation
# presents the main classes, objects, methods and attributes
# it presents them for a beginner in pandas, so that the main content of pandas can be understood.
# (it doesnt take 10 minutes)




# ---creating a dictionary---
# data for the dataframe table
# (the batter for the cake)

# dictionary batter = {key: value, key: value}
# with key ('price' and 'volume') as columns for the dataframe table, and
# with value (the ['l', 'i', 's', 't', 's']) as a list of each one of the values for each row (line)
# 8 values on the list means 8 rows on the dataframe table

# creating a dictionary:
batter = {
                    'price': [10, 11, 9, 13, 14, 18, 17, 19],
                    'volume': [50, 60, 40, 100, 50, 100, 40, 50]
               }



# ---creating the dataframe---
# creating the week_revenue dataframe

# with the:

# -   pandas.DataFrame() class
# the parenthesis() means action, this is how we know it's a 'verb'
# classes and methods are followed by parenthesis() in python and in many programming languages

# -   dictionary 'batter' object
# a dictionary is an object. It as if it was a 'noun'

# here, we mean that, everytime we type 'week_revenue'
# we are gonna call this object created with the pandas.DataFrame() class

week_revenue = pd.DataFrame(batter)



# ---creating the 'week_starting' column---
# at the right side of the table, as the last column
# creating the 'week_starting' column.
# the notation for calling a column of the dataframe in pandas
# is: name_of_the_dataframe['column_name']

# this newly created column is just a new column.
# this column is n-o-t yet set as the index
week_revenue['week_starting'] = pd.date_range(
                                                                                        '01/01/2018',
                                                                                        periods = 8,
                                                                                        freq =  'W'
                                                                                    )

# 'date_range()' is a pandas method.
# This sort of list will fill up each row, so that each row is going to have a 'time-point',
# that is, each row is going to have a 'datetime64' data.
# These time-points given by the pandas.date_range() method are 'equally spaced time points'.
# link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.date_range.html

# '01/01/2018' is the start date
# 'periods =  8' means 8 rows, that is, 8 values, on the dataframe table
# 'freq = 'W'' means a weekly distance between the dates on each row

# here, this column is set to be a list of values created
# by the pandas.date_range() method



# --- about the index and the 'resample()' method ---
# the 'resample()' method, that will be used later, will return (create)
# an object (dataframe or series) with an index of its own
# this index will be created with the column that has the time-series
# in this case, column with the time-series is the 'week_starting' column.
# it can get confusing

# so, it's important to understand that:
# in the dataframe week_revenue created just now
# the time-series column called 'week_starting' is n-o-t set as the index
# 'week_starting' is just another column

# for the index, the pandas.DataFrame() class
# has generated one automatically with integers (numbers).

# That is:
# Since no index was set when calling pandas.DataFrame(),
# the class has generated an index of its own,
# an index that is not any of the columns and
# that has been populated with integers (numbers)
# starting from 0 (zero)



# printing the week_revenue dataframe table
print('the week_revenue table: \n', week_revenue, '\n\n')

# printing the week_revenue dataframe table index
print('the week_revenue table index: \n', week_revenue.index, '\n\n')

# printing the week_revenue table columns
# the daterange() data is just a column, called 'week_starting':
print('the week_revenue table columns: \n', week_revenue.columns, '\n\n')



# ---setting a new columns order to get things organized---
# the notation for selecting more than 1 column of the dataframe
# in pandas is
# name_of_the_dataframe[[column_1, column_2, column_3]]
week_revenue = week_revenue[[ 'week_starting', 'price', 'volume']]



# ---adding new column 'revenue'
# a new column is always gonna be added at the right end, the right side of the dataframe table
# the 'revenue' column has its value set to 'price' times 'volume'. That is:
# 'revenue' = 'price' X 'volume'
week_revenue['revenue'] = week_revenue['price'] * week_revenue['volume']


# ---creating the html file for the weekly table, so that it can be seen from the browser---
# this file should be opened with the browser to visualize the file.
# Updates can be seen by refreshing the page after running the code again
# when the code is run, a new html file with the same name is gonna be created, deleting the old one
week_revenue.to_html('week_revenue.html')



# ---selecting the columns of interest for summing up---
# the weekly value rows will become monthly value rows
# using the 'resample' method

# (the selection is going to do the same thing as a 'drop' in pandas, it's dropping the 'price' column.
# that is, it's deleting the 'price' column)

# why dropping the price values column:
# we want the average price for each month line
# pandas has the 'mean()' math operation in the 'resample' method for the columns
# but the mean value of the price column for each month is just a misleading value
# summing up the price values column will only sum up the price tags
# the price tags are not the same thing as the actual selling
# you're not getting the mean price value with this calculation
# if the price tags are changing on each line of the week table
# it just means the price is changing over time (each week has its own product price)
# They need to be summed up as many times as they've been actually sold
# to get the mean value, and this is the 'revenue' column value

# so, we need to get the month table, and there, get the revenue column
# for the month, and divide it by the number of sellings for the month,
# that is, the volume column. Then we can derive the average price column.

# the 'resample' method can apply a math operation,
# in this case it's the sum() operation, on all of the columns of the table
# if we dont select a column when 'resampling' a dataframe table
# it's gonna select all of the columns
# and then return all of them with the sum() operation
# so. we are not selecting 'price' column, as it's just not interesting.

# In the week_revenue dataframe, we have the revenue displayed for each week.
# Through the 'resample' method, the new dataframe generated will display the
# revenue values for each month, by summing up the weeks.

# From there, we can get the the monthly average price,
# by dividing the monthly revenue by the monthly volume of sales. That is:
# 'monthly average price' = 'monthly revenue' / 'monthly volume of sales'

# so, selecting the columns:
week_revenue = week_revenue[['week_starting', 'volume', 'revenue']]



# ---Applying the 'pandas.DataFrame.resample()' method---
# changing the time frequency of the dataframe lines from weekly to monthly lines

# The 'week_revenue' dataframe has the 'volume' and 'revenue' columns.
# 'resample' is going to return (create) a dataframe with the 'volume' and 'revenue' columns
# but each row (each line) of the dataframe is gonna be a monthy "chunk of time'
# each of the 4 weekly value rows (lines) are summed up into 1 single monthly value row (line)

# The 'pandas.DataFrame.resample()' return data is either
# a pandas.DataFrame object, that is, a dataframe
# or a pandas.Series series, that is, an sort of 'indexed list'
# in this case, it returned a dataframe, as more than one column was returned.
# If only one column was returned from the method 'resample', it would return a series object

# The 'resample' method has changed the 'time-series' column (named 'week_starting'), it became
# an index of the dataframe. It is in the dataframe, but not as 'column': it's there as an 'index'
# It wont be selected as a column in the dataframe returned (created) by the resample method
# that is: even though you see it as a column of the table, it cannot be accessed with the word 'column' via code.
# Now it's an index object, it can only be accessed the word 'index', and it has other properties
# The original prior index is simply not in the new dataframe returned from the 'resample' method.
# It as if the old index was dropped away

# The new index has the same 'name' attribute as the old 'week_starting' column, where it came from
# that is --- month_revenue.index.name == 'week_starting'
# it's good practice fixing the name of this newly created index right after 'resampling' the table
# it helps not losing track of what has been done

#so, applying the 'resample' method
month_revenue = week_revenue.resample('M', on='week_starting').sum()

# "M" stands for "month".

# "on='week_starting'" means the column where the 'resample' method is gonna be applied on
# I mean, the column on which the time points are going to change, leading to the change
# on the number of rows of the table
# This column selected has to be a time-series, datetime64 data filled column

# '.sum()' is the action that is going to take place on the dataframe selected.

# an action has always to be selected after calling 'resample()' method,
# either in case the rows of the new dataframe are less in number than in the prior dataframe
# or in the case the rows of the new dataframe are more in number than the prior dataframe.
# in this case, the new dataframe returned from resample method has less rows than the
# prior dataframe. And the action applied on was '.sum()'. It could have been 'mean()'  too
# for instance.





# printing the 'month_revenue' dataframe table
print('the month_revenue table: \n', month_revenue, '\n\n')

# the index of  the 'month_revenue' dataframe is a set of 'datetime64' data rows
# the 'resample' method has already set its name to 'week_starting' (a mismatching name)
# printing the 'month_revenue' dataframe table index
print('the month_revenue table index: \n', month_revenue.index, '\n\n')

# printing the 'month_revenue' table columns
# notice that the 'week_starting' index is just not listed,
# since it's not a column, it's an index
print('the month_revenue table columns: \n', month_revenue.columns, '\n\n')



# ---setting index's name to 'month_starting' (fixing the name, as it was 'week_starting' ) ---
month_revenue.index.name = 'month_starting'

# printing the month_revenue dataframe table index
print('the month_revenue table index: \n', month_revenue.index, '\n\n')



# ---creating a new column called "mean_monthly_price"---
# with its value set to be the mean price for the products on each month, that is:
# 'price' = 'revenue' / 'volume'   ---> (on a monthly basis in this case, that is, in this table)
month_revenue['mean_monthly_price'] = month_revenue['revenue'] / month_revenue['volume']



# ---selecting the columns in the right order for the dataframe table display---
# notice that we don't select the index named 'month_starting'.
# since it's the index, it's as if it was already 'selected', and therefore it's displayed by default
# 'selecting' it as a column returns an error
month_revenue = month_revenue[['mean_monthly_price', 'volume', 'revenue']]



# ---exporting the dataframe into an html file, so that it can be seen on the browser---
month_revenue.to_html('month_revenue.html')

