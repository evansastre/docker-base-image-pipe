FROM office-registry.cn-hongkong.cr.aliyuncs.com/base/node:20.10.0-alpine-example1

RUN echo "https://mirrors.aliyun.com/alpine/v3.19/main/" > /etc/apk/repositories     && echo "https://mirrors.aliyun.com/alpine/v3.19/community" >> /etc/apk/repositories

RUN apk update

RUN apk add --no-cache udev ttf-freefont git

RUN apk add --no-cache chromium

RUN apk --update add procps && rm -rf /var/cache/apk/*