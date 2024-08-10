import os
import re
import tkinter as tk
from tkinter import filedialog

def remove_ib_resource_from_files(folder_path):
    if not os.path.exists(folder_path):
        update_text_widget("错误: 文件夹不存在。\n")
        return

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ini'):
                file_path = os.path.join(root, file)
                process_file(file_path)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    pattern = re.compile(r'^ib = Resource_Bak_IB[0-9]$')
    found = False
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if pattern.match(line.strip()):
                found = True
                continue
            file.write(line)

    if found:
        update_text_widget(f"在文件 {file_path} 中找到并删除了匹配的行。\n")
    else:
        update_text_widget(f"在文件 {file_path} 中未找到匹配的行。\n")

def update_text_widget(message):
    app.after(0, lambda: text_widget.insert(tk.END, message))

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_var.set(folder_path)

def run_script():
    folder_path = entry_var.get()
    remove_ib_resource_from_files(folder_path)

app = tk.Tk()
app.title("INI 文件处理")
app.geometry('500x300')

text_widget = tk.Text(app, height=10, width=50)
text_widget.pack(pady=20)

scrollbar = tk.Scrollbar(app, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

entry_var = tk.StringVar()

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, textvariable=entry_var, width=50)
entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(frame, text="选择文件夹", command=select_folder)
browse_button.pack(side=tk.LEFT, padx=5)

run_button = tk.Button(app, text="运行", command=run_script)
run_button.pack(pady=5)

app.mainloop()