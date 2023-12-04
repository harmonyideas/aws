# collection-of-s3-bucket/iam policies
This project contains a collection of iam/s3 bucket policies

FileName      | Description |  policy type
------------- | -------------  |--------------
s3-bucket-allow-cloudtrail-log-receive.json | CloudTrail log receive. | bucket 
s3-bucket-allow-get-put-delete-path.json | GET/PUT/DELETE access to specific path within a bucket | user/group/role
s3-bucket-anonymous-get-access.json | Anonymous GET access | bucket 
s3-bucket-deny-object-delete.json | Bucket and object delete deny | bucket
s3-bucket-enforce-ssl-requests.json | Bucket enforce SSL requests only | bucket
s3-bucket-full-access-iam.json | Full access (and S3 console) for specific IAM users | user/group/role
s3-bucket-origin-access-control-get.json | CloudFront origin access control (OAC) GET access | bucket
s3-bucket-restrict-list-put-delete-path.json | Restricted LIST & PUT/DELETE access to specific path within a bucket | user/group/role
