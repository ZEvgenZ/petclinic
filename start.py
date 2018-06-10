#!/usr/bin/env python

import boto3
low_level_client = boto3.client('ec2')
keypairs = low_level_client.describe_key_pairs()


# Go to high level
ec2 = boto3.resource('ec2', region_name = 'us-east-2')

key_pair = 'aws_ssh_key'
subnet ='subnet-6dfc4017'

instances = ec2.create_instances(
        ImageId='ami-2a0f324f', 
        MinCount=1, 
        MaxCount=1,
        InstanceType="t2.micro",        
    KeyName='aws_ssh_key',

    NetworkInterfaces=[{'SubnetId': subnet, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': ['sg-bfe75ad5']}])
       
work =['app', 'db']

i=0
for instance in instances:
    instance.create_tags(Tags=[{"Key": "Name", "Value": work[i] }])
    
    instance.wait_until_running()
    i = i+1
i=0
for instance in instances:
    print(instance.id, instance.instance_type, instance.vpc, instance.private_ip_address, instance.public_ip_address)
    f = open('hosts', 'a') 
    f.write("[%s]" % (work[i]) + '\n' + instance.private_ip_address + '\n' ) 
    f.close()
   # f = open('host1', 'a') 
   # f.write(instance.private_ip_address + "    "+ work[i] + '\n' ) 
   # f.close()
    i = i+1 
