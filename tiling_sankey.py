def sankey(refs,tile_list):
    links = {}
    num = 0
    for j in range(len(refs)):
        num = num + j
    source = []
    target = []
    value = [0]*(num+len(refs))
    pres = [0]*len(refs)
    
    for k in range(len(refs)):
        if k<len(refs)-1:
            for a in range(k+1,len(refs)):
                source.append(k)
                target.append(a)
    for o in range(len(refs)):
        source.append(o)
        target.append(o)

    
    for sl in tile_list:
        for j in range(int(sl[0])):
            pres = [0]*len(refs)
            for c in sl[2:]:
                for h in range(len(refs)):
                    if c.split('[')[0]+'('+c.split('(')[1][0]+')' == refs[h]:
                        pres[h] = pres[h] + 1
              
            for n in range(num+len(refs)):
                for m in range(len(refs)):
                    for p in range(len(refs)):
                        if (refs[source[n]] == refs[m]) & (refs[target[n]] == refs[p]):
                            if (pres[m]>0) & (pres[p]>0):
                                value[n] = value[n] + 1

            for q in range(num,num+len(refs)):
                if pres[source[q]]>1:
                    value[q] = value[q] + 1 
    
    temp_val = []
    temp_source = []
    temp_target = []
    for i in range(len(value)):
        if value[i]!=0:
            temp_val.append(value[i])
            temp_source.append(source[i])
            temp_target.append(target[i])
            
    fig = go.Figure(data=[go.Sankey(
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(color = "black", width = 0.5),
          label = refs,
          color = "goldenrod"
        ),
        link = dict(
          source = temp_source, 
          target = temp_target,
          value = temp_val,
          color = ['rgba(0,50,90, 0.4)', 'rgba(246,126,94, 0.4)', 'rgba(106,118,132, 0.4)', 'rgba(116,81,173, 0.4)', 'rgba(20,103,172, 0.4)', 'rgba(41,171,226, 0.4)', 'rgba(51,51,51, 0.4)', 'rgba(0,51,90, 0.4)',
                  'rgba(0,50,90, 0.6)', 'rgba(246,126,94, 0.6)', 'rgba(106,118,132, 0.6)', 'rgba(116,81,173, 0.6)', 'rgba(20,103,172, 0.6)']
      ))])

    fig.update_layout(title_text="Sankey Diagram", font_size=10)
    fig.show()
