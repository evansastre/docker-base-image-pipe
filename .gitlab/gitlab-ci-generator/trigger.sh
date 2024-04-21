# echo >> $(git rev-parse --show-toplevel)/devops-base/jdk/Dockerfile
echo >> $(git rev-parse --show-toplevel)/.gitlab-ci.yml
git add ../../
git commit -m "update - $1"
git push origin HEAD
