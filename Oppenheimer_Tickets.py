#!/usr/bin/env python
# coding: utf-8

# In[5]:


import smtplib
from email import encoders
from email.utils import COMMASPACE
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
import requests
import filecmp
import smtplib
import os
import datetime
import time

# Variable for date and time
x = 0


def check_website_for_updates(url):
    '''
    
    This is the function that checks if the website has been updated
    '''
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant element that indicates an update
        # You need to inspect the website's HTML to identify the element uniquely.
        # Replace 'class_name' with the actual class name or use other methods to find the relevant element.
        update_element = soup.find('div', class_='Showtime')
        
        if update_element and "IMAX 70MM" in soup.get_text():
            print("The website has been updated!")
            sendEmail(url)
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


# In[4]:


def sendEmail(x):
    '''
    
    The emailer. You'll need to add email address and app-specific password.
    '''
    # Login credentials
    email = # Enter email
    password = # Enter password
                
    # Sonstruct email message
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = "AMC Updated"


    body = ''





    # First body
    link_text = x
    link_url = x
    body += f'<a href="{link_url}">{link_text}</a>'       



    msg.attach(MIMEText(body, 'html'))

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(email, password)
            smtp.send_message(msg)
            print('Sent email.')
    # If there is an error while sending the email
    except Exception as e:
        print('Could not send email')
        print('Error: ' + str(e))
        print('')


        print('Done.')
        


# In[7]:


# URL of the website to monitor for updates (just change the date)
website_url = "https://www.amctheatres.com/movies/oppenheimer-66956/showtimes/oppenheimer-66956/2023-08-18/universal-cinema-amc-at-citywalk-hollywood/all"

# Interval in seconds between checks (e.g., 1 hour = 3600 seconds)
check_interval = 60

# Print starting time
current_datetime = datetime.datetime.now()
print(f"Starting Date and Time: {current_datetime}")

while True:
    if check_website_for_updates(website_url):
        print('Done.')
        break
    else:
        continue


    x += 1
    if x == 60:
        x = 0
        current_datetime = datetime.datetime.now()
        print(f"Current Date and Time: {current_datetime} - still running")
    time.sleep(check_interval)

