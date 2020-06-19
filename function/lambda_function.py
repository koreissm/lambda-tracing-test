import os
import json
import mysql.connector
from mysql.connector import errorcode

from datadog_lambda.metric import lambda_metric
from datadog_lambda.wrapper import datadog_lambda_wrapper

from ddtrace import tracer

@datadog_lambda_wrapper
def lambda_handler(event, context):
    employees = get_employees()
    return {
        'statusCode': 200,
        'body': json.dumps(employees, ensure_ascii=False)
    }

def get_employees():

	config = {
	  'user': os.environ['DB_USER'],
	  'password': os.environ['DB_PASSWORD'],
	  'host': os.environ['DB_HOST'],
	  'database': os.environ['DB_NAME'],
	  'raise_on_warnings': True
	}

	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()

	employees = dict()
	cursor.execute("select * from Employee")
	for row in cursor:
		employees[row[0]] = row[1]
	cnx.close()

	return employees