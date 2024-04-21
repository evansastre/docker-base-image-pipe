FROM dockerregistry.com/base/alinux3:230602.1-example2

ENV LANG C.UTF-8
ENV JAVA_HOME /usr/lib/jvm/java-17-zulu-openjdk-jdk/
ENV PATH $JAVA_HOME/bin:$PATH

WORKDIR /app

ARG JOB_TOKEN

RUN mkdir /app/{gc,dumps}

# jdk 17
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/17/zulu17.44.53-ca-jdk17.0.8.1-linux.x86_64.rpm -o /root/zulu17.44.53-ca-jdk17.0.8.1-linux.x86_64.rpm && yum localinstall /root/zulu17.44.53-ca-jdk17.0.8.1-linux.x86_64.rpm -y && rm -rf /root/*.rpm

# add
ADD devops-base/java/resources/skywalking-agent.tar.gz /app/skywalking/

ENTRYPOINT ["java","--version"]

