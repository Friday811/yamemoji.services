#!/bin/bash

docker build -t yamemoji .
docker run -d -p 8635:8635 yamemoji
