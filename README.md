# Public Python Speed Test Documentation

## Pre Req 
* Up to date Python3 environment
* Install and setup local MySQL - schema to follow
* Install Speedtest CLI
`pip install speedtest-cli` 
* Install Dotenv for reading environment variables
`pip install python-dotenv`
* Install Python MySQL
`pip install mysql-connector-python`

## Installation & Running
* Clone Repo
* Create .env file requires:
```
mysql-pw="PASSWORD-HERE"
```


## MySQL Schema
Schema - speedtest
Table - results

The script assumes you have created a user named 'speedtest' with write privelages to the MySQL Schema called 'speedtest'

Col Name | Type
---------|-------
idspeedtest | int
client | json
server | json
bytes_received | double
bytes_sent | double
download | double
upload | double
ping | double
share | varchar(150)
timestamp | datetime
