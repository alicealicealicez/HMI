#downsamples files to 20000 zmws
def downsample(demux):

    zmw_dict=defaultdict(lambda:defaultdict(list))
    for i in demux.keys():
        n=0
        samfile=pysam.AlignmentFile(demux[i],'rb',check_sq=False)
        for read in samfile.fetch(until_eof=True):
            zmw=read.qname.split('/')[1]
            zmw_dict[i][zmw].append(1)
            n+=1

    zmws = [len(set(zmw_dict[x].keys())) for x in zmw_dict.keys()]


    for n,i in enumerate(demux.keys()):
        ds_cmd = "bamsieve -v --percentage {percent} {infile} {outfile}"
        
        cmd = ds_cmd.format(percent=str(2000000/zmws[n]),
                    infile=demux[i],
                    outfile=demux[i].split('.bam')[0]+'.s.bam')
         
        print(cmd)
        p= subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out = p.communicate()
        rc = p.returncode
