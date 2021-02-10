#!/bin/bash
set -e
set -o pipefail

TAG=`git describe --tags $(git rev-list --tags --max-count=1)`
DOCKER=`which docker`
NUMCORES=`nproc --all`

mkdir -p COHORT_QC/ref_test_data

docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION -v $PWD:$PWD -w $PWD $1/awscli:v0.0.1 \
  aws s3 cp s3://singlecelltestsets/TESTDATA_CODEBUILD/cohort-qc COHORT_QC/ref_test_data/ --recursive

docker run -w $PWD -v $PWD:$PWD -v /refdata:/refdata -v /var/run/docker.sock:/var/run/docker.sock \
  -v $DOCKER:$DOCKER --rm \
  $1/single_cell_pipeline:$TAG \
  single_cell cohort_qc --input_yaml single_cell/tests/jenkins/cohort_qc/inputs.yaml \
  --maxjobs $NUMCORES --nocleanup --sentinel_only  \
  --context_config single_cell/tests/jenkins/context_config.yaml \
  --submit local --loglevel DEBUG \
  --tmpdir COHORT_QC/temp \
  --pipelinedir COHORT_QC/pipeline --submit local --out_dir COHORT_QC/output 

docker run -w $PWD -v $PWD:$PWD -v /refdata:/refdata -v /var/run/docker.sock:/var/run/docker.sock \
  -v $DOCKER:$DOCKER --rm \
  $1/single_cell_pipeline:$TAG \
  python single_cell/tests/jenkins/cohort_qc/test_cohort_qc.py cohort_qc/output cohort_qc/ref_test_data/refdata SPECTRUM

docker run -w $PWD -v $PWD:$PWD --rm $1/single_cell_pipeline:$TAG rm -rf COHORT_QC
