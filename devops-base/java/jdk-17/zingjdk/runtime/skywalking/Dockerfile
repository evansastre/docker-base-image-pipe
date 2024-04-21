FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ENV LANG C.UTF-8
ENV JAVA_HOME /opt/zing/zing-jdk17.0.0-23.08.201.0-1-x86_64/
ENV PATH $JAVA_HOME/bin:$PATH

WORKDIR /app

ARG JOB_TOKEN

RUN mkdir /app/{gc,dumps}

# zingjdk 17
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/17/zing23.08.201.0-1-jdk17.0.9-linux.x86_64.rpm -o /root/zing23.08.201.0-1-jdk17.0.9-linux.x86_64.rpm && yum localinstall /root/zing23.08.201.0-1-jdk17.0.9-linux.x86_64.rpm -y && rm -rf /root/*.rpm

# add
ADD devops-base/java/resources/skywalking-agent.tar.gz /app/skywalking/

ENTRYPOINT ["java","--version"]

