import sys

message = sys.argv[1]
print("Received commits message:" + message)
print()
if len(message) < 7:
    print("Message too short: " + message)
    sys.exit(1)
sys.exit(0)
