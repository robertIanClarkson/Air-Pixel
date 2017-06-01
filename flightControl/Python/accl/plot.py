#!/usr/bin/python
import plotly.plotly as py;
import plotly.graph_objs as go;

acclX = [];
acclY = [];
acclZ = [];
start       = False;
startSec    = "";
startMin    = "";
startHour   = "";
endSec      = "";
endMin      = "";
endHour     = "";

# open file to for read
print "Opening file";
f = open('data.txt', 'r');

dataCount = 0;
dataCountObj = [];
print "Reading File";
for line in f:
    if(line.find("|") > 0): # line contains data
        dataCount += 1;
        dataCountObj.append(dataCount);
        try:
            aX, aY, aZ, trash = line.split(" | ");
            acclX.append(int(aX));
            acclY.append(int(aY));
            acclZ.append(int(aZ));
        except ValueError:
            print "value error"
    elif(line.find(":") > 0): # line contains timeStamp
        chunks = line.split(":");
        print chunks;
        if(start == False):
            startHour   = chunks[0];
            startMin    = chunks[1];
            startSec    = chunks[2];
            start       = True;
        else:
            endHour     = chunks[0];
            endMin      = chunks[1];
            endSec      = chunks[2];

print "Creating Online Plots";

acclXTrace = go.Scatter(
    x = dataCountObj,
    y = acclX,
    mode = 'lines+markers',
    name = 'aX'
);
acclYTrace = go.Scatter(
    x = dataCountObj,
    y = acclY,
    mode = 'lines+markers',
    name = 'aY'
);
acclZTrace = go.Scatter(
    x = dataCountObj,
    y = acclZ,
    mode = 'lines+markers',
    name = 'aZ'
);


accl = [acclXTrace, acclYTrace, acclZTrace];

py.plot(accl, filename='Accel_FIFO');

print "Plots Created";
