# -AWS-Security-Monitoring-Dashboard-
AWS Security Monitoring Dashboard (Enhanced Edition)

A real-time AWS cloud security monitoring solution designed using CloudTrail, CloudWatch, SNS, and Lambda — fully deployable under the AWS Free Tier

Features

- Monitors critical security events:
  - `RootAccountUsageCount` – Tracks root user activity
  - `UnauthorizedAPICallCount` – Detects failed API calls due to lack of permissions
  - `SecurityGroupChangeCount` – Monitors security group changes
  - `IAMPolicyChangeCount` – Captures IAM policy modifications
  - ❌ `FailedConsoleLoginCount` – *Omitted due to policy constraints*

- ☁️ Uses:
  - AWS CloudTrail for event logging
  - CloudWatch Logs & Metric Filters for security metrics
  - CloudWatch Alarms for real-time alerting
  - SNS for critical/warning email notifications
  - Lambda for alert enhancement

 Screenshots

![Dashboard](screenshots/dashboard-view.png)

##  Folder Structure

| Folder | Description |
|--------|-------------|
| `lambda/` | Lambda function code for alert processing |
| `cloudwatch/` | Metric filter configurations |
| `sns/` | Notes on topic creation and subscription setup |
| `dashboard/` | CloudWatch dashboard setup details |
| `screenshots/` | UI views of the dashboard (optional) |
| `implementation-guide.pdf` | Full PDF guide with step-by-step instructions |

Full Guide

Download the detailed implementation guide here:
👉 [implementation-guide.pdf](./implementation-guide.pdf)

How to Use

1. Set up CloudTrail and log destination (S3)
2. Create metric filters and alarms in CloudWatch
3. Set up SNS topics for alerts
4. Deploy the Lambda function for notification enhancement
5. Build the CloudWatch Dashboard for visualizing metrics

Author

Syed Fuzail and Syed Yusuf Hussain 
🎓 Final Year CSE | Cloud Security & DevOps Enthusiast  
📍 Bangalore, India  
📧 [LinkedIn](www.linkedin.com/in/syed-fuzail-abdullah-758b89269) hwww.linkedin.com/in/syed-yusuf-?
| [GitHub](https://github.com/syedfuzailabbdulla)



