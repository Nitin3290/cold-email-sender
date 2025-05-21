import os
from dotenv import load_dotenv

load_dotenv()

your_name = os.getenv("YOUR_NAME")
position = os.getenv("POSITION")
skills_summary = os.getenv("SKILLS_SUMMARY")
portfolio_url = os.getenv("PORTFOLIO_URL")
linkedin_url = os.getenv("LINKEDIN_URL")
your_email = os.getenv("EMAIL_ADDRESS")

def generate_email(name, company):
    portfolio_line = (
        f"\nI’ve attached my resume for your reference, and you can view my portfolio here:\n👉 {portfolio_url}\n"
        if portfolio_url else "\nI’ve attached my resume for your reference.\n"
    )
    
    return f"""Hi {name},

I hope you're doing well. My name is {your_name}, and I'm actively seeking {position} opportunities. With hands-on experience in {skills_summary}, I’ve built and contributed to projects that deliver real impact.{portfolio_line}
I'd really appreciate it if you could consider me for any relevant openings at {company}, or keep me in mind for future roles. Thank you for your time and support!

Warm regards,  
{your_name}  
📧 {your_email}  
🔗 {linkedin_url}
"""