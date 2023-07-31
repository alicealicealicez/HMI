def get_satags(file):
    samfile = pysam.AlignmentFile(file, "rb")
    not_sa_reads=[]
    for read in samfile:
        try:
            SA_tags.append(read.get_tag("SA"))
        except:
            not_sa_reads.append(read.query_name)
    with open('bc1009_TC-062.notsa.txt'.format(key),'w') as out:
            for item in list((not_sa_reads)):
                out.write(item+'\n')
