FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/go:1.20.1.linux-amd64-example1

ARG JOB_TOKEN

RUN yum install -y unzip findutils mysql-devel git

RUN adduser admin
USER admin

WORKDIR /home/admin

RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/sonar-scanner/4.8/sonar-scanner-4.8.0.2856-linux.zip -o ~/sonar-scanner-4.8.0.2856-linux.zip \
    && unzip ~/sonar-scanner-4.8.0.2856-linux.zip

RUN go install gotest.tools/gotestsum@latest

ENV PATH="$PATH:~/sonar-scanner-4.8.0.2856-linux/bin/:/home/admin/go/bin"


