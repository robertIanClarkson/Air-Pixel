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
            start = True;
        else:
            endHour = chunks[0];
            endMin = chunks[1];
            endSec = chunks[2];

print "Creating Online Plots";

gyroXTrace = go.Scatter(
    x = dataCountObj,
    y = gyroX,
    mode = 'lines+markers',
    name = 'X'
);
gyroYTrace = go.Scatter(
    x = dataCountObj,
    y = gyroY,
    mode = 'lines+markers',
    name = 'Y'
);
gyroZTrace = go.Scatter(
    x = dataCountObj,
    y = gyroZ,
    mode = 'lines+markers',
    name = 'Z'
);
acclXTrace = go.Scatter(
    x = dataCountObj,
    y = acclX,
    mode = 'lines+markers',
    name = 'X'
);
acclYTrace = go.Scatter(
    x = dataCountObj,
    y = acclY,
    mode = 'lines+markers',
    name = 'Y'
);
acclZTrace = go.Scatter(
    x = dataCountObj,
    y = acclZ,
    mode = 'lines+markers',
    name = 'Z'
);
magnXTrace = go.Scatter(
    x = dataCountObj,
    y = magnX,
    mode = 'lines+markers',
    name = 'X'
);
magnYTrace = go.Scatter(
    x = dataCountObj,
    y = magnY,
    mode = 'lines+markers',
    name = 'Y'
);
magnZTrace = go.Scatter(
    x = dataCountObj,
    y = magnZ,
    mode = 'lines+markers',
    name = 'Z'
);

gyro = [gyroXTrace, gyroYTrace, gyroZTrace];
accl = [acclXTrace, acclYTrace, acclZTrace];
magn = [magnXTrace, magnYTrace, magnZTrace];

# py.plot(gyro, filename='Gyroscrope');
py.plot(accl, filename='Accelerometer_rate_25Hz_blocked');
# py.plot(magn, filename='Magnetometer');
print "Plots Created";
