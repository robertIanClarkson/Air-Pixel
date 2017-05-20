module.exports = function(mag){
  var fs = require('fs');
  //create a counter object
  var count = 0;
  var initTime = Date.now();
  //get readings
  setInterval(function(){
    count++;
    mag.readTemp(function(err, temp){
      if(err){
        console.log("LSM303: Failed to read heading : " + err);
      }else{
        fs.appendFile("/home/pi/cube/sensors/lsm303/data/lsmTEMP.dat", "\n" + count + " | " + JSON.stringify(temp) + " | " + (Date.now() - initTime), function(err){
          if(err){
            console.log("LSM303: Failed to write to lsmTEMP.dat : " + err);
          }
        });
      }
    });
  }, 60);
};
