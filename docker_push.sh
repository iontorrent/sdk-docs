#!/bin/bash
set -e

repo_name="iontorrent"
image_name="sdk-docs-builder"

for name in $(docker images --format '{{.Repository}}:{{.Tag}}'); do
    if [[ $name =~ $repo_name/$image_name:.* ]]; then
        docker push $name
    fi
done
