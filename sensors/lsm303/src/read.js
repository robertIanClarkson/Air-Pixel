//import
var lsm303 = require('lsm303');
var logHeading = require("./logs/logHeading");
var logAccel = require("./logs/logAccel");
var logTemp = require("./logs/logTemp");

//initiate chip
var chip = new lsm303();

//create our mag and accel variables
var mag = chip.magnetometer();
var accel = chip.accelerometer();

mag.setOffset(0,0,0);

console.log("Beginning logHeading");
logHeading(mag);
console.log("Beginning logAccel");
logAccel(accel);
console.log("Beginning logTemp");
logTemp(mag);
