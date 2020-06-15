# NYC Parking Violations
```
For this project, we will analyze millions of NYC Parking violations since January 2016.
```

## Part 1: Python Scripting
```
In the first part, we simply want to develop a python command line interface that can connect to the OPCV API and demonstrate that the data is accessible via python.
```

### A) File Structure
![Tree](https://user-images.githubusercontent.com/6689256/75619232-76abd600-5b47-11ea-842e-f60372c5fd0f.PNG)

### B) Associated Files

#### 1. Python Scripting Files:
* ```main.py```
``` 
It parses the arguments --page_size, --num_pages, --output into the api.py file for function call.
The code can be found in this repository under nyc_parking_violations
```

* ```api.py```
``` 
It has all the functions and error handling code to implement the exercise. 
The APP Token, domain, etc are also defined here alongside necessary packages.
The code can be found in this repository under nyc_parking_violations > src > bigdata 1
```

#### 2. Supplementary Files:
* ```Docker File```
``` 
It is a text document that contains all commands a user could call on the command line to assemble an image.
It is located in the root directory of our project.
```

* ```Requirements.txt```
``` 
This file is used for specifying what python packages are required to run the project you are looking at.
It is located in the root directory of our project.
```

#### 3. Output:
* ```NYC_PV_Sample.csv```
``` 
It is a simple .csv file to record first 1000 records to see how the info is rendered from the API.
This result is populated based on the method called through the results_filter command.
```

* ```results.json```
``` 
This is our main output which shows the json output we have called from the API.
It will store as many rows we pass as part of our arguments - num_pages and pages_size.
It is located in the root directory of our project.
```

### C) Commands

#### 1. Docker Build:
* ```Docker build```
``` 
docker build -t bigdata1:2.0 .
```
* ```Docker run on /bin/bash```
```
docker run -v "$(pwd):/app" -e APP_TOKEN=<api_token> -it bigdata1:2.0 /bin/bash
```
* ```Docker mount with arguments```
```
docker run -v "$(pwd):/app" -e APP_TOKEN=<api_token> -it bigdata1:2.0 python -m main --page_size=3 --num_pages=2 --output=results.json
```

#### 2. Deploying via Docker Hub:
* ```Connection to docker hub```
``` 
docker login --username=tanaydocker
Password: <put your docker login password>
```
* ```Build image inside docker hub```
```
docker build -t bigdata1:2.0 .
```
* ```Load the docker image```
```
docker images | grep bigdata1
```
* ```Tag the docker image```
```
docker tag <UUID image> tanaydocker/bigdata1:2.0
```
* ```Push the image on the docker hub```
```
docker push tanaydocker/bigdata1
```
* ```Link to the docker hub```
```
https://hub.docker.com/repository/docker/tanaydocker/bigdata1
```

#### 3. SSH into AWS EC2:
* ```Set permissions for the .pem file```
``` 
chmod 0400 <file_name>.pem
```
* ```Launch EC2 instance```
```
ssh -i <file_name>.pem ubuntu@<ip_address>
```

#### 4. Execute docker modules inside EC2:
* ```Install docker```
``` 
sudo apt install docker.io
```
* ```Login  to docker from EC2```
```
sudo docker login --username=tanaydocker
```
* ```Pull the instance```
```
sudo docker pull tanaydocker/bigdata1:2.0
```
* ```Set the APP_TOKEN```
```
export APP_TOKEN=<Your api_token>
```
* ```Docker run on /bin/bash```
```
sudo docker run -v ${PWD}:/app/out -e APP_TOKEN=${APP_TOKEN}  -it tanaydocker/bigdata1:2.0 python -m main --page_size=2 --num_pages=5
```
* ```Docker mount with arguments```
```
sudo docker run -v ${PWD}:/app/out -e APP_TOKEN=${APP_TOKEN}  -it tanaydocker/bigdata1:2.0 python -m main --page_size=2 --num_pages=5 --output=./out/results.json
```

#### 5. Verify results:
* ```Total Rows```
```
results_all = int(client.get(dataset_id, select='COUNT(*)')[0]['COUNT'])
48782608
```
* ```Print the metadata to see the API structure```
```
metadata = client.get_metadata(dataset_id)
[x['name'] for x in metadata['columns']]

['Plate',
 'State',
 'License Type',
 'Summons Number',
 'Issue Date',
 'Violation Time',
 'Violation',
 'Judgment Entry Date',
 'Fine Amount',
 'Penalty Amount',
 'Interest Amount',
 'Reduction Amount',
 'Payment Amount',
 'Amount Due',
 'Precinct',
 'County',
 'Issuing Agency',
 'Violation Status',
 'Summons Image']
```
* ```Check content```
```
cat results.json | wc -l  && cat results.json
```
* ```Display the output```
```
16
<NOTE: 6 from the the initial commit and 10 from the latest request which got appended to the older records>

{"plate": "FRN1379", "state": "NY", "license_type": "PAS", "summons_number": "8536112864", "issue_date": "04/25/2017", "violation_time": "12:07P", "violation": "NO PARKING-STREET CLEANING", "judgment_entry_date": "08/10/2017", "fine_amount": "45", "penalty_amount": "60", "interest_amount": "0.33", "reduction_amount": "0.1", "payment_amount": "105.23", "amount_due": "0", "precinct": "090", "county": "K", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSVmVrNXFSWGhOYW1jeVRrRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "HJX2831", "state": "NY", "license_type": "PAS", "summons_number": "8499659664", "issue_date": "09/06/2017", "violation_time": "05:39P", "violation": "NO PARKING-DAY/TIME LIMITS", "fine_amount": "65", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "65", "amount_due": "0", "precinct": "013", "county": "NY", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSUk5VOVVXVEZQVkZreVRrRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "GFE3007", "state": "NY", "license_type": "PAS", "summons_number": "8599806622", "issue_date": "10/06/2017", "violation_time": "09:10A", "violation": "NO STANDING-DAY/TIME LIMITS", "fine_amount": "115", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "115", "amount_due": "0", "precinct": "020", "county": "NY", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSVk5VOVVaM2RPYWxsNVRXYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "3H17B", "state": "NY", "license_type": "OMT", "summons_number": "7298277870", "issue_date": "12/16/2015", "violation_time": "08:37A", "violation": "NO STANDING-TAXI STAND", "fine_amount": "115", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "115", "payment_amount": "0", "amount_due": "0", "precinct": "018", "county": "NY", "issuing_agency": "TRAFFIC", "violation_status": "HEARING HELD-NOT GUILTY", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VG5wSk5VOUVTVE5PZW1jelRVRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "AL69588", "state": "CT", "license_type": "PAS", "summons_number": "4649015182", "issue_date": "10/19/2018", "violation_time": "07:09A", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "25", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "75", "amount_due": "0", "precinct": "000", "county": "BX", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1FOVVRWGhPVkVVMFRXYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "GNH3608", "state": "NY", "license_type": "PAS", "summons_number": "8556124628", "issue_date": "10/08/2018", "violation_time": "08:31A", "violation": "FAIL TO DSPLY MUNI METER RECPT", "fine_amount": "35", "penalty_amount": "10", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "45", "amount_due": "0", "precinct": "108", "county": "Q", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSVk1VNXFSWGxPUkZsNVQwRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "E66FRD", "state": "NJ", "license_type": "PAS", "summons_number": "8510916299", "issue_date": "04/15/2017", "violation_time": "11:50A", "violation": "NO PARKING-DAY/TIME LIMITS", "fine_amount": "65", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "65", "amount_due": "0", "precinct": "019", "county": "NY", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSVmVFMUVhM2hPYWtrMVQxRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "FJS2611", "state": "NY", "license_type": "PAS", "summons_number": "8510959470", "issue_date": "04/14/2017", "violation_time": "10:53A", "violation": "REG. STICKER-EXPIRED/MISSING", "fine_amount": "65", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "65", "payment_amount": "0", "amount_due": "0", "precinct": "024", "county": "NY", "issuing_agency": "TRAFFIC", "violation_status": "HEARING HELD-NOT GUILTY", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSVmVFMUVhekZQVkZFelRVRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "HSS4770", "state": "NY", "license_type": "PAS", "summons_number": "8698874058", "issue_date": "01/16/2019", "violation_time": "07:54P", "violation": "EXPIRED MUNI METER", "fine_amount": "35", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "35", "amount_due": "0", "precinct": "109", "county": "Q", "issuing_agency": "TRAFFIC", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSWk5VOUVaek5PUkVFeFQwRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "K86KLS", "state": "NJ", "license_type": "PAS", "summons_number": "4652385468", "issue_date": "01/16/2019", "violation_time": "11:42A", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "BK", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWk1VMXFUVFJPVkZFeVQwRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "DPC9000", "state": "NY", "license_type": "PAS", "summons_number": "5094819537", "issue_date": "12/23/2016", "violation_time": "04:40P", "violation": "FAILURE TO STOP AT RED LIGHT", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "QN", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGxSQk5VNUVaM2hQVkZWNlRuYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "CLW5371", "state": "NY", "license_type": "PAS", "summons_number": "4620968547", "issue_date": "06/06/2016", "violation_time": "09:47A", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "QN", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWmVVMUVhekpQUkZVd1RuYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "T698617C", "state": "NY", "license_type": "OMT", "summons_number": "4620354417", "issue_date": "05/23/2016", "violation_time": "03:39P", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "BK", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWmVVMUVUVEZPUkZGNFRuYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "BPJ8770", "state": "NY", "license_type": "PAS", "summons_number": "4620354533", "issue_date": "05/23/2016", "violation_time": "03:41P", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "BK", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWmVVMUVUVEZPUkZWNlRYYzlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "GTB1802", "state": "NY", "license_type": "PAS", "summons_number": "4620354521", "issue_date": "05/23/2016", "violation_time": "03:41P", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "QN", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWmVVMUVUVEZPUkZWNVRWRTlQUT09&locationName=_____________________", "description": "View Summons"}}
{"plate": "GTW7446", "state": "NY", "license_type": "PAS", "summons_number": "4620980146", "issue_date": "06/06/2016", "violation_time": "11:17A", "violation": "PHTO SCHOOL ZN SPEED VIOLATION", "fine_amount": "50", "penalty_amount": "0", "interest_amount": "0", "reduction_amount": "0", "payment_amount": "50", "amount_due": "0", "precinct": "000", "county": "QN", "issuing_agency": "DEPARTMENT OF TRANSPORTATION", "summons_image": {"url": "http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VGtSWmVVMUVhelJOUkVVd1RtYzlQUT09&locationName=_____________________", "description": "View Summons"}}
```

- [x] This module is completed


## Part 2: Loading into ElasticSearch
```
In this second part, we want to leverage docker-compose to bring up a service that encapsulates our bigdata1 container and an  elasticsearch container and ensures that they are able to interact. 
```

### A) File Structure
![Tree_2](https://user-images.githubusercontent.com/6689256/76740778-ccd26900-6744-11ea-9f44-38f961639f1c.PNG)

### B) Associated Files

#### 1. Python Scripting Files:
* ```main.py```
``` 
It parses the arguments --page_size, --num_pages, --output -- elastic_search into the api.py file for function call.
The code can be found in this repository under nyc_parking_violations
```

* ```api.py```
``` 
It has all the functions and error handling code to implement the exercise. 
The APP Token, domain, etc are also defined here alongside necessary packages.
The code can be found in this repository under nyc_parking_violations > src > bigdata 1
```

* ```elasticsearch.py```
``` 
It has all the functions to create the necessary instance for elastic search module. 
The data formatting related tasks are also accomplished here.
The code can be found in this repository under nyc_parking_violations > src > bigdata 1
```

#### 2. Supplementary Files:
* ```Docker File```
``` 
Same content as part 1.
```

* ```Requirements.txt```
``` 
Only update from part 1 here is an additional exercise to install elasticsearch.
```

* ```docker-compose.yml```
``` 
Docker-compose is a tool for defining and running multi-container Docker applications. With Compose, we use a YAML/YML file to configure our application's services.

NOTE: Remember, docker-compose. yml files are used for defining and running multi-container Docker applications, whereas Dockerfiles are simple text files that contain the commands to assemble an image that will be used to deploy containers.
```

#### 3. Output:
* ```results.json```
``` 
This is our main output which shows the json output we have called from the API.
It will store as many rows we pass as part of our arguments - num_pages and pages_size.
It is located in the root directory of our project.
This is a sample to the 1 million records we will try to push into elastic search later.
```

### C) Commands

#### 1. Setting up docker:
* ```Clean all the previous images```
``` 
docker system prune -a
```
* ```Allocate memory to docker for uploading large volume of data in Kibana```
```
docker-machine rm default
docker-machine create -d virtualbox --virtualbox-cpu-count=2 --virtualbox-memory=4096 --virtualbox-disk-size=50000 default
docker-machine stop
exit
```
* ```Set up the necessary JVM heap memory for the Elastic Search```
```
docker-machine ssh
sudo sysctl -w vm.max_map_count=262144
exit
```
```
NOTE: This step is optional for people who have issues with elastic search image dying within seconds of initiating docker-compose build.
```
* ```Get IP address of the docker```
```
docker inspect -f "{{ .NetworkSettings.IPAddress }}" <containerNameOrId>
```

#### 2. Docker-Compose Build:
* ```Build the Pyth, Elastic Search and Kibana instances```
``` 
docker-compose build pyth
```
* ```Launch the above services in detach mode```
```
docker-compose up -d
```
* ```Check if the services are up and ruuning?```
```
docker ps -a
```
* ```Check logs to see if Elastic Search is ready via localhost/docker's IP address```
```
docker-compose logs elasticsearch
```
```
NOTE: It takes the system good 2-4 minutes to get the services running. We can continue to monitor the log and see if that has
any error. If all goes fine, in some time the logs will show - services being initiated and then display the running status.
```
* ```Check logs to see if Kibana is ready via localhost/docker's IP address```
```
docker-compose logs kibana
```
```
NOTE: It takes the system good 2-4 minutes to get the services running. We can continue to monitor the log and see if that has
any error. If all goes fine, in some time the logs will show - kibana up and is connected to the elastic search instance.
```
* ```To kill the services```
```
docker-compose down
```

#### 3. Verify the build and successful logins into Elastic Search:
* ```Verifying the build status```
``` 
docker-compose run pyth bash
```
* ```Verfiy Elastic search via curl```
``` 
curl <docker's ip>:9200
```
* ```Verfiy Elastic search via broswer```
``` 
Go to: http://<docker's ip>:9200/
```
* ```Result from Elastic Search Instance on successful ping at the server```
``` 
{
  "name" : "qRCd9Tu",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "ZVOIVq7WQhqQ6ckxbjX-Lw",
  "version" : {
    "number" : "6.3.2",
    "build_flavor" : "default",
    "build_type" : "tar",
    "build_hash" : "053779d",
    "build_date" : "2018-07-20T05:20:23.451332Z",
    "build_snapshot" : false,
    "lucene_version" : "7.3.1",
    "minimum_wire_compatibility_version" : "5.6.0",
    "minimum_index_compatibility_version" : "5.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

#### 4. Push into Elastic Search
* ```Run the service```
``` 
docker-compose run -e APP_TOKEN=<api_token> pyth python main.py --page_size=5 --num_pages=10 --output=results.json --elastic_search=True
```
* ```Load the data using curl```
``` 
curl -o output.txt http://<docker's ip>:9200/bigdata1/_search?q=state:NY&size=5 
```
* ```Output via curl```
``` 
{"took":101,"timed_out":false,"_shards":{"total":5,"successful":5,"skipped":0,"failed":0},"hits":{"total":6,"max_score":0.6931472,"hits":[{"_index":"bigdata1","_type":"_doc","_id":"8349526865","_score":0.6931472,"_source":{"plate":"GWH9469","state":"NY","license_type":"PAS","summons_number":8349526865,"issue_date":"2016-09-13","violation_time":"10:02A","violation":"INSP. STICKER-EXPIRED/MISSING","judgment_entry_date":"2016-12-29","fine_amount":65.0,"penalty_amount":60.0,"interest_amount":8.91,"reduction_amount":2.61,"payment_amount":131.3,"amount_due":0.0,"precinct":"032","county":"NY","issuing_agency":"TRAFFIC","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSTk1FOVVWWGxPYW1jeVRsRTlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8487142308","_score":0.6931472,"_source":{"plate":"42274JZ","state":"NY","license_type":"COM","summons_number":8487142308,"issue_date":"2017-04-11","violation_time":"02:35P","violation":"FAIL TO DSPLY MUNI METER RECPT","fine_amount":35.0,"penalty_amount":0.0,"interest_amount":0.0,"reduction_amount":15.0,"payment_amount":20.0,"amount_due":0.0,"precinct":"108","county":"Q","issuing_agency":"TRAFFIC","violation_status":"HEARING HELD-GUILTY REDUCTION","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSUk5FNTZSVEJOYWsxM1QwRTlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8612879700","_score":0.35667494,"_source":{"plate":"HRZ6089","state":"NY","license_type":"PAS","summons_number":8612879700,"issue_date":"2018-05-09","violation_time":"09:44A","violation":"INSP. STICKER-EXPIRED/MISSING","judgment_entry_date":"2018-08-23","fine_amount":65.0,"penalty_amount":60.0,"interest_amount":17.66,"reduction_amount":0.0,"payment_amount":0.0,"amount_due":142.66,"precinct":"069","county":"K","issuing_agency":"TRAFFIC","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSWmVFMXFaek5QVkdOM1RVRTlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8612880026","_score":0.35667494,"_source":{"plate":"T735621C","state":"NY","license_type":"OMT","summons_number":8612880026,"issue_date":"2018-05-12","violation_time":"06:23A","violation":"FIRE HYDRANT","judgment_entry_date":"2018-09-13","fine_amount":115.0,"penalty_amount":60.0,"interest_amount":23.21,"reduction_amount":0.0,"payment_amount":0.0,"amount_due":198.21,"precinct":"061","county":"K","issuing_agency":"TRAFFIC","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSWmVFMXFaelJOUkVGNVRtYzlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8487142450","_score":0.35667494,"_source":{"plate":"GWG7210","state":"NY","license_type":"PAS","summons_number":8487142450,"issue_date":"2017-04-11","violation_time":"05:35P","violation":"EXPIRED MUNI METER","fine_amount":35.0,"penalty_amount":0.0,"interest_amount":0.0,"reduction_amount":0.0,"payment_amount":35.0,"amount_due":0.0,"precinct":"115","county":"Q","issuing_agency":"TRAFFIC","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSUk5FNTZSVEJOYWxFeFRVRTlQUT09&locationName=_____________________","description":"View Summons"}}},{"_index":"bigdata1","_type":"_doc","_id":"8090011093","_score":0.2876821,"_source":{"plate":"88653MG","state":"NY","license_type":"COM","summons_number":8090011093,"issue_date":"2016-08-24","violation_time":"08:15A","violation":"BIKE LANE","fine_amount":115.0,"penalty_amount":0.0,"interest_amount":0.0,"reduction_amount":10.0,"payment_amount":105.0,"amount_due":0.0,"precinct":"009","county":"NY","issuing_agency":"TRAFFIC","violation_status":"HEARING HELD-GUILTY REDUCTION","summons_image":{"url":"http://nycserv.nyc.gov/NYCServWeb/ShowImage?searchID=VDBSQk5VMUVRWGhOVkVFMVRYYzlQUT09&locationName=_____________________","description":"View Summons"}}}]}}
```

- [x] This module is completed


## Part 3: Visualizing and Analysis on Kibana
```
Kibana is an open source data visualization dashboard for Elasticsearch. It provides visualization capabilities on top of the content indexed on an Elasticsearch cluster. Users can create bar, line and scatter plots, or pie charts and maps on top of large volumes of data. Fianlly all the visualizations can be together put up as a dashboard
```

### A) Commands

#### 1. Verify the build and successful logins into Kibana:
* ```Verfiy Kibana via curl```
``` 
curl <docker's ip>:5601
```
* ```Verfiy Kibana via broswer```
``` 
Go to: http://<docker's ip>:5601/
```
* ```Result from Kibana Instance on successful ping at the server```
```
The user interface of Kibana module. Check for "kibana homepage.png" inside the folder - part 3.
```

#### 2. Push 1 Millions records into Kibana via Elastic Search
* ```Run the service```
``` 
docker-compose run -e APP_TOKEN=<api_token> pyth python main.py --page_size=1000 --num_pages=1000 --output=results.json --elastic_search=True
```

### B) Set Up Kibana and visualize the data

#### 1. Initial Configuration:
* ```Create index pattern```
![kibana step 1](https://user-images.githubusercontent.com/6689256/76834130-ffdb3200-6802-11ea-9c06-eafc14f13344.png)

* ```Configure Settings```
![kibana step 2](https://user-images.githubusercontent.com/6689256/76834158-09fd3080-6803-11ea-93aa-f24dcceef162.png)

* ```Discover the field and metrics for the index pattern for 1 million records pushed via Elastic Search```
![kibana_discover_1 million records](https://user-images.githubusercontent.com/6689256/76834192-1a151000-6803-11ea-86c2-0b5064c84ea4.png)


#### 2. All Charts:
* ```Line Chart: Average Change by Month```
![Line Chart](https://user-images.githubusercontent.com/6689256/76834464-9c9dcf80-6803-11ea-886a-7d24b6fa1d49.png)

* ```Table View: Different Amounts by Year```
![Table View](https://user-images.githubusercontent.com/6689256/76837154-6a42a100-6808-11ea-9714-a983e87b14f0.png)

* ```Heatmap: Top States by Penalty Amount```
![Heatmap](https://user-images.githubusercontent.com/6689256/76834602-dcfd4d80-6803-11ea-8b44-867c71ea086d.png)

* ```Area Chart: Average Amount for Different Amounts```
![Area Chart](https://user-images.githubusercontent.com/6689256/76838724-b68ee080-680a-11ea-8ad4-d6e4155fc5fa.png)

* ```Word Cloud: Violation Keywords in NYC```
![Word Cloud](https://user-images.githubusercontent.com/6689256/76834739-0ddd8280-6804-11ea-86fd-539fb32e693e.png)

* ```Pie Chart: Top 20 states by Shares of Summons```
![Pie Chart](https://user-images.githubusercontent.com/6689256/76838064-015c2880-680a-11ea-8fe0-f98729e09e88.png)


#### 3. Dashboard:
* ```Top Line Overview of NYC Parking Violations```
![Dashboard](https://user-images.githubusercontent.com/6689256/76836977-19cb4380-6808-11ea-9590-0d9cc617f075.png)


#### 4. Deploying via Docker Hub:
* ```Link to the docker hub for part 2 and part3```
```
https://hub.docker.com/repository/docker/tanaydocker/pyth
```

- [x] This module is completed


## Appendix
```
All the additional info about the project - the tools used, the servers required, system configuration, references, etc are included in this section.
```

### A) Project Specifications

#### 1. Application Summary
* ```System Specification:```
``` 
Operating System: Windows 10
RAM Size: 16 GB
Memory: 500 GB
```

* ```Tools Used:```
``` 
Programming Language: Python (Version 3.7)
Editor: Sublime Text (Version 3)
Platform: Docker Desktop (Version 2.2.0.3)
Shell: Git Bash (Version 2.25.1)
```

* ```Services Commissioned:```
``` 
Cloud Platform: Amazon Web Services (AWS)
Database Engine: Elastic Search (NoSQL distributive system)
Visualization Tool: Kibana
Version Control System: Git
```

#### 2. Communication Channel
* ```Offline:```
``` 
Classrom: Room 10-155
Timing: Friday, 1800 to 2100 Hours
Address: Baruch Vertical Campus,
55, Lexington Avenue,
New York, USA
```

* ```Online:```
``` 
Slack: STA9760
Members: 53
```

### B) References

#### 1. Guide
* ```Prof. Taqqui Karim```
``` 
Subject: 9760 - Big Data Technologies
Session: Spring, 2020
```

#### 2. Links
- [Argument Parsing in Python](https://pymotw.com/2/argparse/)
- [Working with JSON in Python](https://realpython.com/python-json/)
- [Mastering Github Markdown](https://guides.github.com/features/mastering-markdown/)
- [String to datetime in Python](https://www.journaldev.com/23365/python-string-to-datetime-strptime)
- [Elastic Search Indexing in Python](https://qbox.io/blog/building-an-elasticsearch-index-with-python)
- [Elastic Search Via Curl](https://okfnlabs.org/blog/2013/07/01/elasticsearch-query-tutorial.html#curl-or-browser)
