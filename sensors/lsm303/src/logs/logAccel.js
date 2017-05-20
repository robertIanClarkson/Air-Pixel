module.exports = function(accel){
  var fs = require('fs');
  //create a counter object
  var count = 0;
  var initTime = Date.now();
  //get readings
  setInterval(function(){
    count++;
    accel.readAxes(function(err, accel){
      if(err){
        console.log("LSM303: Failed to read axes : " + err);
      }else{
        fs.appendFile("/home/pi/cube/sensors/lsm303/data/lsmACCEL.dat", "\n" + count + " | " + JSON.stringify(accel) + " | " + (Date.now() - initTime), function(err){
          if(err){
            console.log("LSM303: Failed to write axes to lsmACCEL.dat : " + err);
          }
        });
      }
    });
  }, 60);
};
