# Amazon-price-notifier
This code notity abou the amazon prices
This Python script performs the following tasks:

Imports:

requests for making HTTP requests.
BeautifulSoup from bs4 for parsing HTML.
lxml for parsing XML and HTML.
smtplib for sending emails.
URL and Headers:

Defines the URL of the Amazon product page.
Sets headers to simulate a request from a web browser to prevent blocking by the website.
HTTP Request:

Sends an HTTP GET request to the Amazon product page, including the defined headers.
Retrieves the HTML content of the page.
Parsing HTML:

Uses BeautifulSoup to parse the HTML content.
Finds the price of the product using its HTML tag and class.
Price Processing:

Extracts the price value from the parsed HTML text.
Converts the price to a floating-point number for comparison.
Email Function:

Defines a function send_mail() to send an email notification if the price of the product drops below a certain threshold.
Email Notification:

Checks if the price of the product is less than $30.
If the condition is met, calls the send_mail() function to send an email notification.
Describe Functionality:

The script fetches the price of a specific SSD product from Amazon.
If the price drops below $30, it sends an email notification to a specified recipient (in this case, kanthiwijesinghe71@gmail.com) with a predefined message indicating the price drop and a link to the product page.
Overall, the script is a basic example of web scraping and email notification functionality. It demonstrates how to extract information from a web page and automate actions based on specific conditions, such as price thresholds.






