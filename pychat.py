import tkinter as tk


class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        # self.test_button = tk.Button(self, text="Click Me!",
        #                              command=self.print_message)
        # self.test_button.pack()
        # self.message_label = tk.Label(self)
        # self.message_label.pack()
        # self.message = tk.Message(self, text="this is a\n"
        #                                      "multiline\n"
        #                                      "message")
        # self.message.pack(side=tk.BOTTOM)
        self.message_history_frame = tk.Frame(self)
        self.message_history_frame.pack(fill=tk.BOTH, expand=True)

        self.message_sent_frame = tk.Frame(self.message_history_frame)
        self.message_sent_frame.pack(side=tk.TOP, fill=tk.X)
        self.message_sent = tk.Message(self.message_sent_frame, text="We sent this message", width=100)
        self.message_sent.pack(side=tk.RIGHT)

        self.message_recv_frame = tk.Frame(self.message_history_frame)
        self.message_recv_frame.pack(side=tk.TOP, fill=tk.X)
        self.message_recv = tk.Message(self.message_recv_frame, text="We received this message", width=100)
        self.message_recv.pack(side=tk.LEFT)

        self.message_send_frame = tk.Frame(self)
        self.message_send_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.message_send_button = tk.Button(self.message_send_frame, text="Send")
        self.message_send_button.pack(side=tk.RIGHT)
        self.message_entry = tk.Entry(self.message_send_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def print_message(self):
        self.message_label.configure(text="Button Clicked")


root = tk.Tk()
root.geometry("500x500")
app = App(root)
root.mainloop()