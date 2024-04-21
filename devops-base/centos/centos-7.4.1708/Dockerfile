#FROM centos:7.4.1708
FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/office-base/centos:7.4.1708

# repo epel from aliyun
RUN yum -y update \
    && curl https://mirrors.aliyun.com/epel/epel-release-latest-7.noarch.rpm -o epel-release-latest-7.noarch.rpm \
    && rpm -ivh epel-release-latest-7.noarch.rpm \
    && yum clean all \ 
    && yum makecache \ 
    && yum repolist 

RUN yum -y install nss-3.79.0-5.el7_9.x86_64 && \
    yum -y install vim wget telnet net-tools && \
    echo "alias ll='ls -l'" >> ~/.bashrc && \
    yum clean all && \
    rm -rf /var/cache/yum

CMD ["/bin/bash"]




