import argparse
from pythonosc import udp_client

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=5005, help="The port the OSC server is listening on")
    args = parser.parse_args()

    # Create OSC client
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    # Send OSC message
    client.send_message("/test", 123)
