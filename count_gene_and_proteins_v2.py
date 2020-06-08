import sys

overlap_threshold = 0.8

maker_calls = open("maker_calls_in_unsorted_untify_v2.txt","w")
new_protein2genome_calls = open("protein2genome_calls_in_unsorted_untify_v2.txt","w")

def add_to_dict(contig_name,st,end,dictionary):
    if contig_name not in dictionary:
        dictionary[contig_name]=[]
    g = list(range(int(st),int(end)+1))
    dictionary[contig_name]+=g
    return(dictionary)

maker_genes={}
for line in open("CtarK1_unsorted_untidy.gff3"):
    i=line.strip().split()
    if len(i)>3:
        if i[2] == "gene":
            #print(line.strip())
            maker_calls.write(line)
            tig = i[0]
            maker_genes = add_to_dict(tig,i[3],i[4],maker_genes)

uncalled_genes = {}
uncalled_gene_list = []

redundant_gene_list = []
protein_2_genome = {}
for line in open("CtarK1_unsorted_untidy.gff3"):
    i=line.strip().split()
    if i[1]=="protein2genome" and i[2]=="protein_match":
        ortho = i[8].split("Name=")[-1].split("-")[0]
        contig = i[0]
        if contig not in maker_genes:
            if ortho not in uncalled_gene_list:
                uncalled_gene_list.append(ortho)  # In the case where multiple proteins map to the same location, I only report/count the first instance here.
                new_protein2genome_calls.write(line)
            uncalled_genes = add_to_dict(contig,i[3],i[4],uncalled_genes)
            continue
        protein_match = list(range(int(i[3]),int(i[4])+1))
        overlap = set(maker_genes[contig]).intersection(protein_match)
        if float(len(overlap))/float(len(protein_match)) <= overlap_threshold:  # threshold to count as unidentified by maker
            if ortho not in uncalled_gene_list:
                uncalled_gene_list.append(ortho)  # In the case where multiple proteins map to the same location, I only report/count the first instance here.
                new_protein2genome_calls.write(line)





        

