#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018
#
# Modified by MPS
#

import threading 
import socket
import time
import cv2

host = ''
port = 9000
locaddr = (host, port)


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . . RECV\n')
            break


print('\r\n\r\nTello Python3 Demo.\r\n')

print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

sock.sendto(b'command', tello_address)
print('command ok')
time.sleep(0.5)
sock.sendto(b'streamon', tello_address)
print('stream on')
time.sleep(1)
sock.close()

cap = cv2.VideoCapture("udp://%s:%s?overrun_nonfatal=1&fifo_size=50000000" % ('192.168.10.1', '11111'))

print('start cap')
while True:
    try:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('tello', cv2.resize(frame, (360, 240)))
            cv2.waitKey(1)
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        cap.release()
        print('\nExit . . .\n')
        break
