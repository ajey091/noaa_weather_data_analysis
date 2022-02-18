# NOAA Weather Data Analysis

Here, we are downloading and analyzing some data from the NOAA dataset - https://www.ncdc.noaa.gov/cdo-web/. This dataset is available via an FTP connection - ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/. Specifically, these can be downloaded using the following `curl` commands:

`curl -0 ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/{year}/{locations_ID}-{year}.gz`

For instance, for Tokyo and year 2015, the following command should be used:

`curl -0 ftp://ftp.ncdc.noaa.gov/pub/data/noaa/isd-lite/2015/476620-99999-2015.gz`

