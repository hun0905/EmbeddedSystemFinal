#include "bbcar_rpc.h"
RPCFunction rpcStop(&RPC_stop, "stop");
RPCFunction rpcCtrl(&RPC_goStraight, "goStraight");
RPCFunction rpcTurn(&RPC_turn, "turn");
RPCFunction rpcLine(&RPC_line, "line");
RPCFunction rpcDemo(&RPC_demo, "Demo");
RPCFunction rpcTag(&RPC_tag, "tag");
extern BBCar car;
BufferedSerial uart(D1,D0);
void RPC_stop (Arguments *in, Reply *out)   {
    car.stop();
    return;
}

void RPC_goStraight (Arguments *in, Reply *out)   {
    int speed = in->getArg<double>();
    car.goStraight(speed);
    return;
}

void RPC_turn (Arguments *in, Reply *out)   {
    int speed = in->getArg<double>();
    double turn = in->getArg<double>();
    car.turn(speed,turn);
    return;
}

void RPC_line(Arguments *in, Reply *out)   {
    //int speed = in->getArg<double>();
    //double turn = in->getArg<double>();
    uart.set_baud(9600);
    bool stop = false;
    int count = 0;
    //car.stop();
    
    bool mode = true;
    while(mode){
        //car.stop();
        
        if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            if(recv[0] == 's')
            {
               //car.stop();
               car.turn(50,1);  
               ThisThread::sleep_for(300ms);            
            }
            if(recv[0] == 'r')
            {
               //car.stop();
               car.turn(50,-0.6);
               ThisThread::sleep_for(300ms);
            }
            if(recv[0] == 'l')
            {
               //car.stop();
               car.turn(50,0.6);
               ThisThread::sleep_for(300ms);
            }
            else
                car.stop();
                
        }
        
    }
    /*while(!mode){
        //car.stop();
        
        if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            count =0;
            if(recv[0] == 'c'){
                car.stop();
                
            }
            else{
                car.turn(50,1);  
                ThisThread::sleep_for(300ms);     
            }
        }
        /*else{
            car.turn(20,1);  
            ThisThread::sleep_for(300ms);   
        }*/
        
    //}
   return;
}
void RPC_demo(Arguments *in, Reply *out)   {
    uart.set_baud(9600);
    bool stop = false;
    int count = 0;
    bool mode = true;
    while(mode){
        if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            if(recv[0] == 's')
            {
               car.turn(30,1);  
               ThisThread::sleep_for(300ms);            
            }
            if(recv[0] == 'r')
            {
               car.turn(30,-0.6);
               ThisThread::sleep_for(300ms);
            }
            if(recv[0] == 'l')
            {
               car.turn(30,0.6);
               ThisThread::sleep_for(300ms);
            }
            else if(recv[0] == 'c')
            {
               if(count%2 == 0)
               {
                    car.turn(100,-0.3);
                    ThisThread::sleep_for(1000ms);
                    car.stop();
                    car.turn(100,1);
                    ThisThread::sleep_for(1000ms);
                    car.stop();
                    car.turn(100,0.3);
                    ThisThread::sleep_for(4000ms);
                    car.stop();
                    car.turn(100,0.3);
                    ThisThread::sleep_for(2700ms);
                    car.stop();
                    count=1;
               }
               else{
                    car.turn(100,0.3);
                    ThisThread::sleep_for(1300ms);
                    car.stop();
                    car.turn(100,1);
                    ThisThread::sleep_for(1000ms);
                    car.stop();
                    car.turn(100,-0.3);
                    ThisThread::sleep_for(4000ms);
                    car.stop();
                    car.turn(100,1);
                    ThisThread::sleep_for(400ms);
                    car.turn(100,-0.3);
                    ThisThread::sleep_for(3900ms);
                    car.stop();
                    count =0;
               }
            }
            else
                car.stop();
        }
    }
   return;
}
void RPC_tag(Arguments *in, Reply *out)   {
    //int speed = in->getArg<double>();
    //double turn = in->getArg<double>();
    uart.set_baud(9600);
    bool stop = false;
    int count = 0;
    while(1){
        if(uart.readable()){
            char recv[1];
            uart.read(recv, sizeof(recv));
            count =0;
            car.goStraight(100);
            if(recv[0] == 'a')
            {
               //car.stop();
               car.goStraight(100);
               ThisThread::sleep_for(500ms);
               car.stop();
               
            }
            else if(recv[0] == 'r')
            {
               car.turn(30,-0.6);
               ThisThread::sleep_for(300ms);
            }
            else if(recv[0] == 'l')
            {
               car.turn(30,0.6);
               ThisThread::sleep_for(300ms);
            }
        }
        else
            break;
    }
   return;
}

