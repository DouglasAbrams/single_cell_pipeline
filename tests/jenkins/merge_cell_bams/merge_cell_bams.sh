#!/bin/bash

TAG=`git describe --tags $(git rev-list --tags --max-count=1)`

mkdir -p MERGE_CELL_BAMS/ref_test_data

docker run -v $PWD:$PWD -w $PWD singlecellpipeline/azurecli:v0.0.1 \
  az storage blob download-batch -s merge-bams -d MERGE_CELL_BAMS/ref_test_data --account-name $1 --account-key $2

docker run -w $PWD -v $PWD:$PWD -v /refdata:/refdata -v /var/run/docker.sock:/var/run/docker.sock \
  -v /usr/bin/docker:/usr/bin/docker --rm \
  $3/single_cell_pipeline:$TAG \
  single_cell merge_cell_bams --input_yaml tests/jenkins/merge_cell_bams/inputs.yaml \
  --maxjobs 4 --nocleanup --sentinel_only  \
  --context_config tests/jenkins/align/context_config.yaml \
  --submit local --loglevel DEBUG \
  --tmpdir MERGE_CELL_BAMS/temp \
  --pipelinedir MERGE_CELL_BAMS/pipeline --submit local --out_dir MERGE_CELL_BAMS/output

LATEST=v0.0.3

docker run -w $PWD -v $PWD:$PWD -v /refdata:/refdata -v /var/run/docker.sock:/var/run/docker.sock \
  -v /usr/bin/docker:/usr/bin/docker --rm \
  $3/samtools:$LATEST bash; \
  sudo for f in MERGE_CELL_BAMS/ref_test_data/testdata/merge-bams/*.bam; do samtools view -f 4 -c $f; done > MERGE_CELL_BAMS/output/unmapped;
  sudo for f in MERGE_CELL_BAMS/ref_test_data/testdata/merge-bams/*.bam; do samtools view -c $f; done > MERGE_CELL_BAMS/output/mapped;
  sudo ls MERGE_CELL_BAMS/ref_test_data/testdata/merge-bams/*.bam | awk '{split($0, r, "."); print r[1] }' > MERGE_CELL_BAMS/output/regions

#docker run -w $PWD -v $PWD:$PWD -v /refdata:/refdata -v /var/run/docker.sock:/var/run/docker.sock \
#  -v /usr/bin/docker:/usr/bin/docker --rm \
#  $3/single_cell_pipeline:$TAG \
#  python tests/jenkins/merge_cell_bams/test_merge_cell_bams.py MERGE_CELL_BAMS/output MERGE_CELL_BAMS/ref_test_data/refdata
