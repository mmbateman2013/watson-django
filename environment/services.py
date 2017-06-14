import sys
import os
import json
from watson_developer_cloud import DiscoveryV1
# from .models import Environment, Collection


WATSON_UN = "dba214e1-bf76-46b7-8d6e-8c5c1aa6b24c"
WATSON_PW = "e5xMPekLUhaN"
WATSON_ENV = "7d2097c0-c1b8-43e7-9311-c555f72d1c4a"
WATSON_COLLECT = ["775d2098-9b2d-4e67-9d95-324e85592815",]
query = "What measures should be taken to reduce risk of fire in oxygen compressors?"

def query_environ(query_text,environ_id_string, collect_ids):
    discovery = DiscoveryV1(
        username=WATSON_UN,
        password=WATSON_PW,
        version="2016-12-01"
    )
    results = []
    for collection in collect_ids:
        qopts = {'query': query_text}
        my_query = discovery.query(environ_id_string, collection, qopts)
        results.append(json.dumps(my_query))
    return results
    
# print query_environ(query,WATSON_ENV,WATSON_COLLECT)
