FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example1

## add java 11
RUN yum install -y java-11 jq curl wget git

## add maven 3.8.8
RUN curl -k https://dlcdn.apache.org/maven/maven-3/3.8.8/binaries/apache-maven-3.8.8-bin.tar.gz -o /tmp/apache-maven-3.8.8-bin.tar.gz && \
    tar xzvf /tmp/apache-maven-3.8.8-bin.tar.gz && \
    ln -s /apache-maven-3.8.8/bin/mvn /usr/bin/mvn && \
    rm -rf /tmp/apache-maven-3.8.8-bin.tar.gz

RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq && chmod +x /usr/bin/yq

ENTRYPOINT ["java","--version"]
