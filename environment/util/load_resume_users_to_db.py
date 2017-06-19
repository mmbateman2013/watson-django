import os
import requests
import datetime
import time
import sys
import os
import json
import decimal

from os import path

from environment.models import Google_Contact

loadPath = "environment/util/upload"

#read in raw files and create files for each entry in raw file
onlyfiles = [f for f in os.listdir(loadPath) if path.isfile(path.join(loadPath, f))]
print len(onlyfiles)

for fn in onlyfiles:
    #write out name
    print "Reading "+ fn
  
    #get filehandle
    with open(path.join(loadPath, fn),'r') as fileinfo:
        json_data = fileinfo.read()
    
    json_array = json.loads(json_data)
  
    for entry in json_array:
        employee_name = entry["Name"]
        resource_name = employee_name.replace(' ','')
        print(resource_name)
        #lookup contact in address book
        gc_set = Google_Contact.objects.filter(contact_resource_name=resource_name)
        if len(gc_set) == 0:
            print 'Trying to save'
            gc = Google_Contact(contact_resource_name=resource_name, contact_name=employee_name)
            gc.contact_email = employee_name.replace(' ', '.') + '@airliquide.com'
            gc.contact_phone_no = '(832) 555-1212'
            gc.save()
    
  
    #Delete the file
    os.remove(path.join(loadPath, fn))
    print "Deleted file "+fn
print "Finished processing files. :)"