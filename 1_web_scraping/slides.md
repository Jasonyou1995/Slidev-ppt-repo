---
theme: seriph
title: Web Scraping for Finance: Your Secret Weapon 🚀
info: |
  ## From Zero to Data Hero – A Fun & Easy Guide
class: text-center
transition: slide-left
mdc: true
---

# Web Scraping for Finance: Your Secret Weapon 🚀

From Zero to Data Hero – A Fun & Easy Guide

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" flex="~ justify-center items-center gap-2" hover="bg-white bg-opacity-10">
    Press Space for next page <div class="i-carbon:arrow-right inline-block"/>
  </span>
</div>

---

# So, What Is Web Scraping?

<div class="grid grid-cols-2 gap-8">
<div>

## The Problem 😩

- Manual data collection
- Hours of copy-paste
- Human errors
- Tedious repetition

</div>
<div>

## The Solution 🚀

- Automated data extraction
- Seconds instead of hours
- Zero typos
- Your personal data intern

</div>
</div>

<div v-click class="mt-8 p-4 bg-blue-100 rounded-lg">
<strong>Web scraping</strong> is teaching a computer to browse websites and extract specific information automatically.
</div>

---

# Why Finance Students Should Care

<div class="grid grid-cols-2 gap-6">
<div>

## Traditional Data Sources

- Financial reports
- News articles
- Market data feeds
- **Limited & Expensive**

</div>
<div>

## Alternative Data Sources

- Social media sentiment
- Job postings
- Shipping rates
- **Free & Competitive Edge**

</div>
</div>

<div v-click class="mt-6 p-4 bg-green-100 rounded-lg">
<strong>Alternative data</strong> gives you insights not found in traditional financial reports!
</div>

---

# Real-World Finance Use Cases

<div class="grid grid-cols-2 gap-4 text-sm">
<div>

### 📈 Market Sentiment

- Scrape Twitter/Reddit
- Gauge public feeling
- Predict price movements

### 🏢 Competitor Analysis

- Track pricing changes
- Monitor job postings
- Understand strategy

</div>
<div>

### 🏡 Real Estate

- Property listings
- Rental yields
- Market trends

### 📄 Regulatory Filings

- SEC EDGAR data
- Insider trading
- Institutional ownership

</div>
</div>

---

# A Website's Blueprint

<div class="grid grid-cols-3 gap-4">
<div class="text-center">
<div class="text-4xl mb-2">🧱</div>
<h3>HTML</h3>
<p class="text-sm">Structure & Content</p>
<p class="text-xs">What you scrape</p>
</div>
<div class="text-center">
<div class="text-4xl mb-2">🎨</div>
<h3>CSS</h3>
<p class="text-sm">Styling & Layout</p>
<p class="text-xs">Helps identify elements</p>
</div>
<div class="text-center">
<div class="text-4xl mb-2">💡</div>
<h3>JavaScript</h3>
<p class="text-sm">Interactivity</p>
<p class="text-xs">Can be tricky to scrape</p>
</div>
</div>

<div v-click class="mt-6 p-4 bg-yellow-100 rounded-lg">
<strong>Think of a website as a house:</strong> HTML is the structure, CSS is the decoration, and JavaScript is the electricity!
</div>

---

# Your First "Hack": Developer Tools

<div class="grid grid-cols-2 gap-6">
<div>

## How to Inspect Element:

1. Right-click on any element
2. Select "Inspect"
3. See the HTML structure
4. Find the treasure map! 🗺️

</div>
<div>

```html
<div class="stock-price">
  <span class="price">$150.25</span>
  <span class="change">+2.5%</span>
</div>
```

</div>
</div>

<div v-click class="mt-4 p-3 bg-blue-100 rounded">
<strong>Pro Tip:</strong> Use the element selector tool to hover over elements and see their HTML structure!
</div>

---

# The Scraping Game Plan

<div class="grid grid-cols-3 gap-4">
<div class="text-center p-4 bg-blue-100 rounded">
<div class="text-3xl mb-2">📡</div>
<h3>1. Request</h3>
<p class="text-sm">Send request to server</p>
<p class="text-xs">Get HTML back</p>
</div>
<div class="text-center p-4 bg-green-100 rounded">
<div class="text-3xl mb-2">🔍</div>
<h3>2. Parse</h3>
<p class="text-sm">Clean up HTML</p>
<p class="text-xs">Make it searchable</p>
</div>
<div class="text-center p-4 bg-purple-100 rounded">
<div class="text-3xl mb-2">📊</div>
<h3>3. Extract</h3>
<p class="text-sm">Find your data</p>
<p class="text-xs">Save it</p>
</div>
</div>

<div v-click class="mt-6 p-4 bg-gray-100 rounded-lg">
<strong>Remember:</strong> Request → Parse → Extract. It's that simple!
</div>

---

# Your Scraping Toolkit 🧰

