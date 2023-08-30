import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText


def send_email(subject, message):
    sender_email = "your_email@gmail.com"  # Replace with your sender email
    receiver_email = "receiver_email@gmail.com"  # Replace with the recipient's email
    smtp_server = "smtp.gmail.com"  # Use your email provider's SMTP server
    smtp_port = 587  # SMTP port (587 for Gmail)
    smtp_username = "your_username"  # Your email username
    smtp_password = "your_password"  # Your email password

    # Create the email content
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Connect and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def check_product_stock(product_url):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    }

    response = requests.get(product_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        availability_element = soup.select_one(".availability")

        if availability_element:
            if "out of stock" in availability_element.get_text().lower():
                return False
            else:
                return True
        else:
            return None
    else:
        print("Failed to fetch the product page.")
        return None


def main():
    product_url = "https://shop.howlonggone.com/products/gonetourage-hat-navy-blue"

    stock_status = check_product_stock(product_url)

    if stock_status is None:
        print("Failed to determine stock status.")
    elif stock_status:
        message = "Product is in stock!"
        print(message)
        send_email("Product In Stock", message)
    else:
        message = "Product is out of stock."
        print(message)
        send_email("Product Out of Stock", message)


if __name__ == "__main__":
    main()
