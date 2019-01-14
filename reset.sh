#!/bin/bash
set -x

setup_python() {
    pushd src/python

    python2 -m virtualenv venv2
    ./venv2/bin/pip install --upgrade pip requests

    python3 -m venv venv3
    ./venv3/bin/pip install --upgrade pip requests

    popd
}

setup_java() {
    pushd src/java

    ./gradlew eclipse idea

    popd
}

# remove any user modifications
git clean -fdx

# setup language skeletons
setup_python
setup_java
