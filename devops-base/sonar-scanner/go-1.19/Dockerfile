FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ARG JOB_TOKEN

RUN yum install -y unzip findutils mysql-devel golang

RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/sonar-scanner/4.8/sonar-scanner-4.8.0.2856-linux.zip -o /opt/sonar-scanner-4.8.0.2856-linux.zip \
    && unzip /opt/sonar-scanner-4.8.0.2856-linux.zip

RUN adduser admin
USER admin

RUN go install gotest.tools/gotestsum@latest

ENV PATH="$PATH:/sonar-scanner-4.8.0.2856-linux/bin/:/home/admin/go/bin"


