# NYC Parking Violations
```For this project, we will analyze millions of NYC Parking violations since January 2016.```

## Part 1: Python Scripting
```In the first part, we simply want to develop a python command line interface that can connect to the OPCV API and demonstrate that the data is accessible via python.```

### File Structure
![Tree](https://user-images.githubusercontent.com/6689256/75619232-76abd600-5b47-11ea-842e-f60372c5fd0f.PNG)

### Associated Files

#### Python Scripting Files:
* ```main.py```
``` 
It parses the arguments --page_size, --num_pages, --output into the api.py file for function call.
The code can be found in this repository under nyc_parking_violations
```

* ```api.py```
``` 
It has all the fucntions and error handling code to implement the exercise. 
The APP Token, domain, etc are also defined here alongside necessary packages.
The code can be found in this repository under nyc_parking_violations > src > bigdata 1
```

#### Supplementary Files:
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

#### Output:
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

### Commands

#### Docker Build:
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

#### Docker Hub:
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
