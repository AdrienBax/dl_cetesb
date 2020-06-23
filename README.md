# dl_cetesb

This Python code downloads CETESB data from the CETESB qualar website, with credentials at the CETESB qualar website.

CETESB qualar website is avalaible with your credentials at [CETESB qualar website](https://cetesb.sp.gov.br/ar/qualar/)


This code has been inspired by:

https://www.curso-r.com/blog/2018-03-19-scraper-cetesb/

https://github.com/williamorim/Rpollution-blog

https://github.com/quishqa/qualR/blob/master/R/CetesbRetrieve.R


## library

You need 3 Python libraries to use this code: numpy, requests, and BeautifulSoup

## parameters
You need to fill these parameters
'myLOGIN = ' put your login for CETESB  example: myLOGIN = 'john@doe.com'
'myPASSWORD = ' put your password for CETESB
'date_start = ' example: date_start = '01/01/2015'
'date_end = ' example: date_start = '01/01/2016'
'code_station = ' example: code_station = '95' for Cid.Universitária-USP-Ipen
'code_variable = ' example: code_variable = '63' code for Ozone

## measurements and stations

William Morin provides two tables to associate the ID numbers used in the CETESB database with station names and variable names.

https://github.com/williamorim/Rpollution-blog/blob/master/content/blog/data/param_ids.csv

https://github.com/williamorim/Rpollution-blog/blob/master/content/blog/data/station_ids.csv


## output
Two matrices, one with the 'date' and one with the 'data', ready to be studied!

