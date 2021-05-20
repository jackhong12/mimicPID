#!/bin/sh
docker run -it \
    --rm \
    -v "$(pwd):/tf/tmp" \
    -e DISPLAY=$DISPLAY \
    --name remote \
    -p 12345:8888 \
    tensorflow-gpu
