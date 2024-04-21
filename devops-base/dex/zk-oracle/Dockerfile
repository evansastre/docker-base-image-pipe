FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/office-base/jdk-8:3.8.8-example1

ARG JOB_TOKEN

# nvm env vars
RUN mkdir -p /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v16.15.1
ENV PATH="/tmp/node-${NODE_VERSION}-linux-x64/bin:${PATH}"

RUN curl -k -o /tmp/node-${NODE_VERSION}-linux-x64.tar.xz https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz \
    && tar -xf /tmp/node-v16.15.1-linux-x64.tar.xz -C /tmp \
    && npm install -g snarkjs@0.6.10
