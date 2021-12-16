import pandas as pd
import boto3
from botocore.exceptions import ClientError
import logging

logging.basicConfig(format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s',level = logging.ERROR)

''' This class have the AWS functions '''
class Functions :

    def create_bucket(self,bucket_name):
        try:
            s3.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)
    
    def upload_file(self,file,bucket_name):
        try:
            s3.upload_file(file,bucket_name,file,ExtraArgs = {
                'ACL' : 'public-read'
            })
        except ClientError as e:
            logging.error(e)

    def read_json_file(self,path):
        try:
            print("\nThis is Json file Content :\n")
            df = pd.read_json(path)
            print(df)
        except ValueError as e :
            logging.error(e)

    def read_csv_file(self,path):
        try:
            print("\nThis is CSV file Content :\n")
            df = pd.read_csv(path)
            print(df)
        except ValueError as e :
            logging.error(e)

''' Where we have the aws credentials from a text file and create the client object '''

with open("access.txt", "r") as file:
    data = file.readlines()
    aws_acess_key = data[0].strip("\n")
    aws_secret_key = data[1].strip("\n")
s3 = boto3.client('s3', 
aws_access_key_id = aws_acess_key,
aws_secret_access_key = aws_secret_key)
print(s3)


aws = Functions()

#Create Bucket

bucket_name = "asignbucket"
aws.create_bucket(bucket_name)

#Upload fiels into Bucket

jsonFile = "emp.json"
csvFile = "emp.csv"

aws.upload_file(jsonFile,bucket_name)
aws.upload_file(csvFile,bucket_name)

#Read files from bucket as data frame

jsonPath = "s3://asignbucket/emp.json"
csvPath = "s3://asignbucket/emp.csv"

aws.read_json_file(jsonPath)
aws.read_csv_file(csvPath)    