---
theme: default
class: text-center
title: Pandas Data Combination
info: |
  Mastering pandas merging, joining, and concatenation - essential skills
  for combining financial datasets efficiently.
  
transition: slide-left
mdc: true
lineNumbers: false
highlighter: monaco
---

# Pandas Data Combination
## Merging, Joining & Concatenation

### Essential Skills for Financial Data Analysis

<div class="pt-12">
  <span class="text-6xl opacity-20">📊</span>
</div>

<!--
SPEAKER NOTES:
Welcome! Today we'll learn how to combine different datasets in pandas - a critical skill for financial analysis.
We'll cover three main methods: concatenation, merging, and joining. Each has its purpose, and we'll learn when to use which.
-->

---

# Why Combine Data?

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## The Problem 💼

- Data scattered across files
- Monthly reports in separate sheets
- Stock prices in one file, company info in another
- Need unified view for analysis

</div>

<div>

## The Solution ✨

- **Merge** stock prices with company info
- **Join** portfolio data with market data  
- **Concatenate** monthly reports into one

</div>

</div>

<div v-click class="mt-8 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
<strong>In finance, you rarely work with just one dataset!</strong>
</div>

<!--
SPEAKER NOTES:
Explain the real-world scenario: financial analysts constantly need to combine data from different sources.
Give examples: combining stock prices with company fundamentals, merging quarterly reports, joining portfolio holdings with current prices.
-->

---

# What You'll Learn Today

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

1. **Concatenation** 📚  
   Stacking data vertically or horizontally

2. **Merging** 🔗  
   Database-style joins on common columns

3. **Joining** ⚡  
   Index-based combination operations

4. **Common Errors** ⚠️  
   What to watch out for

5. **Practice** 💪  
   Hands-on exercises with financial data

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Set expectations: we'll cover three main methods, learn about common pitfalls, and practice with exercises.
Each method has specific use cases - we'll learn when to use which.
-->

---

# The Three Methods

<div class="grid grid-cols-3 gap-6 mt-8">

<div v-click class="p-4 bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/20 dark:to-blue-800/20 rounded-lg border border-blue-200 dark:border-blue-700">

## `concat()`

**Use Case:**  
Stacking similar data

**Key Feature:**  
Simple row/column stacking

</div>

<div v-click class="p-4 bg-gradient-to-br from-green-50 to-green-100 dark:from-green-900/20 dark:to-green-800/20 rounded-lg border border-green-200 dark:border-green-700">

## `merge()`

**Use Case:**  
Database-style joins

**Key Feature:**  
Join on common columns

</div>

<div v-click class="p-4 bg-gradient-to-br from-purple-50 to-purple-100 dark:from-purple-900/20 dark:to-purple-800/20 rounded-lg border border-purple-200 dark:border-purple-700">

## `join()`

**Use Case:**  
Index-based combination

**Key Feature:**  
Quick index alignment

</div>

</div>

<!--
SPEAKER NOTES:
Introduce the three methods with clear distinctions:
- concat: simplest, just stacking
- merge: most powerful, like SQL joins
- join: convenient when using index as key
-->

---

layout: section
class: text-center
---

# Part 1: Concatenation
## Stacking Data Together

<div class="text-6xl opacity-20 mt-8">📚</div>

<!--
SPEAKER NOTES:
We start with the simplest method - concatenation. Think of it as stacking Excel sheets.
-->

---

# Concatenation: The Concept

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## What It Does

**Concatenation** = **Stacking** data together

- **Vertical**: Add more rows (same columns)
- **Horizontal**: Add more columns (same rows)

</div>

<div class="flex items-center justify-center">

<div class="text-4xl opacity-30">⬇️</div>

<div class="text-4xl opacity-30 ml-4">➡️</div>

</div>

</div>

<div v-click class="mt-8 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg border border-yellow-200 dark:border-yellow-800">
<strong>Key Point:</strong> No matching required - just stack!
</div>

<!--
SPEAKER NOTES:
Explain the analogy: like stacking Excel sheets on top of each other (vertical) or side by side (horizontal).
No need to match anything - just combine.
-->

---

# Example: Monthly Stock Prices

## Two DataFrames with Same Structure

<div class="grid grid-cols-2 gap-6 mt-6">

<div v-click>

**January Data:**

