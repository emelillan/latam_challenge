# dummy http GCP cloud function using functionframework


# Import the 'functionframework' package
import functions_framework
from google.cloud import storage
import pandas as pd
import json


@functions_framework.http
def main(request):
    print("working")
    # Get data from GCS using Cloud Storage client library
    storage_client = storage.Client()
    bucket = storage_client.bucket('latam')
    blob = bucket.blob('farmers-protest-tweets-2021-2-4.json')
    data = blob.download_as_string()
    json_data = json.loads(data)
    df = pd.DataFrame(json_data)
    print(df.head())
    return 'Hello, World!'
