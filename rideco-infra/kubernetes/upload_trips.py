from azure.storage.blob import BlobServiceClient
import os

conn_str = os.getenv("ADLS_CONNECTION_STRING")
container_name = os.getenv("ADLS_CONTAINER")

blob_service = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service.get_container_client(container_name)

with open('/data/trips.csv', 'rb') as data:
    container_client.upload_blob(
        name="trips/trips.csv",
        data=data,
        overwrite=True
    )

print("Uploaded trips.csv to ADLS Bronze")
