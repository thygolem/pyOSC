import argparse
from pythonosc import osc_server

def print_handler(address, *args):
    print(f"{address}: {args}")

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port", type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    # Create OSC server
    server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), osc_server.Dispatcher())
    print(f"Serving on {server.server_address}")

    # Add OSC message handler
    server.dispatcher.map("/test", print_handler)

    # Start OSC server
    server.serve_forever()
