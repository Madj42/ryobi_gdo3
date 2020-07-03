# ryobi_gdo2

To get your door id, download and run the doorid.py file using Python.  Make sure to edit the username and password variables in the script beforehand.  You'll also need to install the requests module using pip.

##Configuration.yaml example:

cover:
  - platform: ryobi_gdo2
    username: !secret ryobi_username
    password: !secret ryobi_password
    device_id:
      - !secret ryobi_device_id
      
light:
  - platform: ryobi_gdo2
    username: !secret ryobi_username
    password: !secret ryobi_password
    device_id:
      - !secret ryobi_device_id
	  
##Secrets.yaml example:

ryobi_username: "captain@morgan.com"
ryobi_password: "Bottle0fRum!"
ryobi_device_id: "51324637f136474"
