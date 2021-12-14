from os import path
import boto3
import pandas as pd
import csv

with open("access.txt", "r") as file:
    data = file.readlines()
    aws_acess_key = data[0].strip("\n")
    aws_secret_key = data[1].strip("\n")


#Client Object

s3 = boto3.client('s3', 
    aws_access_key_id = aws_acess_key,
    aws_secret_access_key = aws_secret_key)
print(s3)


#Creating Bucket

s3.create_bucket(ACL='private',Bucket='bucketaveen')

#Uploading File

file = "emp.csv"
s3.upload_file(file,"bucketaveen",file)


#List Buckets

for bucket in s3.list_buckets()['Buckets']:
    print(bucket['Name'])

# buckets = [bucket for bucket in s3.buckets.all()]
# print(buckets)

#Delete Items in Bucket

s3.delete_objects(Bucket='bucketaveen',Delete={
    'Objects':[{
        'Key':'emp.csv'
    },],
    'Quiet':True|False
})

#Get all objects in a Bucket

response = s3.list_objects(Bucket='bucketaveen')
print(response['Contents'])


#Get Object

response = s3.get_object(Bucket='bucketaveen',Key = 'emp.csv')
d = response['Body'].read()
print(len(d))
print(type(d))

with open("s3emp.csv",'wb') as f:
    f.write(d)


#Read CSV file from Bucket

path = 's3://bucketaveen/emp.csv'
df = pd.read_csv(path)
print(df.head())

#Resource Object

s3 = boto3.resource('s3', 
    aws_access_key_id = aws_acess_key,
    aws_secret_access_key = aws_secret_key)
print(s3)


#Deleting Bucket
bucket = s3.Bucket('bucketaveen')
bucket.delete()




