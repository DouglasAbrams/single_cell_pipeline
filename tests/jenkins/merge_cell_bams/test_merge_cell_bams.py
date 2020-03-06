import os
import sys
from single_cell.utils import compare
import pandas as pd
import pysam

def get_merged_counts(path):
    bam_fnames = [os.path.join(path, file) for file in os.listdir(path) if file.endswith(".bam")]
    bams = [pysam.AlignmentFile(bam, "rb") for bam in bam_fnames]

    regions = [fname.split(".")[0] for fname in bam_fnames]
    mapped = [bam.mapped for bam in bams]
    unmapped = [bam.unmapped for bam in bams]
    return pd.DataFrame({"interval":regions, "mapped": mapped, "unmapped": unmapped})

def compare_split_counts():
    output_path = sys.argv[1]
    ref_path = sys.argv[2]

    refcounts = os.path.join(ref_path, "counts.csv")
    counts = get_merged_counts(output_path)

    counts = pd.read_csv(counts)
    refcounts = pd.read_csv(refcounts)

    compare.compare_tables(counts, refcounts)


if __name__ == "__main__":
    compare_split_counts()

