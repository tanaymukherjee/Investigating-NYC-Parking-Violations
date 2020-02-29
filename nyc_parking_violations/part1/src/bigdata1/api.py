import os
import sys
import pandas as pd
import numpy as np
from sodapy import Socrata
import requests
import json


# Store the data id and domain corresponding to NYC parking violation API
domain = "data.cityofnewyork.us"
dataset_id = 'nc67-uf89'

# Call the api_token for open NYC data
app_key = os.environ.get("APP_TOKEN")

# Setting up the API call with the domain and app_token
client = Socrata(domain, app_key)

# Printing the domian and session details
print("Domain: {domain:}\nSession: {session:}\nURI Prefix: {uri_prefix:}".format(**client.__dict__))

# Set the timeout to 60 seconds    
client.timeout = 60

# First 1000 results, returned as JSON from API / converted to Python list of dictionaries by sodapy
results_filter = str(client.get(dataset_id, limit=1000))

# Convert to pandas DataFrame
df = pd.DataFrame.from_records(results_filter)
# First few records for sample
df.head()
# Save the data frame to a CSV file
# df.to_csv("NYC_PV_Sample.csv")

# Shows the total count of the rows in the API 
results_all = int(client.get(dataset_id, select='COUNT(*)')[0]['COUNT'])
print(results_all)


# Use meta_data to see the structure of the table we are trying to fetch
metadata = client.get_metadata(dataset_id)
[x['name'] for x in metadata['columns']]

# Define the function to call the output
def get_results(page_size, num_pages, output) -> dict:

    # Define the num_pages in case the default value is not passed
    if not num_pages:
        num_pages = results_all // page_size + 1

    # Putting the whole code inside a try-catch block to pick hints for code failures
    try:
        # Iterate through the records in the pages and then for reach record.
        for i in range(num_pages):

            # Print the record in the CLI
            records = client.get(dataset_id, limit=page_size, offset=i*page_size)
            print(records)

            # Print the records in an output file
            with open("output", "w") as file:
                for i in range(num_pages):
                    for j in records:
                        file.write(f"{j}\n")

    except HTTPError as e:
        print(f"Evaluate the loops again!: {e}")
        raise


# Utility methods for exception handling
def raise_for_status(response):

    # Custom raise_for_status with more appropriate error message.
    http_error_msg = ""

    if 400 <= response.status_code < 500:
        http_error_msg = "{0} Client Error: {1}".format(
            response.status_code, response.reason
        )

    elif 500 <= response.status_code < 600:
        http_error_msg = "{0} Server Error: {1}".format(
            response.status_code, response.reason
        )

    if http_error_msg:
        try:
            more_info = response.json().get("message")
        except ValueError:
            more_info = None
        if more_info and more_info.lower() != response.reason.lower():
            http_error_msg += ".\n\t{0}".format(more_info)
        raise requests.exceptions.HTTPError(http_error_msg, response=response)   
