FROM dockerregistry.com/office-base/node:20.11.1

ARG JOB_TOKEN
# 安装 sonar-scanner-cli
RUN curl --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/sonar-scanner/4.8/sonar-scanner-4.8.0.2856-linux.zip -o /sonar-scanner-4.8.0.2856-linux.zip \
    && unzip /sonar-scanner-4.8.0.2856-linux.zip \
    && ln -s /sonar-scanner-4.8.0.2856-linux/bin/sonar-scanner /usr/local/bin/

# 安装 jq命令
RUN apt-get update && \
    apt-get install -y jq   
# RUN echo 'deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib' > /etc/apt/sources.list \
#     && apt update \
#     && apt install -y jq

# 设置时区，前端单测依赖时区
ENV TZ=Asia/Shanghai

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["node"]