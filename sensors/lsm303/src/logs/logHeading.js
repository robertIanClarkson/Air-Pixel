module.exports = function(mag){
  var fs = require('file-system');
  //create a counter object
  var count = 0;
  var initTime = Date.now();
  //get readings
  setInterval(function(){
    count++;
    mag.readHeading(function(err, heading){
      if(err){
        console.log("LSM303: Failed to read heading : " + err);
      }else{
        fs.appendFile("/home/pi/cube/sensors/lsm303/data/lsmHEAD.dat", "\n" + count + " | " + JSON.stringify(heading) + " | " + (Date.now() - initTime), function(err){
          if(err){
            console.log("LSM303: Failed to write to lsmHEAD.dat : " + err);
          }
        });
      }
    });
  }, 60);
};
