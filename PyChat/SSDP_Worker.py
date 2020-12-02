import threading
import ssdpy


class SSDP_Worker (threading.Thread):
    def __init__(self, usn):
        super().__init__()
        self.server = ssdpy.SSDPServer(usn)

    def run(self):
        self.server.serve_forever()
