import ephem
import sys
import datetime
import numpy


Date,time = str(sys.argv[1]) , str(sys.argv[2])  # Inputed date and time
Obs_Lat, Obs_Long =  str(sys.argv[3]),str(sys.argv[4]) # Observatory latitude,longitude
elevation = float(sys.argv[5])

#Example/test coordinate
'''
Now = '2017/06/23 5:00:00'
Obs_Lat, Obs_Long = '18:47:25.08' , '98:58:54.11'  # Observatory latitude,longitude
elevation = 0
'''

observer = ephem.Observer()
observer.lat,observer.lon, observer.elevation = Obs_Lat, Obs_Long ,elevation
observer.date = Date+' '+time


#print observer.date
#print observer.previous_rising(ephem.Sun())
print 'Sun set:' ,observer.previous_setting(ephem.Sun()) ,'UTC'
print 'Sun rise:',observer.next_rising(ephem.Sun()) , 'UTC'
#print observer.next_setting(ephem.Sun())
print '-----Evening Twilight-----'
observer.horizon = '-6'
print 'Evening Civ. Twilight:' ,observer.previous_setting(ephem.Sun(), use_center=True) ,'UTC'
observer.horizon = '-12'
print 'Evening Nau. Twilight:' ,observer.previous_setting(ephem.Sun(), use_center=True) ,'UTC'
observer.horizon = '-18'
print 'Evening Ast. Twilight:' ,observer.previous_setting(ephem.Sun(), use_center=True) ,'UTC'

print '-----Morning Twilight-----'
observer.horizon = '-18'
print 'Evening Ast. Twilight:' ,observer.next_rising(ephem.Sun(), use_center=True) ,'UTC'
observer.horizon = '-12'
print 'Evening Nau. Twilight:' ,observer.next_rising(ephem.Sun(), use_center=True) ,'UTC'
observer.horizon = '-6'
print 'Evening Civ. Twilight:' ,observer.next_rising(ephem.Sun(), use_center=True) ,'UTC'
