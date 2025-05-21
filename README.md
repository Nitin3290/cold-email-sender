# 💌 Cold Email Automation Tool – For Job & Internship Outreach

This tool helps you **send personalized cold emails with your resume** to multiple recruiters **without coding**. Just fill out a `.env` file and a `recruiters.csv`, and the script will do the rest.

---

## 🧠 What is Cold Emailing?

Cold emailing means **emailing someone you don’t know personally** – like recruiters or hiring managers – to introduce yourself and ask if they’re open to roles or can refer you.

This tool automates the entire process:

- Reads recruiter names and companies from a file
- Writes a polite, professional email for each person
- Attaches your resume
- Sends the emails through your Gmail account (safely using an app password)

---

## 📋 What You Need

1. A Gmail account with **2-Step Verification (2FA)** turned on
2. A **Gmail App Password** (used securely instead of your actual password)
3. A resume file (PDF)
4. A list of recruiters (in `.csv` format)

---

## 🛠 Setup Guide (Step-by-Step)

### 🐍 Step 1: Set Up Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 🔐 Step 2: Create and Fill `.env` File

```bash
cp .env.example .env
```

Then, open `.env` and fill in your personal details:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SUBJECT=Open to Opportunities – Let's Connect
CSV_PATH=recruiters.csv
RESUME_PATH=Your_Resume.pdf

YOUR_NAME=Your Full Name
POSITION=Data Analyst / Software Developer
LOCATION=Your City, Country
PHONE_NUMBER=+XX-XXXXXXXXXX
SKILLS_SUMMARY=skilled in Python, SQL, machine learning and problem-solving
LINKEDIN_URL=https://linkedin.com/in/yourusername
PORTFOLIO_URL=Your_Portfolio_Link  # Leave blank if not available
```

✅ Everything you edit here will automatically reflect in the emails – no code editing needed!

---

### 📄 Step 3: Add Recruiters in `recruiters.csv`

Prepare your CSV file like this:

```csv
Name,Email,Company
Jane Doe,jane.doe@example.com,Microsoft
John Smith,john.smith@example.com,Google
```

---

### 📤 Step 4: Run the Script

Now just run:

```bash
python main.py
```

Each recruiter will receive:

- A **personalized message** with their name + company
- Your **resume attached**
- A **clean, respectful tone** that's optimized for cold outreach

---

## ✉️ Sample Email Sent

```
Hi Jane,

I hope you're doing well. My name is Nitin, and I'm actively seeking Data Analyst / Software Developer opportunities. With hands-on experience in building real-world solutions using Python, SQL, and machine learning, I’ve built and contributed to projects that deliver real impact.

I’ve attached my resume for your reference, and you can view my portfolio here:
👉 http://yourportfolio.com

I'd really appreciate it if you could consider me for any relevant openings at Microsoft, or keep me in mind for future roles. Thank you for your time and support!

Warm regards,
Nitin
📧 your_email@gmail.com
🔗 https://linkedin.com/in/Nitin3290
```

---

## 💡 Tips for Effective Cold Emailing

- ✔ Always **double-check email addresses**
- ✔ Send in small batches (10–20) to avoid spam flagging
- ✔ Be **respectful and concise**
- ✔ Keep your subject line polite but noticeable
- ✔ Don’t ask for a job — ask to be considered or remembered

---

## 🛠 Customize the Email Content

Edit the `generate_email.py` file to:

- Change tone (more formal or more casual)
- Add/remove signature lines
- Add extra fields (like GitHub or phone)

---

## ⚙️ Advanced Users

- Want to use Outlook/Zoho instead of Gmail? Modify `send_email.py`
- Want rich HTML emails? Use `MIMEText(body, 'html')` instead of `'plain'`

---

## 📄 License & Credits

This tool is free and open-source.  
Created with ❤️ by [Nitin](https://github.com/Nitin3290)

> Please use responsibly — cold emailing is a privilege, not a spam tool.
