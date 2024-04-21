# FROM office-registry.cn-hongkong.cr.aliyuncs.com/office-base/centos:7.4.1708
FROM dockerregistry.com/base/alinux3:230602.1-example2
# FROM dockerregistry.com/office-base/alinux3:230602.1-example1
# FROM online-dockerregistry.com/base/alinux3:230602.1-example1
ARG JOB_TOKEN

ENV PATH="/usr/local/python3/bin:${PATH}"
ENV GIT_PYTHON_REFRESH=quiet
ENV LC_ALL=en_US.utf8

# os common dependencies
RUN yum update -y \
    && yum install gcc-c++ gcc openssl-devel bzip2-devel libffi-devel python3-libs git jq -y

# maven
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/maven/3.8.4/apache-maven-3.8.4-bin.tar.gz   -o /apache-maven-3.8.4-bin.tar.gz  \
    && tar xzvf apache-maven-3.8.4-bin.tar.gz \
    && ln -s /apache-maven-3.8.4/bin/mvn /usr/local/bin/mvn \
    && rm -rf /apache-maven-3.8.4-bin.tar.gz


# jdk 8 11 17
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/8/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -o /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm \
    && curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/jdk/11/jdk-11.0.13_linux-x64_bin.rpm   -o /root/jdk-11.0.13_linux-x64_bin.rpm \
    && curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/17/zulu17.44.53-ca-jdk17.0.8.1-linux.x86_64.rpm  -o /root/zulu17.44.53-ca-jdk17.0.8.1-linux.x86_64.rpm \
    && yum localinstall /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm  -y \
    && yum localinstall /root/jdk-11.0.13_linux-x64_bin.rpm -y \
    && yum localinstall /root/zulu17.44.53-ca-jdk17.0.8.1-linux.x86_64.rpm -y \
    && rm -rf /root/*.rpm

# default jdk8
RUN echo '1' |  alternatives --config java

# Development Tools
RUN yum group info 'Development Tools' \
    && yum groupupdate 'Development Tools' -y \
    && yum groups mark install 'Development Tools' -y  \
    && yum groupinstall "Development Tools" -y

# remove default jdk 
RUN alternatives --remove java /usr/lib/jvm/java-1.8.0-alibaba-dragonwell-8.15.16.372-2.al8.x86_64/jre/bin/java &&  \
    yum remove java-11-openjdk-headless.x86_64 -y

# python3
# RUN echo export PATH="/usr/local/python3/bin:$PATH" >> ~/.bashrc \
#     && source ~/.bashrc
RUN wget --no-check-certificate  --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/python3/3.7.17/Python-3.7.17.tar.xz   \
    && xz -d Python-3.7.17.tar.xz \
    && tar -xf Python-3.7.17.tar \
    && cd Python-3.7.17 \
    && ./configure prefix=/usr/local/python3 --enable-optimizations \
    && make  \
    && make install \
    && rm -rf /Python-3.7.17.tar

RUN ln -sf /usr/local/python3/bin/python3.7 /usr/bin/python3 \
    && ln -sf /usr/local/python3/bin/pip3 /usr/bin/pip3 \
    && python3 -m pip install --upgrade pip

RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple \
    && pip3 config set install.trusted-host mirrors.aliyun.com


RUN pip3 install kubernetes \
    && pip3 install oss2  \
    && pip3 install urllib3  \
    && pip3 install numpy  \
    && pip3 install python-gitlab  \
    && pip3 install beautifulsoup4 \
    && pip3 install lxml  \
    && pip3 install GitPython==3.1.30  \
    && pip3 install plutonium-238


# && pip3 install gitpython -i http://pypi.douban.com/simple --trusted-host pypi.douban.com \

# docker-compose jupiter-server项目单测会用到
RUN yum install -y yum-utils \
    && yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo \
    && sed -i 's/\$releasever/7/g' /etc/yum.repos.d/docker-ce.repo \
    && yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y \
    && curl -kSL https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose \
    && chmod 755 /usr/local/bin/docker-compose


ENTRYPOINT ["java","--version"]
