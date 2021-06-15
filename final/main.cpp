#include "mbed.h"
#include "bbcar.h"
#include "bbcar_rpc.h"
Ticker servo_ticker;
PwmOut pin5(D5), pin6(D6);
BufferedSerial xbee(D10, D9);
BBCar car(pin5, pin6, servo_ticker);
int main() {
   char buf[256], outbuf[256];
   double pwm_table0[] = {-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150};
   double speed_table0[] ={-15.785,-15.625,-14.669,-11.480,-5.501,-0.080,0.000,10.922,14.589,15.546,15.944};
   double pwm_table1[] = {-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150};
   double speed_table1[] = {-15.067,-15.067,-14.031,-11.560,-5.740,0.000,5.580,11.241,14.031,15.067,15.307};
   car.setCalibTable(11, pwm_table0, speed_table0, 11, pwm_table1, speed_table1);
   FILE *devin = fdopen(&xbee, "r");
   FILE *devout = fdopen(&xbee, "w");
   while (1) {
      memset(buf, 0, 256);
      for( int i = 0; ; i++ ) {
         char recv = fgetc(devin);
         if(recv == '\n') {
            printf("\r\n");
            break;
         }
         buf[i] = fputc(recv, devout);
      }
   RPC::call(buf, outbuf);
   }
}

