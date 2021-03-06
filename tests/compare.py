'''
Created on Jun 14, 2018

@author: dgrewal
'''
import warnings

import numpy as np
from single_cell.utils import csvutils


def exact_compare_cols(data, reference, column_name):
    data_index = set(data.index)
    reference_index = set(reference.index)

    assert data_index == reference_index

    index_order = sorted(data_index)
    data = data.reindex(index_order)
    reference = data.reindex(index_order)

    assert data[column_name].equals(reference[column_name])


def approx_compare_cols(data, reference, column_name, eps=0.001):
    data_index = set(data.index)
    reference_index = set(reference.index)

    assert data_index == reference_index

    index_order = sorted(data_index)
    data = data.reindex(index_order)
    reference = data.reindex(index_order)

    diff = data[column_name] - reference[column_name]

    assert np.nanmax(diff.tolist()) < eps


def load_hmmcopy_reads_data(readsfile):
    keepcols = [
        'ideal', 'valid', 'gc', 'map', 'state',
        'cor_gc', 'copy']

    reads = csvutils.read_csv_and_yaml(readsfile)

    reads = reads.set_index(['cell_id', 'chr', 'start', 'end'])

    reads = reads[keepcols]

    return reads


def load_metrics_data(filename):
    reads = csvutils.read_csv_and_yaml(filename)

    reads = reads.set_index(['cell_id'])

    return reads


def compare_tables(data, refdata):
    data_cols = set(data.columns.values)
    ref_cols = set(refdata.columns.values)

    common_cols = list(data_cols.intersection(ref_cols))

    missing_cols = list(ref_cols - data_cols)

    if missing_cols:
        warnings.warn("missing cols in reference: {}".format(missing_cols))

    for colname in common_cols:
        exact_compare_cols(data, refdata, colname)


def compare_reads(readsdata, refreadsdata):
    reads = load_hmmcopy_reads_data(readsdata)
    refreads = load_hmmcopy_reads_data(refreadsdata)

    exact_compare_cols(reads, refreads, 'ideal')
    exact_compare_cols(reads, refreads, 'valid')
    exact_compare_cols(reads, refreads, 'state')
    exact_compare_cols(reads, refreads, 'gc')
    exact_compare_cols(reads, refreads, 'map')
    approx_compare_cols(reads, refreads, 'copy')


def compare_metrics(metricsdata, refmetricsdata):
    metrics = load_metrics_data(metricsdata)
    refmetrics = load_metrics_data(refmetricsdata)

    compare_tables(metrics, refmetrics)
