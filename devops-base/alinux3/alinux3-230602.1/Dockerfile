FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1

# repo epel from aliyun
RUN yum -y update  && \
    echo -e "[centos-updates]\nname=CentOS-7 - Updates\nbaseurl=http://mirror.centos.org/centos/7/updates/\$basearch/\nenabled=1\ngpgcheck=1\ngpgkey=http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7" >> /etc/yum.repos.d/centos-updates.repo 

ARG ARG gitlab_package_registry_docker_base_1443_token
RUN yum install -y fontconfig mkfontscale unzip
RUN mkdir -p /usr/share/fonts/chinese \
    && chmod -R 755 /usr/share/fonts/chinese \
    && curl -k --header "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token" https://gitlab.example.com/api/v4/projects/1443/packages/generic/fonts/1.0.0/Fonts.zip -o /tmp/Fonts.zip --create-dirs \
    && unzip /tmp/Fonts.zip -d /tmp \
    && mv /tmp/Fonts/* /usr/share/fonts/chinese \
    && cd  /usr/share/fonts/chinese \
    && mkfontscale

# security tool and os common dependencies/tool 
RUN yum -y install nss-3.79.0-5.el7_9.x86_64 && \
    yum update -y libstdc++.x86_64 libstdc++.i686 && \
    yum -y install vim wget telnet net-tools iputils tar jq curl tcpdump bind-utils lsof git && \
    echo "alias ll='ls -l'" >> ~/.bashrc && \
    yum clean all && \
    rm -rf /var/cache/yum

#RUN echo
RUN echo -e "export LANG=en_US.UTF-8\nexport LC_CTYPE=en_US.UTF-8\nexport LC_NUMERIC=zh_CN.UTF-8\nexport LC_TIME=zh_CN.UTF-8\nexport LC_COLLATE=en_US.UTF-8\nexport LC_MONETARY=zh_CN.UTF-8\nexport LC_MESSAGES=en_US.UTF-8\nexport LC_PAPER=zh_CN.UTF-8\nexport LC_NAME=zh_CN.UTF-8\nexport LC_ADDRESS=zh_CN.UTF-8\nexport LC_TELEPHONE=zh_CN.UTF-8\nexport LC_MEASUREMENT=zh_CN.UTF-8\nexport LC_IDENTIFICATION=zh_CN.UTF-8\n" >> ~/.bashrc

# Set timezone to CST
RUN rm -f /etc/localtime && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && date


CMD ["/bin/bash"]
