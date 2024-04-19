import os
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

# Set the FTP server parameters
FTP_HOST = "0.0.0.0"  # Listen on all network interfaces
FTP_PORT = 21
FTP_USER = "user"
FTP_PASSWORD = "password"
FTP_DIRECTORY = "D:\\FTP"  # The directory to be shared

def run_ftp_server():
    # Create a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only anonymous user
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmwMT')
    authorizer.add_anonymous(FTP_DIRECTORY)

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (optional)
    handler.banner = "Welcome to the FTP server"

    # Specify a masquerade address and the range of ports to use for passive connections
    handler.masquerade_address = FTP_HOST
    handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on the defined address and port
    server = servers.FTPServer((FTP_HOST, FTP_PORT), handler)

    # Set a limit for maximum connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # Start the FTP server
    print(f"Starting FTP server on {FTP_HOST}:{FTP_PORT}...")
    server.serve_forever()

if __name__ == "__main__":
    run_ftp_server()
