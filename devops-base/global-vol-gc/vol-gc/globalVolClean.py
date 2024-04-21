import logging
import os,sys
import shutil
from kubernetes import client,config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s[line :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)

globalVolPath = eval(os.getenv("GLOBAL_VOL_PATH", "['/Users/evans/data/office-base-cluster','/Users/evans/data/office-dev-cluster','/Users/evans/data/office-test-cluster','/Users/evans/data/office-chaos-cluster',]"))




def deletePath(historyPathDict,pathDict):
    for clusterPath in globalVolPath:
        cluster = clusterPath.split('/')[-1]
        if pathDict.get(cluster,None) != None:
            for ns in historyPathDict[cluster]:
                if pathDict[cluster].get(ns,None) == None:
                    logging.info("开始删除目录【%s】", os.path.join(clusterPath,ns))
                    shutil.rmtree(os.path.join(clusterPath,ns))
                    continue
                for pods in historyPathDict[cluster][ns]:
                    if pods not in pathDict[cluster][ns]:
                        logging.info("开始删除目录【%s】", os.path.join(os.path.join(clusterPath, ns),pods))
                        try:
                            shutil.rmtree(os.path.join(os.path.join(clusterPath, ns),pods))
                        except :
                            print("Unexpected error:", sys.exc_info()[0])
def fetchGlobalPath(pathDict):
    historyPathDict = {}
    for p in globalVolPath:
        clusterNamePath = p.split('/')[-1]
        historyPathDict.setdefault(clusterNamePath,{})
        logging.info("开始扫描目录【%s】下的子目录", p)
        for ns in os.listdir(p):
            if pathDict[clusterNamePath].get(ns, None) == None:
                logging.info("开始删除目录【%s】", os.path.join(p, ns))
                try:
                    shutil.rmtree(os.path.join(p, ns))
                except:
                    print("Unexpected error:", sys.exc_info()[0])
                continue
            historyPathDict[clusterNamePath].setdefault(ns,[])
            for service in os.listdir(os.path.join(p,ns)):
                for pod in os.listdir(os.path.join(os.path.join(p,ns),service)):
                    if pod not in pathDict[clusterNamePath][ns]:
                        logging.info("开始删除目录【%s】", os.path.join(os.path.join(os.path.join(p, ns),service),pod))
                        try:
                            shutil.rmtree(os.path.join(os.path.join(os.path.join(p, ns),service),pod))
                        except :
                            print("Unexpected error:", sys.exc_info()[0])

    return historyPathDict
def fetchPath():
    pathDict = {}
    for context in clusterContext:
        pathDict.setdefault(context,{})
        config.kube_config.load_kube_config(config_file=config_file, context=context)
        CoreV1ApiIns = client.CoreV1Api()
        pods = CoreV1ApiIns.list_pod_for_all_namespaces().items
        for pod in pods:
            podNamespace = pod.metadata.namespace
            podName = pod.metadata.name
            if pathDict[context].get(podNamespace,None) == None:
                pathDict[context].setdefault(podNamespace,[])
            pathDict[context][podNamespace].append(podName)
    return pathDict
def clean():
    pathDict = fetchPath()
    historyPathDict = fetchGlobalPath(pathDict)



if __name__ == '__main__':
    config_file = F"~/.kube/config"
    clusterContext = [c.split("/")[-1] for c in globalVolPath]
    print(clusterContext)
    clean()

