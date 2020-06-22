# dl_cetesb

Python code to download CETESB data using python
CETESB qualar website is avalaible with credentials at [CETESB qualar website](https://cetesb.sp.gov.br/ar/qualar/)


This code has been inspired by:

https://www.curso-r.com/blog/2018-03-19-scraper-cetesb/

https://github.com/quishqa/qualR/blob/master/R/CetesbRetrieve.R

https://github.com/williamorim/Rpollution-blog

## library

You need 3 libraries to use this code: numpy, requests, and BeautifulSoup

## parameters
You need to fill these parameters
'myLOGIN = ' put your login for CETESB  example: myLOGIN = 'john@doe.com'
'myPASSWORD = ' put your password for CETESB
'date_start = ' example: date_start = '01/01/2015'
'date_end = ' example: date_start = '01/01/2016'
'code_station = ' example: code_station = '95' for Cid.Universitária-USP-Ipen
'code_variable = ' example: code_variable = '63' for Ozone

## measurements and stations
Two tables are provided two know by William Morin to find the station and variable (CETESB) codes:

https://github.com/williamorim/Rpollution-blog/blob/master/content/blog/data/param_ids.csv

https://github.com/williamorim/Rpollution-blog/blob/master/content/blog/data/station_ids.csv

## output
Two matrix with the 'date' and 'data' ready to be studied!

