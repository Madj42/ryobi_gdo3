import requests
username = ''
password = ''
uandp = {'username':username,'password':password}
r = requests.post('https://tti.tiwiconnect.com/api/login',data=uandp)

s = requests.get('https://tti.tiwiconnect.com/api/devices',params=uandp)
s_dict= s.json()
s_dict= (s_dict['result'])
doorval= str(s_dict)
doorval= doorval.split(',')
print(doorval[1])