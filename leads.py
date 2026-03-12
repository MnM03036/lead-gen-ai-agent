# leads.py
# This simulates what Apollo.io's API actually returns
# Real Apollo response is the same structure, just from an HTTP call

def get_mock_leads():
    return [
        {
            "id": "001",
            "name": "Sarah Chen",
            "title": "CEO",
            "company": "Stacklane",
            "industry": "B2B SaaS",
            "employees": 23,
            "location": "San Francisco, CA",
            "email": "sarah@stacklane.io",
            "linkedin": "linkedin.com/in/sarahchen",
            "company_description": "Project management software for remote engineering teams"
        },
        {
            "id": "002", 
            "name": "Marcus Webb",
            "title": "Founder",
            "company": "Revflow",
            "industry": "B2B SaaS",
            "employees": 41,
            "location": "Austin, TX",
            "email": "marcus@revflow.com",
            "linkedin": "linkedin.com/in/marcuswebb",
            "company_description": "Revenue operations automation for mid-market sales teams"
        }
    ]