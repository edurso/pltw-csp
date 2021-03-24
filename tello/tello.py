import threading 
import socket

class Drone():

    def __init__(self):
        """
        Initialize Drone Object
        """
        self.local_address = ('',  9001) # (host, port) Local Address
        self.drone_address = ('192.168.10.1', 8889) # (host, port) Tello Address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Socket
        self.sock.bind(self.local_address) # Bind UDP Transmission to Local Address
        recvThread = threading.Thread(target=self.recv)
        recvThread.start()
        self.command_mode()

    def recv(self):
        """
        Recieves Data From Tello
        """
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                print(data.decode(encoding="utf-8"))
            except Exception:
                print ('\nExit . . .\n')
                break
    
    def send_packet(self, msg: str) -> int:
        """
        Sends the given message to the drone.
        """
        return self.sock.sendto(msg.encode(encoding="utf-8"), self.drone_address)
    
    def interactive_loop_cli(self):
        print ('####################### TELLO DRONE APPLICATION #######################')
        commands = ['command', 'takeoff', 'land', 'flip', 'forward', 'back', 'left', 'right', 'up', 'down', 'cw', 'ccw', 'speed', 'end', 'kill']
        print ('Commands are:\n\t' + '\n\t'.join(commands))
        while True: 
            try:
                msg = input('')
                if not msg:
                    break  
                if 'end' in msg or 'kill' in msg:
                    self.kill() 
                    break
                self.send_packet(msg)
            except KeyboardInterrupt:
                print ('\n . . .\n')
                self.kill() 
                break
    
    def command_mode(self):
        """
        Enables the drone in command mode
        """
        self.send_packet(self, 'command')
    
    def takeoff(self):
        """
        Starts autonomous take off sequence
        """
        self.send_packet(self, 'takeoff')
    
    def land(self):
        """
        Starts autonomous landing sequence
        """
        self.send_packet(self, 'land')
    
    def flip(self):
        """
        Filps the drone midair
        """
        self.send_packet(self, 'flip')
    
    def forward(self, quantity: int):
        self.send_packet(self, 'forward ' + quantity)
    
    def back(self, quantity: int):
        self.send_packet(self, 'back ' + quantity)
    
    def left(self, quantity: int):
        self.send_packet(self, 'left ' + quantity)
    
    def right(self, quantity: int):
        self.send_packet(self, 'right ' + quantity)
    
    def up(self, quantity: int):
        self.send_packet(self, 'up ' + quantity)
    
    def down(self, quantity: int):
        self.send_packet(self, 'down ' + quantity)
    
    def clockwise(self, degrees: int):
        self.send_packet(self, 'cw ' + degrees)
    
    def counterclockwise(self, degrees: int):
        self.send_packet(self, 'back ' + degrees)
    
    def speed(self, quantity: int):
        self.send_packet(self, 'speed ' + quantity)
    
    def kill(self):
        self.sock.close()
