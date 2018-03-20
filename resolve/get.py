import os
import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

from resolve import decimalencoder

dynamodb = boto3.resource('dynamodb')


def get(event, context):
    """returns a specific item from the dynamo table"""
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response


def get_by_inchi_key(event, context):
    """returns a specific item from the dynamo table, by using the inchi key as lookup"""
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.query(
        KeyConditionExpression=Key('inchiKey').eq(event['pathParameters']['inchiKey'])
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response

