FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ARG JOB_TOKEN
RUN yum install -y python38 python38-pip unzip findutils mysql-devel
RUN pip3.8 install coverage pytest pytest-cov 
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/sonar-scanner/4.8/sonar-scanner-4.8.0.2856-linux.zip -o /sonar-scanner-4.8.0.2856-linux.zip \
    && unzip /sonar-scanner-4.8.0.2856-linux.zip \
    && ln -s /sonar-scanner-4.8.0.2856-linux/bin/sonar-scanner /usr/local/bin/
RUN adduser admin 
USER admin