| Date | Stock | Price |
|------|-------|-------|
| 2024-01-15 | AAPL | 150.00 |
| 2024-01-16 | AAPL | 151.50 |

</div>

<div v-click>

**February Data:**

| Date | Stock | Price |
|------|-------|-------|
| 2024-02-15 | AAPL | 152.00 |
| 2024-02-16 | AAPL | 153.25 |

</div>

</div>

<div v-click class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
<strong>Goal:</strong> Combine into one DataFrame with all dates
</div>

<!--
SPEAKER NOTES:
Show a concrete example: monthly stock price data that needs to be combined.
Both DataFrames have the same structure - perfect for concatenation.
-->

---

# Concatenation: Vertical Stacking

## Adding More Rows

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

**Step 1:** Create the DataFrames

```python {1-2|3-4|all}
jan = pd.DataFrame({'Date': ['2024-01-15', '2024-01-16'],
                    'Stock': ['AAPL', 'AAPL'],
                    'Price': [150.00, 151.50]})
feb = pd.DataFrame({'Date': ['2024-02-15', '2024-02-16'],
                    'Stock': ['AAPL', 'AAPL'],
                    'Price': [152.00, 153.25]})
```

**Step 2:** Stack them together

```python
result = pd.concat([jan, feb])
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Result:</strong> All rows from both DataFrames stacked together
</div>

<!--
SPEAKER NOTES:
Show the code step by step. First create the DataFrames, then concatenate.
The result will have all rows from both - 4 rows total.
-->

---

# Concatenation: Horizontal Stacking

## Adding More Columns

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

**Step 1:** Create DataFrames with different columns

```python {1-2|3-4|all}
prices = pd.DataFrame({'AAPL': [150, 151, 152],
                       'MSFT': [300, 301, 302]})
volumes = pd.DataFrame({'AAPL_Vol': [1000, 1100, 1200],
                        'MSFT_Vol': [2000, 2100, 2200]})
```

**Step 2:** Stack horizontally

```python
result = pd.concat([prices, volumes], axis=1)
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
<strong>Key:</strong> `axis=1` means "add columns" (horizontal)
</div>

<!--
SPEAKER NOTES:
Explain horizontal stacking: when you want to add columns instead of rows.
The axis=1 parameter is crucial - without it, it stacks vertically by default.
-->

---

# Concatenation Parameters

## Key Options

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

```python {1|2|3|4|all}
pd.concat([df1, df2], 
         axis=0,           # 0=rows (default), 1=columns
         ignore_index=True, # Reset index: 0,1,2,3...
         keys=['Jan', 'Feb']) # Label each source
```

</v-clicks>

</div>

<div class="grid grid-cols-2 gap-4 mt-6">

<div v-click class="p-3 bg-blue-50 dark:bg-blue-900/20 rounded">
<strong>ignore_index=True</strong><br>
Creates new index 0, 1, 2, 3...
</div>

<div v-click class="p-3 bg-green-50 dark:bg-green-900/20 rounded">
<strong>keys=['Jan', 'Feb']</strong><br>
Creates MultiIndex to track sources
</div>

</div>

<!--
SPEAKER NOTES:
Explain the key parameters:
- axis: direction of stacking
- ignore_index: clean up the index after concatenation
- keys: useful for tracking where data came from
-->

---

# Concatenation: With Keys

## Tracking Data Sources

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```python {1-2|3-4|all}
jan = pd.DataFrame({'Price': [150, 151]})
feb = pd.DataFrame({'Price': [152, 153]})

result = pd.concat([jan, feb], keys=['January', 'February'])
```

</div>

<div v-click class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
<strong>Result:</strong> MultiIndex showing which month each row came from
</div>

<!--
SPEAKER NOTES:
Show how keys create a MultiIndex - useful when you need to know the source of each row.
This is helpful for tracking data provenance.
-->

---

layout: section
class: text-center
---

# Part 2: Merging
## Database-Style Joins

<div class="text-6xl opacity-20 mt-8">🔗</div>

<!--
SPEAKER NOTES:
Now we move to merging - the most powerful method, similar to SQL joins.
-->

---

# Merging: The Concept

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## What It Does

**Merging** = **Joining** two tables on common columns

- Requires a **key column** to match rows
- Like Excel VLOOKUP, but more powerful
- Supports different join types

</div>

