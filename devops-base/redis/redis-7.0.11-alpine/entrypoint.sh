#! /bin/sh



if [ ! -f "/data/redis.conf" ];then
  cp /opt/redis.conf /data/redis.conf
fi

sed -i  -e '23c masterauth '"$PASSWORD"'' -e '35c requirepass '"$PASSWORD"''  /data/redis.conf

python3 /root/redis-k8s.py
redis-server /data/redis.conf

