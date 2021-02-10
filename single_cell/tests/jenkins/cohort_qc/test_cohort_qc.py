import os.path
import sys
from single_cell.tests.jenkins import compare
from single_cell.utils import csvutils


def get_inputs(path, cohort_label):
    """"
    return paths pipeline outputs in out_dir path
    """
    cna_table = os.path.join(path, cohort_label, "cna_table.tsv.gz")
    cohort_maf = os.path.join(path, cohort_label, "cohort_oncogenic_filtered.maf")
    segments = os.path.join(path, cohort_label, "segments.tsv.gz")

    return cna_table, cohort_maf, oncoplot, segments


def test_cohort_qc(args):
    output_path = args[1]
    ref_path = args[2]
    cohort_label = args[3]

    ref_cna_table, ref_cohort_maf, ref_segments = get_inputs(ref_path, cohort_label)
    cna_table, cohort_maf, segments = get_inputs(output_path, cohort_label)

    ref_cna_table = pd.read_csv(ref_cna_table, sep="\t", compression=None)
    cna_table = pd.read_csv(ref_cna_table, sep="\t", compression=None)
    ref_segments = pd.read_csv(ref_cna_table, sep="\t", compression=None)
    segments = pd.read_csv(ref_cna_table, sep="\t", compression=None)

    compae.compare_tables(ref_cohort_table, cohort_table)
    compae.compare_tables(ref_segments, segments)

    ref_cohort_maf = pd.read_csv(ref_cohort_maf, sep="\t", chunksize=10 ** 5)
    cohort_maf =  pd.read_csv(cohort_maf, sep="\t", chunksize=10 ** 5)

    for ref, out in zip(ref_cohort_maf, cohort_maf):
        compare.compare_tables(ref, out)

 
if __name__ == "__main__":
    test_cohort_qc(sys.argv)
