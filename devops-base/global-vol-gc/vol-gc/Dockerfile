FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

RUN yum install python3 -y

RUN pip3 install kubernetes==21.7.0

COPY devops-base/global-vol-gc/vol-gc/globalVolClean.py /opt/globalVolClean.py

ENTRYPOINT ["python3","/opt/globalVolClean.py"]


