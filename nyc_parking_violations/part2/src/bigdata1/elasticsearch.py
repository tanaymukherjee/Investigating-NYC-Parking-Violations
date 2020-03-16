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

