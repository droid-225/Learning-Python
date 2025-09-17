import time

#print(time.ctime(10000000)) # epoch is the date and time from which a computer measures system time
# ctime() converts time in seconds since the epoch to a readable string

#print(time.time()) # returns current seconds since epoch

#print(time.ctime(time.time())) # returns current date and time in a readable format

#time_object = time.localtime() # creates time object, also called a struct time object
#utc_time_object = time.gmtime() # returns the utc time object
#print(time_object)
#local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# string format time (strftime()) method formats time objects based on given format
# (see python docs for directives) and returns it as a string
#print(local_time)

#time_string = "20 April, 2020"
#time_object = time.strptime(time_string, "%d %B, %Y")
# converts a time string into a time object based on specified format of the time string

#print(time_object)

# .asctime() accepts the following 9 fields:
# year, month, day, hours, minutes, secs, #day of the week, #day of the year, daylight savings time boolean
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, -1)
time_string = time.asctime(time_tuple) # converts time tuple or time object into a time string
print(time_string)

# .mkctime() also accepts the following 9 fields:
# year, month, day, hours, minutes, secs, #day of the week, #day of the year, daylight savings time boolean
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, -1)
time_number = time.mktime(time_tuple) # converts time tuple or time object into seconds since epoch
print(time_number)