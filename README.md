# 📧 Auto Email Generator

A Python-based automation tool that generates and sends personalized emails using templates and user data. This project is designed to save time, reduce manual effort, and ensure consistent communication—ideal for outreach, marketing, or notification systems.

---

## 👨‍💻 About the Developer

**Name**: Goutham Krishna C M  
**GitHub**: [gouthamkriz](https://github.com/gouthamkriz)  
**Role**: Aspiring AI Engineer focused on building real-world automation and AI-powered tools.

---

## 🎯 Project Goal

To automate the creation and delivery of customized emails using Python, enabling efficient and scalable communication for individuals or businesses.

---

## 🚀 Features

- Generate personalized emails using templates and dynamic data
- Send emails via SMTP (e.g., Gmail)
- Supports bulk emailing from CSV files
- Easy to configure and extend

---

## 🛠️ Tech Stack

- Python 3.x
- `smtplib` and `email` libraries
- `pandas` for reading user data
- CSV or Excel for input data

---

## 📦 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/gouthamkriz/auto-email-generator.git
cd auto-email-generator
```

### Step 2: Install Dependencies

```bash
pip install pandas
```


### Step 3: Prepare Your Files

- email_template.txt – Write your email with placeholders like {name}, {company}, etc.
- contacts.csv – A CSV file with columns like name, email, company, etc.
Example contacts.csv:
name,email,company
Alice,alice@example.com,TechCorp
Bob,bob@example.com,DataWorks


Example email_template.txt:
Subject: Hello {name} from {company}

Hi {name},

We’re excited to connect with you at {company}. Let us know how we can help!

Best regards,  
Goutham