<div class="flex items-center justify-center text-4xl opacity-30">

🔑

</div>

</div>

<div v-click class="mt-8 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
<strong>Key Point:</strong> Rows are matched based on common values!
</div>

<!--
SPEAKER NOTES:
Explain merging as database-style joins. Unlike concatenation, merging requires matching on a key.
This is like SQL joins or Excel VLOOKUP.
-->

---

# Example: Stock Prices + Company Info

## Two Related DataFrames

<div class="grid grid-cols-2 gap-6 mt-6">

<div v-click>

**Stock Prices:**

| Ticker | Price | Volume |
|--------|-------|--------|
| AAPL | 150 | 1000 |
| MSFT | 300 | 2000 |

</div>

<div v-click>

**Company Info:**

| Ticker | Company | Sector |
|--------|---------|--------|
| AAPL | Apple Inc. | Technology |
| MSFT | Microsoft | Technology |

</div>

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Goal:</strong> Combine to get Price + Company name together
</div>

<!--
SPEAKER NOTES:
Show a practical example: stock prices in one DataFrame, company information in another.
We want to combine them using the Ticker column as the key.
-->

---

# Basic Merge: Inner Join

## Matching on Common Column

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

**Step 1:** Create the DataFrames

```python {1-3|4-7|all}
prices = pd.DataFrame({'Ticker': ['AAPL', 'MSFT'],
                       'Price': [150, 300],
                       'Volume': [1000, 2000]})
info = pd.DataFrame({'Ticker': ['AAPL', 'MSFT'],
                     'Company': ['Apple Inc.', 'Microsoft'],
                     'Sector': ['Technology', 'Technology']})
```

**Step 2:** Merge on Ticker

```python
result = pd.merge(prices, info, on='Ticker')
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
<strong>Result:</strong> Only rows where Ticker matches in both DataFrames
</div>

<!--
SPEAKER NOTES:
Show the merge operation step by step. The 'on' parameter specifies which column to match on.
Inner join (default) only keeps rows that exist in both DataFrames.
-->

---

# Merge: Join Types Explained

## Four Types of Joins

<div class="grid grid-cols-2 gap-4 mt-6">

<div v-click class="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-700">

### `inner`

**What It Keeps:**  
Only matching rows (default)

</div>

<div v-click class="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-700">

### `left`

**What It Keeps:**  
All rows from left DataFrame

</div>

<div v-click class="p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg border border-yellow-200 dark:border-yellow-700">

### `right`

**What It Keeps:**  
All rows from right DataFrame

</div>

<div v-click class="p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg border border-purple-200 dark:border-purple-700">

### `outer`

**What It Keeps:**  
All rows from both DataFrames

</div>

</div>

<!--
SPEAKER NOTES:
Explain the four join types with visual understanding:
- inner: intersection (most restrictive)
- left: keep everything from left, add matching from right
- right: keep everything from right, add matching from left
- outer: union (most inclusive)
-->

---

# Visual: Join Types

## Understanding the Difference

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Left DataFrame** (prices): AAPL, MSFT, GOOGL  
**Right DataFrame** (info): AAPL, MSFT, TSLA

- **Inner**: AAPL, MSFT (both have) ✅
- **Left**: AAPL, MSFT, GOOGL (all from left) ✅
- **Right**: AAPL, MSFT, TSLA (all from right) ✅
- **Outer**: AAPL, MSFT, GOOGL, TSLA (everything) ✅

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
<strong>Tip:</strong> Left join is most common - keep all your data, add info when available
</div>

<!--
SPEAKER NOTES:
Use a concrete example to show the difference between join types.
Most financial analysts use left joins to preserve all their data.
-->

---

# Merge: Left Join Example

## Keep All Prices, Add Info When Available

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

```python {1-3|4-6|7-8|all}
prices = pd.DataFrame({'Ticker': ['AAPL', 'MSFT', 'GOOGL'],
                       'Price': [150, 300, 2500]})
info = pd.DataFrame({'Ticker': ['AAPL', 'MSFT'],
                     'Sector': ['Tech', 'Tech']})

result = pd.merge(prices, info, on='Ticker', how='left')
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Result:</strong> All prices kept, GOOGL has NaN for Sector
</div>

