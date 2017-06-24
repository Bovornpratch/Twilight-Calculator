# Twilight-Calculator


This is a python wrapper to calculate the twilight time of an observer at a given position on Earth at a certain time. The script relies on calculations from pyephem to perform the calculations (special thanks to the pyephem team). It is designed to be a used as a quick reference used to plan observations. 

Dependencies include  pyephem numpy and datetime which can be obtain using
	
	pip install ephem numpy datetime
	
(although datetime is usually shiped with most python distributions)

The scipt input includes
	
	The observation date: YYYY/MM/DD or YYYY-MM-DD format
	The observer timezone: -4 (EST) , +7 (Bangkok, Chiang mai) .....
	The observing latitude: Deg:Min:sec format
	The observing longitude: Deg:Min:sec format
	The observing elevation: int/float number
	
	Example input: python Twilight_cal.py 2017/06/23 7 18:47:25.08  98:58:54.11 0


