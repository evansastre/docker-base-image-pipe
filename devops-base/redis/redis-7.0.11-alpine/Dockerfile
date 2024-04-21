FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/office-base/redis:7.0.11-alpine
RUN apk update
RUN apk add python3
RUN apk add py3-pip
RUN pip3 install kubernetes
RUN pip3 install --upgrade  urllib3
COPY devops-base/redis/redis-7.0.11-alpine/redis-k8s.py /root/redis-k8s.py
COPY devops-base/redis/redis-7.0.11-alpine/entrypoint.sh /root/entrypoint.sh
RUN  chmod 777 /root/entrypoint.sh

ENTRYPOINT ["/root/entrypoint.sh"]
