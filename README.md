# Knock Unlock 🔐  
*A Rhythm‑Based Authentication System*

---

## 📌 Overview
Knock Unlock is a secure authentication system that grants access using a unique knock rhythm captured via a microphone. Instead of traditional passwords or complex machine learning models, the system authenticates users based on the **time gaps between consecutive knocks**, making it reliable, explainable, and lightweight.

This project was developed as part of a hackathon challenge to explore alternative authentication mechanisms using sound and temporal patterns.

---

## ❓ Problem Statement
Traditional authentication methods such as passwords, PINs, and patterns suffer from several drawbacks:
- They can be observed or stolen
- Users tend to reuse weak credentials
- They are not intuitive in physical environments

There is a need for an authentication mechanism that is:
- Hard to guess
- Easy to use
- Resistant to casual observation

---

## 💡 Proposed Solution
Knock Unlock introduces **rhythm‑based authentication**, where a user unlocks access by performing a specific knock pattern on a surface.

The system:
1. Records audio via a microphone
2. Detects individual knock events
3. Extracts the time gaps between knocks
4. Compares the rhythm against a stored reference pattern
5. Grants or denies access based on tolerance‑based matching

This approach avoids heavy machine learning and instead relies on **deterministic time‑gap analysis**, which is more stable for small datasets.

---

## ⭐ Key Features
- 🎤 Microphone‑based knock detection  
- ⏱️ Time‑gap (rhythm‑based) pattern recognition  
- 🔐 Deterministic and explainable authentication  
- ⚡ Lightweight and real‑time execution  
- ❌ No machine learning required  
- 📉 Low false acceptance rate  

---

## 🧠 Why Not Machine Learning?
Machine learning models (CNN/LSTM with MFCC features) were initially explored. However:
- Knock sounds are highly similar in spectral features
- Small datasets led to unstable training
- Accuracy plateaued due to overlapping features

Since knock authentication relies primarily on **rhythm**, a deterministic time‑gap approach proved:
- More reliable
- Easier to explain
- Faster at runtime
- Better suited for real‑world use

---

## 🏗️ System Architecture
Microphone
↓
Audio Recording
↓
Knock Detection
↓
Time Gap Extraction
↓
Rhythm Matching
↓
Access Granted / Denied


---

## 🛠️ Technical Approach
1. Record knock audio using a microphone
2. Detect knock peaks using energy thresholding
3. Extract inter‑knock time intervals
4. Enroll multiple correct samples to compute:
   - Mean time gaps
   - Standard deviation
5. Normalize gaps using ratio‑based comparison
6. Authenticate using tolerance‑based matching

---

## 📁 Project Structure
knock-unlock/
├── record_knock.py # Records fresh audio from microphone
├── extract_gaps.py # Detects knocks and extracts time gaps
├── enroll_pattern.py # Enrollment / calibration
├── verify_pattern.py # Authentication logic
├── pattern.json # Stored reference knock pattern
├── requirements.txt
└── README.md

---

---

## ⚙️ Setup Instructions  

### Prerequisites  
- Python 3.9 or higher  
- Working microphone  

### Install Dependencies  
```bash
pip install sounddevice numpy scipy librosa
🔐 Enrollment (One‑Time Setup)
Enroll the authorized knock rhythm:

bash
python enroll_pattern.py
During enrollment:

5 valid knock samples are recorded

Knock count consistency is enforced

Mean and standard deviation are computed

Pattern is saved to pattern.json

🔓 Authentication
For every authentication attempt:

bash
python record_knock.py
python verify_pattern.py
Output
✅ GRANTED → Access allowed
❌ DENIED → Access rejected

One retry is allowed before final denial.

☁️ Google Technologies Used
Google Cloud Platform (GCP) – Cloud infrastructure

Firebase (Firestore) – Backend logging

TensorFlow Lite (Explored) – Used during experimentation

🔒 Security Considerations
Unique rhythm acts as a temporal password

Inconsistent knock counts are rejected

Deterministic logic reduces false acceptance

No sensitive biometric data stored

⚠️ Limitations
Highly inconsistent knocking may cause false rejection

Designed primarily for single‑user authentication

Very noisy environments may affect detection

🚀 Future Enhancements
Multi‑user enrollment

GUI‑based authentication

Adaptive tolerance tuning

OS‑level unlock integration

🧪 Demo Flow
Run enrollment

Perform correct knock → ✅ GRANTED

Perform incorrect knock → ❌ DENIED

🏁 Conclusion
Knock Unlock demonstrates a secure and intuitive authentication system using rhythm‑based knock patterns.
By leveraging deterministic time‑gap analysis instead of machine learning, the system achieves higher stability, explainability, and real‑time performance — suitable for hackathon and real‑world use.
