import json
import logging
import os
import time

import boto3

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'splash' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the resolver item, requires 'splash' keyword")
    if 'inchiKey' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the resolver item, requires 'inchiKey' keyword")
    if 'origin' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the resolver item, requires 'origin' keyword")
    if 'record' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the resolver item, requires 'record' url")

    #add support for checking if inchi/splash pattern is valid

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': data['splash'] + data['inchiKey'] + data['origin'],
        'splash': data['splash'],
        'inchiKey': data['inchiKey'],
        'origin': data['origin'],
        'url': data['record'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response