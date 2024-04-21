FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ARG JOB_TOKEN

# jdk 8
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/8/jdk-8u311-linux-x64.rpm   -o  /root/jdk-8u311-linux-x64.rpm && yum localinstall /root/jdk-8u311-linux-x64.rpm -y && rm -rf /root/*.rpm

## add maven 3.8.8
RUN curl -k https://dlcdn.apache.org/maven/maven-3/3.8.8/binaries/apache-maven-3.8.8-bin.tar.gz -o /tmp/apache-maven-3.8.8-bin.tar.gz && \
    tar xzvf /tmp/apache-maven-3.8.8-bin.tar.gz && \
    ln -s /apache-maven-3.8.8/bin/mvn /usr/bin/mvn && \
    rm -rf /tmp/apache-maven-3.8.8-bin.tar.gz

# RUN wget https://go.dev/dl/go1.19.1.linux-amd64.tar.gz && tar -C /usr/local/ -xzf go1.19.1.linux-amd64.tar.gz && \\
RUN yum update -y  && \
    yum install -y gcc glibc-devel  && \
    wget https://mirrors.aliyun.com/golang/go1.19.1.linux-amd64.tar.gz && tar -C /usr/local/ -xzf go1.19.1.linux-amd64.tar.gz && \
    rm -rf /tmp/*

ENV GOLANG_VERSION 1.19.1
ENV GOPATH /usr/local/go
ENV PATH $GOPATH/bin:$PATH
ENV GOROOT /usr/local/go
RUN chmod -R 777 "$GOPATH" && go version