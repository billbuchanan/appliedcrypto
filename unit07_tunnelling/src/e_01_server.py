import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_cert_chain(certfile="mycert.pem") 

def handle(conn):
    conn.write(b'GET / HTTP/1.1\n')
    print(conn.recv().decode())

while True:
  sock = socket.socket()
  sock.bind(('', 444))
  sock.listen(5)
  context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
  context.load_cert_chain(certfile="mycert.pem") 
  context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1  # optional
  context.set_ciphers('AES256+ECDH:AES256+EDH')
  while True:
    conn = None
    ssock, addr = sock.accept()
    try:
      conn = context.wrap_socket(ssock, server_side=True)
      handle(conn)
    except ssl.SSLError as e:
      print(e)
    finally:
      if conn:
        conn.close()
