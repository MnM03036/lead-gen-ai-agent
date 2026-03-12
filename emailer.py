# emailer.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def write_cold_email(lead: dict, sender_name: str, sender_company: str, value_prop: str) -> str:
    """
    Takes a lead dict, returns a personalized cold email string.
    """
    
    # This is your prompt engineering in action
    # Notice: system prompt sets behavior, user prompt delivers the specific task
    
    system_prompt = """You are an expert B2B cold email writer. 
You write short, personalized, non-salesy cold emails that get replies.
Rules:
- Maximum 4 sentences in the body
- Never use: "I hope this email finds you well", "synergy", "revolutionize"  
- Always reference something SPECIFIC about their company
- End with a low-friction CTA (not "hop on a call")
- Output ONLY the email, no subject line, no commentary"""

    user_prompt = f"""Write a cold email from {sender_name} at {sender_company}.

Lead info:
- Name: {lead['name']}
- Title: {lead['title']}
- Company: {lead['company']}
- What they do: {lead['company_description']}
- Location: {lead['location']}
- Team size: {lead['employees']} employees

Our value proposition: {value_prop}

Write the email body only."""

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_prompt
    )
    
    response = model.generate_content(user_prompt)
    
    return response.text


# Test it immediately
if __name__ == "__main__":
    from leads import get_mock_leads
    
    leads = get_mock_leads()
    first_lead = leads[0]
    
    email = write_cold_email(
        lead=first_lead,
        sender_name="Alex Rivera",
        sender_company="SalesBot AI",
        value_prop="We help B2B SaaS companies automate lead research so SDRs spend time selling, not googling"
    )
    
    print(f"=== Email for {first_lead['name']} at {first_lead['company']} ===")
    print(email)
    print()