// Define helper functions for reading and writing bytes
// Copyright (c) 2017 Christopher Erwin, Robert Clarkson
//

// Store the file pointer and any other data needed.
struct SensorConfig {
    int file;
};
typedef struct SensorConfig SensorConfig;

int initSensor(SensorConfig* config);
void initGyro(SensorConfig* config);
void initAccel(SensorConfig* config);
void readByte(SensorConfig* config, char addr[], char data[]);
