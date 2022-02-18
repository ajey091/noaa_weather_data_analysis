import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_palette(sns.color_palette("Set2"))

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


cols = ['year','month','day','hour','temp','dew','sea_level',
        'wind_dir','wind_speed','sky_cond','prec_1','prec_6']

tokyo_data = pd.DataFrame(columns = cols)
bangalore_data = pd.DataFrame(columns = cols)
shanghai_data = pd.DataFrame(columns = cols)
paris_data = pd.DataFrame(columns = cols)
mexico_data = pd.DataFrame(columns = cols)
cairo_data = pd.DataFrame(columns = cols)
chicago_data = pd.DataFrame(columns = cols)
sf_data = pd.DataFrame(columns = cols)
miami_data = pd.DataFrame(columns = cols)
buenos_data = pd.DataFrame(columns = cols)


for city in locations:
    for year in range(2013,2018):
        os.environ['dir_name'] = str(year)
        os.chdir(os.environ['dir_name'])



        tokyo_data = pd.concat([tokyo_data,pd.read_csv(f'Tokyo_{year}',delim_whitespace=True, header=None, names=cols)])
        tokyo_data = tokyo_data[tokyo_data.temp != -9999]

        bangalore_data = pd.concat([bangalore_data,pd.read_csv(f'Bangalore_{year}',delim_whitespace=True, header=None, names=cols)])
        bangalore_data = bangalore_data[bangalore_data.temp != -9999]

        shanghai_data = pd.concat([shanghai_data,pd.read_csv(f'Shanghai_{year}',delim_whitespace=True, header=None, names=cols)])
        shanghai_data = shanghai_data[shanghai_data.temp != -9999]

        paris_data = pd.concat([paris_data,pd.read_csv(f'Paris_{year}',delim_whitespace=True, header=None, names=cols)])
        paris_data = paris_data[paris_data.temp != -9999]

        mexico_data = pd.concat([mexico_data,pd.read_csv(f'Mexico_City_{year}',delim_whitespace=True, header=None, names=cols)])
        mexico_data = mexico_data[mexico_data.temp != -9999]

        cairo_data = pd.concat([cairo_data,pd.read_csv(f'Cairo_{year}',delim_whitespace=True, header=None, names=cols)])
        cairo_data = cairo_data[cairo_data.temp != -9999]

        chicago_data = pd.concat([chicago_data,pd.read_csv(f'Chicago_{year}',delim_whitespace=True, header=None, names=cols)])
        chicago_data = chicago_data[chicago_data.temp != -9999]

        sf_data = pd.concat([sf_data,pd.read_csv(f'San_Francisco_{year}',delim_whitespace=True, header=None, names=cols)])
        sf_data = sf_data[sf_data.temp != -9999]

        miami_data = pd.concat([miami_data,pd.read_csv(f'Miami_{year}',delim_whitespace=True, header=None, names=cols)])
        miami_data = miami_data[miami_data.temp != -9999]

        buenos_data = pd.concat([buenos_data,pd.read_csv(f'Buenos_Aires_{year}',delim_whitespace=True, header=None, names=cols)])
        buenos_data = buenos_data[buenos_data.temp != -9999]

        os.chdir("..")


tokyo_data['date_time'] = pd.to_datetime(tokyo_data[['day','month','year']]) + pd.to_timedelta(tokyo_data.hour, unit='h')
bangalore_data['date_time'] = pd.to_datetime(bangalore_data[['day','month','year']]) + pd.to_timedelta(bangalore_data.hour, unit='h')
shanghai_data['date_time'] = pd.to_datetime(shanghai_data[['day','month','year']]) + pd.to_timedelta(shanghai_data.hour, unit='h')
paris_data['date_time'] = pd.to_datetime(paris_data[['day','month','year']]) + pd.to_timedelta(paris_data.hour, unit='h')
mexico_data['date_time'] = pd.to_datetime(mexico_data[['day','month','year']]) + pd.to_timedelta(mexico_data.hour, unit='h')
cairo_data['date_time'] = pd.to_datetime(cairo_data[['day','month','year']]) + pd.to_timedelta(cairo_data.hour, unit='h')
chicago_data['date_time'] = pd.to_datetime(chicago_data[['day','month','year']]) + pd.to_timedelta(chicago_data.hour, unit='h')
sf_data['date_time'] = pd.to_datetime(sf_data[['day','month','year']]) + pd.to_timedelta(sf_data.hour, unit='h')
miami_data['date_time'] = pd.to_datetime(miami_data[['day','month','year']]) + pd.to_timedelta(miami_data.hour, unit='h')
buenos_data['date_time'] = pd.to_datetime(buenos_data[['day','month','year']]) + pd.to_timedelta(buenos_data.hour, unit='h')


for year in range(2013,2014):
    plt.subplots(figsize=(10, 8))
    plt.plot(tokyo_data['date_time'], tokyo_data['temp']/10,'.',label='Tokyo',markersize=1)
    plt.plot(bangalore_data['date_time'], bangalore_data['temp']/10,'.',label='Bangalore',markersize=1)
    plt.plot(shanghai_data['date_time'], shanghai_data['temp']/10,'.',label='Shanghai',markersize=1)
    plt.plot(paris_data['date_time'], paris_data['temp']/10,'.',label='Paris',markersize=1)
    plt.plot(mexico_data['date_time'], mexico_data['temp']/10,'.',label='Mexico',markersize=1)
    plt.plot(cairo_data['date_time'], cairo_data['temp']/10,'.',label='Cairo',markersize=1)
    plt.plot(chicago_data['date_time'], chicago_data['temp']/10,'.',label='Chicago',markersize=1)
    plt.plot(sf_data['date_time'], sf_data['temp']/10,'.',label='San Francisco',markersize=1)
    plt.plot(miami_data['date_time'], miami_data['temp']/10,'.',label='Miami',markersize=1)
    plt.plot(buenos_data['date_time'], buenos_data['temp']/10,'.',label='Buenos Aires',markersize=1)

    plt.xlabel('Year')
    plt.ylabel('Air temperature (C)')
    plt.legend()
    plt.show()
