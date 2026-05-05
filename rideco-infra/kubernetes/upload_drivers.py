from azure.storage.blob import BlobServiceClient
import os

conn_str = os.getenv("ADLS_CONNECTION_STRING")
container_name = os.getenv("ADLS_CONTAINER")

blob_service = BlobServiceClient.from_connection_string(conn_str)
container_client = blob_service.get_container_client(container_name)

with open('/data/drivers.csv', 'rb') as data:
    container_client.upload_blob(
        name="drivers/drivers.csv",
        data=data,
        overwrite=True
    )

print("Uploaded drivers.csv")