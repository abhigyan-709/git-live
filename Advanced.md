Q.1) What is VPC and explain the use of it.
answer:- Amazon Virtual Private Cloud(VPC) is a service that allows users to launch AWS resources in logically isolated virtual  network. It provides control over networking aspects, such as IP address ranges, subnets, routing, and gateways, enabling secure and scalable application deployment.
The use of VPC:
1. Network Isolation : You can create an isolated environment for your workloads.
2. Customization : Design the network architecture as per your requirements.
3. Security : Control inbound and outbound traffic using security groups and network ACLs.
4. Scalability : Easily extend your VPC by adding subnets or modifying routes.

Q.2)What is IAM Role?
answer:- IAM roles helps you to manage permissions for your service and application. Unlike IAM users, which are associated with a specific person roles are designed to be assumed by anyone who needs term, making term incredible flexible.
conside a role as a set of permissions that can be temporarily assigned to entire like AWS (serivce EC2 LAMBDA) or even users from another AWS account. TUS is great sewnty as roles use temporary credentials that expose automatically.

Q.3) What is the difference between public and private subnets in AWS VPC?
answer:- *Public Subnets- Resources like web servers or bastion hosts should be in public subnets, accessible via an Internet Gateway(IGW).
*Private Subnets- Resources like databases and application servers should reside in private subnets, ensuring restricted access accessible via NAT Gateway/Instances.

Q.4) What is managed policy and inline policy.
answer:- 
*Managed Policy:- 
1. A standalone IAM policy that can be attached to multiple users, groups, or roles.
2. Can be reused across multiple IAM identities.
3. AWS Managed Policies (predefined by AWS) and Customer Managed Policies (created by users).
4. A ReadOnlyAccess managed policy applied to multiple users needing read access.
*Inline Policy:- 
1. A policy that is embedded directly into a specific IAM user, group, or role.
2. Tied to a single IAM identity and cannot be reused.
3. Only created and used within a single IAM identity.
4. A developer role with an inline policy granting access to a specific S3 bucket.

Q.5) What is the use of S3 bucket and what is the difference between google drive and S3 bucket.
answer:- An S3 Bucket in Amazon Simple Storage Service (S3) is a scalable object storage service used for storing and retrieving any amount of data from anywhere on the internet.
Uses of S3 Bucket:
Data Storage – Store any type of data (images, videos, backups, logs, etc.).
Website Hosting – Host static websites directly from an S3 bucket.
Backup & Disaster Recovery – Store backups and archive data for durability.
Big Data Analytics – Store large datasets for analytics and machine learning.
Content Delivery – Integrates with AWS CloudFront for faster content delivery.
Security & Access Control – Manage access with IAM roles, bucket policies, and encryption.
*Google Drive:-
1. Cloud storage for personal & collaborative file management.
2. 	User-level sharing (view/edit access via Google account).
3. Works with Google Workspace (Docs, Sheets, Drive, etc.).
4. Auto-syncs with local devices using Google Drive app.
*S3 Bucket:-
1. object storage for developers and businesses.
2. IAM roles, bucket policies, ACLs, signed URLs.
3. Integrated with AWS services (EC2, Lambda, CloudFront, etc.).
4. No automatic syncing; requires AWS CLI/tools to upload/download.

Q.6) Define how you will give access in AWS IAM to the group of students who will have only read only access to the S3 buckets.
answer:- 
Step 1: Create an IAM Group
Sign in to the AWS Management Console.
Go to IAM (Identity and Access Management).
Click User groups in the left panel.
Click Create group.
Enter a Group Name (e.g., StudentsReadOnlyGroup).
Click Next (We will attach permissions later).
Click Create group.

Step 2: Attach a Read-Only Policy to the Group
Open the IAM Group you created (StudentsReadOnlyGroup).
Click the Permissions tab.
Click Attach policies.
In the search bar, type: "AmazonS3ReadOnlyAccess".
Select the AmazonS3ReadOnlyAccess managed policy.
Click Attach policy.
 This policy allows users in the group to list and read objects from all S3 buckets, but they cannot upload, delete, or modify files.

Step 3: Create IAM Users and Add Them to the Group
Go to IAM > Users.
Click Add users.
Enter usernames for the students (e.g., student1, student2, etc.).
Select AWS Management Console access (if they need console access).
Set an auto-generated password (optional: require password reset).
Click Next: Permissions.
Select Add user to group and choose StudentsReadOnlyGroup.
Click Next and then Create users.