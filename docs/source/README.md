### Output Structure

```
base dir/
    "patient"/
        grouplevel_high_impact_maf.maf
        grouplevel_high_impact_merged_snvs.csv 
        grouplevelmaf.maf
        grouplevel_snvs.csv
        mutationreport.html
    patient name/
        sample name/
            ibrary name/
                mainreport.html
                A108833A_adjacent_distance_class_mutsig.pdf
                A108833A_num_cells_class_top10_mutsig.pdf
                A108833Asnvs_high_impact.csv
                samplelevelmaf.maf 
                snvs_all.csv 
                trinuc.csv 
                A108833A_adjacent_distance_class_top10_mutsig.pdf 
                A108833Asnv_adjacent_distance.pdf 
                datatype_summary.csv 
                snv_alt_counts.pdf 
                snvs_high_impact.csv 
                A108833A_num_cells_class_mutsig.pdf 
                A108833Asnv_genome_count.pdf 
                snv_cell_counts.pdf 
                summary.csv 
```

### Output Descriptions
| FILENAME                                           | DESCRIPTION                                                                                         |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| grouplevel_high_impact_maf.maf                     | patient maf filtered on variant consequence and impact                                              |
| grouplevel_high_impact_merged_snvs.csv             | all snvs for patient filtered for high impact                                                       |
| grouplevelmaf.maf                                  | single maf with all maf data from patient                                                           |
| grouplevel_snvs.csv                                | al snvs for patient                                                                                 |
| mutationreport.html                                | html report characterizing patient-level variants                                                   |
| mainreport.html                                    | html report containing library-level analyses                                                       |
| {library}_adjacent_distance_class_top10_mutsig.pdf | bar plot of top 10 mutational signatures in the library grouped by adjacent distance                |
| {library}_adjacent_distance_class_mutsig.pdf       | heatmap of library signatures groupedby adjacent distance                                           |
| {library}_num_cells_class_top10_mutsig.pdf         | bar plot of top 10 mutational signatures grouped by number of cells                                 |
| {library}_num_cells_class_mutsig.pdf               | heatmap of mutational signatures grouped by number of cells                                         |
| {library}snvs_high_impact.csv                      | high impact snvs for the library (effect_impact=="HIGH")                                            |
| {library}Asnv_adjacent_distance.pdf                | scatterplot of distance between mutations                                                           |
| {library}snv_genome_count.pdf                      | scatterplot of distance between mutations                                                           |
| samplelevelmaf.maf                                 | barplot of number of snvs across the genome                                                         |
| snvs_all.csv                                       | all snvs for the library                                                                            |
| trinuc.csv                                         | trinucleotide contexts for the snvs in the library                                                  |
| datatype_summary.csv                               | number of cells with snvs, cnvs and haplotype variants                                              |
| snv_alt_counts.pdf                                 | histogram of alt counts/snv for the library                                                         |
| snvs_high_impact.csv                               | high impact snvs for the library (effect_umpact = {"HIGH", "NON_SYNONYMOUS_CODING", "STOP_GAINED"}) |
| snv_cell_counts.pdf                                | histogram of cell counts/snv for the library                                                        |
| summary.csv                                        | number of mutations and number of cells in the library                                              |