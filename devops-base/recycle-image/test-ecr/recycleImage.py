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

ecraddress = os.getenv("ECR_ADDRESS", "463216706112.dkr.ecr.ap-east-1.amazonaws.com")
excludeImageName = os.getenv("EXCLUDE_IMAGE_NAME", "['office/base/','online/']")
KUBERNETES_SERVICE_HOST = os.environ.get('KUBERNETES_SERVICE_HOST','10.238.0.1')
KUBERNETES_SERVICE_PORT = os.environ.get('KUBERNETES_SERVICE_PORT','443')
awsAccessKeyId = os.environ.get('AWS_ACCESS_KEY_ID','')
awsSecretAccessKey = os.environ.get('AWS_SECRET_ACCESS_KEY','')
regionName = os.environ.get('REGION_NAME','ap-east-1')

def excludeImage(excludeImageName,image):
    excludeImageName = eval(excludeImageName)
    for i in excludeImageName:
        if i in image:
            return True

def deleteEcrImage(queryUsingImageDict,queryEcrImageDict):
    for k,v in queryEcrImageDict.items():
        if queryUsingImageDict.get(k,None) == None:
            logging.info("扫描到ecr中镜像仓库【%s】未在集群运行时中引用,运行时仓库列表为【%s】,将删除此仓库", k, queryUsingImageDict)
            response = ecrClient.delete_repository(
                repositoryName=k,
                force=True
            )
        else:
            for ecrTag in v:
                if ecrTag not in queryUsingImageDict[k]:
                    logging.info("扫描到ecr中镜像仓库【%s】tag【%s】未在集群运行时中引用,运行时tag为【%s】,将删除此tag", k, ecrTag, queryUsingImageDict[k])
                    response = ecrClient.batch_delete_image(
                        repositoryName=k,
                        imageIds=[
                            {
                                'imageTag': ecrTag,
                            },
                        ]
                    )


def queryUsingImage():
    queryUsingImageDict = {}
    AppsV1ApiIns = client.AppsV1Api()
    CoreV1ApiIns = client.CoreV1Api()
    deployments = AppsV1ApiIns.list_deployment_for_all_namespaces().items
    statefulsets = AppsV1ApiIns.list_stateful_set_for_all_namespaces().items
    pods = CoreV1ApiIns.list_pod_for_all_namespaces().items
    for pod in pods:
        podNamespace = pod.metadata.namespace
        podName = pod.metadata.name
        containers = pod.spec.containers
        for container in containers:
            image = container.image
            if image and ecraddress in image:
                if excludeImage(excludeImageName=excludeImageName,image=image):
                    continue
                logging.info("扫描到环境【%s】应用【%s】正在使用镜像名称【%s】", podNamespace, podName, image)
                imageName = image.split(":")[0]
                repositoryName = '/'.join(imageName.split('/')[1:])
                imageTag = "latest" if len(image.split(":")) == 1 else image.split(":")[-1]
                queryUsingImageDict.setdefault(repositoryName, [])
                if imageTag not in queryUsingImageDict[repositoryName]:
                    queryUsingImageDict[repositoryName].append(imageTag)
    for deployment in deployments:
        containers = deployment.spec.template.spec.containers
        appNamespace = deployment.metadata.namespace
        appName = deployment.metadata.name
        for container in containers:
            image = container.image
            if image and ecraddress in image:
                if excludeImage(excludeImageName=excludeImageName,image=image):
                    continue
                logging.info("扫描到环境【%s】应用【%s】正在使用镜像名称【%s】", appNamespace,appName,image)
                imageName = image.split(":")[0]
                repositoryName = '/'.join(imageName.split('/')[1:])
                imageTag = "latest" if len(image.split(":")) == 1 else image.split(":")[-1]
                queryUsingImageDict.setdefault(repositoryName,[])
                if imageTag not in queryUsingImageDict[repositoryName]:
                    queryUsingImageDict[repositoryName].append(imageTag)
    for statefulset in statefulsets:
        containers = statefulset.spec.template.spec.containers
        appNamespace = statefulset.metadata.namespace
        appName = statefulset.metadata.name
        for container in containers:
            image = container.image
            if image and ecraddress in image:
                if excludeImage(excludeImageName=excludeImageName,image=image):
                    continue
                logging.info("扫描到环境【%s】应用【%s】正在使用镜像名称【%s】", appNamespace,appName,image)
                imageName = image.split(":")[0]
                repositoryName = '/'.join(imageName.split('/')[1:])
                imageTag = "latest" if len(image.split(":")) == 1 else image.split(":")[-1]
                queryUsingImageDict.setdefault(repositoryName,[])
                if imageTag not in queryUsingImageDict[repositoryName]:
                    queryUsingImageDict[repositoryName].append(imageTag)
    runningImageSum = 0
    for k,v in queryUsingImageDict.items():
        runningImageSum += 1
        logging.info("扫描到集群运行时镜像列表为【%s】 Tag为【%s】", k, v)

    return queryUsingImageDict

def queryEcrImage():
    queryEcrImageDict = {}
    ecrResponse = ecrClient.describe_repositories()["repositories"]
    for e in ecrResponse:
        if excludeImage(excludeImageName=excludeImageName, image=e['repositoryName']):
            continue
        repositoryName = e['repositoryName']
        ecrImagesList = ecrClient.list_images(
            repositoryName=e['repositoryName'],
            maxResults=1000,
        )
        queryEcrImageDict.setdefault(repositoryName, [])
        for ecrimageTag in ecrImagesList["imageIds"]:
            if ecrimageTag.get("imageTag", None) != None:
                queryEcrImageDict[repositoryName].append(ecrimageTag["imageTag"])
    for k,v in queryEcrImageDict.items():
        logging.info("扫描到ecr镜像列表为【%s】 Tag为【%s】", k, v)
    return queryEcrImageDict
def cleanImage():
    queryUsingImageDict = queryUsingImage()
    queryEcrImageDict = queryEcrImage()
    deleteEcrImage(queryUsingImageDict,queryEcrImageDict)

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