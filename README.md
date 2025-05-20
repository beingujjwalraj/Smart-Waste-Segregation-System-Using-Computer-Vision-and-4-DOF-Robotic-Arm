# ♻️ Smart Waste Segregation System Using Computer Vision and 4-DOF Robotic Arm

A project developed as part of the **Techniques and Management of E-Waste Recycling (ID6101)** course, this system automates the sorting of electronic waste (e-waste) using AI-powered computer vision and a 4-DOF robotic arm, reducing manual labor and increasing recycling efficiency.

## 👨‍💻 Team Members
- **Ujjwal Raj (ME22B1072)**
- **S Sreevidya (EC24M1001)**
- **RA Srinethe (EC24M1002)**

## 📌 Problem Statement

Traditional e-waste segregation depends on manual labor, which is slow, unsafe, and error-prone. With global e-waste generation reaching 62 million metric tons in 2022 and only 22% of it formally processed, there is a dire need for intelligent automation in this field.

## 💡 Project Objective

To design a smart, AI-powered robotic system that:
- Automatically detects and classifies e-waste items using computer vision (YOLOv8).
- Uses a programmable 4-DOF robotic arm to sort and place items based on category.
- Can be deployed for real-world, on-site waste segregation with minimal manual intervention.

## ⚙️ System Components

### 🔍 Computer Vision
- **Dataset**: 36-class e-waste dataset from Roboflow with bounding box annotations.
- **Model**: YOLOv8n (Ultralytics 8.3.107), trained on 370 curated images.
- **Performance**:  
  - Precision: **68.4%**
  - Recall: **49.5%**
  - mAP@0.5: **55.8%**
  - High-accuracy classes: Monitor, Router, Fan, LED (>85% mAP@0.5)

### 🤖 Robotic Arm
- **Model**: Pro-Range ESP32 4-DOF Robotic Arm with Web Control
- **Features**:
  - 4 Degrees of Freedom
  - Controlled via Wi-Fi using ESP32
  - Servo motors with 0°–180° range
- **Integration**: Receives object class from computer vision system and picks/places the object accordingly.

## 📽️ Demo

A demonstration video was recorded in **TLC-313** showcasing:
- Real-time detection and classification
- Robotic arm picking and placing identified e-waste


## 📈 Roadmap

### ✅ Completed
- Data curation and training of YOLOv8 model
- Robotic arm assembly and ESP32 integration
- System integration and testing

### 🔜 Future Work
- Develop a real-time monitoring app for tracking e-waste type and volume
- Portable design for field deployment
- Full end-to-end recycling automation, including dismantling and preprocessing

## 📚 References

1. Lahoti et al., *Multi-class waste segregation using computer vision and robotic arm*, PeerJ Computer Science (2024) [DOI: 10.7717/peerj-cs.1957](https://doi.org/10.7717/peerj-cs.1957)
2. Duan, Y. (2024), *EITCE Conference* [DOI: 10.1145/3711129.3711229](https://doi.org/10.1145/3711129.3711229)
3. Le Quang Thao (2023), *Journal of Material Cycles and Waste Management* [DOI: 10.1007/s10163-023-01796-4](https://doi.org/10.1007/s10163-023-01796-4)

## 🛠️ Technologies Used

- Python 3
- YOLOv8 (Ultralytics)
- Roboflow
- OpenCV
- ESP32 (Arduino IDE)
- HTML/CSS (for web control interface)

---

> “Automating waste segregation today ensures a cleaner, safer tomorrow.” 🌍
