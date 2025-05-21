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
2. A **Gmail App Password** (used securely NOT YOUR ACTUAL PASSWORD)
   • After turning on 2FA, go to: https://myaccount.google.com/apppasswords
   • Select “Mail” as the app and “Other” (or “Custom”) as the device
   • Generate the password and copy it safely – you’ll use this instead of your actual Gmail password
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

### 🔐 Step 2: Open and Fill `.env` File

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

### 🚀 Step 4: Run the Script

```bash
python main.py
```

You’ll see a cool welcome screen with your name, and each recruiter will receive:

- A **personalized message** with their name + company
- Your **resume attached**
- A **clean, respectful tone** optimized for cold outreach

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

- ✅ Double-check email addresses
- ✅ Send in small batches (10–20 per run)
- ✅ Be respectful and concise
- ✅ Don’t demand — just express interest
- ✅ Avoid spammy phrases or ALL CAPS subjects

---

## 🛠 Customizing the Email

Edit `generate_email.py` if you:

- Want to change tone (formal, casual)
- Add/remove signature lines
- Include more fields (GitHub, phone, etc.)

---

## ⚙️ For Advanced Users

- Want to use Outlook/Zoho instead of Gmail? → Tweak `send_email.py`
- Prefer fancy HTML emails? → Replace `MIMEText(body, 'plain')` with `'html'`

---

## 👨‍💻 Fun Touch (Startup Style Banner)

When you run the script, it prints your name (from `.env`) in a big banner using `pyfiglet` for fun 😎

---

## 📄 License & Credits

This tool is **free and open-source**.  
Built with ❤️ by [Nitin](https://github.com/Nitin3290)

> Use responsibly – cold emailing is a privilege, not a spam weapon.
