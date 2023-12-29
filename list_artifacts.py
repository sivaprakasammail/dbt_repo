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

list_blobs_with_prefix('gk_dbt_artifacts', os.environ['BUILD_ID'])
