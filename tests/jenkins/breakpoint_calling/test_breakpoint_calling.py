import os.path
import sys
from single_cell.utils import compare


def get_inputs(path):
    '''
    get metrics and gc metrics given a directory and library
    :param path:  path to metrics files
    :param library_id: library id associated with metrics files
    '''

    lumpy_data = os.path.join(path, "lumpy_breakpoints.csv.gz")

    destruct_data = os.path.join(path, "destruct_breakpoints.csv.gz")

    return lumpy_data, destruct_data


if __name__ == "__main__":

    output_path = sys.argv[1]
    ref_path = sys.argv[2]

    ref_lumpy, ref_destruct = get_inputs(ref_path)
    lumpy, destruct = get_inputs(output_path)

    compare.compare_breakpoint_calls(ref_lumpy, lumpy)
    compare.compare_breakpoint_calls(ref_destruct, destruct)
