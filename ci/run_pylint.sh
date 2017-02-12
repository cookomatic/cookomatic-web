#!/usr/bin/env bash

if [[ $RUN_PYLINT == true ]]
then
    echo -e "\n### Running pylint"
    pylint cookomatic_web --ignore tests --disable=no-member --disable too-few-public-methods --disable unused-argument --disable invalid-name
    pylint cookomatic_web/tests --disable=no-member --disable too-few-public-methods --disable unused-argument --disable missing-docstring --disable protected-access --disable duplicate-code
fi
