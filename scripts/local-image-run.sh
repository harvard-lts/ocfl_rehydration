#!/bin/bash

docker run --rm --name my-rehydrate --mount type=bind,source=${PWD},target=/app -it artifactory.huit.harvard.edu/lts/rehydrate:1.0.0
