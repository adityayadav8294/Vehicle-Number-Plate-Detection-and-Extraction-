# 🚗 Vehicle Number Plate Detection & Extraction System

<p align="center">
  <img src="assets/demo.png" width="850" alt="Vehicle Number Plate Detection Demo"/>
</p>

---

## 📌 Overview

The **Vehicle Number Plate Detection & Extraction System** is a deep learning–based computer vision project that detects and tracks vehicle license plates from video input using a YOLO-based object detection model.

This system processes video frames, identifies number plates, tracks them across frames, and generates an annotated output video.

It demonstrates practical implementation of object detection, tracking, and modular Python architecture suitable for real-world surveillance and smart traffic systems.

---

## 🎯 Key Features

✔ YOLO-based license plate detection  
✔ Frame-by-frame video processing  
✔ Object tracking support  
✔ Annotated output video generation  
✔ Modular & scalable architecture  
✔ Clean production-ready structure  

---

## 🛠 Tech Stack

- Python 3.x  
- YOLO (Object Detection Model)  
- OpenCV  
- NumPy  
- Custom Tracking Module  

---

## 🏗 Project Structure

```
Vehicle-Number-Plate-Detection-and-Extraction/
│
├── input/                # Add your test video here
├── assets/               # Demo images
├── my_tracking/          # Tracking module
│   ├── __init__.py
│   └── tracking.py
│
├── utils/                # Utility functions
│   ├── __init__.py
│   └── video.py
│
├── main.py               # Main execution file
├── requirements.txt      # Dependencies
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/adityayadav8294/Vehicle-Number-Plate-Detection-and-Extraction-
cd Vehicle-Number-Plate-Detection-and-Extraction-
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Place your test video inside the `input/` folder, then run:

```bash
python main.py
```

The system will:
- Load the YOLO model
- Process video frames
- Detect license plates
- Track detected objects
- Generate an annotated output video

---

## 🧠 How It Works

1. Video frames are read using OpenCV.
2. Each frame is passed to the YOLO detection model.
3. Bounding boxes are generated for detected license plates.
4. Tracking logic assigns IDs across frames.
5. Annotated frames are written into an output video.

---

## 📊 Real-World Applications

- Smart traffic monitoring
- Automated toll systems
- Parking management systems
- Law enforcement surveillance
- Smart city infrastructure

---

## 🚀 Future Enhancements

- OCR integration for plate number extraction
- Real-time webcam support
- Web dashboard interface
- Cloud deployment
- Database logging system

---

## 👨‍💻 Author

**Aditya Kumar**

📧 Email: adityasingh829442@gmail.com  
🌐 Portfolio: https://aditya82.netlify.app/

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐

---

## 📜 License

This project is intended for educational and research purposes.