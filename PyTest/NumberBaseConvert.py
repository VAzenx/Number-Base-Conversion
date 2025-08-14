#กำหนดให้โปรแกรมนี้เป็นเครื่องมือแปลงเลขฐานต่างๆ
#รองรับเลขฐาน 2, 8, 10 และ 16
# ใช้ tkinter สำหรับ GUI
# ใช้ ttk สำหรับ widget
#Cr.Wutthipong Wongwai INe
#ไม่ได้เขียนเองทั้งหมด

import tkinter as tk
from tkinter import ttk, messagebox
import re

class BaseConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("เครื่องมือแปลงเลขฐาน by.wutthipong wongwai")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        self.binary_var = tk.StringVar()
        self.octal_var = tk.StringVar()
        self.decimal_var = tk.StringVar()
        self.hex_var = tk.StringVar()
        
        self.binary_var.set("0")
        self.octal_var.set("0")
        self.decimal_var.set("0")
        self.hex_var.set("0")
        
        self.setup_ui()
        
        self.binary_var.trace('w', lambda *args: self.convert_from_binary())
        self.octal_var.trace('w', lambda *args: self.convert_from_octal())
        self.decimal_var.trace('w', lambda *args: self.convert_from_decimal())
        self.hex_var.trace('w', lambda *args: self.convert_from_hex())
        
        self.updating = False
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        title_label = ttk.Label(main_frame, text="เครื่องมือแปลงเลขฐาน", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Binary (เลขฐาน 2)
        ttk.Label(main_frame, text="Binary (ฐาน 2):", font=("Arial", 12)).grid(
            row=1, column=0, sticky=tk.W, pady=5, padx=(0, 10))
        binary_entry = ttk.Entry(main_frame, textvariable=self.binary_var, 
                                font=("Courier", 11), width=30)
        binary_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        ttk.Button(main_frame, text="คัดลอก", 
                  command=lambda: self.copy_to_clipboard(self.binary_var.get())).grid(
            row=1, column=2, pady=5)
        
        # Octal (เลขฐาน 8)
        ttk.Label(main_frame, text="Octal (ฐาน 8):", font=("Arial", 12)).grid(
            row=2, column=0, sticky=tk.W, pady=5, padx=(0, 10))
        octal_entry = ttk.Entry(main_frame, textvariable=self.octal_var, 
                               font=("Courier", 11), width=30)
        octal_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        ttk.Button(main_frame, text="คัดลอก", 
                  command=lambda: self.copy_to_clipboard(self.octal_var.get())).grid(
            row=2, column=2, pady=5)
        
        # Decimal (เลขฐาน 10)
        ttk.Label(main_frame, text="Decimal (ฐาน 10):", font=("Arial", 12)).grid(
            row=3, column=0, sticky=tk.W, pady=5, padx=(0, 10))
        decimal_entry = ttk.Entry(main_frame, textvariable=self.decimal_var, 
                                 font=("Courier", 11), width=30)
        decimal_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        ttk.Button(main_frame, text="คัดลอก", 
                  command=lambda: self.copy_to_clipboard(self.decimal_var.get())).grid(
            row=3, column=2, pady=5)
        
        # Hexadecimal (เลขฐาน 16)
        ttk.Label(main_frame, text="Hexadecimal (ฐาน 16):", font=("Arial", 12)).grid(
            row=4, column=0, sticky=tk.W, pady=5, padx=(0, 10))
        hex_entry = ttk.Entry(main_frame, textvariable=self.hex_var, 
                             font=("Courier", 11), width=30)
        hex_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(0, 10))
        ttk.Button(main_frame, text="คัดลอก", 
                  command=lambda: self.copy_to_clipboard(self.hex_var.get())).grid(
            row=4, column=2, pady=5)
        
        # ปุ่มล้างทั้งหมด
        clear_button = ttk.Button(main_frame, text="ล้างทั้งหมด", 
                                 command=self.clear_all)
        clear_button.grid(row=5, column=0, columnspan=3, pady=20)
        
        # คำแนะนำการใช้งาน
        info_frame = ttk.LabelFrame(main_frame, text="คำแนะนำ", padding="10")
        info_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        main_frame.rowconfigure(6, weight=1)
        
        info_text = tk.Text(info_frame, height=8, wrap=tk.WORD, font=("Arial", 10))
        info_text.pack(fill=tk.BOTH, expand=True)
        
        instructions = """วิธีการใช้งาน:
1. พิมพ์ตัวเลขในช่องใดช่องหนึ่ง ระบบจะแปลงค่าให้อัตโนมัติ
2. Binary: ใช้เฉพาะเลข 0 และ 1 เท่านั้น
3. Octal: ใช้เลข 0-7 เท่านั้น  
4. Decimal: ใช้เลข 0-9 ตามปกติ
5. Hexadecimal: ใช้เลข 0-9 และ A-F (หรือ a-f)
6. คลิกปุ่ม "คัดลอก" เพื่อคัดลอกค่าไปยัง clipboard
7. คลิกปุ่ม "ล้างทั้งหมด" เพื่อรีเซ็ตค่าทั้งหมดเป็น 0"""
        
        info_text.insert(tk.END, instructions)
        info_text.config(state=tk.DISABLED)
    
    def convert_from_binary(self):
        if self.updating:
            return
        try:
            value = self.binary_var.get().strip()
            if not value or not re.match(r'^[01]+$', value):
                return
            
            decimal_value = int(value, 2)
            self.update_other_bases(decimal_value, 'binary')
        except ValueError:
            pass
    
    def convert_from_octal(self):
        if self.updating:
            return
        try:
            value = self.octal_var.get().strip()
            if not value or not re.match(r'^[0-7]+$', value):
                return
            
            decimal_value = int(value, 8)
            self.update_other_bases(decimal_value, 'octal')
        except ValueError:
            pass
    
    def convert_from_decimal(self):
        if self.updating:
            return
        try:
            value = self.decimal_var.get().strip()
            if not value or not re.match(r'^\d+$', value):
                return
            
            decimal_value = int(value, 10)
            self.update_other_bases(decimal_value, 'decimal')
        except ValueError:
            pass
    
    def convert_from_hex(self):
        if self.updating:
            return
        try:
            value = self.hex_var.get().strip()
            if not value or not re.match(r'^[0-9A-Fa-f]+$', value):
                return
            
            decimal_value = int(value, 16)
            self.update_other_bases(decimal_value, 'hex')
        except ValueError:
            pass
    
    def update_other_bases(self, decimal_value, source):
        self.updating = True
        
        if source != 'binary':
            self.binary_var.set(bin(decimal_value)[2:])
        if source != 'octal':
            self.octal_var.set(oct(decimal_value)[2:])
        if source != 'decimal':
            self.decimal_var.set(str(decimal_value))
        if source != 'hex':
            self.hex_var.set(hex(decimal_value)[2:].upper())
        
        self.updating = False
    
    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        messagebox.showinfo("คัดลอกเรียบร้อย", f"คัดลอก '{text}' ไปยัง clipboard แล้ว")
    
    def clear_all(self):
        self.updating = True
        self.binary_var.set("0")
        self.octal_var.set("0")
        self.decimal_var.set("0")
        self.hex_var.set("0")
        self.updating = False

def main():
    root = tk.Tk()
    app = BaseConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()