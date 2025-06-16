import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
    sns = boto3.client('sns')
    
    try:
        # Parse CloudWatch alarm from SNS
        message = json.loads(event['Records'][0]['Sns']['Message'])
        alarm_name = message['AlarmName']
        new_state = message['NewStateValue']
        reason = message['NewStateReason']
        timestamp = message['StateChangeTime']
        
        # Determine severity
        critical_alarms = ['Root Account Usage Alert', 'IAM Policy Changes']
        severity = "🚨 CRITICAL" if alarm_name in critical_alarms else "⚠️ WARNING"
        
        # Create enhanced alert message
        alert_message = f"""
{severity} SECURITY ALERT

Alarm: {alarm_name}
State: {new_state}
Time: {timestamp}
Reason: {reason}

        """
        
        # Get the original SNS topic ARN from the event
        topic_arn = event['Records'][0]['Sns']['TopicArn']
        
        # Send enhanced notification back to the same topic
        response = sns.publish(
            TopicArn=topic_arn,
            Message=alert_message,
            Subject=f'{severity.split()[0]} Security Alert: {alarm_name}'
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Alert processed and enhanced successfully')
        }
        
    except Exception as e:
        print(f'Error processing alert: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
