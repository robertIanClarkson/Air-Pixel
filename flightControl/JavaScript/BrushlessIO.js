var raspi = require('raspi');
var I2C = require('raspi-i2c').I2C;
raspi.init(function () {
    var i2c = new I2C();
    console.log(i2c.readByteSync(0x18)); // Read one byte from the device at address 18
});
