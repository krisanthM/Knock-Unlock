🔐 Knock Unlock
A Rhythm-Based Authentication System
📌 Overview

Knock Unlock is a secure and intuitive authentication system that grants access using a unique knock rhythm captured through a microphone. Instead of relying on traditional passwords or computationally heavy machine learning models, the system authenticates users by analyzing the time gaps between consecutive knocks.

This makes the system lightweight, explainable, and reliable, especially in physical environments. The project was developed as part of a hackathon challenge to explore alternative authentication mechanisms using sound and temporal patterns.

❓ Problem Statement

Traditional authentication methods such as passwords, PINs, and unlock patterns have inherent limitations:

Susceptible to observation and shoulder-surfing

Weak or reused credentials reduce security

Not intuitive for physical or embedded systems

There is a clear need for an authentication method that is:

Hard to guess

Easy to perform

Resistant to casual observation

Suitable for real-world physical interaction

💡 Proposed Solution

Knock Unlock introduces rhythm-based authentication, where access is granted only when the user performs a predefined knock pattern on a surface.

Authentication Flow:

Audio is recorded via a microphone

Individual knock events are detected

Time gaps between consecutive knocks are extracted

The extracted rhythm is compared with a stored reference

Access is granted or denied using tolerance-based matching

This solution avoids complex ML pipelines and instead relies on deterministic time-gap analysis, which is more stable for small datasets and real-time use.

⭐ Key Features

Microphone-based knock detection

Time-gap (rhythm-based) authentication

Deterministic and explainable logic

Lightweight and real-time execution

No machine learning required

Low false acceptance rate

🧠 Why Not Machine Learning?

Machine learning models such as CNNs and LSTMs using MFCC features were initially explored. However:

Knock sounds have very similar spectral characteristics

Small datasets resulted in unstable model training

Feature overlap caused accuracy to plateau

Since knock authentication fundamentally depends on rhythm, a deterministic approach proved to be:

More reliable

Faster at runtime

Easier to debug and explain

Better suited for embedded and real-world environments

🏗️ System Architecture
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

🛠️ Technical Approach

Record knock audio using a microphone

Detect knock peaks using energy-based thresholding

Extract inter-knock time intervals

Enroll multiple valid samples to compute:

Mean time gaps

Standard deviation

Normalize time gaps using ratio-based comparison

Authenticate using tolerance-based matching

📁 Project Structure
knock-unlock/
├── record_knock.py        # Records knock audio from microphone
├── extract_gaps.py        # Detects knocks and extracts time gaps
├── enroll_pattern.py     # Enrollment and calibration
├── verify_pattern.py     # Authentication logic
├── pattern.json          # Stored reference knock pattern
├── requirements.txt
└── README.md

⚙️ Setup Instructions
🔧 Prerequisites

Python 3.9 or higher

Working microphone

📦 Install Dependencies
pip install sounddevice numpy scipy librosa

🔐 Enrollment (One-Time Setup)

Enroll the authorized knock rhythm:

python enroll_pattern.py


During enrollment:

5 valid knock samples are recorded

Knock count consistency is enforced

Mean and standard deviation are calculated

Pattern is stored in pattern.json

🔓 Authentication

For each authentication attempt:

python record_knock.py
python verify_pattern.py

Output:

✅ GRANTED → Access allowed

❌ DENIED → Access rejected

One retry is allowed before final denial.

☁️ Google Technologies Used

Google Cloud Platform (GCP) – Cloud infrastructure

Firebase (Firestore) – Backend logging

TensorFlow Lite – Explored during experimentation

🔒 Security Considerations

Knock rhythm acts as a temporal password

Inconsistent knock counts are automatically rejected

Deterministic logic reduces false acceptance

No sensitive biometric or spectral data is stored

🚀 Future Enhancements

Multi-user enrollment support

GUI-based authentication interface

Adaptive tolerance tuning

OS-level or IoT-level unlock integration

🧪 Demo Flow

Run enrollment

Perform correct knock → ✅ GRANTED

Perform incorrect knock → ❌ DENIED

🏁 Conclusion

Knock Unlock demonstrates a secure, intuitive, and efficient authentication mechanism using rhythm-based knock patterns. By leveraging deterministic time-gap analysis instead of machine learning, the system achieves:
