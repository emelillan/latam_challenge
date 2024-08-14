# Description: This file contains the main function that will be executed when the cloud function is triggered.

import functions_framework
from google.cloud import storage
import json

from src.q1_memory import q1_memory
from src.q2_memory import q2_memory
from src.q3_memory import q3_memory

from src.q1_time import q1_time
from src.q2_time import q2_time
from src.q3_time import q3_time


generator_functions = {
    "q1_memory": q1_memory,
    "q2_memory": q2_memory,
    "q3_memory": q3_memory,
    "q1_time": q1_time,
    "q2_time": q2_time,
    "q3_time": q3_time,
}


@functions_framework.http
def main(request):

    # Get request data
    payload = request.get_json()
    function = payload['function'].lower()
    function_to_call = generator_functions[function]

    # Get data from GCS using Cloud Storage client library
    storage_client = storage.Client()
    bucket = storage_client.bucket('latam-challenge')
    blob = bucket.blob('farmers-protest-tweets-2021-2-4.json')
    data = blob.download_as_string()

    # save data in the tmp folder
    with open('/tmp/data.json', 'wb') as f:
        f.write(data)

    # call the function
    result = function_to_call('/tmp/data.json')
    result = {str(k): v for k, v in result}

    # return the result as a json
    return json.dumps(result)
