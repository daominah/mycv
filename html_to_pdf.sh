#!/usr/bin/env bash

wkhtmltopdf --image-quality 100  --page-size A4 readme.html readme.pdf
if [ $? -ne 0 ]; then
    echo "error, maybe on Windows, try again"
    export execPath="/c/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
    "$execPath" --image-quality 100  --page-size A4 readme.html readme.pdf
    if [ $? -ne 0 ]; then
        echo "error"
    else
        echo "seems good"
    fi
else
    echo "seems good"
fi
