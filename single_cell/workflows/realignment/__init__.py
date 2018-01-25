'''
Created on Jul 6, 2017

@author: dgrewal
'''
import os
import pypeliner
import pypeliner.managed as mgd

import tasks


def create_realignment_workflow(input_bams, input_bais, output_bams, config,
                                out_dir, realign, sample_ids):

    output_bams = dict([(sampid, output_bams[sampid])
                        for sampid in sample_ids])

    workflow = pypeliner.workflow.Workflow()

    workflow.setobj(
        obj=mgd.OutputChunks('sample_id'),
        value=sample_ids,
    )

    chromosomes = config["chromosomes"]

    workflow.setobj(
        obj=mgd.OutputChunks('chrom'),
        value=chromosomes,
    )

    workflow.transform(
        name='realignment',
        axes=('chrom',),
        ctx={'mem': config["memory"]['med']},
        func=tasks.realign,
        args=(
            mgd.InputFile('bam', 'sample_id', fnames=input_bams),
            mgd.InputFile('bai', 'sample_id', fnames=input_bais),
            mgd.TempOutputFile('realigned.bam', 'chrom', 'sample_id'),
            mgd.TempSpace('realignment_temp', 'chrom', cleanup='before'),
            config,
            mgd.InputInstance('chrom')
        )
    )

    workflow.transform(
        name='merge_realignment',
        ctx={'mem': config["memory"]['med']},
        axes=('sample_id',),
        func=tasks.merge_realignment,
        args=(
            mgd.TempInputFile('realigned.bam', 'chrom', 'sample_id'),
            mgd.OutputFile('bam_realn', 'sample_id', fnames=output_bams),
            config,
            mgd.InputInstance('sample_id')
        )
    )

    return workflow
