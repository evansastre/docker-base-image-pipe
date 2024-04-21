import logging
import os
import boto3
from kubernetes import client
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

excludeImageName = os.getenv("EXCLUDE_IMAGE_NAME", "['online/base/','office/']")
KUBERNETES_SERVICE_HOST = os.environ.get('KUBERNETES_SERVICE_HOST','')
KUBERNETES_SERVICE_PORT = os.environ.get('KUBERNETES_SERVICE_PORT','')
awsAccessKeyId = os.environ.get('AWS_ACCESS_KEY_ID','')
awsSecretAccessKey = os.environ.get('AWS_SECRET_ACCESS_KEY','')
regionName = os.environ.get('REGION_NAME','ap-east-1')

def excludeImage(excludeImageName,image):
    excludeImageName = eval(excludeImageName)
    for i in excludeImageName:
        if i in image:
            return True

def queryEcrImage():
    queryEcrRepositoryList = []
    ecrResponse = ecrClient.describe_repositories()["repositories"]
    for e in ecrResponse:
        repositoryName = e['repositoryName']
        if excludeImage(excludeImageName=excludeImageName, image=repositoryName):
            continue
        queryEcrRepositoryList.append(repositoryName)
    return queryEcrRepositoryList

def putLifecyclePolicy(queryEcrRepositoryList):
    print(queryEcrRepositoryList)
    for k in queryEcrRepositoryList:
        response = ecrClient.put_lifecycle_policy(
            repositoryName=k,
            lifecyclePolicyText='''{
              "rules": [
                {
                  "rulePriority": 1,
                  "description": "recycling policy",
                  "selection": {
                    "tagStatus": "any",
                    "countType": "imageCountMoreThan",
                    "countNumber": 20
                  },
                  "action": {
                    "type": "expire"
                  }
                }
              ]
            }'''
        )
        logging.info("正在为仓库【%s】 添加生命周期策略,返回结果【%s】", k,response)


def cleanImage():
    queryEcrRepositoryList = queryEcrImage()
    putLifecyclePolicy(queryEcrRepositoryList)


if __name__ == '__main__':
    #构造apiserver client
    apiserver = 'https://'+ KUBERNETES_SERVICE_HOST + ":" + KUBERNETES_SERVICE_PORT
    with open('/var/run/secrets/kubernetes.io/serviceaccount/token', 'r') as file:
        Token = file.read().strip('\n')
    configuration = client.Configuration()
    configuration.host = apiserver
    configuration.verify_ssl = False
    configuration.api_key = {"authorization": "Bearer " + Token}
    client.Configuration.set_default(configuration)
    #构造ecr client
    ecrClient = boto3.client('ecr',region_name=regionName,aws_access_key_id=awsAccessKeyId,aws_secret_access_key=awsSecretAccessKey)

    #删除回收image入口函数
    cleanImage()