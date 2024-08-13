# dummy http GCP cloud function using functionframework


from google.cloud import functionframework


@functionframework.http
def main(request):
    print("working")
    return 'Hello, World!'
