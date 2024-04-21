FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ARG JOB_TOKEN
WORKDIR /app

# Install jacoco and prometheus
RUN curl -k https://nexus.example.com/repository/maven-central/io/prometheus/jmx/jmx_prometheus_javaagent/0.16.1/jmx_prometheus_javaagent-0.16.1.jar -o /app/jmx_exporter/jmx_prometheus_javaagent-0.16.1.jar --create-dirs && \
    curl -k https://nexus.example.com/repository/maven-central/org/jacoco/org.jacoco.agent/0.8.10/org.jacoco.agent-0.8.10-runtime.jar -o /app/jacoco/jacocoagent.jar --create-dirs

# jdk 11
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/jdk/11/jdk-11.0.13_linux-x64_bin.rpm   -o /root/jdk-11.0.13_linux-x64_bin.rpm && yum localinstall /root/jdk-11.0.13_linux-x64_bin.rpm -y && rm -rf /root/*.rpm

## add maven 3.8.8
RUN curl -k https://dlcdn.apache.org/maven/maven-3/3.8.8/binaries/apache-maven-3.8.8-bin.tar.gz -o /tmp/apache-maven-3.8.8-bin.tar.gz && \
    tar xzvf /tmp/apache-maven-3.8.8-bin.tar.gz && \
    ln -s /apache-maven-3.8.8/bin/mvn /usr/bin/mvn && \
    rm -rf /tmp/apache-maven-3.8.8-bin.tar.gz

# add
ADD devops-base/java/resources/jacoco-0.8.7 /app/jacoco-0.8.7
ADD devops-base/java/resources/pinpoint-agent-1.8.2.tar.gz /app/pinpoint-agent/
ADD devops-base/java/resources/skywalking-agent.tar.gz /app/skywalking/
ADD devops-base/java/resources/prometheus-jmx-config.yaml /app/jmx_exporter/
ADD devops-base/java/resources/jmx.access /app/
ADD devops-base/java/resources/jmx.password /app/
RUN chmod 400 /app/jmx.password

ENTRYPOINT ["java","--version"]
