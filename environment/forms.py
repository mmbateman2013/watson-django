import sys
import os
import json
from django import forms
from models import Collection
from watson_developer_cloud import DiscoveryV1

WATSON_UN = "dba214e1-bf76-46b7-8d6e-8c5c1aa6b24c"
WATSON_PW = "e5xMPekLUhaN"
WATSON_ENV = "7d2097c0-c1b8-43e7-9311-c555f72d1c4a"

class QueryForm(forms.Form):
    queryText = forms.CharField(max_length=1000, required=True)
    collection = forms.ModelChoiceField(queryset=Collection.objects.all().order_by('collectionName'), required=False)
    
    def query_environ(self):
        discovery = DiscoveryV1(
            username=WATSON_UN,
            password=WATSON_PW,
            version="2016-12-01"
        )
        qopts = {'query': self.queryText}
        my_query = discovery.query(WATSON_ENV, self.collection, qopts)
        return json.dumps(my_query)