<!--
SPEAKER NOTES:
Show left join in action - preserves all rows from the left DataFrame.
Missing values (NaN) appear when there's no match in the right DataFrame.
-->

---

# Merge: Multiple Keys

## Matching on Multiple Columns

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

```python {1-3|4-6|7-8|all}
df1 = pd.DataFrame({'Date': ['2024-01-01', '2024-01-01'],
                    'Ticker': ['AAPL', 'MSFT'],
                    'Price': [150, 300]})
df2 = pd.DataFrame({'Date': ['2024-01-01', '2024-01-01'],
                    'Ticker': ['AAPL', 'MSFT'],
                    'Volume': [1000, 2000]})

result = pd.merge(df1, df2, on=['Date', 'Ticker'])
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
<strong>Key Point:</strong> Both Date AND Ticker must match
</div>

<!--
SPEAKER NOTES:
Show merging on multiple keys - common in time series data.
Both conditions must be satisfied for a match.
-->

---

# Merge: Different Column Names

## Using `left_on` and `right_on`

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

```python {1-3|4-6|7-8|all}
prices = pd.DataFrame({'Stock': ['AAPL', 'MSFT'],
                       'Price': [150, 300]})
info = pd.DataFrame({'Ticker': ['AAPL', 'MSFT'],
                     'Sector': ['Tech', 'Tech']})

result = pd.merge(prices, info, 
                  left_on='Stock', right_on='Ticker')
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
<strong>Use Case:</strong> When column names differ but contain same data
</div>

<!--
SPEAKER NOTES:
Show how to merge when column names are different but contain the same information.
This is common when combining data from different sources with different naming conventions.
-->

---

# Merge: Handling Overlapping Columns

## Using Suffixes

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

```python {1-3|4-6|7-8|all}
df1 = pd.DataFrame({'Ticker': ['AAPL'], 'Value': [150]})
df2 = pd.DataFrame({'Ticker': ['AAPL'], 'Value': [300]})

result = pd.merge(df1, df2, on='Ticker', 
                  suffixes=('_Price', '_Volume'))
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
<strong>Result:</strong> Columns become `Value_Price` and `Value_Volume`
</div>

<!--
SPEAKER NOTES:
Explain how suffixes help when both DataFrames have columns with the same name.
This prevents column name conflicts and makes the result clear.
-->

---

layout: section
class: text-center
---

# Part 3: Joining
## Index-Based Combination

<div class="text-6xl opacity-20 mt-8">⚡</div>

<!--
SPEAKER NOTES:
Now we cover joining - a convenient shortcut when your key is already the index.
-->

---

# Joining: The Concept

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

## What It Does

**Joining** = **Merging** using index instead of columns

- Faster syntax for index-based operations
- Default is **left join** on index
- Similar to merge, but index-focused

</div>

<div class="flex items-center justify-center text-4xl opacity-30">

📇

</div>

</div>

<div v-click class="mt-8 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-800">
<strong>Key Point:</strong> Use when your key is already the index!
</div>

<!--
SPEAKER NOTES:
Explain joining as a convenience method when the key column is already set as the index.
It's essentially a shortcut for merge with left_index=True, right_index=True.
-->

---

# Join: Basic Example

## Index-Based Combination

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

```python {1-2|3-4|5-6|all}
prices = pd.DataFrame({'Price': [150, 300]},
                      index=['AAPL', 'MSFT'])
info = pd.DataFrame({'Sector': ['Tech', 'Tech']},
                    index=['AAPL', 'MSFT'])

result = prices.join(info)
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
<strong>Result:</strong> Automatically matches on index (Ticker)
</div>

<!--
SPEAKER NOTES:
Show the simplicity of join when using index - no need to specify the key column.
The index values are automatically used for matching.
-->

---

# Join: Different Join Types

## Same Options as Merge

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

```python {1-2|3-4|5-6|all}
prices = pd.DataFrame({'Price': [150, 300, 2500]},
                      index=['AAPL', 'MSFT', 'GOOGL'])
info = pd.DataFrame({'Sector': ['Tech', 'Tech']},
                    index=['AAPL', 'MSFT'])

result = prices.join(info, how='left')
```

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
<strong>Default:</strong> `how='left'` (keeps all from left DataFrame)
</div>

<!--
SPEAKER NOTES:
Show that join supports the same join types as merge.
The default is left join, which is usually what you want.
-->

