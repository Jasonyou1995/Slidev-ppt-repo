---
theme: apple-basic
class: text-center
title: Reading HTML Tables with Pandas
info: |
  Learn how to extract data from web pages using pd.read_html()
  - Simple, one-line solution for web data extraction
transition: slide-left
mdc: true
lineNumbers: false
highlighter: shiki
---

# Reading HTML Tables
## Extract Web Data in One Line

<div class="pt-12">
  <span class="text-6xl opacity-30">🌐</span>
</div>

<div class="pt-4 text-xl opacity-75">
  Turn web tables into pandas DataFrames instantly
</div>

---

# The Problem

<div class="grid grid-cols-2 gap-12 mt-12">

<div>

## Before ❌

- Copy data manually
- Paste into Excel
- Clean formatting
- Takes forever!

</div>

<div>

## After ✅

- One line of code
- Automatic extraction
- Ready to analyze
- Done in seconds!

</div>

</div>

---

# The Solution: `pd.read_html()`

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

```python
import pandas as pd

# Extract all tables from a webpage
tables = pd.read_html('https://example.com/data.html')

# Get the first table
df = tables[0]
```

</div>

<div class="mt-8 text-lg opacity-75">
That's it! Your data is now in a DataFrame.
</div>

---

# How It Works

<v-clicks>

1. **Fetches** the webpage
2. **Finds** all HTML tables
3. **Converts** each table to DataFrame
4. **Returns** a list of DataFrames

</v-clicks>

<div v-click class="mt-8 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
<strong>Note:</strong> Always returns a list, even if there's only one table!
</div>

---

# Real Example: FDIC Failed Banks

<div class="text-left" style="max-width: 800px; margin: 0 auto;">

```python
import pandas as pd

# Get failed bank data from FDIC
df = pd.read_html(
    'http://www.fdic.gov/bank/individual/failed/banklist.html'
)[0]

# View the data
print(df.head())
```

</div>

<div class="mt-6 text-sm opacity-60">
Result: A clean DataFrame with bank names, dates, and locations
</div>

---

# Installation

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```bash
pip install "pandas[html]"
pip install requests
```

</div>

<div class="mt-8 text-lg">
Installs pandas, HTML parsers, and requests (for sites that block direct access)
</div>

---

# Exercise 1: Wikipedia COVID-19 Data

<div class="text-left" style="max-width: 800px; margin: 0 auto;">

```python
import pandas as pd
import requests

# Solution: Add headers to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# Get page with headers (fixes 403 error)
url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic'
response = requests.get(url, headers=headers)
response.raise_for_status()

# Read tables from HTML text
tables = pd.read_html(response.text)

print(f"Found {len(tables)} tables")
print(tables[0].head())
```

</div>

<div class="mt-6 text-sm opacity-60">
Note: Wikipedia may block requests without proper headers. Use requests library to add headers.
</div>

---

# Exercise 2: NASA Near Earth Objects (When things not working: check direct download)

<div class="text-left" style="max-width: 800px; margin: 0 auto;">

```python
import pandas as pd

# Get asteroid data from NASA
url = 'https://cneos.jpl.nasa.gov/ca/'
neo_df = pd.read_html(url)[0]

# View approaching asteroids
print(neo_df.head())
```

</div>

<div class="mt-6 text-sm opacity-60">
Perfect for practicing with date/time and scientific data
</div>

---

# Exercise 3: IMF Economic Data

<div class="text-left" style="max-width: 800px; margin: 0 auto;">

```python
import pandas as pd

# Access IMF World Economic Outlook
url = 'https://www.imf.org/en/Publications/WEO/weo-database'
tables = pd.read_html(url)

# Find GDP growth table
for table in tables:
    if 'GDP' in str(table.columns):
        gdp_df = table
        break

print(gdp_df.head())
```

</div>

---

# Useful Tips

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

- **Always check** how many tables were found
- **Use `match`** to find specific tables: `pd.read_html(url, match="GDP")`
- **Clean data** after extraction (remove commas, convert types)
- **Save results** to avoid re-scraping: `df.to_csv('data.csv')`

</v-clicks>

</div>

---

# Common Issues

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## Problem
403 Forbidden Error

## Solution
- Use `requests` with headers
- Mimic browser user-agent
- Pass HTML text to `pd.read_html()`

</div>

<div>

## Problem
No tables found

## Solution
- Check if page loads correctly
- Try different parser
- Verify URL

</div>

</div>

<div class="mt-6 text-sm opacity-60">
Many sites block direct access. Always use headers when needed!
</div>

---

# Summary

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

✅ **One line** extracts web tables

✅ **Automatic** conversion to DataFrame

✅ **Works with** any HTML table

✅ **Perfect for** quick data gathering

</v-clicks>

</div>

<div v-click class="mt-8 text-xl font-semibold">
Simple, powerful, and ready to use!
</div>

---

layout: center
class: text-center
---

# Thank You!

<div class="pt-12">
  <span class="text-6xl opacity-30">📊</span>
</div>

<div class="pt-8 text-xl opacity-75">
Questions?
</div>
