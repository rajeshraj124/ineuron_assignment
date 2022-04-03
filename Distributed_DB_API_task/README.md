# Distributed Database Application

## Application Architecture
<img title="App Architecture" alt="architecture" width="600px" src="application-architecture.png"/>


## About Project
Project to fetch data from MySQl & MongoDB.

#### Access Data from MySQL Database
* Request URL: http://localhost:9000/db-app
* Request Type: POST
* Set `Content-Type` to `application/json` in request header
* Request body: `{"username": "", "password": "", "query": "SELECT * FROM CARDATASET.CAR", "type": "MYSQL"}`

#### Access Data from MongoDB
* Request URL: http://localhost:9000/db-app
* Request Type: POST
* Set `Content-Type` to `application/json` in request header
* Request body: `{"db-name": "BPST", "collection": "my_collection","connection-string":"mongodb+srv://rajesh:Sonu124@cluster0.3dtrx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", "type": "MongoDB"}`

<i>**Note:** Assumption - you have installed MySQL in your local system, and you can execute/run python code with required packages for this project.</i>
