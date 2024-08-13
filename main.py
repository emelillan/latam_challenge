# dummy http GCP cloud function using functionframework


# Import the 'functionframework' package
import functions_framework


@functions_framework.http
def main(request):
    print("working")
    # Get data from GCS using Cloud Storage client library
    # storage_client = storage.Client()
    # bucket = storage_client.bucket('my-bucket')
    # blob = bucket.blob('my-file')
    # data = blob.download_as_string()
    # print(data)
    return 'Hello, World!'
