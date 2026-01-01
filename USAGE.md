# 📄 USAGE.md
## How to Use Knock Unlock 🔐

This document explains how to set up, enroll, and use the Knock Unlock system step by step.

---

## 📋 Requirements
- Python 3.9 or higher
- A working microphone
- Quiet environment for best accuracy

---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Knock-Unlock.git
cd Knock-Unlock
```

2. Install dependencies:
```bash
pip install sounddevice numpy scipy librosa
```

---

## 🔐 Step 1: Enrollment (One-Time Setup)

Enrollment registers the authorized knock rhythm.

Run:
```bash
python enroll_pattern.py
```

### What to do:
- Press **ENTER** when prompted  
- Perform the same knock pattern each time  
- Complete **5 valid samples**  

### What happens:
- Audio is recorded for each attempt  
- Knocks are detected  
- Time gaps between knocks are extracted  
- Mean and standard deviation are calculated  
- The pattern is saved to `pattern.json`  

⚠️ If an inconsistent knock is detected, the system will ask you to retry.

---

## 🔓 Step 2: Authentication (Every Use)

For each authentication attempt, run:
```bash
python record_knock.py
python verify_pattern.py
```

### Output:
- ✅ **GRANTED** → Access allowed  
- ❌ **DENIED** → Access rejected  

If the first attempt fails, **one retry is allowed** before final denial.
