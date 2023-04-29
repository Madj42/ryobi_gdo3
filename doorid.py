import requests
username = ''
password = ''
uandp = {'username':username,'password':password}
r = requests.post('https://tti.tiwiconnect.com/api/login',data=uandp)

s = requests.get('https://tti.tiwiconnect.com/api/devices',params=uandp)

for result in s.json()['result']:
  if 'gdoMasterUnit' in result['deviceTypeIds']:
    print(result['metaData']['name'], '- Device ID:',  result['varName'])