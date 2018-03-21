import os
import json
import boto3
import logging
from boto3.dynamodb.conditions import Key, Attr
import pprint

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
    result = table.scan(
        FilterExpression=Attr('inchiKey').begins_with(event['pathParameters']['inchiKey'])
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response


def get_by_splash_key(event, context):
    """returns a specific item from the dynamo table, by using the splash key as lookup"""
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.scan(
        FilterExpression=Attr('splash').begins_with(event['pathParameters']['splash'])
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response

