FROM dockerregistry.com/office-base/zulujdk-8:3.8.8-jacoco-example2

ARG JOB_TOKEN

# nvm env vars
RUN mkdir -p /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION v16.15.1
ENV PATH="/tmp/node-${NODE_VERSION}-linux-x64/bin:${PATH}"

RUN curl -k -o /tmp/node-${NODE_VERSION}-linux-x64.tar.xz https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz \
    && tar -xf /tmp/node-v16.15.1-linux-x64.tar.xz -C /tmp \
    && npm install -g snarkjs@0.6.10

RUN yum install gcc gcc-c++ cmake gmp-devel libsodium libsodium-devel nasm curl m4 -y \
    && npm install express pm2 -g
