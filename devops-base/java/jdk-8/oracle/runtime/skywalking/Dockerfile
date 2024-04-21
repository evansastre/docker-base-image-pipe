FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ENV LANG C.UTF-8
ENV JAVA_HOME /usr/java/jdk1.8.0_311-amd64/
ENV PATH $JAVA_HOME/bin:$PATH

WORKDIR /app

ARG JOB_TOKEN

RUN mkdir /app/{gc,dumps}

# oraclejdk 8
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/8/jdk-8u311-linux-x64.rpm -o /root/jdk-8u311-linux-x64.rpm && yum localinstall /root/jdk-8u311-linux-x64.rpm -y && rm -rf /root/*.rpm

# add
ADD devops-base/java/resources/skywalking-agent.tar.gz /app/skywalking/

ENTRYPOINT ["java","--version"]


