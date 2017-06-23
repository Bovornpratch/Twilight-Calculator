import ephem
import sys


Obs_Lat, Obs_Long = '18:47:25.08' , '98:58:54.11'  # Observatory latitude,longitude
elevation = 0


observer = ephem.Observer()
observer.lat,observer.lon, observer.elevation = Obs_Lat, Obs_Long ,elevation