---

# Join vs Merge: When to Use?

<div class="grid grid-cols-2 gap-6 mt-8">

<div v-click class="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-700">

## Use `join()` when:

- Key is already the index
- Quick index alignment
- Simple left join needed

</div>

<div v-click class="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-700">

## Use `merge()` when:

- Key is a regular column
- Need column-based matching
- Need specific join type

</div>

</div>

<div v-click class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
<strong>Rule of thumb:</strong> If key is index → use `join()`, else → use `merge()`
</div>

<!--
SPEAKER NOTES:
Provide clear guidance on when to use which method.
Most of the time, merge is more flexible, but join is convenient when using index.
-->

---

# Quick Comparison

## Same Result, Different Syntax

<div class="grid grid-cols-2 gap-6 mt-6">

<div v-click>

**Using join()** (index-based):

```python
result = prices.join(info)
```

</div>

<div v-click>

**Using merge()** (equivalent):

```python
result = pd.merge(prices, info, 
                  left_index=True, right_index=True)
```

</div>

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Both produce the same result!</strong>
</div>

<!--
SPEAKER NOTES:
Show that join and merge can produce the same results - it's just a matter of syntax preference.
Join is more concise when using index.
-->

---

layout: section
class: text-center
---

# Part 4: Common Errors
## What to Watch Out For

<div class="text-6xl opacity-20 mt-8">⚠️</div>

<!--
SPEAKER NOTES:
Now we'll cover common mistakes that beginners make - learning from errors is important!
-->

---

# Error 1: Duplicate Keys

## Unexpected Row Multiplication

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Problem:** Duplicate keys create Cartesian product

```python
left = pd.DataFrame({'key': ['A', 'A'], 'val': [1, 2]})
right = pd.DataFrame({'key': ['A', 'A'], 'val': [3, 4]})
result = pd.merge(left, right, on='key')
# Result: 4 rows instead of 2!
```

**Solution:** Check for duplicates first

```python
left['key'].duplicated().any()  # Check before merging
```

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Explain the duplicate key problem - this is a common gotcha.
When keys are duplicated, pandas creates all possible combinations, which can explode your data size.
Always check for duplicates before merging.
-->

---

# Error 2: Missing Key Column

## KeyError When Column Doesn't Exist

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Problem:** Column name typo or doesn't exist

```python
result = pd.merge(df1, df2, on='Tiker')  # Typo!
# KeyError: 'Tiker'
```

**Solution:** Verify column names

```python
print(df1.columns.tolist())  # Check available columns
print(df2.columns.tolist())
```

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Show how typos in column names cause errors.
Always verify column names before merging - print them out to be sure.
-->

---

# Error 3: Data Type Mismatch

## String vs Numeric Keys Don't Match

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Problem:** Same values, different types

```python
df1 = pd.DataFrame({'key': [1, 2, 3]})      # Integer
df2 = pd.DataFrame({'key': ['1', '2', '3']}) # String
result = pd.merge(df1, df2, on='key')
# Result: No matches! (1 != '1')
```

**Solution:** Convert to same type

```python
df2['key'] = df2['key'].astype(int)
```

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Explain type mismatch - a subtle but common error.
Pandas is strict about data types - '1' (string) is not the same as 1 (integer).
Always check and convert types before merging.
-->

---

# Error 4: Index Not Reset

## Unexpected Index After Concat

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Problem:** Old index preserved, creates duplicates

```python
result = pd.concat([df1, df2])
# Index: [0,1,2,0,1,2] - duplicates!
```

**Solution:** Use `ignore_index=True`

```python
result = pd.concat([df1, df2], ignore_index=True)
# Index: [0,1,2,3,4,5] - clean!
```

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Show the index duplication problem after concatenation.
This is why ignore_index=True is often needed - it creates a clean sequential index.
-->

---

# Error 5: Wrong Axis

## Concatenating Rows Instead of Columns

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Problem:** Forgot `axis=1` for horizontal stacking

```python
result = pd.concat([prices, volumes])  # Wrong!
# Stacks vertically instead of horizontally
```

**Solution:** Specify `axis=1`

```python
result = pd.concat([prices, volumes], axis=1)
```

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Show the axis confusion - a common mistake.
Remember: axis=0 is vertical (default), axis=1 is horizontal.
-->

---

