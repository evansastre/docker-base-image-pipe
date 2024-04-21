# docker_image_base

# 基础镜像升级策略
* $type    # 镜像类型，按照语言或类型区分，比如: java,golang,nginx..
* $version   # 类型对应的版本

1. 将基础镜像推送到线上的base命名空间,将经过安全组修改的镜像临时命名为: \$type:\$version-temp;
2. 按照服务优先级做灰度;
3. 将经过灰度验证后的基础镜像重新命名为一个release镜像，该命名策略规范为: \$type:\$verion-example{1....n};
4. 自动化升级所有项目的基础镜像为安全修复后的release镜像;



# 项目结构说明1
```
docker_image_base
|
│
└───devops-base        # 生产环境基础镜像
│   │
│   └───$type    # 镜像类型，按照语言或类型区分，比如: java,golang,nginx..
│       │
│       └──$version   # 类型对应的版本
│           │
│           └───Dockerfile          │
│           └───Dockerfile.conf   
│

```
