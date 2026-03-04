# 🚧 Road Monitoring System (Phase 1)

A real-time **road monitoring pipeline** designed to capture, manage, and organize roadway data efficiently.  
Built as a foundation for future pothole detection using **ML/DL (YOLOv8)**.

---

## 📌 Overview

This project focuses on building the **data pipeline and system architecture** before integrating detection models.

It simulates real-world road monitoring by:
- Capturing images from live video  
- Managing storage intelligently  
- Logging every system event  
- Preparing structured data for future model integration  

> ⚠️ This is **Phase 1—focusing on system design before model integration.**

---

## 🚀 Features

- 📸 **Automated Image Capture**
  - Captures frames from live video at regular intervals  

- 🗂 **Organized Data Storage**
  - `captured_images/` → all captured images  
  - `normal/` → non-pothole images  
  - `pothole/` → reserved for pothole detections  

- 🧹 **Smart Cleanup System**
  - Automatically deletes old images  
  - Keeps only the most recent relevant data  

- 📍 **Metadata Embedding**
  - Each image contains:
    - Date  
    - Time  
    - Location (currently added manually)  
    - Coordinates  

- 📜 **Logging System**
  - Logs all events:
    - Image captured  
    - Image moved  
    - Image deleted  
  - Includes timestamp and location for traceability  

---

## ⚙️ Testing Mode

To enable faster testing, real-world timing was scaled down:

| Function          | Real Time | Test Time |
|------------------|----------|----------|
| Capture Interval | 4 hours  | 40 seconds |
| Cleanup Interval | 24 hours | 2 minutes |

This allows rapid validation without long waiting times.

---

## 🧠 System Workflow

1. Capture image from webcam  
2. Add metadata overlay (time, date, location)  
3. Save to `captured_images/`  
4. (Future) Detect pothole  
5. Move image to:
   - `normal/` OR  
   - `pothole/`  
6. Log every action  
7. Cleanup old images automatically  

---

## 🛠 Tech Stack

- Python  
- OpenCV  
- NumPy  
- Logging  

---

## 📂 Project Structure
The project contains folders for storing images and logs. The captured_images folder stores all captured images from the live video. Based on processing, images are then categorized into either the normal folder or the pothole folder. A logs folder is used to store application logs, including details like image capture, movement, and deletion with timestamps and location. The main script camera_capture.py handles image capture, processing, and storage management. Additionally, the project includes a README.md file for documentation and a requirements.txt file for managing dependencies.
## 🔜 Future Enhancements

- Pothole detection using **YOLOv8**  
- GPS integration for automatic location tagging  
- Real-time dashboard  
- Alert system for road damage


<img width="657" height="344" alt="Screenshot 2026-03-04 at 8 30 40 AM" src="https://github.com/user-attachments/assets/d2666cb3-bc72-4420-9a23-89e77474e681" />


---

![Mumbai_Street_01_2026-03-04_08-22-31](https://github.com/user-attachments/assets/00749a72-bc8f-4ae6-9900-93446c9e07ec)


## 💡 Key Learning

> A strong ML/DL system is not just about models—  
> it’s about building a reliable and scalable pipeline around them.

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
