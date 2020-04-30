import boto3
import sys
Stack_Name = sys.argv[1]

def validate_resources(Stack_Name):
    client = boto3.client('cloudformation')
    iam = boto3.resource('iam')
    stack_resources = client.list_stack_resources(StackName=Stack_Name)
    for resource in stack_resources['StackResourceSummaries']:
        if resource['ResourceType'] == 'AWS::IAM::Role':
            print "IAM Role: " + resource['PhysicalResourceId'] + " is being validated"
            arn = iam.Role(resource['PhysicalResourceId']).arn
            print "IAM Role: " + resource['PhysicalResourceId'] + " has been validated successfully"
        elif resource['ResourceType'] == 'AWS::IAM::InstanceProfile':
            print "Instance Profile: " + resource['PhysicalResourceId'] + " is being validated"
            arn = iam.InstanceProfile(resource['PhysicalResourceId']).arn
            print "Instance Profile: " + resource['PhysicalResourceId'] + " has been validated successfully"
        elif resource['ResourceType'] == 'AWS::IAM::ManagedPolicy':
            print "IAM Policy: " + resource['PhysicalResourceId'] + " is being validated"
            policy_id = iam.Policy(resource['PhysicalResourceId']).policy_id
            print "IAM Policy: " + resource['PhysicalResourceId'] + " has been validated successfully"
        elif resource['ResourceType'] == 'AWS::CloudFormation::Stack':
            print "Nested Stack: " + resource['PhysicalResourceId'] + " is being validated"
            validate_resources(resource['PhysicalResourceId'].split('/')[1])
            print "Nested Stack: " + resource['PhysicalResourceId'] + " has been validated successfully"
        else:
            print "Resource: " + resource['PhysicalResourceId'] + " could not be validated"


validate_resources(Stack_Name)