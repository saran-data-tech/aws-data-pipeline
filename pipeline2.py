import boto3
import csv
import io

def lambda_handler(event, context):
    
    s3 = boto3.client('s3')
    
    input_bucket = 'my-output-data-bucket-saran'
    output_bucket = 'my-output-data-bucket-saran'
    file_name = 'filtered_data.csv'
    
    response = s3.get_object(Bucket=input_bucket, Key=file_name)
    content = response['Body'].read().decode('utf-8')
    
    reader = csv.DictReader(io.StringIO(content))
    ages = []
    count = 0
    for row in reader:
        ages.append(int(row['age']))
        count += 1
    
    average_age = sum(ages) / len(ages)
    
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['metric', 'value'])
    writer.writerow(['total_chennai_people', count])
    writer.writerow(['average_age', average_age])
    
    s3.put_object(
        Bucket=output_bucket,
        Key='final_report.csv',
        Body=output.getvalue()
    )
    
    return {
        'statusCode': 200,
        'body': f'Report done! Total: {count} people, Average age: {average_age}'
    }
```

---

### File 3: `data.csv`
Copy and paste this:
```
name,age,city
Alice,25,Chennai
Bob,30,Mumbai
Charlie,22,Delhi
Saran,20,Chennai