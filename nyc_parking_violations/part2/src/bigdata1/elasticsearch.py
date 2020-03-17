import os
import sys
import pandas as pd
import numpy as np
from sodapy import Socrata
import requests
import json
from datetime import datetime
from elasticsearch import Elasticsearch
from time import sleep

# Creating an index and adding documents
def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass
    return es

# Commented part to show how to delete a document for future reference
# def delete_index(index_name, doc_type, id):
#    res = es.delete(index=index_name, doc_type=doc_type, id=doc_id)
#    print(res)

# Formatting data from the API
def data_formatting(ref):
    for key, value in ref.items():
        if 'amount' in key:
            ref[key] = float(value)
        elif 'number' in key:
            item[key] = int(value)            
        elif 'date' in key:
            ref[key] = datetime.strptime(ref[key], '%m/%d/%Y').date()

# Update the document and defining the call output for body reference
def call_ref(ref, es, index):
    data_formatting(ref)
    id=ref['summons_number']
    output = es.index(index=index, body=ref, id=id)
    print(output['result'], 'Summons_# %s' % id)
