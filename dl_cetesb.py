import requests
from bs4 import BeautifulSoup
#############################################################################
url = 'https://qualar.cetesb.sp.gov.br/qualar/autenticador'
url2 = 'https://qualar.cetesb.sp.gov.br/qualar/exportaDados.do?method=pesquisar'

rlog = {'cetesb_login':LOGIN,'cetesb_password':PASSWORD}
rdata = {'irede':'A','dataInicialStr':'01/01/2015','dataFinalStr':'01/01/2016','iTipoDado':'P','estacaoVO.nestcaMonto':'95','parametroVO.nparmt':'63'} 

s = requests.session()
r = s.request('POST',url,data=rlog)
rr = s.request('POST',url2,data=rdata)
soup = BeautifulSoup(rr.content,'html.parser')

txt=[]
for td in soup.find_all('td'):
    txt = txt + [ td.text.strip() ]
    #print(txt)
    
n=0
for l in range(len(txt)):
    if txt[l] == 'Automático': n+=1
      
date_sta = np.zeros([n,3])
data_sta = np.zeros([n]);data_sta[:] = np.nan

n=0
for l in range(len(txt)):
    if txt[l] == 'Automático':
       da = txt[l+3].split('/')
       for i in range(3): date_sta[n,i]= np.float(da[i])
       cc = np.float(txt[l+9])
       data_sta[n]= cc     
       n+=1
       
