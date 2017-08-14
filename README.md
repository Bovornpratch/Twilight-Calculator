# Twilight-Calculator


This is a python wrapper to calculate sunrise, sunset twilight time for an observer at a given position on Earth at a certain time. The script relies on calculations from pyephem to perform the calculations (special thanks to the pyephem team). It is designed to be a used as a quick reference used to plan observations. 

Dependencies include  pyephem numpy and datetime which can be obtain using
	
	pip install ephem numpy datetime
	
(although datetime is usually shiped with most python distributions)

The scipt input includes
	
	The observation date: YYYY/MM/DD or YYYY-MM-DD format
	The observer time: Observer time ib UTC , hh:mm:ss format
	The observing latitude: Deg:Min:sec format
	The observing longitude: Deg:Min:sec format
	The observing elevation: int/float number
	
	Example input: python Twilight_cal.py 2017/06/23 7 18:47:25.08  98:58:54.11 0


Since the script is designed to aid in planning observations, we assume set the time to ~midnight of that date (23:59:00 to be precise).
Hence, the 'sunrise' is the sunrise of the next day or the 'end' of that night's observation and 'sunset' is the sunset of that date in other words the 'start' of that observing night.

In addition, the wrapper also gives out each twilight time. This includes the civil twilight (alt=-6), nautical twilight (alt=-12) and the astronomical twilight (alt=-18) for both evening and morning twilights. One must keep in mind that the reported time by the script it the 'END' of the twilight. In other words, it is when the sun obtains that certain altitude. 

So, the evening twilight time would be the following

	Sunset to Sun altitude = -6  = 'Civil Twilight'
	Sun altitude = -6 to Sun altitude = -12  = 'nautical Twilight'
	Sun altitude = -12 to Sun altitude = -18 = 'Astronomical Twilight'
	
while the morning twilight time would range in the opposite.


	Sun altitude = -6 to Sun rise = 'Civil Twilight'
	Sun altitude = -12 to Sun altitude = -6  = 'nautical Twilight'
	Sun altitude = -18 to Sun altitude = -12 = 'Astronomical Twilight'
	
The observing night usually starts after the astronomical twilight has ended (Alt > -18) and ends when we start the morning astronomical twilight (Alt > -18)

More about twilights can be found at https://www.timeanddate.com/astronomy/different-types-twilight.html



