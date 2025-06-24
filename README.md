# Number Base Converter GUI

เครื่องมือแปลงเลขฐานแบบ GUI ที่พัฒนาด้วย Python และ Tkinter สำหรับแปลงเลขระหว่างฐาน 2, 8, 10, และ 16

## ✨ Features

- 🔄 **แปลงแบบอัตโนมัติ**: พิมพ์ตัวเลขในช่องใดช่องหนึ่ง ระบบจะแปลงให้ทุกฐานทันที
- 📋 **คัดลอกง่าย**: ปุ่มคัดลอกสำหรับแต่ละค่าที่แปลงแล้ว  
- ✅ **ตรวจสอบความถูกต้อง**: ตรวจสอบรูปแบบตัวเลขที่ถูกต้องสำหรับแต่ละฐาน
- 🧹 **ล้างค่าทั้งหมด**: รีเซ็ตค่าทั้งหมดด้วยคลิกเดียว
- 📖 **คำแนะนำในตัว**: มีคำแนะนำการใช้งานในแอพ
- 🇹🇭 **ภาษาไทย**: UI ภาษาไทยที่เข้าใจง่าย

## 🔢 รองรับเลขฐาน

| ฐาน | ชื่อ | ตัวเลขที่ใช้ | ตัวอย่าง |
|-----|------|-------------|---------|
| 2 | Binary | 0-1 | 1010 |
| 8 | Octal | 0-7 | 377 |
| 10 | Decimal | 0-9 | 255 |
| 16 | Hexadecimal | 0-9, A-F | FF |

## 🚀 Installation & Usage

### Requirements
- Python 3.x
- Tkinter (มักจะติดตั้งมาพร้อมกับ Python แล้ว)

### วิธีการติดตั้งและใช้งาน

1. **Clone repository**
   ```bash
   git clone https://github.com/your-username/number-base-converter.git
   cd number-base-converter
   ```

2. **รันแอพพลิเคชัน**
   ```bash
   python base_converter.py
   ```

3. **วิธีใช้งาน**
   - พิมพ์ตัวเลขในช่องใดช่องหนึ่ง
   - ระบบจะแปลงค่าให้อัตโนมัติในทุกฐาน
   - คลิก "คัดลอก" เพื่อคัดลอกค่าไปยัง clipboard
   - คลิก "ล้างทั้งหมด" เพื่อรีเซ็ตค่า

## 📸 Screenshots

*แอพพลิเคชันจะแสดง interface ที่เรียบง่าย ใช้งานสะดวก พร้อมช่องสำหรับแต่ละเลขฐาน*

## 🛠️ Technical Details

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Architecture**: Object-oriented design
- **Features**: 
  - Real-time conversion
  - Input validation with regex
  - Clipboard integration
  - Event-driven programming

## 📝 Example Usage

```python
# ตัวอย่างการแปลง
Binary: 1010      → Decimal: 10
Octal: 12         → Decimal: 10  
Decimal: 10       → Hex: A
Hexadecimal: A    → Binary: 1010
```
## 🏷️ Tags

`python` `gui` `tkinter` `converter` `binary` `octal` `decimal` `hexadecimal` `utility` `thai`

---
