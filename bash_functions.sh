#! /bin/bash

function md() {
    mkdir -p "$@" && cd "$1"
}

