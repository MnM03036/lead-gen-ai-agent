# agent.py
import csv
import os
from datetime import datetime
from leads import get_mock_leads
from emailer import write_cold_email

def run_agent(icp: dict, sender: dict):
    """
    icp = who you're targeting
    sender = who the email is from
    """
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Agent starting...")
    print(f"Target ICP: {icp['description']}\n")
    
    # STEP 1: Get leads
    print(">> Fetching leads...")
    leads = get_mock_leads()
    print(f"   Found {len(leads)} leads\n")
    
    results = []
    
    # STEP 2: Process each lead
    for i, lead in enumerate(leads):
        print(f">> Processing lead {i+1}/{len(leads)}: {lead['name']} at {lead['company']}")
        
        # Filter by ICP — basic check
        if lead['employees'] < icp['min_employees'] or lead['employees'] > icp['max_employees']:
            print(f"   SKIP — {lead['employees']} employees outside range\n")
            continue
            
        # Write personalized email
        print(f"   Writing email...")
        email_body = write_cold_email(
            lead=lead,
            sender_name=sender['name'],
            sender_company=sender['company'],
            value_prop=sender['value_prop']
        )
        
        # Build result record
        result = {
            "name": lead['name'],
            "email": lead['email'],
            "title": lead['title'],
            "company": lead['company'],
            "employees": lead['employees'],
            "location": lead['location'],
            "personalized_email": email_body,
            "status": "ready_to_send"
        }
        
        results.append(result)
        print(f"   Done.\n")
    
    # STEP 3: Save to CSV
    output_file = save_to_csv(results)
    
    print(f"[DONE] Processed {len(results)} leads")
    print(f"Output saved to: {output_file}")
    
    return results


def save_to_csv(results: list) -> str:
    """Save results to CSV — drag this into Google Sheets instantly."""
    
    if not results:
        print("No results to save.")
        return None
    
    filename = f"leads_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    fieldnames = results[0].keys()  # column headers from dict keys
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    return filename


# Entry point
if __name__ == "__main__":
    
    icp = {
        "description": "B2B SaaS founders in the US, 5-50 employees",
        "min_employees": 5,
        "max_employees": 50,
        "industry": "B2B SaaS"
    }
    
    sender = {
        "name": "Alex Rivera",
        "company": "SalesBot AI",
        "value_prop": "We help B2B SaaS founders close enterprise deals faster with AI-powered deal coaching"
    }
    
    results = run_agent(icp=icp, sender=sender)
    
    # Print preview
    print("\n=== EMAIL PREVIEW ===")
    for r in results:
        print(f"\nTO: {r['name']} <{r['email']}>")
        print(f"COMPANY: {r['company']}")
        print(f"EMAIL:\n{r['personalized_email']}")
        print("-" * 50)