import tkinter as tk
from tkinter.constants import TOP, X


class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.message_list = []
        self.create_widgets()
    
    def create_widgets(self):
        self.message_history_frame = tk.Frame(self)
        self.message_history_frame.pack(fill=tk.BOTH, expand=True)
        self.message_history_frame.grid_columnconfigure(0, weight=1)
        self.message_history_frame.grid_rowconfigure(0, weight=1)

        self.message_history_scollbar = tk.Scrollbar(self.message_history_frame)
        self.message_history_scollbar.grid(row=0, column=1, sticky="NS")
        self.message_history_canvas = tk.Canvas(self.message_history_frame,
                                                yscrollcommand=self.message_history_scollbar.set)
        self.message_history_canvas.config(scrollregion=self.message_history_canvas.bbox(tk.ALL))
        self.message_history_canvas.grid(row=0, column=0, sticky="NESW")
        self.message_history_scollbar.config(command=self.message_history_canvas.yview)

        # self.message_sent_frame = tk.Frame(self.message_history_frame)
        # self.message_sent_frame.pack(side=tk.TOP, fill=tk.X)
        # self.message_sent = tk.Message(self.message_sent_frame, text="We sent this message", width=100)
        # self.message_sent.pack(side=tk.RIGHT)

        # self.message_recv_frame = tk.Frame(self.message_history_frame)
        # self.message_recv_frame.pack(side=tk.TOP, fill=tk.X)
        # self.message_recv = tk.Message(self.message_recv_frame, text="We received this message", width=100)
        # self.message_recv.pack(side=tk.LEFT)



        self.message_send_frame = tk.Frame(self)
        self.message_send_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.message_send_button = tk.Button(self.message_send_frame, text="Send", command=self.send_message)
        self.message_send_button.pack(side=tk.RIGHT)
        self.message_entry = tk.Entry(self.message_send_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def print_message(self):
        self.message_label.configure(text="Button Clicked")

    def send_message(self):
        message_string = self.message_entry.get()
        if len(message_string) == 0:
            return
        new_message = Message(self.message_history_canvas, Message.SENT, message_string)
        self.message_list.append(new_message)
        new_message.pack(side=tk.TOP, fill=tk.X)
        self.message_entry.delete(0, tk.END)



class Message(tk.Frame):
    SENT = 1
    RECEIVED = 2
    def __init__(self, parent, message_type, text, width=100):
        super().__init__(parent)
        self.message = tk.Message(self, text=text, width=width)
        if (message_type == Message.SENT):
            self.message.pack(side=tk.RIGHT)
        elif (message_type == Message.RECEIVED):
            self.message.pack(side=tk.LEFT)
        else:
            raise ValueError(f"Unrecognised message_type: {message_type}")
