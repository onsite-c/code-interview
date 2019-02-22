#!/bin/bash
set -eux

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

setup_go() {
    local project=${GOPATH:-~/go}/src/code-interview
    rm -rf ${project}
    mkdir -p ${project}

    cat > ${project}/cli.go <<EOF
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, world!")
}
EOF
}

# remove any user modifications
git reset --hard origin/master
git clean -fdx

# setup language skeletons
setup_python
setup_java
setup_go
