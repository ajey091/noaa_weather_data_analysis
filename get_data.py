# We will choose 10 cities and get data for 10 years for the 10 cities.
# The 10 chosen cities are the following:
#             'Tokyo':'476620-99999',
#              'Bangalore':'427056-99999',
#              'Shanghai':'583620-99999',
#              'Paris':'071570-99999',
#              'Mexico_City':'766800-99999',
#              'Cairo':'623660-99999',
#              'Chicago':'725300-94846',
#              'San_Francisco':'724940-23234',
#              'Melbourne':'722040-12838',
#              'Buenos_Aires':'875850-99999'
#
# We get the data from 2013-2017 for these cities.
#
#
#

import subprocess
import os

locations = {'Tokyo':'476620-99999',
             'Bangalore':'427056-99999',
             'Shanghai':'583620-99999',
             'Paris':'071570-99999',
             'Mexico_City':'766800-99999',
             'Cairo':'623660-99999',
             'Chicago':'725300-94846',
             'San_Francisco':'724940-23234',
             'Miami':'722040-12838',
             'Buenos_Aires':'875850-99999'}


for year in range(2013,2018):
    subprocess.run(["mkdir", str(year)])
    os.environ['dir_name'] = str(year)
    os.chdir(os.environ['dir_name'])
    for city in locations:
        url = f'ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/{year}/{locations[city]}-{year}.gz'
        file_name = f'{city}_{year}.gz'
        print (url)
        subprocess.run(["curl", "-0", url, "--output", file_name])
        subprocess.run(["gunzip", file_name])
    os.chdir("..")
