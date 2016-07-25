#!/bin/bash


WORKING_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILD_DIR=${WORKING_DIR}/build
VERSION_FILE="${WORKING_DIR}/../job_server/setup.py"
CURRENT_VERSION=`grep 'version=' ${VERSION_FILE} | awk -F\' '{print $2}'`
DEPLOYMENT_ZIP="job-server-${CURRENT_VERSION}.zip"

if [[ "${CURRENT_VERSION}" == *-dev ]]
then
    VERSION="latest"
else
    VERSION="${CURRENT_VERSION}"
fi

function build_deployment_bundle ()
{
    echo "Building deployment artifact zip ${DEPLOYMENT_ZIP}"

    mkdir -p ${BUILD_DIR}
    rsync -av ${WORKING_DIR}/config/elasticbeanstalk/ ${BUILD_DIR} \
        && rsync -av ${WORKING_DIR}/../job_server/ ${BUILD_DIR}/job_server \
        && cp ${WORKING_DIR}/Dockerfile ${BUILD_DIR}
    cd ${BUILD_DIR} \
        && zip -r ${WORKING_DIR}/${DEPLOYMENT_ZIP} .
    cd ${WORKING_DIR}
    rm -rf ${BUILD_DIR}

    echo "Deployment artifact built"
}


build_deployment_bundle