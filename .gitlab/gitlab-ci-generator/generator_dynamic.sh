# read from folder structure and create job for each foler which contain dockerfile

gitlab_ci_template_target="$(git rev-parse --show-toplevel)/.gitlab-ci-generate.yml" 
gitlab_ci_generator_dir=$(git rev-parse --show-toplevel)/.gitlab/gitlab-ci-generator
echo "Dockerfiles:  "  > $gitlab_ci_generator_dir/values.yaml
Dockerfiles_root="$(git rev-parse --show-toplevel)/devops-base"

#write Dockerfile name and Dockerfile path to values.yaml
for i in `find $Dockerfiles_root  -type f -name "Dockerfile*" | grep -v '\.conf$'`; \
    do  
        echo "  - Dockerfile: ${i##*/}" >> $gitlab_ci_generator_dir/values.yaml;  \
        Dockerfile_dir_abs_path="${i%/*}"; \
        Dockerfile_dir=${Dockerfile_dir_abs_path//$(git rev-parse --show-toplevel)\/}; \
        echo "    Dockerfile_dir: $Dockerfile_dir" >> $gitlab_ci_generator_dir/values.yaml; \
        echo "    image_name:  $(cat ${i}.conf  | jq -r .name )" >> $gitlab_ci_generator_dir/values.yaml; \
        echo "    image_tag:  $(cat ${i}.conf  | jq -r .version )" >> $gitlab_ci_generator_dir/values.yaml; \
        echo "    image_space:  $(cat ${i}.conf  | jq -r .online_space )" >> $gitlab_ci_generator_dir/values.yaml; \
        registry=$(cat ${i}.conf  | jq '.registry'); \
        if [[  $registry != "null" ]] ; then echo "    Dockerfile_registry:  $registry" >> $gitlab_ci_generator_dir/values.yaml; fi \
done

helm template gitlab-ci-template $gitlab_ci_generator_dir/ -s templates/gitlab-ci-template.yaml > $gitlab_ci_template_target