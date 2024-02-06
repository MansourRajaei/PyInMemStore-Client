import socket

def send_request(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect(('localhost', 8080))
            client_socket.send(command.encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            return response
    except Exception as e:
        return str(e)

def BiuldInputHelp():
    print("Please enter the command according to the instructions below :")
    print("SET key value")
    print("GET key")
    print("DELETE key")
    print("EXPIRE key time")
    print("TTL key")
    print("BEGIN")
    print("COMMIT")
    print("ROLLBACK")
    print("LIST")
    print("SORT")
    print("EXIT")
    print("\n")

command = ""
BiuldInputHelp()
while True:
    command = input("Please enter the command: ")
    if str(command).upper() == "EXIT":
        break
    elif command == "" :
        command = input("Please enter the command: ")
    else:
        response = send_request(command)
        print(f"Command: {command}")
        print(f"Response: {response}")

print ("Disconnected")


