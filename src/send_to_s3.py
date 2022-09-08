import os
import boto3


def send_to_s3(filename):
    client = boto3.client(
        service_name=os.environ.get('SERVICE_NAME'),
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('REGION_NAME')
    )
    
    with open(filename, "rb") as f:
        client.upload_fileobj(f, 'gamescollector', 'gamesinformations')
        f.close()
        
