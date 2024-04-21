FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/office-base/amazonlinux:2023

RUN yum install zip -y \
    && yum install python3-pip -y \
    && pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip3 config set install.trusted-host mirrors.aliyun.com

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

