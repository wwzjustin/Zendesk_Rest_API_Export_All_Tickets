import requests
import json
import csv
import urllib
import pandas 


## ------Set the request parameters------
#group_url = 'https://[organization].zendesk.com/api/v2/groups.json'
#user = '[your email]'+'/token'
#pwd = '[token]'

## -----Do the HTTP get request-----
#group = requests.get(group_url, auth=(user, pwd))
#data = group.json()


## --------Example 1: Print the name of the first group in the list
##print( 'First group = ', data['groups'][0]['name'] )

##---------- Example 2: Print the name of each group in the list
##group_list = data['groups']
##for group in group_list:
   ## print(group['name'])data
    

######-----------------------------------------------------------------------------


# Get Data

params = {
    'query': 'type:ticket status:open',
    'sort_by': 'created_at',
    'sort_order': 'desc'        # from oldest to newest
}

get_tickets_url= 'https://[organization].zendesk.com/api/v2/search.json?' + urllib.urlencode(params)

get_org_url= 'https://[organization].zendesk.com/api/v2/organizations.json'

user = '[your email]'+'/token'
pwd = '[token]'
headers = {'Accept':'application/json'}



#output = json.loads('{}')
fields = ['via','created_at', 'updated_at', 'id','type','has_incidents','result_type','subject','priority','status','organization_id','ticket_form_id','due_at','custom_fields','fields','description']
output =pandas.DataFrame()
org = pandas.DataFrame()



while get_tickets_url:
    get_tickets= requests.get(get_tickets_url, auth=(user,pwd), headers=headers)
    data = get_tickets.json()
    #merged_dict = {key: value for (key, value) in (dictA.items() + dictB.items())}
    zen = pandas.DataFrame(data['results'])
    
    output=pandas.concat([output,zen])
    get_tickets_url = data['next_page']
 
 
while get_org_url:
    get_org= requests.get(get_org_url, auth=(user,pwd), headers=headers)
    data = get_org.json()
    zen = pandas.DataFrame(data['organizations'])
    org=pandas.concat([org,zen])
    get_org_url = data['next_page']




#with open('test.txt', 'w') as outfile:
#json.dump(data, outfile)

dir=r'~/Dropbox/tickets.csv'   # write the dataframe to csv file
output.to_csv(dir,sep=",",encoding='utf-8')



dir=r'~/Dropbox/Zendesk_organizations.csv'
org.to_csv(dir,sep=",",encoding='utf-8')

##-----------------------------------Using Zenpy package------------------------------------------------





#  Zenpy API

#creds = {
 #   'email' : '[your email]',
  #  'token' : '[token]',
   # 'subdomain': '[organization]'}

#import zenpy

#import datetime

#zenpy = zenpy.Zenpy(**creds)

###yesterday = datetime.datetime.now() - datetime.timedelta(days=5)
##today = datetime.datetime.now()

##for ticket in zenpy.search(" ", created_between=[yesterday, today], type='ticket'):
  #  print ticket, organization
