import boto3
import os

client = boto3.client("s3")

s3 = boto3.resource("s3")
print(s3.buckets.all())

print(os.getcwd())
print(os.listdir("D:\PythonExplore"))
for file in os.listdir():
    print(file)
    if ".py" in file:
        upload_file_bucket = "firsttestbuct"
        upload_file_key = "python/" + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
