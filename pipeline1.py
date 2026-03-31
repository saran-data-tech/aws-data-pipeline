import boto3
import csv
import io

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    
    input_bucket = 'my-input-data-bucket-saran'
    output_bucket = 'my-output-data-bucket-saran'
    file_name = 'data.csv'
    
    response = s3.get_object(Bucket=input_bucket, Key=file_name)
    content = response['Body'].read().decode('utf-8')
    
    reader = csv.DictReader(io.StringIO(content))
    filtered = [row for row in reader if row['city'] == 'Chennai']
    
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['name','age','city'])
    writer.writeheader()
    writer.writerows(filtered)
    
    s3.put_object(
        Bucket=output_bucket,
        Key='filtered_data.csv',
        Body=output.getvalue()
    )
    
    return {
        'statusCode': 200,
        'body': f'Done! {len(filtered)} records saved.'
    }