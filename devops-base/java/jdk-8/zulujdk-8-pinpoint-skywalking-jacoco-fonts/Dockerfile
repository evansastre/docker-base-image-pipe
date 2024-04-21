FROM dockerregistry.com/office-base/zulujdk-8:3.8.8-jacoco-example2

ARG gitlab_package_registry_docker_base_1443_token

RUN yum install -y fontconfig mkfontscale unzip GraphicsMagick  ghostscript libpng libjpeg

RUN curl -k --header "PRIVATE-TOKEN: $gitlab_package_registry_docker_base_1443_token" https://gitlab.example.com/api/v4/projects/1443/packages/generic/fonts/1.0.0/Fonts.zip -o /tmp/Fonts.zip --create-dirs \
    && unzip /tmp/Fonts.zip -d /tmp \
    && mkdir -p /usr/share/fonts/chinese \
    && chmod -R 755 /usr/share/fonts/chinese \
    && mv /tmp/Fonts /usr/share/fonts/chinese \
    && cd  /usr/share/fonts/chinese \
    && mkfontscale
