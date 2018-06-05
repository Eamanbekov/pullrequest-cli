#!/bin/bash -e

if [[ -z "$PYPI_USERNAME" || -z "$PYPI_PASSWORD" || -z "$PYPI_URL" ]]; then
    echo "You must set PYPI_USERNAME, PYPI_PASSWORD, and PYPI_URL to run this script"
    exit 1
fi

cat <<EOF >> ~/.pypirc
[distutils]
index-servers=pypi
[pypi]
repository=https://upload.pypi.org/pypi
username=$PYPI_USERNAME
password=$PYPI_PASSWORD
EOF
python setup.py sdist upload;
rm ~/.pypirc;