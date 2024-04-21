FROM dockerregistry.com/base/alinux3:230602.1-example2

ENV LANG C.UTF-8
ENV JAVA_HOME /usr/lib/jvm/zulu-8
ENV PATH $JAVA_HOME/bin:$PATH

ARG JOB_TOKEN

# zulujdk 8
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/8/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -o /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm && yum localinstall /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -y && rm -rf /root/*.rpm

## add maven 3.8.8
RUN curl -k https://dlcdn.apache.org/maven/maven-3/3.8.8/binaries/apache-maven-3.8.8-bin.tar.gz -o /tmp/apache-maven-3.8.8-bin.tar.gz && \
    tar xzvf /tmp/apache-maven-3.8.8-bin.tar.gz -C /opt && \
    ln -s /opt/apache-maven-3.8.8/bin/mvn /usr/bin/mvn && \
    rm -rf /tmp/apache-maven-3.8.8-bin.tar.gz

ENTRYPOINT ["java","--version"]
