import glob
from google.cloud import storage
import os

def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name, prefix=prefix, delimiter=delimiter)

    # Note: The call returns a response only when the iterator is consumed.
    print("Blobs:")
    for blob in blobs:
        print('https://storage.cloud.google.com/gk_dbt_artifacts/' + blob.name)

    if delimiter:
        print("Prefixes:")
        for prefix in blobs.prefixes:
            print(prefix)

def upload_from_directory(directory_path: str, dest_bucket_name: str, dest_blob_name: str):
    storage_client = storage.Client()
    rel_paths = glob.glob(directory_path + '/**', recursive=True)
    bucket = storage_client.get_bucket(dest_bucket_name)
    for local_file in rel_paths:
        remote_path = f'{dest_blob_name}/{"/".join(local_file.split(os.sep)[1:])}'
        if os.path.isfile(local_file):
            blob = bucket.blob(remote_path)
            blob.upload_from_filename(local_file)


if __name__ == "__main__":
    upload_from_directory('target', 'gk_dbt_artifacts', os.environ['BUILD_ID'])
    list_blobs_with_prefix('gk_dbt_artifacts', os.environ['BUILD_ID'])
