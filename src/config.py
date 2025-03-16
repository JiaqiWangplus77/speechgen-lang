import os
import boto3

def get_polly_client():
    """获取 AWS Polly 客户端"""
    return boto3.client("polly", region_name="eu-central-1")