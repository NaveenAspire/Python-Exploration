"""This module contains s3 operations code example"""
from os import path
import csv
import boto3
import pandas as pd

#Client Object

s3 = boto3.client('s3')
print(s3)


#Creating Bucket

# s3.create_bucket(ACL='private',Bucket='bucketaveen')

#Uploading File

# file = "emp.csv"
# s3.upload_file(file,"bucketaveen",file)


#List Buckets

# for bucket in s3.list_buckets()['Buckets']:
#     print(bucket['Name'])

# buckets = [bucket for bucket in s3.buckets.all()]
# print(buckets)

#Delete Items in Bucket

# s3.delete_objects(Bucket='bucketaveen',Delete={
#     'Objects':[{
#         'Key':'emp.csv'
#     },],
#     'Quiet':True|False
# })

#Get all objects in a Bucket

response = s3.list_objects(Bucket='bucketaveen')
print(response['Contents'])


#Get Object

# response = s3.get_object(Bucket='bucketaveen',Key = 'emp.csv')
# d = response['Body'].read()
# print(len(d))
# print(type(d))

# with open("s3emp.csv",'wb') as f:
#     f.write(d)


#Read CSV file from Bucket

PATH = 's3://asignbucket/emp.csv'
df = pd.read_csv(PATH)
print(df.head())

# #Resource Object

s3 = boto3.resource('s3')
print(s3)


# #Deleting Bucket
# bucket = s3.Bucket('bucketaveen')
# bucket.delete()

# Cpoy the object from one bucket to another bucket


copy_source = {'Bucket' : 'firsttestbuct', 'Key': 'Courier bill - Reimbursement.jpg'}
s3.Object('bucketaveen', 'Courier bill - Reimbursement.jpg').copy(copy_source)
