# Define the provider
provider "google" {
  project = "your-gcp-project-id"
  region  = "your-gcp-region"
}

# Create a service account
resource "google_service_account" "my_service_account" {
  account_id   = "my-service-account-id"
  display_name = "My Service Account"
}

# Assign the Cloud Functions Invoker role
resource "google_project_iam_member" "cloud_functions_invoker" {
  project = var.project_id
  role    = "roles/cloudfunctions.invoker"
  member  = "serviceAccount:${google_service_account.my_service_account.email}"
}

# Assign the Cloud Functions Developer role
resource "google_project_iam_member" "cloud_functions_developer" {
  project = var.project_id
  role    = "roles/cloudfunctions.developer"
  member  = "serviceAccount:${google_service_account.my_service_account.email}"
}

# Assign the IAM Service Account User role
resource "google_project_iam_member" "service_account_user" {
  project = var.project_id
  role    = "roles/iam.serviceAccountUser"
  member  = "serviceAccount:${google_service_account.my_service_account.email}"
}

# Assign the IAM Service Account Token Creator role
resource "google_project_iam_member" "service_account_token_creator" {
  project = var.project_id
  role    = "roles/iam.serviceAccountTokenCreator"
  member  = "serviceAccount:${google_service_account.my_service_account.email}"
}