# Error Prevention Checklist

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

✅ **Before merging:** Check for duplicate keys  
✅ **Verify columns:** Print column names to confirm  
✅ **Check data types:** Ensure keys have same type  
✅ **Use `ignore_index`:** When concatenating vertically  
✅ **Specify `axis`:** When concatenating horizontally  

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Summarize the error prevention checklist.
Following these steps will prevent most common errors.
-->

---

layout: section
class: text-center
---

# Part 5: Practice Exercises
## Hands-On Learning

<div class="text-6xl opacity-20 mt-8">💪</div>

<!--
SPEAKER NOTES:
Now let's practice! Exercises help solidify understanding.
-->

---

# Exercise 1: Concatenate Monthly Data

## Task: Combine Three Monthly Reports

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Given:**
- `jan_data`: January stock prices
- `feb_data`: February stock prices  
- `mar_data`: March stock prices

**Goal:** Create one DataFrame with all three months

**Hint:** Use `pd.concat()` with `ignore_index=True`

</v-clicks>

</div>

<!--
SPEAKER NOTES:
First exercise - simple concatenation of monthly data.
This reinforces the basic concatenation concept.
-->

---

# Exercise 1: Solution

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```python {1-2|3-4|all}
# Combine all months
all_months = pd.concat([jan_data, feb_data, mar_data], 
                       ignore_index=True)

print(all_months.head())
```

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Check:</strong> Does your result have all rows from all three DataFrames?
</div>

<!--
SPEAKER NOTES:
Show the solution step by step.
The ignore_index parameter ensures a clean index.
-->

---

# Exercise 2: Merge Portfolio with Prices

## Task: Add Current Prices to Portfolio

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Given:**
- `portfolio`: Your holdings (Ticker, Shares)
- `prices`: Current prices (Ticker, Price)

**Goal:** Calculate portfolio value (Shares × Price)

**Hint:** Merge first, then multiply columns

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Second exercise - practical portfolio calculation.
This shows a real-world use case for merging.
-->

---

# Exercise 2: Solution

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```python {1-2|3-4|all}
# Merge portfolio with prices
combined = pd.merge(portfolio, prices, on='Ticker')

# Calculate value
combined['Value'] = combined['Shares'] * combined['Price']
```

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Check:</strong> Does each row show Ticker, Shares, Price, and Value?
</div>

<!--
SPEAKER NOTES:
Show the solution - merge first, then calculate.
This demonstrates a common workflow in financial analysis.
-->

---

# Exercise 3: Left Join Missing Data

## Task: Find Stocks Without Sector Info

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Given:**
- `stocks`: All stocks you track (Ticker, Price)
- `sectors`: Sector info for some stocks (Ticker, Sector)

**Goal:** Identify which stocks are missing sector data

**Hint:** Use left join, then filter for NaN values

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Third exercise - using left join to find missing data.
This is a common data quality check.
-->

---

# Exercise 3: Solution

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```python {1-2|3-4|all}
# Left join to keep all stocks
result = pd.merge(stocks, sectors, on='Ticker', how='left')

# Find missing sectors
missing = result[result['Sector'].isna()]
```

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Check:</strong> Does `missing` contain stocks without sector info?
</div>

<!--
SPEAKER NOTES:
Show the solution - left join preserves all stocks, then filter for NaN.
This is useful for data quality checks.
-->

---

# Exercise 4: Multiple Key Merge

## Task: Match Date + Ticker

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Given:**
- `daily_prices`: Date, Ticker, Price
- `daily_volumes`: Date, Ticker, Volume

**Goal:** Combine prices and volumes for same Date+Ticker

**Hint:** Use `on=['Date', 'Ticker']`

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Fourth exercise - merging on multiple keys.
This is common in time series financial data.
-->

---

# Exercise 4: Solution

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```python {1-2|all}
# Merge on multiple keys
combined = pd.merge(daily_prices, daily_volumes, 
                   on=['Date', 'Ticker'])
```

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Check:</strong> Are Date and Ticker both used for matching?
</div>

<!--
SPEAKER NOTES:
Show the solution - simple but important for time series data.
Both keys must match for a row to be included.
-->

---

# Exercise 5: Handle Overlapping Columns

## Task: Merge with Same Column Names

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Given:**
- `df1`: Ticker, Value (prices)
- `df2`: Ticker, Value (volumes)

