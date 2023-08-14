import socket
from concurrent.futures import ThreadPoolExecutor as threadpool

pool = threadpool(1000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 12743))
