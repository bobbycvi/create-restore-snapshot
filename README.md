# Create and Restore RDS Snapshot

This Python script allows you to create an RDS snapshot in one AWS account and restore it in another AWS account. It utilizes the AWS SDK for Python (Boto3) and requires AWS access keys and secret keys for both the source and destination accounts.

## Prerequisites

- Python 3.x
- AWS access keys and secret keys for both the source and destination accounts
- Boto3 library (can be installed via pip)

## Usage

1. Install the required dependencies:

```shell
pip install boto3

2. Set up the AWS access keys and secret keys as environment variables:

export SOURCE_ACCESS_KEY=your_source_access_key
export SOURCE_SECRET_ACCESS_KEY=your_source_secret_access_key
export DESTINATION_ACCESS_KEY=your_destination_access_key
export DESTINATION_SECRET_ACCESS_KEY=your_destination_secret_access_key

3. Run the Python script with the following command:

python create_restore_rds_snapshot.py --region your_region --source-access-key $SOURCE_ACCESS_KEY --source-secret-key $SOURCE_SECRET_ACCESS_KEY --destination-access-key $DESTINATION_ACCESS_KEY --destination-secret-key $DESTINATION_SECRET_ACCESS_KEY --snapshot-identifier your_snapshot_identifier

The script will create a snapshot in the source account and restore it in the destination account.

Error Handling
The script includes error handling for common exceptions that may occur during the API calls. If an error occurs, the error message will be displayed.

Feel free to enhance the error handling further or add more error checking based on your specific requirements.

Please make sure to replace `'your_region'`, `'your_snapshot_identifier'`, `'your_source_access_key'`, `'your_source_secret_access_key'`, `'your_destination_access_key'`, and `'your_destination_secret_access_key'` with the appropriate values.
