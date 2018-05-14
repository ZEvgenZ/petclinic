#!/usr/bin/env python

import boto3
low_level_client = boto3.client('ec2')
keypairs = low_level_client.describe_key_pairs()


# Go to high level
ec2 = boto3.resource('ec2', region_name = 'us-west-2')

key_pair = 'oRudenk'
subnet ='subnet-c8fc75b1'

instances = ec2.create_instances(
        ImageId='ami-4e79ed36', 
        MinCount=1, 
        MaxCount=2,
        InstanceType="t2.micro",
    KeyName='oRudenk',
    
    NetworkInterfaces=[{'SubnetId': subnet, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': ['sg-6f437411']}])
   

for instance in instances:
    instance.create_tags(Tags=[{"Key": "Name", "Value": "Worker"}])
    instance.wait_until_running()

for instance in instances:
    print(instance.id, instance.instance_type, instance.vpc)
