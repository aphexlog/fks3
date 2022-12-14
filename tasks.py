import os, logging
import boto3
import orjson as oj
from invoke import task


client = boto3.client('s3', region_name='us-west-2')

buckets_list = client.list_buckets()

@task
def list_buckets(c):
    """List all buckets"""
    print(oj.dumps(buckets_list, option=oj.OPT_INDENT_2).decode())

@task
def delete_bucket(c):
    """Delete a bucket"""
    bucket_name = input('Enter bucket name: ')
    try:
        client.delete_bucket(Bucket=bucket_name)
    except Exception as err:
        print(err)

@task
def empty_bucket(c):
    """Empty a bucket"""
    bucket_name = input('Enter bucket name: ')
    for obj in client.list_objects(Bucket=bucket_name)['Contents']:
        client.delete_object(Bucket=bucket_name, Key=obj['Key'])
