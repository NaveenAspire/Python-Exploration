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

""" This class have the AWS functions """


class Functions:
    def create_bucket(self, bucket_name):
        try:
            s3.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)

    def upload_file(self, file, bucket_name):
        try:
            s3.upload_file(file, bucket_name, file, ExtraArgs={"ACL": "public-read"})
        except ClientError as e:
            logging.error(e)

    def read_json_file(self, path):
        try:
            print("\nThis is Json file Content :\n")
            df = pd.read_json(path)
            print(df)
        except ValueError as e:
            logging.error(e)

    def read_csv_file(self, path):
        try:
            print("\nThis is CSV file Content :\n")
            df = pd.read_csv(path)
            print(df)
        except ValueError as e:
            logging.error(e)


""" Where we have the aws credentials from a text file and create the client object """


s3 = boto3.client("s3")
print(s3)


aws = Functions()

# Create Bucket
parser = argparse.ArgumentParser(description="Give an input as bucket name")
parser.add_argument(
    "--bucket", type=str, default="asignbucket", help="Name of the S3 bucket"
)
args = parser.parse_args()


bucket_name = args.bucket
aws.create_bucket(bucket_name)

# Upload fiels into Bucket

jsonFile = "emp.json"
csvFile = "emp.csv"

aws.upload_file(jsonFile, bucket_name)
aws.upload_file(csvFile, bucket_name)

# Read files from bucket as data frame

jsonPath = "s3://asignbucket/emp.json"
csvPath = "s3://asignbucket/emp.csv"

aws.read_json_file(jsonPath)
aws.read_csv_file(csvPath)
