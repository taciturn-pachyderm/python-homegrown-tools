#!/usr/bin/env bash
__bin="$(realpath ${BASH_SOURCE[0]})"
__dir="$(dirname "$__bin")"

case $1 in

    clean)
        find "$__dir" -name "__pycache__" -type d -exec rm -rf {} \;
        rm -rf "$__dir/build/" "$__dir/dist/" "$__dir"/*.egg*/
        ;;
        
    build)   python setup.py build ;;
    install) python setup.py install ;;
esac
