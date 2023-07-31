#3d scatterplot for tiling output visualization
def scat3D(x1, y1, z1, tile_list):
    xl = []
    yl = []
    zl = []

    pl = False
    sb = False
    itr = False

    ref_dict = {1:{'ref':x1, 'list' : xl, 'tf' : pl},
           2:{'ref':z1, 'list' : zl, 'tf' : sb},
           3:{'ref':y1, 'list' : yl, 'tf' : itr}}

    for sl in tile_list:
        for j in range(int(sl[0])):
            for m in ref_dict:
                ref_dict[m]['tf'] = False

            for i in sl[2:]:
                for j in ref_dict:
                    if i.split('[')[0] == ref_dict[j]['ref']:
                        if ref_dict[j]['tf'] == False:
                            ref_dict[j]['list'].append(int(i.split('[')[1].split('-')[1].split(']')[0])-int(i.split('[')[1].split('-')[0])-1)
                            ref_dict[j]['tf'] = True 
                        else:
                            ref_dict[j]['list'][-1] = ref_dict[j]['list'][-1]+(int(i.split('[')[1].split('-')[1].split(']')[0])-int(i.split('[')[1].split('-')[0])-1)
            for k in ref_dict:
                if ref_dict[k]['tf'] == False:
                    ref_dict[k]['list'].append(0)

    x = xl
    y = yl
    z = zl

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z,
               linewidths=1, alpha=.7,
               edgecolor='k',
               s = 50,
               c=z)
    ax.set_xlabel(x1+' coverage')
    ax.set_ylabel(y1+' coverage')
    ax.set_zlabel(z1+' coverage')
    ax.set_title('Mission Bio 3D scatterplot')
    plt.show()
