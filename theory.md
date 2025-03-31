Q.1 Define how you will give access in AWS IAM to the group of students who will have only read only access to the S3 buckets.

Ans:
Steps: 
 Step-1:Create an IAM Group
 -->Go to AWS IAM Console → Click on User Groups → Create Group.
 -->Enter a Group Name (ex:"Students")
 -->Click Create Group.

 Step-2:Attach Read-Only Policy to the Group
 -->Go to IAM Policies 
 -->Choose json and enter s3 read-only ploicy
     {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name",
                "arn:aws:s3:::your-bucket-name/*"
            ]
        }
    ]
}
-->Then next , name the policy and create Policy
-->Go to IAM Groups, select "Students" group and Attach the s3 read only policy

 Step-3:Add Students to the Group
 --> Go to IAM Users - Create Users.
 --> Assign students to Student Group

Result:
 --> All students in the group can only view and download files from the S3 bucket.They cannot upload, delete, or modify any files.


Q.2 What is VPC and explain the use of it.\

Ans: AWS Virtual Private Cloud (VPC) is a logically isolated section of the AWS cloud where you can launch AWS resources in a customized network environment. It allows you to control IP addressing, subnets, route tables, security settings, and internet access for your AWS services.

Uses of  AWS VPC: 
--> Network Isolation → Ensures your AWS resources are separated from other users.
--> Security → Control access using security groups, NACLs, and VPNs.
--> Custom Networking → Define private and public subnets with your own IP ranges.
--> Internet Control → Decide which resources can access the internet and which remain private.
--> Scalability → Easily scale your infrastructure with Elastic Load Balancing (ELB) and NAT gateways.

Q.3 What is the use of S3 bucket and what is the difference between google drive and S3 bucket.

Ans: Amazon S3 (Simple Storage Service) is an object storage service that allows you to store, retrieve, and manage any amount of data in a secure, scalable, and highly available way.
Difference between S3 and G Drive are: 

-->s3 is a Object Storage but G drive is a Cloud based storage.
-->s3 stores large structured and unstructured data whereas G drive is for Personal and Team Collaboration
-->s3 is pay as you go model but gdrive is free till 15gb then paid storage option available.
and many more differences in scalability, performance etc.

Q.4 What is IAM Role?

Ans: An IAM Role in AWS is a set of permissions that define what actions a service or user can perform. Unlike IAM Users, IAM Roles do not have long-term credentials (passwords or access keys). Instead, they use temporary security credentials to grant access to AWS services.

Q.5 What is the difference between public and private subnets in AWS VPC?

Ans: Public Subnet has Direct Internet Access and Private Subnet has no direct access.However, private subent can use NAT for OUTBOUND internet.Public SUbnet is less secure than Private Subnet as it is purely exposed to internet.Public Subnet uses a Internet gateway and Private Subnet uses Nat Gateway.

Q.6 What is managed policy and inline policy?

Ans: A Managed Policy is a reusable policy that can be attached to multiple IAM users, groups, or roles. It is stored separately from the IAM entity. BUT An Inline Policy is directly embedded within a single IAM user, group, or role. It cannot be reused.