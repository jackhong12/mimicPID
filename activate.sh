#!/bin/sh
docker run -it \
    --rm \
    -v "$(pwd):/tf/tmp" \
    -e DISPLAY=$DISPLAY \
    --name remote \
    --gpus all \
    -p 8888:8888 \
    tensorflow-gpu
