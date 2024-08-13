# dummy http GCP cloud function using functionframework


# Import the 'functionframework' package
import functions_framework


@functions_framework.http
def main(request):
    print("working")
    return 'Hello, World!'
