#!/bin/bash
repo_name="iontorrent"
image_name="sdk-docs-builder"

#build docker file
# n.b.: assume Dockerfile is in same dir
if docker build --rm -t $repo_name/$image_name .; then
  echo "$image_name is successfully built."
fi
