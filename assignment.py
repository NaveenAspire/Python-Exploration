"""This module has pandas operations and store the pytho file in aws s3  service"""

import logging
import argparse
import pandas as pd
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(
    format="Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s",
    level=logging.ERROR,
)

# This class have the AWS functions


class Functions:
    """ This class contains some functions for performing s3 operations. """
    def create_bucket(self, bucket_name):
        """ This function used to create a bucket in s3 service"""
        try:
            s3.create_bucket(Bucket=bucket_name)
        except ClientError as err:
            logging.error(err)

    def upload_file(self, file, bucket_name):
        """This function used to upload files into the s3 bucket"""
        try:
            s3.upload_file(file, bucket_name, file, ExtraArgs={"ACL": "public-read"})
        except ClientError as err:
            logging.error(err)

    def read_json_file(self, path):
        """ This function used to read the json file contents as data frame"""
        try:
            print("\nThis is Json file Content :\n")
            json_df = pd.read_json(path)
            print(json_df)
        except ValueError as err:
            logging.error(err)

    def read_csv_file(self, path):
        """ This function used to read the csv file contents as data frame"""
        try:
            print("\nThis is CSV file Content :\n")
            csv_df = pd.read_csv(path)
            print(csv_df)
        except ValueError as err:
            logging.error(err)


#Where we have the aws credentials from a text file and create the client object


s3 = boto3.client("s3")
print(s3)


aws = Functions()

# Create Bucket
parser = argparse.ArgumentParser(
    description="Give an Operation like create bucket, upload files, read files"
)

subparser = parser.add_subparsers(dest="operation")

create_bucket = subparser.add_parser("create bucket")
upload_files = subparser.add_parser("upload files")
read_files = subparser.add_parser("read files")

args = parser.parse_args()
BUCKET_NAME = 'asignbucket'

if args.operation == "create bucket":
    aws.create_bucket(BUCKET_NAME)

# Upload fiels into Bucket

if args.operation == "upload files":
    JSON_FILE = "emp.json"
    CSV_FILE = "emp.csv"

    aws.upload_file(JSON_FILE, BUCKET_NAME)
    aws.upload_file(CSV_FILE, BUCKET_NAME)

# Read files from bucket as data frame

if args.operation == "read files":
    JSON_PATH = "s3://asignbucket/emp.json"
    CSV_PATH = "s3://asignbucket/emp.csv"

    aws.read_json_file(JSON_PATH)
    aws.read_csv_file(CSV_PATH)
