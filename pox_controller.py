from pox.core import core
from pox.openflow import *
import requests
import json

log = core.getLogger()

# Change this to your ML server's URL
ML_SERVER_URL = 'http://127.0.0.1:5002/process_traffic'

class TrafficMonitor(EventMixin):
    def __init__(self, connection):
        self.connection = connection
        connection.addListeners(self)

    def _handle_packet_in(self, event):
        packet = event.parsed
        # Here you can capture relevant data from the packet
        # For example, you could extract source and destination IPs and ports
        traffic_data = {
            "src_ip": packet.src,
            "dst_ip": packet.dst,
            "protocol": packet.protocol,
            "packet_length": len(packet)
        }
        
        log.debug(f"Captured traffic: {traffic_data}")
        
        # Send traffic data to ML server
        self.send_to_ml_server(traffic_data)

    def send_to_ml_server(self, traffic_data):
        try:
            response = requests.post(ML_SERVER_URL, json=traffic_data)
            if response.status_code == 200:
                log.info("Traffic data sent to ML server successfully.")
            else:
                log.error(f"Failed to send data to ML server: {response.status_code} - {response.text}")
        except Exception as e:
            log.error(f"Error sending data to ML server: {str(e)}")

class POXController(EventMixin):
    def __init__(self):
        core.openflow.addListeners(self)

    def _handle_ConnectionUp(self, event):
        log.info(f"Switch {event.dpid} connected.")
        TrafficMonitor(event.connection)

def launch():
    core.openflow.addListeners(POXController())
    log.info("POX Controller for real-time traffic monitoring started.")

