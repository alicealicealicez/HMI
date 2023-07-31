def barcode_var(infile, outfile):
    in_file = open(infile, 'r')
    in_sam = Reader(in_file)
    big_list = []
    for i in in_sam:
        try:
            x = next(in_sam)
            start = x.pos
            l = [4144-start,4145-start,4146-start,4147-start,4148-start,4155-start,4156-start,4157-start,4158-start,4159-start]
            rois = []
            for j in l:
                try:
                    rois.append(x.gapped('seq')[j])
                except:
                    pass
            big_list.append(rois)
        except:
            pass

    new_list = []
    for i in big_list:
        if len(i):
            new_list.append(i)
    new_list = pd.DataFrame(new_list)
    new_list.columns = ['4144','4145','4146','4147','4148','4155','4156','4157','4158','4159']
    counts_tab = new_list.groupby(['4144','4145','4146','4147','4148','4155','4156','4157','4158','4159']).size().reset_index(name='Count')
    counts_tab.to_csv(outfile)