**Goal:** Merge and distinguish the two Value columns

**Hint:** Use `suffixes` parameter

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Fifth exercise - handling column name conflicts.
This shows the importance of suffixes.
-->

---

# Exercise 5: Solution

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

```python {1-2|all}
# Merge with suffixes
result = pd.merge(df1, df2, on='Ticker',
                  suffixes=('_Price', '_Volume'))
```

</div>

<div v-click class="mt-6 p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
<strong>Check:</strong> Do you see `Value_Price` and `Value_Volume` columns?
</div>

<!--
SPEAKER NOTES:
Show the solution - suffixes prevent column name conflicts.
This makes the result clear and unambiguous.
-->

---

# Key Takeaways

<div class="text-left" style="max-width: 600px; margin: 0 auto;">

<v-clicks>

1. **`concat()`**: Stack data vertically or horizontally
2. **`merge()`**: Join on common columns (most flexible)
3. **`join()`**: Quick index-based combination
4. **Always check**: Duplicates, column names, data types
5. **Choose wisely**: Right tool for the right job

</v-clicks>

</div>

<!--
SPEAKER NOTES:
Summarize the key points from the entire presentation.
Each method has its place - understanding when to use which is key.
-->

---

# Decision Tree

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Need to combine data?**

→ **Same structure, just stack?** → Use `concat()`

→ **Match on columns?** → Use `merge()`

→ **Match on index?** → Use `join()`

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
<strong>Remember:</strong> Start simple with concat, use merge for most cases, join when convenient
</div>

<!--
SPEAKER NOTES:
Provide a decision tree to help students choose the right method.
This is a practical guide they can refer back to.
-->

---

# Real-World Finance Use Cases

<div class="grid grid-cols-2 gap-6 mt-6">

<div v-click class="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">

### Portfolio Analysis
Merge holdings with prices

### Time Series
Concatenate monthly/quarterly data

</div>

<div v-click class="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">

### Company Research
Join stock data with fundamentals

### Risk Analysis
Combine positions with market data

</div>

</div>

<div v-click class="mt-6 p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
<strong>These operations are the foundation of financial data analysis!</strong>
</div>

<!--
SPEAKER NOTES:
Connect the concepts to real-world financial applications.
This helps students see the practical value of what they've learned.
-->

---

# Practice Makes Perfect

<div class="text-left" style="max-width: 700px; margin: 0 auto;">

<v-clicks>

**Next Steps:**
1. Try the exercises with your own data
2. Experiment with different join types
3. Practice error handling
4. Build a portfolio analysis project

</v-clicks>

</div>

<div v-click class="mt-6 p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
<strong>Remember:</strong> These operations are the foundation of data analysis!
</div>

<!--
SPEAKER NOTES:
Encourage practice and experimentation.
The best way to learn is by doing.
-->

---

# Summary

## Three Powerful Tools

<div class="grid grid-cols-3 gap-4 mt-8">

<div class="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-700">

### `concat()`

**Best For:**  
Stacking similar data

**Key Parameter:**  
`axis=0` (rows) or `axis=1` (cols)

</div>

<div class="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-700">

### `merge()`

**Best For:**  
Database-style joins

**Key Parameters:**  
`on='column'`, `how='left/right/inner/outer'`

</div>

<div class="p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg border border-purple-200 dark:border-purple-700">

### `join()`

**Best For:**  
Index-based combination

**Key Parameter:**  
`how='left/right/inner/outer'`

</div>

</div>

<div class="mt-8 p-4 bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 rounded-lg">
<strong>Master these, and you can combine any financial datasets!</strong>
</div>

<!--
SPEAKER NOTES:
Final summary slide - reinforce the three main methods.
End on a positive, empowering note.
-->

---

layout: center
class: text-center
---

# Questions?

<div class="text-4xl opacity-50 mt-12">💬</div>

### Thank you for your attention!

<div class="text-left mt-8" style="max-width: 600px; margin: 0 auto;">

**Resources:**
- Pandas documentation: https://pandas.pydata.org/docs/
- Practice datasets: Kaggle, Yahoo Finance
- Next topic: Grouping and aggregations

</div>

<!--
SPEAKER NOTES:
Closing slide - invite questions and provide resources.
Thank the audience for their attention.
-->
