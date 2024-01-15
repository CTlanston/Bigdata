import boto3
import json

class DynamoLoader:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    def _get_data_from_s3(self, s3_uri):
        bucket_name = s3_uri.split('/')[2]
        object_key = '/'.join(s3_uri.split('/')[3:])
        response = self.s3.get_object(Bucket=bucket_name, Key=object_key)
        return json.loads(response['Body'].read().decode('utf-8'))

    def _process_and_insert(self, data, table):
        for item in data:
            item = {k: int(v) if isinstance(v, str) and v.isnumeric() else v for k, v in item.items()}
            try:
                table.put_item(Item=item)
            except Exception as e:
                print(f"Error inserting item: {item}")
                print(e)

    def load_data(self, s3_uri, table_name):
        data = self._get_data_from_s3(s3_uri)
        table = self.dynamodb.Table(table_name)
        self._process_and_insert(data, table)

# Sample usage:
if __name__ == "__main__":
    loader = DynamoLoader()
    s3_uri = r's3://bigdata-lab-bucket/train.json'
    table_name = 'recipes'
    loader.load_data(s3_uri, table_name)
