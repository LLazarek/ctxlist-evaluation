#!/bin/python

axisLabelSize = 30
axisTicSize = 20
lMargin = 16
tMargin = 7
rMargin = 5
keySpacing = 5
keySize = 28
titleSize = 40
titleYOffset = 4
ylabelOffset = -7
lineWidth = 4



gplotConfigs = [
    {
        "gplot":"simpleIteration.gplot",
        "type":"Basic Iteration",
        "scale":"Linearly",
        "ylabel":"Execution time (ms)",
        "ymax":140,
        "keypos":"1, 1",
        "data":"simpleIteration.dat",
        "trend":'fit [1:10] g(x) "simpleIteration.dat" using 1:3 via d,h',
        "dec_a":2,
        "dec_b":2,
        "dec_c":2,
        "dec_d":2,
        "dec_h":2
    },
    {
        "gplot":"expensiveIteration.gplot",
        "type":"CheckStyle Pattern",
        "scale":"Linearly",
        "ylabel":"Execution time (ms)",
        "ymax":5000,
        "keypos":"1, 0.4",
        "data":"expensiveIteration.dat",
        "trend":'fit [1:10] g(x) "expensiveIteration.dat" using 1:3 via d,h',
        "dec_a":0,
        "dec_b":2,
        "dec_c":0,
        "dec_d":0,
        "dec_h":2
    },
    {
        "gplot":"memory.gplot",
        "type":"Memory",
        "scale":"Cubically",
        "ylabel":"Memory consumption (MB)",
        "ymax":600,
        "keypos":"1, 0.4",
        "data":"memory.dat",
        "trend":'fit [1:10] g(x) "memory.dat" using 1:3 via d,h',
        "dec_a":4,
        "dec_b":2,
        "dec_c":0,
        "dec_d":0,
        "dec_h":2
    },
    {
        "gplot":"randomAccess.gplot",
        "type":"Random Access",
        "scale":"Quadratically",
        "ylabel":"Execution time (ms)",
        "ymax":120,
        "keypos":"1, 1",
        "data":"randomAccess.dat",
        "trend":'d = 0.0305332371;\nh = 0.6663482219;',
        "dec_a":4,
        "dec_b":2,
        "dec_c":2,
        "dec_d":2,
        "dec_h":2
    },
    {
        "gplot":"looptype2.gplot",
        "type":"Loop Type 2",
        "scale":"Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":1200,
        "keypos":"0.8, 1",
        "data":"looptype2.dat",
        "trend":'fit [1:10] g(x) "looptype2.dat" using 1:3 via d,h',
        "dec_a":4,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"looptype3.gplot",
        "type":"Loop Type 3",
        "scale":"Linearly",
        "ylabel":"Execution time (ms)",
        "ymax":125,
        "keypos":"1, 1",
        "data":"looptype3.dat",
        "trend":'fit [1:10] g(x) "looptype3.dat" using 1:3 via d,h',
        "dec_a":2,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"looptype4.gplot",
        "type":"Loop Type 4",
        "scale":"Linearly",
        "ylabel":"Execution time (ms)",
        "ymax":130,
        "keypos":"1, 1",
        "data":"looptype4.dat",
        "trend":'fit [1:10] g(x) "looptype4.dat" using 1:3 via d,h',
        "dec_a":2,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"removeElement.gplot",
        "type":"Element Removal",
        "scale":"Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":135,
        "keypos":"0.8, 1",
        "data":"removeElement.dat",
        "trend":'d = 0.009370242;\nh = 0.7100570828;',
        "dec_a":4,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"removeIndex.gplot",
        "type":"Index Removal",
        "scale":"Sub-Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":50,
        "keypos":"0.8, 1",
        "data":"removeIndex.dat",
        "trend":'d = 0.0112108525;\nh = 0.6903204666;',
        "dec_a":4,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"size.gplot",
        "type":"Size Calculation",
        "scale":"Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":800,
        "keypos":"0.8, 1",
        "data":"size.dat",
        "trend":'d = 0.0115950718;\nh = 0.5533611726;',
        "dec_a":4,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"sort.gplot",
        "type":"Sorting",
        "scale":"Sub-Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":1500,
        "keypos":"1, 1",
        "data":"sort.dat",
        "trend":'fit [1:10] g(x) "sort.dat" using 1:3 via d,h',
        "dec_a":2,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"sortType.gplot",
        "type":"Variational Sorting",
        "scale":"Sub-Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":1750,
        "keypos":"0.95, 1",
        "data":"sortType.dat",
        "trend":'fit [1:10] g(x) "sortType.dat" using 1:3 via d,h',
        "dec_a":2,
        "dec_b":2,
        "dec_c":2,
        "dec_d":4,
        "dec_h":2
    },
    {
        "gplot":"findElement.gplot",
        "type":"Finding Element",
        "scale":"Sub-Cubically",
        "ylabel":"Execution time (ms)",
        "ymax":115,
        "keypos":"0.8, 1",
        "data":"findElement.dat",
        "trend":'d = 0.0168390699;\nh = 0.4989543855;',
        "dec_a":4,
        "dec_b":2,
        "dec_c":2,
        "dec_d":2,
        "dec_h":2
    }
]


def gplotStr(conf):
 return """set title "{type} Scales {scale}\\nwith Features" offset -5,{titleYOffset} font ",{titleSize}"
set xlabel "Number of features" font ",{axisLabelSize}"
set ylabel "{ylabel}" font ",{axisLabelSize}" offset {ylabelOffset},0

set xrange[1:100]
set yrange[0:{ymax}]
set border 3
set tics scale 0 font ",{ticSize}"
set bmargin 5
set lmargin {lmargin}
set tmargin {tmargin}
set rmargin {rmargin}

set key spacing {keySpacing} font ",{keySize}" at graph {keyPos}
#set key off

#set terminal pngcairo size 1070, 860
#set output 'performance_vs_features.png'

set termoption enhanced
f(x) = a*x**b + c;
fit f(x) "{data}" using 1:2 via a,b,c
g(x) = d*exp(h*x);
{trend}

plot "{data}" using 1:2 linecolor rgb "blue" title "CtxList", \\
"{data}" using 1:3 linecolor rgb "red" title "V<List>", \\
f(x) with lines linecolor rgb "blue" lw {lw} title sprintf("CtxList trend: %.{a}f x^{{%.{b}f}} + %.{c}f", a, b, c), \\
g(x) with lines linecolor rgb "red" lw {lw} title sprintf("V<List> trend: %.{d}f e^{{%.{h}f x}}", d, h)

pause -1
""".format(type=conf['type'], scale=conf['scale'], titleYOffset=titleYOffset, titleSize=titleSize, axisLabelSize=axisLabelSize, ylabel=conf['ylabel'], ylabelOffset=ylabelOffset, ymax=conf['ymax'], ticSize=axisTicSize, lmargin=lMargin, rmargin=rMargin, tmargin=tMargin, keySpacing=keySpacing, keySize=keySize, keyPos=conf['keypos'], data=conf['data'], trend=conf['trend'], lw=lineWidth, a=conf['dec_a'], b=conf['dec_b'], c=conf['dec_c'], d=conf['dec_d'], h=conf['dec_h'])

def generate(gplotConfigs):
    for gplot in gplotConfigs:
        with open(gplot['gplot'], 'w') as f:
            f.write(gplotStr(gplot))


if __name__ == '__main__':
    generate(gplotConfigs)
