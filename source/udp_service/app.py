
import random
from socket import *
import requests
import json

UDP_PORT = 2333

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', UDP_PORT))

print(f"[Yaarl is listening on {UDP_PORT}/udp]")

CONVERTAPIURL="http://localhost:7374/convert/?from=FROM&to=TO&data=DATA"
LOGBOOKAPIURL="http://localhost:7373/api/logbook/entry"

while True:
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(512)

        # Capitalize the message from the client
        message = message.decode()

        # Otherwise, the server responds
        print (f"[Log Received] {message}")

        api_from = "adif"
        api_to = "yaarl"

        api_url = CONVERTAPIURL.replace("FROM", api_from).replace("TO",api_to).replace("DATA",message)

        print (f"[Sending to Conversion API]")
        json_response = requests.get(url=api_url)

        if json_response.status_code == 200:

            json_logdata = json.dumps(str(json_response.content))

            headers= {'Accept': '*/*',
                'Connection': 'close',
                'Content-Type': 'application/json',
                'User-Agent': 'yaarl udp listener v0.1'}
            
            print (f"[Sending to Yaarl Log API]")
            print (json_logdata)
            
            log_response = requests.post(url=LOGBOOKAPIURL, headers=headers, data=json_logdata)
            print (f"Got: {log_response.status_code}, {log_response.content}")

        else:
            print ("[Error] Conversion API failed.")



