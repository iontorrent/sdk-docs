#!/bin/bash

repo_name='iontorrent'
image_name='sdk-docs-builder'

docker run -v $(pwd):/src $repo_name/$image_name
