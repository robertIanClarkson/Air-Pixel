// Define helper functions for reading and writing bytes
// Copyright (c) 2017 Christopher Erwin, Robert Clarkson
//
//

#include <stdio.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <sys/ioctl.h>
#include <fcntl.h>
#include "io.h"

int initSensor(SensorConfig* config) {
    // Most of this was borrowed from the LSM90DS0_I2CS example
    // from ControlEverything.com...

    // Set up accelerometer

    // Create the I2C bus and sensor configuration
    char *bus = "/dev/i2c-1";
    if ((config->file = open(bus, O_RDWR)) < 0) {
        printf("Failed to open bus.\n");
        return -1;
    }

    return 0;
}

void initGyro(SensorConfig* config) {
    // Get I2C device
    ioctl(config->file, I2C_SLAVE, 0x6B);

    // Select control register 1 (0x20)
    // X, Y, Z Axis enable, power on mode, data rate o/p 95 Hz (0x0F)
    char cfg[2] = {0};
    cfg[0] = 0x20;
    cfg[1] = 0x0F;
    write(config->file, cfg, 2);

    // Select control register 4 (0x23)
    // Full scale 2000 dps, continuous update (0x30)
    cfg[0] = 0x23;
    cfg[1] = 0x30;
    write(config->file, cfg, 2);

    //sleep(1);
}

void initAccel(SensorConfig* config) {
    // Get I2C device
    ioctl(config->file, I2C_SLAVE, 0x1D);

    // Select control register 2 (0x21)
    // X, Y, Z Axis enable, power on mode, data rate o/p 95 Hz (0x0F)
    char cfg[2] = {0};
    cfg[0] = 0x20;
    cfg[1] = 0x67;
    write(config->file, cfg, 2);

    // Select control register 5 (0x24)
    // Full scale selection, +/- 16g (0x20)
    cfg[0] = 0x21;
    cfg[1] = 0x20;
    write(config->file, cfg, 2);

    //sleep(1);
}

// Read one byte from addr and return it
void readByte(SensorConfig* config, char addr[], char data[]) {
    write(config->file, addr, 1);

    if (read(config->file, data, 1) != 1) {
        printf("ERROR: Input/output error\n");
    }
}
