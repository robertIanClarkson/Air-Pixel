var lsm303 = require('lsm303');
var ls = new lsm303();

var x = 0, y=0, z=0;

var mag = ls.magnetometer;
var accel = ls.accelerometer;


