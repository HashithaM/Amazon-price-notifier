# Amazon-price-notifier
This code notity abou the amazon prices
This Python script utilizes Selenium WebDriver to automate interactions with web pages. Let's break down its functionality:

Importing Libraries:

The script imports necessary modules from Selenium (webdriver, ElementClickInterceptedException, NoSuchElementException, chrome.service, By, Keys) and the time module.
Setting up WebDriver:

It configures the Chrome WebDriver with the path to the Chrome driver executable and sets up options for Chrome.
Interacting with Web Elements:

There are several examples commented out in the code that demonstrate interactions with various web elements:
Finding and clicking buttons and links.
Entering text into input fields.
Performing actions like pressing Enter key.
Automating Cookie Clicker Game:

The script navigates to a Cookie Clicker game page.
It continuously clicks on a cookie element.
After a certain time (timeout), it checks for available upgrades in the store and purchases the most expensive one that can be afforded.
This cycle continues for a duration of five minutes (five_min).
At the end, it prints the cookies per second rate.
Quitting WebDriver:

After completing the task, the WebDriver session is terminated.
Describing the Code:

The script demonstrates various interactions with web elements using Selenium WebDriver.
It also showcases the automation of a simple game (Cookie Clicker) by continuously clicking on a cookie, purchasing upgrades, and monitoring the cookies per second rate.
Some comments and questions within the code indicate the author's thought process or points of confusion.
Overall, this script provides a practical example of how Selenium WebDriver can be used for web automation tasks, from basic interactions with elements to more complex tasks like game automation.












