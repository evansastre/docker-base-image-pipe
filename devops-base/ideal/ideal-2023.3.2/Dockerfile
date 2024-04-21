FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/base/alinux3:230602.1-example3

ARG JOB_TOKEN

# jdk 11
RUN curl -k --header "JOB-TOKEN: $JOB_TOKEN" https://gitlab.example.com/api/v4/projects/1443/packages/generic/jdk/11/jdk-11.0.13_linux-x64_bin.rpm   -o /root/jdk-11.0.13_linux-x64_bin.rpm && yum localinstall /root/jdk-11.0.13_linux-x64_bin.rpm -y && rm -rf /root/*.rpm
# 下载 IntelliJ IDEA 2023.3.2 版本
RUN wget --no-check-certificate -O idea.tar.gz https://download-cf.jetbrains.com/idea/ideaIC-2023.3.2.tar.gz \
    && tar -xzf idea.tar.gz \
    && rm idea.tar.gz
    

# 设置环境变量
ENV PATH="/idea-IC-233.13135.103/bin:${PATH}"
