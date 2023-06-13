import argparse
import boto3
from botocore.exceptions import ClientError

def create_restore_snapshot(region, source_access_key, source_secret_key, destination_access_key, destination_secret_key, snapshot_identifier):
    # Initialize the RDS clients for the source and destination accounts
    source_client = boto3.client('rds', region_name=region, aws_access_key_id=source_access_key, aws_secret_access_key=source_secret_key)
    destination_client = boto3.client('rds', region_name=region, aws_access_key_id=destination_access_key, aws_secret_access_key=destination_secret_key)

    try:
        # Create a snapshot in the source account
        snapshot_response = source_client.create_db_snapshot(
            DBSnapshotIdentifier=snapshot_identifier,
            DBInstanceIdentifier='my-db-instance'
        )
        snapshot_id = snapshot_response['DBSnapshot']['DBSnapshotIdentifier']
        print(f"Snapshot created: {snapshot_id}")

        # Restore the snapshot in the destination account
        restore_response = destination_client.restore_db_instance_from_db_snapshot(
            DBInstanceIdentifier='my-restored-db-instance',
            DBSnapshotIdentifier=snapshot_id,
            AvailabilityZone='us-east-1a',
            DBSubnetGroupName='my-db-subnet-group',
            VpcSecurityGroupIds=['security-group-id'],
            MultiAZ=False,
            PubliclyAccessible=True
        )
        restored_db_id = restore_response['DBInstance']['DBInstanceIdentifier']
        print(f"DB instance restored: {restored_db_id}")

    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create and restore an RDS snapshot between AWS accounts.')
    parser.add_argument('--region', required=True, help='AWS region')
    parser.add_argument('--source-access-key', required=True, help='Source AWS access key')
    parser.add_argument('--source-secret-key', required=True, help='Source AWS secret key')
    parser.add_argument('--destination-access-key', required=True, help='Destination AWS access key')
    parser.add_argument('--destination-secret-key', required=True, help='Destination AWS secret key')
    parser.add_argument('--snapshot-identifier', required=True, help='Snapshot identifier')

    args = parser.parse_args()

    create_restore_snapshot(args.region, args.source_access_key, args.source_secret_key, args.destination_access_key, args.destination_secret_key, args.snapshot_identifier)

