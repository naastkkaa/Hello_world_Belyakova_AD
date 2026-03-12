short_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCATGGG'
g_number = short_dna.count("G")
c_number = short_dna.count("C")
overall_len = g_number + c_number
gc_content = overall_len / len(short_dna)

print("GC content is: ", gc_content)

print("GC content is: ", gc_content * 100, "%")  # то же самое, только в процентах
