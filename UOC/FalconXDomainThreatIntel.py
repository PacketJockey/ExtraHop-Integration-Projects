#!/usr/bin/env python
import json
import requests
import pandas as pd



# Suppress SSL warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json',
          }
req_body = 'client_id=YOUR-KEY-HERE&client_secret=YOUR-SECRET-HERE'
endpoint = 'https://api.crowdstrike.com/oauth2/token'

r = requests.post(endpoint, req_body, headers=headers, verify=False)
at = r.json()["access_token"]
#at


# In[134]:


headers = {#'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json',
           'authorization': 'bearer ' + at #<---- Pass 'at' variable to be used as the bearer token       
          }
endpoint = "https://api.crowdstrike.com/intel/queries/indicators/v1?filter=type:'domain'"
r = requests.get(endpoint,headers=headers)
ioc = r.json()['resources']
#ioc
#ThreatType/TargetedCrimeware
#filter=labels:'IPAddressType/Sinkhole'"


# In[135]:


df = pd.DataFrame(ioc)
pd.set_option('display.max_rows', None)
df.rename( columns={0:'domain'}, inplace=True )
df
dom = df['domain']
s = pd.Series(dom)
fx_doms = s.str.rsplit(pat='_',n=1, expand=True)
fx_doms = fx_doms[1]
folder = '/app/notebooks/attack/start/threatintel/fxdoms.csv'
fx_doms.to_csv(folder, index = False)
#fx_doms


# In[136]:


get_ipython().system('ls -al threatintel/fxdoms.csv')


# In[137]:


myAPI = 'YOUR-API-KEY'


# In[138]:


## Upload Threat Intelligence Kit to Reveal(x) Sensor
get_ipython().system('threatintel/threatTK.py -o threatintel/ -tc FalconXDOMAINs --generate-stix --input-file threatintel/fxdoms.csv  --list-type domain --eda sensor.i.rx.tours $myAPI False')


# In[ ]:




