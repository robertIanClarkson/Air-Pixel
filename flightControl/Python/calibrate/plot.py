import plotly.plotly as py;
import plotly.graph_objs as go;

gyroX = [];
gyroY = [];
gyroZ = [];
acclX = [];
acclY = [];
acclZ = [];
magnX = [];
magnY = [];
magnZ = [];
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
            gX, gY, gZ, aX, aY, aZ, mX, mY, mZ, trash = line.split(" | ");
            gyroX.append(int(gX));
            gyroY.append(int(gY));
            gyroZ.append(int(gZ));
            acclX.append(int(aX));
            acclY.append(int(aY));
            acclZ.append(int(aZ));
            magnX.append(int(mX));
            magnY.append(int(mY));
            magnZ.append(int(mZ));
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

gyroXTrace = go.Scatter(
    x = dataCountObj,
    y = gyroX,
    mode = 'lines+markers',
    name = 'gX'
);
gyroYTrace = go.Scatter(
    x = dataCountObj,
    y = gyroY,
    mode = 'lines+markers',
    name = 'gY'
);
gyroZTrace = go.Scatter(
    x = dataCountObj,
    y = gyroZ,
    mode = 'lines+markers',
    name = 'gZ'
);
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
magnXTrace = go.Scatter(
    x = dataCountObj,
    y = magnX,
    mode = 'lines+markers',
    name = 'mX'
);
magnYTrace = go.Scatter(
    x = dataCountObj,
    y = magnY,
    mode = 'lines+markers',
    name = 'mY'
);
magnZTrace = go.Scatter(
    x = dataCountObj,
    y = magnZ,
    mode = 'lines+markers',
    name = 'mZ'
);

gyro = [gyroXTrace, gyroYTrace, gyroZTrace];
accl = [acclXTrace, acclYTrace, acclZTrace];
magn = [magnXTrace, magnYTrace, magnZTrace];
everyone = [gyroXTrace, gyroYTrace, gyroZTrace, acclXTrace, acclYTrace, acclZTrace, magnXTrace, magnYTrace, magnZTrace]

# py.plot(gyro, filename='Gyroscrope_test_5v');
# py.plot(accl, filename='Accelerometer_rate_CTRL_0_filters');
# py.plot(magn, filename='Magnetometer');
py.plot(everyone, filename='FLIP_avg_5_x10pace');

print "Plots Created";