<div class="grid grid-cols-3 gap-4">
<div class="text-center p-4 bg-blue-100 rounded">
<div class="text-3xl mb-2">👨‍⚕️</div>
<h3>Beautiful Soup</h3>
<p class="text-sm">HTML Parser</p>
<p class="text-xs">Perfect for beginners</p>
</div>
<div class="text-center p-4 bg-green-100 rounded">
<div class="text-3xl mb-2">🤖</div>
<h3>Selenium</h3>
<p class="text-sm">Browser Automation</p>
<p class="text-xs">Handles JavaScript</p>
</div>
<div class="text-center p-4 bg-purple-100 rounded">
<div class="text-3xl mb-2">🏭</div>
<h3>Scrapy</h3>
<p class="text-sm">Full Framework</p>
<p class="text-xs">For large projects</p>
</div>
</div>

<div v-click class="mt-6 p-4 bg-yellow-100 rounded-lg">
<strong>Start with Beautiful Soup</strong> - it's the easiest to learn and perfect for most finance data!
</div>

---

# Let's Code! Your First Scrape

<div class="grid grid-cols-2 gap-6">
<div>

## Step 1: Setup

```bash
pip install requests beautifulsoup4
```

## Step 2: The Code

```python
import requests
from bs4 import BeautifulSoup

# Get the webpage
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first quote
quote = soup.find('div', class_='quote')
text = quote.find('span', class_='text').text
author = quote.find('small', class_='author').text

print(f"Quote: {text}")
print(f"Author: {author}")
```

</div>
<div>

## What This Does:

1. **Requests** the webpage
2. **Parses** the HTML
3. **Finds** the quote element
4. **Extracts** the text and author
5. **Prints** the results

<div v-click class="mt-4 p-3 bg-green-100 rounded">
<strong>Success!</strong> You've just scraped your first data!
</div>

</div>
</div>

---

# When Websites Fight Back: Selenium

<div class="grid grid-cols-2 gap-6">
<div>

## The Problem

- Some sites need login
- Content loads with JavaScript
- Beautiful Soup can't click buttons
- **Need a real browser!**

</div>
<div>

## The Solution

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open a browser
driver = webdriver.Chrome()

# Go to login page
driver.get("https://example.com/login")

# Fill in credentials
driver.find_element(By.ID, 'username').send_keys("user")
driver.find_element(By.ID, 'password').send_keys("pass")

# Click login
driver.find_element(By.TAG_NAME, 'button').click()

# Now scrape the page!
driver.quit()
```

</div>
</div>

<div v-click class="mt-4 p-3 bg-blue-100 rounded">
<strong>Selenium</strong> is like having a robot that can use a real browser for you!
</div>

---

# Scraping Like a Pro: Best Practices

<div class="grid grid-cols-2 gap-4 text-sm">
<div>

### 🚦 Read the Rules

- Check `robots.txt`
- Respect rate limits
- Follow terms of service

### 🐌 Be Gentle

- Add delays between requests
- Don't overload servers
- Use `time.sleep(2)`

</div>
<div>

### 🆔 Identify Yourself

- Set custom User-Agent
- Include contact info
- Be transparent

### 🔒 Respect Privacy

- No personal data
- No paywall content
- Use APIs when available

</div>
</div>

<div v-click class="mt-6 p-4 bg-red-100 rounded-lg">
<strong>Remember:</strong> With great power comes great responsibility. Be a good internet citizen!
</div>

---

# Your Hero's Journey Begins!

<div class="grid grid-cols-3 gap-4">
<div class="text-center p-4 bg-green-100 rounded">
<div class="text-3xl mb-2">🌱</div>
<h3>Start Small</h3>
<p class="text-sm">Simple static sites</p>
<p class="text-xs">Blogs, quotes</p>
</div>
<div class="text-center p-4 bg-blue-100 rounded">
<div class="text-3xl mb-2">📈</div>
<h3>Level Up</h3>
<p class="text-sm">Wikipedia tables</p>
<p class="text-xs">More complex data</p>
</div>
<div class="text-center p-4 bg-purple-100 rounded">
<div class="text-3xl mb-2">🏆</div>
<h3>Boss Battle</h3>
<p class="text-sm">Financial sites</p>
<p class="text-xs">Stock prices, news</p>
</div>
</div>

<div v-click class="mt-8 p-6 bg-gradient-to-r from-blue-100 to-purple-100 rounded-lg text-center">
<h2 class="text-2xl font-bold mb-2">The world of data is now at your fingertips!</h2>
<p class="text-lg">Go build something amazing! Good luck! 🎉</p>
</div>

---

# Thank You!

<div class="text-center">
<h2 class="text-3xl font-bold mb-4">Questions?</h2>
<p class="text-lg mb-6">Let's discuss your scraping ideas!</p>
<div class="grid grid-cols-2 gap-4 text-sm">
<div>
<h3 class="font-bold">Resources</h3>
<ul class="text-left">
<li>Beautiful Soup docs</li>
<li>Selenium docs</li>
<li>Python requests</li>
</ul>
</div>
<div>
<h3 class="font-bold">Practice Sites</h3>
<ul class="text-left">
<li>quotes.toscrape.com</li>
<li>books.toscrape.com</li>
<li>httpbin.org</li>
</ul>
</div>
</div>
</div>

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" flex="~ justify-center items-center gap-2" hover="bg-white bg-opacity-10">
    Press Space for next page <div class="i-carbon:arrow-right inline-block"/>
  </span>
</div>
