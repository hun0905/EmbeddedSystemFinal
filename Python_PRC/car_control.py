import time
import serial
import sys,tty,termios
class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def get():
    inkey = _Getch()
    while(1):
        k=inkey()
        if k!='':break
    if k=='\x1b':
        k2 = inkey()
        k3 = inkey()
        if k3=='A':
            print ("up")
            s.write("/goStraight/run 100 \n".encode())
        if k3=='B':
            print ("down")
            s.write("/goStraight/run -100 \n".encode())
        if k3=='C':
            print ("right")
            s.write("/turn/run 100 -0.3\n".encode())
        if k3=='D':
            print ("left")
            s.write("/turn/run 100 0.3 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
    elif k=='q':
        print ("quit") 
        return 0
    elif k=='p':
        print ("park")
        d1 = input("d1: ")
        d2 = input("d2: ")
        dir = input("direction: ")

        s.write(f"/park/run {d2} \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        if dir != 'n':
            if dir == 'w':
                s.write("/turn/run 100 -0.3 \n".encode())
            elif dir == 'e':
                s.write("/turn/run 100 0.3 \n".encode())
                
            time.sleep(3)
            s.write("/stop/run \n".encode())
            s.write(f"/park/run {d1} \n".encode())
            time.sleep(1)
            s.write("/stop/run \n".encode())
    elif k=='l':
        print ("line")
        s.write("/line/run\n".encode())
        #time.sleep(1)
        #s.write("/stop/run \n".encode())
    elif k==',':
        print ("left")
        s.write("/turn/run 100 0.5 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
    elif k=='.':
        print ("right")
        s.write("/turn/run 100 -0.5 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
    elif k=='a':
        print ("AprilTag")
        s.write("/tag/run \n".encode())
        #time.sleep(1)
        s.write("/stop/run \n".encode())
    elif k=='c':
        print ("circle") 
        s.write("/turn/run 100 -0.3 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        s.write("/turn/run 100 -0.3 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        s.write("/goStraight/run 50 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        s.write("/turn/run 100 0.3 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        s.write("/turn/run 100 0.3 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
        s.write("/turn/run 100 0.3 \n".encode())
        time.sleep(1)
        s.write("/stop/run \n".encode())
    else:
        print ("not an arrow key!")
    return 1

if len(sys.argv) < 1:
    print ("No poprt input")
s = serial.Serial(sys.argv[1])
while get():
    i = 0