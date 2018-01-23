#!/bin/python3
"""Grabs snapshot of website with given url and then emails that image to a recipient."""
# Change your gmail App security - To allow this script to login to a gmail account for testing.
# https://myaccount.google.com/u/1/lesssecureapps?rfn=27&rfnc=1&eid=-411141621748264578&et=0&asae=2&pli=1
import subprocess
import base64
import smtplib

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

url = "https://p.datadoghq.com/sb/rklUvX-b63b9afb58" # Add your own Screenboard Public Url
# Define these once; use them twice!
strFrom = "" # Authorized email account
strTo = "" # Destened email
uPaswd = "" # Authorized email account password
SUBJECT = "Test"
consumer_url = "https://mail.google.com/mail/b/{}/smtp/".format(strFrom)
attachment = "images/20180122-dashboard-full.png"

def screenshot():
    subprocess.call(["webkit2png", "-F", "-d", "-D", "images/", "-o", "dashboard", "--delay", "10", url])


def email_img():
    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'test message'
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:%s"><br>' % (attachment), 'html')
    msgAlternative.attach(msgText)

    # This example assumes the image is in the current directory
    fp = open(attachment, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<{}>'.format(attachment))
    msgRoot.attach(msgImage)

    # Send the email (this example assumes SMTP authentication is required)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.set_debuglevel(True)
    server.ehlo()
    server.starttls()
    server.login(strFrom, uPaswd)
    server.sendmail(strFrom, strTo, msgRoot.as_string())
    server.quit()

screenshot()
email_img()
