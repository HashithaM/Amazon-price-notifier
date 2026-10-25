# Browser Automation Experiments

A collection of Selenium exercises for navigating pages, locating elements, submitting forms, and automating browser interactions. Despite the repository name, the active script currently runs a Cookie Clicker bot; Amazon price scraping and several other exercises remain as commented examples.

## What it demonstrates

- Launching Chrome with Selenium
- Selecting elements with CSS selectors, XPath, names, and link text
- Filling and submitting forms
- Reading page content and attributes
- Running a timed Cookie Clicker strategy that buys the most expensive affordable upgrade

## Requirements

- Python 3
- Google Chrome and a compatible ChromeDriver
- `selenium`

```bash
pip install selenium
python main.py
```

Update the ChromeDriver path in `main.py` for your system before running.

## Notes

This is a learning project rather than a production price-monitoring service. The commented examples include personal-looking sample data; replace those values with obvious placeholders before sharing or reusing the code.
