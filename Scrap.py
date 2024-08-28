import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract company details from LinkedIn company page
def get_company_details(company_linkedin):
    response = requests.get(company_linkedin)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Attempt to find the company industry
    industry_section = soup.find('div', class_='org-top-card",",","-summary-info-list__info-item')
    if industry_section:
        industry = industry_section.get_text(strip=True)
    else:
        industry = 'Not found'

    # You can similarly add more details to extract (e.g., company size, headquarters, etc.)
    return {
        'Industry': industry,
        # Add other fields as needed
    }

# Function to extract job details and company LinkedIn page
def get_job_details(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract job title
    job_title = soup.find('h1', class_='topcard__title').get_text(strip=True) if soup.find('h1', class_='topcard__title') else 'Not found'
    
    # Extract job description
    description = soup.find('div', class_='description__text').get_text(strip=True) if soup.find('div', class_='description__text') else 'Not found'
    
    # Extract company LinkedIn page link
    company_linkedin = 'Not found'
    company_section = soup.find('a', class_='topcard__org-name-link')
    if company_section and 'href' in company_section.attrs:
        company_linkedin = company_section['href']
    
    # Extract company details
    company_details = {}
    if company_linkedin != 'Not found':
        company_details = get_company_details(company_linkedin)
    
    return job_title, description, company_linkedin, company_details

# Example list of job links
job_links = [
"https://sg.linkedin.com/jobs/view/operations-director-singapore-at-mise-en-place-talent-3953541438?position=9&pageNum=55&refId=FB2n%2BESbPmvRQNPv4Q9R7A%3D%3D&trackingId=pWvAI4qPBTgE8kboOOI36Q%3D%3D&trk=public_jobs_jserp-result_search-card",
"https://sg.linkedin.com/jobs/view/business-development-commercial-lead-at-equinor-a-s-3997358980?position=10&pageNum=70&refId=Y5Md98ALLvowok9%2Bd4OwAw%3D%3D&trackingId=pU5SHk25ckLwARSnpQlmzQ%3D%3D&trk=public_jobs_jserp-result_search-card",
]

# Data collection
job_data = []
for link in job_links:
    job_title, description, company_linkedin, company_details = get_job_details(link)
    job_data.append({
        'Link': link,
        'Job Title': job_title,
        'Description': description,
        'Company LinkedIn': company_linkedin,
        'Industry': company_details.get('Industry', 'Not found'),
        # Add other fields as needed
    })

# Save to CSV
df = pd.DataFrame(job_data)
df.to_csv('job_descriptions.csv', index=False)
