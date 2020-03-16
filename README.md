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
-- the image link goes here

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
Only updated from part 1 here is an additional exercise to install elasticsearch.
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
```

### C) Commands

#### 1. Docker-Compose Build:
* ```Clean all the previous images```
``` 
docker system prune -a
```
* ```Set up the necessary JVM heap memory for the exercise```
```
docker-machine ssh
```
```
sudo sysctl -w vm.max_map_count=262144
```
```
exit
```
```
NOTE: This step is optional for people who have issues with elastic search image dying within seconds of us initiating docker-compose.
```
* ```Get IP address of the docker```
```
docker inspect -f "{{ .NetworkSettings.IPAddress }}" <containerNameOrId>
```

- [x] This module is under progress

## Part 3: Visualizing and Analysis on Kibana
- [ ] This module is yet to be started

## Part 4: Deploying to EC2 Instance
- [ ] This module is yet to be started
