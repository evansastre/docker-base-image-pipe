FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ENV LANG C.UTF-8
ENV JAVA_HOME /usr/lib/jvm/zulu-8
ENV PATH $JAVA_HOME/bin:$PATH

WORKDIR /app

ARG JOB_TOKEN

RUN mkdir /app/{gc,dumps}

# zulujdk 8
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/8/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -o /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm && yum localinstall /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -y && rm -rf /root/*.rpm

# add
ADD devops-base/java/resources/skywalking-agent.tar.gz /app/skywalking/

ENTRYPOINT ["java","--version"]


