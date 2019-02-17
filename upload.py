#!/bin/env python3

import boto3
import sys
import mimetypes

session = boto3.Session()
dynamo = session.resource("dynamodb")
pages = dynamo.Table('web')

mimetypes.init()
mimeType = mimetypes.guess_type(sys.argv[1])[0]

with open(sys.argv[1], 'rb') as file_con:
    fileBytes = file_con.read()

new_item = pages.put_item(
    Item={
        'page': sys.argv[1],
        'content': fileBytes,
        'mimeType': mimeType
    }
)
