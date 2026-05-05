resource "google_storage_bucket" "bucket" {
  name     = "rideco-bucket"
  location = "US"
}