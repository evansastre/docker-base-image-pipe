
# upload package
curl --header "PRIVATE-TOKEN: <your_access_token>" --upload-file node-v10.15.3-linux-x64.tar.xz "https://gitlab.example.com/api/v4/projects/6383/packages/generic/node/10.15.3/node-v10.15.3-linux-x64.tar.xz"

# download package
RUN curl --header "PRIVATE-TOKEN: <your_access_token>" https://gitlab.example.com/api/v4/projects/6383/packages/generic/node/10.15.3/node-v10.15.3-linux-x64.tar.xz -o /node-v10.15.3-linux-x64.tar.xz \
    && tar -xf /node-v10.15.3-linux-x64.tar.xz \
    && chmod 755 /node-v10.15.3-linux-x64/bin/* \
    && ln -s /node-v10.15.3-linux-x64/bin/* /usr/local/bin/