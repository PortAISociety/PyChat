import tkinter as tk
from .pychat import *
from .SSDP_Worker import SSDP_Worker

root = tk.Tk()
root.geometry("500x500")
app = App(root)

# ssdp_worker = SSDP_Worker("port-ai-soc-py-chat")
# ssdp_worker.start()

root.mainloop()
