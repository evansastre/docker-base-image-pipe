FROM dockerregistry.com/base/alinux3:230602.1-example2

ARG JOB_TOKEN
WORKDIR /

# repo epel from fluentbit
RUN echo -e "[fluent-bit]\nname = Fluent Bit\nbaseurl = https://packages.fluentbit.io/centos/7/$basearch/\ngpgcheck=1\ngpgkey=https://packages.fluentbit.io/fluentbit.key\nrepo_gpgcheck=1\nenabled=1" >> /etc/yum.repos.d/fluent-bit.repo

RUN yum install -y fluent-bit && rm -rf /etc/fluent-bit/* && \
    yum clean all && \
    rm -rf /var/cache/yum