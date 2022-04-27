import rrdtool
ret = rrdtool.create("RRD/trend.rrd",
                     "--start",'N',
                     "--step",'60',
                     "DS:CPU:GAUGE:600:U:U",
                     "DS:RAM:GAUGE:600:U:U",
                     "DS:STG:GAUGE:600:U:U",
                     "RRA:AVERAGE:0.5:1:24")
if ret:
    print (rrdtool.error())