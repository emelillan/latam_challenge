# dummy http GCP cloud function using functionframework


from google.cloud import functionframework


@functionframework.http
def hello_http(request):
    return 'Hello, World!'
