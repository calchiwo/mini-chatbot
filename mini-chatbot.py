import tkinter as tk

def get_ai_reply(user_text):
    text = user_text.lower()

    if "hello" in text:
        return "Hello, nice to meet you."
    if "how are you" in text:
        return "I am fine, and you."
    if "name" in text:
        return "My name is MiniBot."
    if "bye" in text:
        return "Goodbye."

    return "I am still learning."

def respond():
    txt = entry.get()
    reply = get_ai_reply(txt)

    chat.insert(tk.END, "You: " + txt + "\n")
    chat.insert(tk.END, "Bot: " + reply + "\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Mini Chatbot")

chat = tk.Text(root, width=40, height=15)
chat.pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Send", command=respond).pack()

root.mainloop()
