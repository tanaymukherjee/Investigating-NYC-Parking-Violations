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

def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    return es

def data_formatting(ref):
    for key, value in ref.items():
        if 'amount' in key:
            ref[key] = float(value)
        elif 'number' in key:
            item[key] = int(value)            
        elif 'date' in key:
            ref[key] = datetime.strptime(ref[key], '%m/%d/%Y').date()

def call_ref(ref, es, index):
    data_formatting(ref)
    res = es.index(index=index, body=ref, id=ref['summons_number'])