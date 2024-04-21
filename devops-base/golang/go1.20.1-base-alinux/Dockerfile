FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

WORKDIR /tmp

# RUN wget https://go.dev/dl/go1.20.1.linux-amd64.tar.gz && tar -C /usr/local/ -xzf go1.20.1.linux-amd64.tar.gz && \\
RUN yum update -y  && \ 
    yum install -y gcc glibc-devel  && \   
    wget https://mirrors.aliyun.com/golang/go1.20.1.linux-amd64.tar.gz && tar -C /usr/local/ -xzf go1.20.1.linux-amd64.tar.gz && \
    rm -rf /tmp/*

ENV GOLANG_VERSION 1.20.1
ENV GOPATH /usr/local/go
ENV PATH $GOPATH/bin:$PATH
ENV GOROOT /usr/local/go
RUN chmod -R 777 "$GOPATH" && go version