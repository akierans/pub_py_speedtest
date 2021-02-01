# Public Python Speed Test Documentation

## Pre Req 
* Up to date Python3 environment
* Install and setup local MySQL - schema to follow
* Install Speedtest CLI
`pip install speedtest-cli`

## Installation & Running
* Clone Repo
* Create .env file requires:
`mongo-pw="PASSWORD-HERE"`
`mysql-pw="PASSWORD-HERE"`


## MySQL Schema - speedtest
Table - results
Col Name | Type
---------|-------
idspeedtest | int
client | json
server | json
bytes_received | double
bytes_sent | double
download | double
upload - double
ping | double
share | varchar(150)
timestamp | datetime
