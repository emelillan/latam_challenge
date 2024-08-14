# dummy http GCP cloud function using functionframework


# Import the 'functionframework' package
import functions_framework
from google.cloud import storage
import pandas as pd
import json
from src.q1_memory import q1_memory


@functions_framework.http
def main(request):

    # Get request data
    request_json = request.get_json()
    print(request_json)
    # Get data from GCS using Cloud Storage client library
    storage_client = storage.Client()
    bucket = storage_client.bucket('latam-challenge')
    blob = bucket.blob('farmers-protest-tweets-2021-2-4.json')
    data = blob.download_as_string()
    # save data in the tmp folder
    with open('/tmp/data.json', 'wb') as f:
        f.write(data)
    result = q1_memory('/tmp/data.json')
    result = {str(k): v for k, v in result}
    # return the result as a json
    return json.dumps(result)
