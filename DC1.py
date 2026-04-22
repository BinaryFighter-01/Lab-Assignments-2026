
# rpc_server.py

from xmlrpc.server import SimpleXMLRPCServer

# Function to compute factorial
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

# Start server
server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(factorial, "fact")

print("Server running...")
server.serve_forever()


# rpc_client.py
import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
n = int(input("Enter number: "))

# Remote call
result = proxy.fact(n)

print("Factorial:", result)