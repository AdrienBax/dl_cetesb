#############################################################################
# BEGIN parameters
#############################################################################
myLOGIN = '' # put your login for CETESB  example: myLOGIN = 'john@doe.com'
myPASSWORD = '' # put your password for CETESB
date_start = '' # example: date_start = '01/01/2015'
date_end = '' # example: date_start = '01/01/2016'
code_station = '' # example: code_station = '95' for Cid.Universitária-USP-Ipen
code_variable = '' # example: code_variable = '63' for Ozone
#############################################################################
# END parameters
#############################################################################
import requests
from bs4 import BeautifulSoup
import numpy as np

url = 'https://qualar.cetesb.sp.gov.br/qualar/autenticador'
url2 = 'https://qualar.cetesb.sp.gov.br/qualar/exportaDados.do?method=pesquisar'

rlog = {'cetesb_login':myLOGIN,\
        'cetesb_password':myPASSWORD}

rdata = {'irede':'A',\
         'dataInicialStr':date_start,\
         'dataFinalStr':date_end,\
         'iTipoDado':'P',\
         'estacaoVO.nestcaMonto':code_station,\
         'parametroVO.nparmt':code_variable} 

s = requests.session()
r = s.request('POST',url,data=rlog)
rr = s.request('POST',url2,data=rdata)
soup = BeautifulSoup(rr.content,'html.parser')

# load webpage text into vector using <td> html tag
txt=[]
for td in soup.find_all('td'):
    txt = txt + [ td.text.strip() ]
    #print(txt)

# find length data : n
n=0
for l in range(len(txt)): 
    if txt[l] == 'Automático': n+=1

# declaration matrix station datA and datE
date_sta = np.zeros([n,3])
data_sta = np.zeros([n]);data_sta[:] = np.nan

# data fill in
n=0
for l in range(len(txt)):
    if txt[l] == 'Automático':
       da = txt[l+3].split('/')
       for i in range(3): date_sta[n,i]= int(da[i])
       var = np.float(txt[l+9])
       data_sta[n] = np.float(txt[l+9])
       n+=1
       
