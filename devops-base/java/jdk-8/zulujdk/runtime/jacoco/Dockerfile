FROM dockerregistry.com/base/alinux3:230602.1-example2

ENV LANG C.UTF-8
ENV JAVA_HOME /usr/lib/jvm/zulu-8
ENV PATH $JAVA_HOME/bin:$PATH

WORKDIR /app

ARG JOB_TOKEN

# zulujdk 8
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/6383/packages/generic/jdk/8/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -o /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm && yum localinstall /root/zulu8.60.0.21-ca-jdk8.0.322-linux.x86_64.rpm -y && rm -rf /root/*.rpm

# Install jacoco and prometheus
RUN curl -k https://nexus.example.com/repository/maven-central/io/prometheus/jmx/jmx_prometheus_javaagent/0.16.1/jmx_prometheus_javaagent-0.16.1.jar -o /app/jmx_exporter/jmx_prometheus_javaagent-0.16.1.jar --create-dirs && \
    curl -k https://nexus.example.com/repository/maven-central/org/jacoco/org.jacoco.agent/0.8.10/org.jacoco.agent-0.8.10-runtime.jar -o /app/jacoco/jacocoagent.jar --create-dirs

# add
ADD devops-base/java/resources/test/skywalking-agent.tar.gz /app/skywalking/
ADD devops-base/java/resources/jacoco-0.8.7 /app/jacoco-0.8.7
ADD devops-base/java/resources/prometheus-jmx-config.yaml /app/jmx_exporter/
ADD devops-base/java/resources/jmx.access /app/
ADD devops-base/java/resources/jmx.password /app/
RUN chmod 400 /app/jmx.password

ENTRYPOINT ["java","--version"]

