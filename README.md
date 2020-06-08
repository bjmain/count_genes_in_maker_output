# count_genes_in_maker_output
Maker output includes gene calls and the associated support from est data, protein2genome, and blastx. Even though a maker gene was not called at a given genomic region, there are still protein annotation data in the final GFF3 file. 
This script counts your maker gene calls, and protein_match hits that occupy at least 20% novel genomic regions compared to all maker annotated genes. This gives a more accurate picture of how many genes were identified. 
