
from socket import *

S = socket(AF_INET, SOCK_STREAM)

F=S.fileno()
print(F, type(F))
