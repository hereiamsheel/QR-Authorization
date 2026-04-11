# 🔐 QR Code Authorization System  

A Python-based QR Code Authentication System using OpenCV and Pyzbar. This project detects QR codes from an image or webcam and verifies authorization data from a text file.

---

## 🚀 Features  

- QR Code detection  
- Real-time webcam scanning  
- Authorization validation using `datafile.txt`  
- Bounding box drawing around detected QR  
- Displays decoded information on screen  

---

## 🛠️ Tech Stack  

- Python  
- OpenCV  
- Pyzbar  
- NumPy  

---

## 📂 Project Structure  

QR-Code-Authorization-System/  
│── datafile.txt      # Stores authorized QR data  
│── image.png         # Sample image for testing  
│── QRCodeAuth.py     # Main script for QR detection and authorization  
│── test.py           # Testing/experimental script  
│── README.md         # Project documentation  

---

## ▶️ How It Works  

1. The system reads input from either an image file or a webcam stream.  
2. QR codes are detected using Pyzbar.  
3. Extracted data is decoded and compared with entries in `datafile.txt`.  
4. If a match is found, access is authorized; otherwise, it is denied.  
5. The result is displayed along with a bounding box around the QR code.  

---

## 📌 Usage  

- Run `QRCodeAuth.py` to start scanning.  
- Place a valid QR code in front of the webcam or provide an image.  
- Ensure authorized data is listed in `datafile.txt`.  

---

## 📈 Future Improvements  

- Add database integration (MySQL/SQLite)  
- Build a web dashboard for analytics  
- Export scan logs   

---

## 👨‍💻 Author  

Developed as a simple and efficient QR-based authentication system using computer vision.