FROM dockerregistry.com/office-base/amazonlinux:2023-example2

RUN pip3 install kubernetes==21.7.0 \
    && pip3 install boto3==1.28.40

COPY devops-base/recycle-image/test-ecr/recycleImage.py /opt/recycleImage.py

ENTRYPOINT ["python3","/opt/recycleImage.py"]


