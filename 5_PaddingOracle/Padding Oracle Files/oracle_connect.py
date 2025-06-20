"""
 Santa Clara University: CSCI 181
"""
sock = None

BLOCKSIZE= 16

SERVERPORT= 12001
SERVERIP = "18.217.20.161"

def oracle_connect():
    import socket
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVERIP, SERVERPORT))
    except socket.error as e:
        print(e)
        return -1

    print("Connected to server successfully.")

    return 1

def oracle_disconnect():
    if not sock:
        print("[WARNING]: You haven't connected to the server yet.")
        return -1

    sock.close()

    print("Connection closed successfully.")

    return 0

def is_padding_okay(block1: bytes, block2: bytes) -> int:
    write_size = BLOCKSIZE * 2
    if not sock:
        print("[WARNING]: You haven't conected to the server yet.")
        return -1

    if len(block1) != len(block2) or len(block1) != BLOCKSIZE:
        print("Unexpected block size")
        return -1

    
    cipher = block1 + block2
    try:
        n_bytes_sent = sock.send(cipher)
        
        if n_bytes_sent != BLOCKSIZE * 2:
            print("Incomplete write to socket.")
            sock.close()
            return -1
    
    except Exception as e:
        print(f"Socket write error: {e}")
        sock.close()
        return -1

    try:
        buf = sock.recv(2)
        if not buf:
            print("Server closed connection")
            return -1
    except Exception as e:
        print(f"Socket read error: {e}")
        return -1
    response_from_oracle = int(chr(buf[0])) - int('0')
    return response_from_oracle


