# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:23:40 2026

@author: 夫大国难测也（Fang-FuDaGuoNanCeYe）
"""


import matplotlib as mp

#注：我去网上查找，各个网页显示的北京地铁、上海地铁配色都不一样。我采用了其中一个。所以这里的配色不能代表相应地铁线路的实际颜色。
#北京地铁
colorsBeijingA = [r"#D8A69E",r"#C19CD2",r"#9F9DD8",r"#70A7B6",r"#A5C882", r"#FAC671",                      #浅色：红、紫、蓝、青蓝、黄绿、橙
                 r"#C85D4D",r"#9642C0",r"#5C59AF",r"#1D8F97",r"#77A42D", r"#D29700",                       #正色：红、紫、蓝、青蓝、黄绿、橙
                 r"#A4160C",r"#621D7D",r"#2D3399",r"#005266",r"#2D6C00", r"#A76400" ,                      #深色：红、紫、蓝、青蓝、黄绿、橙
                 r"#E6081B"  ];                                                                            #鲜红，改自3号线的红，可用于突出显示
colorsBeijingB = [ colorsBeijingA[color+subcolor] for color in range(0,6) for subcolor in range(0,18,6) ]; #按浅红、红、深红、浅紫、紫、深紫、……排序

#上海地铁
colorsShanghaiA = [r"#EA97A2",r"#C6AFD4",r"#87CAED",r"#B5D197",r"#DAAA68",                                 #浅色：红、紫、青蓝、黄绿、橙
                 r"#C81C1E",r"#944D9A",r"#0094D8",r"#8CC220",r"#D0771C",                                   #正色：红、紫、青蓝、黄绿、橙
                 r"#871C2B",r"#5B186F",r"#004D7A",r"#478200",r"#A35A00",                                   #深色：红、紫、青蓝、黄绿、橙
                 r"#E3002B"];                                                                              #鲜红，改自1号线的红，但是没有北京3明显
colorsShanghaiB = [ colorsShanghaiA[color+subcolor] for color in range(0,5) for subcolor in range(0,15,5) ];#按浅红、红、深红、浅紫、紫、深紫、……排序

#下面是应用示例

def cm2Inch(length):
    return length / 2.54;

def plotExample(data : dict, colors : list, title : str):
    legend = list(data.keys());
    dataForPlot = list(map(list,zip(*data.values())));
    [fig,ax1] = mp.pyplot.subplots(figsize=(cm2Inch(14.4),cm2Inch(8.1)));
    mp.pyplot.subplots_adjust(right=0.75,bottom=0.15)
    
    #虽然正规论文没法用Noto Sans，不过做视频为了字体不侵权，暂时用Noto Sans演示。
    mp.pyplot.title(title, fontsize=10, fontdict={'font_properties':"Noto Sans SC"},color = "#000000");
    ax1.set_xscale("log");
    ax1.set_yscale("log");
    for i in range(0,len(data)):
        ax1.plot(dataForPlot[0][i],dataForPlot[1][i],c=colors[i],marker="o",linestyle="None");
    mp.pyplot.xlabel('x值误差', fontsize=10, fontdict={'font_properties':"Noto Sans SC"},color = "#000000");
    mp.pyplot.ylabel('y值误差', fontsize=10, fontdict={'font_properties':"Noto Sans SC"},color = "#000000");
    mp.pyplot.xticks(fontsize=10)
    mp.pyplot.yticks(fontsize=10)
    ax1.legend(legend,bbox_to_anchor=(1.03, 1), prop={"size":10, "family":"Noto Sans SC"});
    #mp.pyplot.savefig(title+".jpg", dpi=300);
    
if(__name__=="__main__"):
    #注：我每个算法只跑了1次，数据的随机性很大，并不能代表算法本身的好坏。
    data = {"简化的GA": [26.2884,28.1727],
            "简化的MA": [199.999999973440922923506590791475900914520025253295898437500000,200.000000012939732452199592671604477800428867340087890625000000],
            "简化的SA": [199.999999953527379414897069409562391228973865509033203125000000,199.999999974239939110054464777022076305001974105834960937500000],
            "简化的SSA":[200.000000050378264476735878929503087420016527175903320312500000,200.000000037733147537077904587476950837299227714538574218750000],
            "简化的DBO":[200.000000015680561585296182158799638273194432258605957031250000,200.000000016167006067213662845460930839180946350097656250000000],
            "简化的HHO":[199.999999999894393365451605859561823308467864990234375000000000,199.999999990698066290595313887479278491809964179992675781250000],
            "简化的MFO":[200.000000124117097391462927191696508089080452919006347656250000,199.999999973746223916326592018322116928175091743469238281250000],
            "简化的COA":[200.000000004692583543963735337456455454230308532714843750000000,199.999999986328199419460815988713875412940979003906250000000000],
            "简化的AFSA":[200.000001881944520373823870329488272545859217643737792968750000,200.000001785786820585055778565219952724874019622802734375000000],
            "简化的ABC":[200.000000000115085108109980183144216425716876983642578125000000,199.999999999374372144922418215173820499330759048461914062500000],
            "简化的LSO":[199.999999999361123784180627183104661526158452033996582031250000,199.999999999190973071216959056073392275720834732055664062500000]
            };
    
    #答案是(200,200)，要求误差，就需要减200求绝对值。
    for i in data.keys():
        data[i] = list(map(lambda x : abs(x - 200),data[i]));
    
    
    plotExample(data,colorsBeijingA,"北京地铁配色  该图仅用于配色展示");
    plotExample(data,colorsShanghaiA,"上海地铁配色  该图仅用于配色展示");