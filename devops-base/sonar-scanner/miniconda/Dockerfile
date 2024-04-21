FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example2

ARG JOB_TOKEN
ARG USERNAME=admin
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN yum install -y unzip findutils mysql-devel

RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/sonar-scanner/4.8/sonar-scanner-4.8.0.2856-linux.zip -o /opt/sonar-scanner-4.8.0.2856-linux.zip \
    && unzip /opt/sonar-scanner-4.8.0.2856-linux.zip

RUN adduser admin
USER admin
ENV PATH="$PATH:/sonar-scanner-4.8.0.2856-linux/bin/"

RUN mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 && \
    rm -rf ~/miniconda3/miniconda.sh
RUN ~/miniconda3/bin/conda init bash