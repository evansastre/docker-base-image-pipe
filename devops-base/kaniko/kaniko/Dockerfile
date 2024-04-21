FROM office-registry-vpc.cn-hongkong.cr.aliyuncs.com/office-base/kaniko-executor:debug-v1

ARG gitlab_package_registry_docker_base_1443_token

# install curl
# COPY devops-base/kaniko/kaniko/curl /usr/local/bin/curl 
# RUN chmod +x /usr/local/bin/cur
RUN wget --no-check-certificate  --header "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token"  https://gitlab.example.com/api/v4/projects/1443/packages/generic/curl/i386/curl \
    && mv curl /usr/local/bin/curl \
    && chmod +x /usr/local/bin/curl

# install jq
# RUN curl -k  --header  "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token"  https://gitlab.example.com/api/v4/projects/1443/packages/generic/jq/1.6/jq -o /usr/local/bin/jq \
#     && chmod +x /usr/local/bin/jq 
RUN wget --no-check-certificate  --header "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token"  https://gitlab.example.com/api/v4/projects/1443/packages/generic/jq/1.6/jq \
    && mv jq /usr/local/bin/jq \
    && chmod +x /usr/local/bin/jq


# install docker
# RUN curl -k  --header "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token" https://gitlab.example.com/api/v4/projects/1443/packages/generic/docker/24.0.4/docker -o  /usr/local/bin/docker  \
#     && chmod +x /usr/local/bin/docker 
RUN wget --no-check-certificate  --header "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token" https://gitlab.example.com/api/v4/projects/1443/packages/generic/docker/24.0.4/docker \
    && mv docker /usr/local/bin/docker \
    && chmod +x /usr/local/bin/docker

