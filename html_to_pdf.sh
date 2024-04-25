#!/usr/bin/env bash

export execPath="/c/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe"
if [ ! -f "execPath" ]; then
    export execPath="/usr/bin/wkhtmltopdf"
fi

"$execPath" --image-quality 100 --enable-local-file-access --page-size A4 readme.html readme.pdf
