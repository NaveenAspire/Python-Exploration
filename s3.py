import boto3
import os

with open("access.txt", "r") as file:
    data = file.readlines()
    access_key_id = data[0].strip("\n")
    secret_access_key = data[1].strip("\n")

client = boto3.client('s3', aws_access_key_id= access_key_id,
 aws_secret_access_key = secret_access_key)

s3 = boto3.resource('s3')
print(s3.buckets.all())

print(os.getcwd())
print(os.listdir("D:\PythonExplore"))
for file in os.listdir():
    print(file)
    if '.py' in file:
        upload_file_bucket = 'firsttestbuct'
        upload_file_key = 'python/'+str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)