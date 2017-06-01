#include <stdio.h>
#include "io.h"

int main(int argc, char** argv) {
    printf("Hello, world!\n");

    SensorConfig sensor = {0};

    initSensor(&sensor);
    
    char addr[1] = {0x28};
    char byte[1] = {0};

    printf("Test Gyro:\n");
    initGyro(&sensor);
    readByte(&sensor, addr, byte);
    printf("%X\n", byte[0]);

    addr[0] = 0x0F;
    readByte(&sensor, addr, byte);
    printf("%X\n", byte[0]);

    printf("Test Accel:\n");
    initAccel(&sensor);
    addr[0] = 0x28;
    readByte(&sensor, addr, byte);
    printf("%X\n", byte[0]);

    addr[0] = 0x0F;
    readByte(&sensor, addr, byte);
    printf("%X\n", byte[0]);

    return 0;
}
