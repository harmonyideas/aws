# iam policies
This folder contains IAM identity and trust policy templates. Placeholders such as `workplace_ip_address_here` and `<ACCOUNT_ID>` must be replaced before use.

FileName      | Description | policy type
------------- | ------------- | --------------
admin-account-owner.json | Allows all actions on all resources, only from the IP address in the condition (flagged for human review) | user/group/role
data-architect-allow.json | Allows broad data, analytics and messaging services (RDS, Redshift, S3, DynamoDB, Kinesis, EMR, Athena and others) from the IP address in the condition; denies `s3:DeleteBucket` | user/group/role
data-scientist-allow.json | Allows broad data and analytics services (RDS, Redshift, S3, DynamoDB, Kinesis, EMR, Athena and others) from the IP address in the condition; denies `s3:DeleteBucket` | user/group/role
database-admin-allow.json | Allows broad access to database and storage services (RDS, Redshift, S3, DynamoDB, SimpleDB, CloudSearch, Elasticsearch and others) from the IP address in the condition; denies `s3:DeleteBucket` | user/group/role
developerboundrypolicy.json | Permission boundary: allows EC2, S3, RDS and limited IAM role actions, and denies all actions on IAM roles and users in the account | permission boundary
enforce-mfa-authentication.json | Trust policy that lets `ec2.amazonaws.com` assume a role only when MFA is present (flagged for human review) | trust policy
fullstatck-developer-allow.json | Allows broad full-stack services (S3, Lambda, EC2, RDS, DynamoDB, API Gateway, CloudFront, Route 53 and others) from the IP address in the condition; denies deleting key resources such as EC2 instances, S3 buckets, Lambda functions, RDS instances, load balancers, Route 53 zones and CloudFront distributions | user/group/role
