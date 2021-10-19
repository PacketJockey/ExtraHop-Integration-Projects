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
#Enter your API Information below
req_body = 'client_id=YOUR-KEY-HERE&client_secret=Your-Secret-Here'
endpoint = 'https://api.crowdstrike.com/oauth2/token'

r = requests.post(endpoint, req_body, headers=headers, verify=False)
at = r.json()["access_token"]
#at


# In[6]:


headers = {#'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json',
           'authorization': 'bearer ' + at #<---- Pass 'at' variable to be used as the bearer token       
          }
endpoint = "https://api.crowdstrike.com/intel/queries/indicators/v1?filter=type:'ip_address'"
r = requests.get(endpoint,headers=headers)
ioc = r.json()['resources']
#ioc


# In[8]:


df = pd.DataFrame(ioc)
pd.set_option('display.max_rows', None)
df.rename( columns={0:'addr'}, inplace=True )
df
ip = df['addr']
s = pd.Series(ip)
fx_ips = s.str.rsplit(pat='_',n=2, expand=True)
fx_ips = fx_ips[2]
folder = '/app/notebooks/attack/start/threatintel/fxips.csv'
fx_ips.to_csv(folder, index = False)
#fx_ips


# In[9]:


get_ipython().system('ls -al threatintel/fxips.csv')


# In[10]:


myAPI = 'YOUR-API-KEY'


# In[11]:


## Upload Threat Intelligence Kit to Reveal(x) Sensor
get_ipython().system('threatintel/threatTK.py -o threatintel/ -tc FalconXIPs --generate-stix --input-file threatintel/fxips.csv  --list-type ip --eda sensor.i.rx.tours $myAPI False')


# In[ ]:




