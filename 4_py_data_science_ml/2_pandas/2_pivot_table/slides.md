---
theme: default
class: text-center
title: Pandas Pivot Tables
info: |
  Mastering pd.pivot_table - transforming messy data into clear summaries.
  Essential for financial analysis and reporting.
  
transition: slide-left
mdc: true
lineNumbers: false
highlighter: monaco
---

# Pandas Pivot Tables
## Transforming Data into Insights

### From Messy Lists to Clear Summaries

<v-click>

**Why pivot tables?**

</v-click>

<v-click>

Turn **long, detailed data** into **simple, easy-to-read summary tables**  
that reveal patterns and insights instantly.

</v-click>

---
layout: default
---

# What You'll Learn Today

<v-clicks>

1. **The Concept**: What pivot tables do (with a simple analogy)
2. **Basic Syntax**: How to create your first pivot table
3. **Key Parameters**: Understanding values, index, columns, aggfunc
4. **Aggregation Functions**: Mean, sum, count, min, max
5. **Advanced Features**: Multiple values, margins, multi-index
6. **Common Errors**: What to watch out for
7. **Practice**: Hands-on exercises

</v-clicks>

---
layout: default
---

# Part 1: The Analogy
## The School Grade Summary

<v-click>

**Imagine you're a teacher** with a messy list of every grade every student got on every test.

</v-click>

---
layout: default
---

# The Problem: Messy Data

## Long List of Individual Grades

<v-clicks>

| Student | Subject | Test Type | Grade |
|---------|---------|-----------|-------|
| Alice   | Math    | Quiz      | 85    |
| Bob     | Math    | Quiz      | 78    |
| Alice   | Math    | Final Exam| 92    |
| Bob     | Science | Quiz      | 88    |
| Charlie | Science | Final Exam| 95    |
| Alice   | Science | Quiz      | 91    |
| Charlie | Math    | Quiz      | 90    |

**Problem**: Hard to see overall performance at a glance!

</v-clicks>

---
layout: default
---

# The Solution: Summary Table

## What You Want to See

<v-clicks>

**Create a grid:**

- **Rows**: Each student (Alice, Bob, Charlie...)
- **Columns**: Each subject (Math, Science...)
- **Values**: Average grade for that student in that subject

</v-clicks>

---
layout: default
---

# The Result: Pivot Table

## Clean Summary View

<v-clicks>

| Student | **Math** | **Science** |
|---------|----------|------------|
| **Alice** | 88.5     | 91.0       |
| **Bob**   | 78.0     | 88.0       |
| **Charlie**| 90.0    | 95.0       |

**Congratulations!** You just created a pivot table in your head!

</v-clicks>

---
layout: default
---

# What Just Happened?

<v-clicks>

You took a **long list** of detailed data  
and **"pivoted"** it into a **summary table**.

**Key insight**: Group by categories (Student, Subject)  
and summarize the numbers (average Grade).

</v-clicks>

---
layout: default
---

# Part 2: Translating to Python
## From Analogy to Code

<v-click>

Now let's do the same thing with `pd.pivot_table`!

</v-click>

---
layout: default
---

# Step 1: The Raw Data

## Create the DataFrame

```python {all|1-8|all}
import pandas as pd

data = {
    'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Alice', 'Charlie'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'Math'],
    'Test Type': ['Quiz', 'Quiz', 'Final Exam', 'Quiz', 'Final Exam', 'Quiz', 'Quiz'],
    'Grade': [85, 78, 92, 88, 95, 91, 90]
}

df = pd.DataFrame(data)
```

<v-click>

**This is our messy list** - just like the teacher's grade book!

</v-click>

---
layout: default
---

# Step 2: Create the Pivot Table

## The Magic Line

```python {all|1-7|all}
summary_table = pd.pivot_table(
    data=df,           # Our messy list of data
    values='Grade',    # The numbers to summarize
    index='Student',   # Rows (down the side)
    columns='Subject', # Columns (across the top)
    aggfunc='mean'     # How to summarize: average
)

print(summary_table)
```

<v-click>

**That's it!** One function call transforms messy data into a summary.

</v-click>

---
layout: default
---

# The Output

## Clean Summary Table

<v-clicks>

```
Subject   Math  Science
Student                
Alice     88.5     91.0
Bob       78.0     88.0
Charlie   90.0     95.0
```

**Same result as the teacher's summary table!**

</v-clicks>

---
layout: default
---

# Part 3: Understanding Parameters
## The Key Ingredients

<v-click>

Think of these as **knobs and dials** you can adjust.

</v-click>

---
layout: default
---

# Parameter 1: `data`

## Your Raw DataFrame

<v-clicks>

```python
data=df  # Your messy, detailed data
```

**What it is**: The DataFrame containing all your raw data.

**Think of it as**: The teacher's complete grade book.

</v-clicks>

---
layout: default
---

# Parameter 2: `values`

## What Numbers to Summarize

<v-clicks>

```python
values='Grade'  # The column with numbers to aggregate
```

**What it is**: The column containing the numeric values you want to summarize.

**Examples**: 
- `'Grade'` - student grades
- `'Sales'` - sales amounts
- `'Price'` - stock prices
- `'Revenue'` - financial revenue

</v-clicks>

---
layout: default
---

# Parameter 3: `index`

## Rows (Down the Side)

<v-clicks>

```python
index='Student'  # What goes in rows
```

**What it is**: The column to group by and display as rows.

**Think of it as**: The "y-axis" of your table.

**Examples**: 
- `'Student'` - each student gets a row
- `'Date'` - each date gets a row
- `'Region'` - each region gets a row

</v-clicks>

---
layout: default
---

# Parameter 4: `columns`

## Columns (Across the Top)

<v-clicks>

```python
columns='Subject'  # What goes in columns
```

**What it is**: The column to group by and display as columns.

**Think of it as**: The "x-axis" of your table.

**Examples**: 
- `'Subject'` - each subject gets a column
- `'Month'` - each month gets a column
- `'Product'` - each product gets a column

</v-clicks>

---
layout: default
---

# Parameter 5: `aggfunc`

## How to Summarize (The Most Powerful!)

<v-clicks>

```python
aggfunc='mean'  # Aggregation function
```

**What it is**: How to combine multiple values into one summary.

**Default**: `'mean'` (average)

**This is where the magic happens!**

</v-clicks>

---
layout: default
---

# Part 4: Aggregation Functions
## Different Ways to Summarize

<v-click>

Let's explore the most common aggregation functions.

</v-click>

---
layout: default
---

# Aggregation Function: `'mean'`

## Calculate the Average

<v-clicks>

```python {all|1-6|all}
avg_grades = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns='Subject',
    aggfunc='mean'
)
```

**What it does**: Calculates the **average** of all grades for each student-subject combination.

**Use case**: Find average performance, average prices, average sales

</v-clicks>

---
layout: default
---

# Aggregation Function: `'sum'`

## Add Everything Up

<v-clicks>

```python {all|1-6|all}
total_sales = pd.pivot_table(
    data=sales_df,
    values='Amount',
    index='Salesperson',
    columns='Month',
    aggfunc='sum'
)
```

**What it does**: **Adds up** all values in each group.

**Use case**: Total sales, total revenue, total volume

</v-clicks>

---
layout: default
---

# Aggregation Function: `'count'`

## Count How Many

<v-clicks>

```python {all|1-6|all}
test_count = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns='Subject',
    aggfunc='count'
)
```

**What it does**: **Counts** how many entries exist in each group.

**Use case**: Number of transactions, number of tests taken, frequency

</v-clicks>

---
layout: default
---

# Aggregation Function: `'min'` and `'max'`

## Find Extremes

<v-clicks>

```python {all|1-6|all}
# Minimum values
lowest = pd.pivot_table(df, values='Grade', 
                       index='Student', columns='Subject',
                       aggfunc='min')

# Maximum values
highest = pd.pivot_table(df, values='Grade',
                        index='Student', columns='Subject',
                        aggfunc='max')
```

**What it does**: Finds the **smallest** or **largest** value in each group.

**Use case**: Lowest price, highest volume, best/worst performance

</v-clicks>

---
layout: default
---

# Quick Reference: Aggregation Functions

<v-clicks>

| Function | What It Does | Example Use |
|----------|--------------|-------------|
| **`'mean'`** | Average | Average grade, average price |
| **`'sum'`** | Total | Total sales, total revenue |
| **`'count'`** | Count | Number of transactions |
| **`'min'`** | Minimum | Lowest price, worst score |
| **`'max'`** | Maximum | Highest price, best score |
| **`'std'`** | Standard deviation | Variability, risk |

</v-clicks>

---
layout: default
---

# Example: Count Tests Taken

## How Many Tests Per Student-Subject?

<v-clicks>

```python {all|1-6|all}
test_count_table = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns='Subject',
    aggfunc='count'
)
```

**Output:**
```
Subject  Math  Science
Student               
Alice       2        1
Bob         1        1
Charlie     1        1
```

**Insight**: Alice took 2 Math tests, others took 1 each.

</v-clicks>

---
layout: default
---

# Part 5: Financial Example
## Sales by Region and Month

<v-click>

Let's apply this to financial data!

</v-click>

---
layout: default
---

# Financial Data Example

## Monthly Sales by Region

<v-clicks>

**Raw Data:**
| Salesperson | Region | Month | Sales |
|-------------|--------|-------|-------|
| Alice       | North  | Jan   | 5000  |
| Bob         | South  | Jan   | 3000  |
| Alice       | North  | Feb   | 6000  |
| Bob         | South  | Feb   | 4000  |

**Goal**: See total sales by region and month

</v-clicks>

---
layout: default
---

# Financial Pivot Table

## Total Sales Summary

```python {all|1-6|all}
sales_summary = pd.pivot_table(
    data=sales_df,
    values='Sales',
    index='Region',
    columns='Month',
    aggfunc='sum'
)
```

<v-click>

**Result**: Clean table showing sales totals by region and month!

</v-click>

---
layout: default
---

# Part 6: Advanced Features
## Multiple Values and Margins

---
layout: default
---

# Multiple Values

## Summarize Multiple Columns

<v-clicks>

```python {all|1-7|all}
multi_summary = pd.pivot_table(
    data=df,
    values=['Grade', 'Hours_Studied'],  # Multiple columns!
    index='Student',
    columns='Subject',
    aggfunc='mean'
)
```

**What it does**: Creates separate tables for each value column.

**Use case**: Compare multiple metrics side-by-side

</v-clicks>

---
layout: default
---

# Adding Margins

## Include Totals

<v-clicks>

```python {all|1-7|all}
with_totals = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns='Subject',
    aggfunc='mean',
    margins=True  # Add row and column totals!
)
```

**What it does**: Adds a "Total" row and column with overall summaries.

**Use case**: See individual values AND grand totals

</v-clicks>

---
layout: default
---

# Multiple Index Levels

## Group by Multiple Rows

<v-clicks>

```python {all|1-7|all}
multi_index = pd.pivot_table(
    data=df,
    values='Grade',
    index=['Student', 'Test Type'],  # Multiple row groups!
    columns='Subject',
    aggfunc='mean'
)
```

**What it does**: Creates hierarchical rows (Student → Test Type).

**Use case**: More detailed breakdowns

</v-clicks>

---
layout: default
---

# Multiple Column Levels

## Group by Multiple Columns

<v-clicks>

```python {all|1-7|all}
multi_cols = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns=['Subject', 'Test Type'],  # Multiple column groups!
    aggfunc='mean'
)
```

**What it does**: Creates hierarchical columns (Subject → Test Type).

**Use case**: More detailed column breakdowns

</v-clicks>

---
layout: default
---

# Part 7: Common Errors
## What to Watch Out For

---
layout: default
---

# Error 1: Wrong Column Name

## KeyError When Column Doesn't Exist

<v-clicks>

**Problem**: Typo in column name

```python
result = pd.pivot_table(df, values='Grad',  # Typo!
                       index='Student', columns='Subject')
# KeyError: 'Grad'
```

**Solution**: Verify column names first

```python
print(df.columns.tolist())  # Check available columns
```

</v-clicks>

---
layout: default
---

# Error 2: Non-Numeric Values

## Can't Calculate Mean of Text

<v-clicks>

**Problem**: Trying to aggregate non-numeric column

```python
result = pd.pivot_table(df, values='Student',  # Text column!
                       index='Subject', aggfunc='mean')
# TypeError: can't compute mean
```

**Solution**: Use numeric column for `values`

```python
result = pd.pivot_table(df, values='Grade',  # Numeric!
                       index='Subject', aggfunc='mean')
```

</v-clicks>

---
layout: default
---

# Error 3: Missing Values (NaN)

## Empty Cells in Result

<v-clicks>

**Problem**: No data for some combinations

```python
result = pd.pivot_table(df, values='Grade',
                       index='Student', columns='Subject')
# Some cells show NaN
```

**Solution**: Handle missing values

```python
result = pd.pivot_table(df, values='Grade',
                       index='Student', columns='Subject',
                       fill_value=0)  # Replace NaN with 0
```

</v-clicks>

---
layout: default
---

# Error 4: Wrong Aggregation Function

## Function Doesn't Exist

<v-clicks>

**Problem**: Typo in aggregation function name

```python
result = pd.pivot_table(df, values='Grade',
                       index='Student', aggfunc='averge')  # Typo!
# ValueError: Unknown function
```

**Solution**: Use correct function names

```python
result = pd.pivot_table(df, values='Grade',
                       index='Student', aggfunc='mean')  # Correct!
```

</v-clicks>

---
layout: default
---

# Error 5: Forgetting aggfunc

## Default is 'mean' - Not Always What You Want!

<v-clicks>

**Problem**: Want sum but get mean (default)

```python
result = pd.pivot_table(df, values='Sales',
                       index='Region', columns='Month')
# Calculates mean, not sum!
```

**Solution**: Always specify `aggfunc` explicitly

```python
result = pd.pivot_table(df, values='Sales',
                       index='Region', columns='Month',
                       aggfunc='sum')  # Be explicit!
```

</v-clicks>

---
layout: default
---

# Error Prevention Checklist

<v-clicks>

✅ **Check column names**: Print `df.columns` first  
✅ **Use numeric columns**: For `values` parameter  
✅ **Specify aggfunc**: Don't rely on default  
✅ **Handle NaN**: Use `fill_value` if needed  
✅ **Verify data types**: Ensure columns match your expectations  

</v-clicks>

---
layout: default
---

# Part 8: Practice Exercises
## Hands-On Learning

---
layout: default
---

# Exercise 1: Basic Pivot Table

## Task: Average Grades by Student and Subject

<v-clicks>

**Given:**
- DataFrame `df` with columns: Student, Subject, Grade

**Goal**: Create a pivot table showing average grade for each student in each subject

**Hint**: Use `index='Student'`, `columns='Subject'`, `aggfunc='mean'`

</v-clicks>

---
layout: default
---

# Exercise 1: Solution

```python {all|1-6|all}
avg_table = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns='Subject',
    aggfunc='mean'
)

print(avg_table)
```

<v-click>

**Check**: Does your table show students as rows and subjects as columns?

</v-click>

---
layout: default
---

# Exercise 2: Count Transactions

## Task: Count Sales by Region

<v-clicks>

**Given:**
- DataFrame `sales_df` with columns: Region, Sales, Date

**Goal**: Count how many sales transactions occurred in each region

**Hint**: Use `aggfunc='count'` and `index='Region'`

</v-clicks>

---
layout: default
---

# Exercise 2: Solution

```python {all|1-5|all}
transaction_count = pd.pivot_table(
    data=sales_df,
    values='Sales',
    index='Region',
    aggfunc='count'
)

print(transaction_count)
```

<v-click>

**Check**: Does your result show the number of sales per region?

</v-click>

---
layout: default
---

# Exercise 3: Total Sales by Month

## Task: Sum Sales Across Months

<v-clicks>

**Given:**
- DataFrame `sales_df` with columns: Month, Sales, Product

**Goal**: Create pivot table showing total sales for each product in each month

**Hint**: Use `index='Product'`, `columns='Month'`, `aggfunc='sum'`

</v-clicks>

---
layout: default
---

# Exercise 3: Solution

```python {all|1-6|all}
total_sales = pd.pivot_table(
    data=sales_df,
    values='Sales',
    index='Product',
    columns='Month',
    aggfunc='sum'
)

print(total_sales)
```

<v-click>

**Check**: Are products in rows and months in columns with totals?

</v-click>

---
layout: default
---

# Exercise 4: Add Margins

## Task: Include Grand Totals

<v-clicks>

**Given:**
- Your pivot table from Exercise 3

**Goal**: Add row and column totals using margins

**Hint**: Add `margins=True` parameter

</v-clicks>

---
layout: default
---

# Exercise 4: Solution

```python {all|1-7|all}
total_sales = pd.pivot_table(
    data=sales_df,
    values='Sales',
    index='Product',
    columns='Month',
    aggfunc='sum',
    margins=True  # Add totals!
)

print(total_sales)
```

<v-click>

**Check**: Do you see a "Total" row and column?

</v-click>

---
layout: default
---

# Exercise 5: Multiple Aggregations

## Task: Both Average and Count

<v-clicks>

**Given:**
- DataFrame `df` with Student, Subject, Grade

**Goal**: Create pivot table showing both average grade AND count of tests

**Hint**: Use `aggfunc=['mean', 'count']` (list of functions)

</v-clicks>

---
layout: default
---

# Exercise 5: Solution

```python {all|1-7|all}
multi_agg = pd.pivot_table(
    data=df,
    values='Grade',
    index='Student',
    columns='Subject',
    aggfunc=['mean', 'count']  # Multiple functions!
)

print(multi_agg)
```

<v-click>

**Check**: Do you see separate tables for mean and count?

</v-click>

---
layout: default
---

# Key Takeaways

<v-clicks>

1. **Pivot tables** transform messy data into clear summaries
2. **Five key parameters**: data, values, index, columns, aggfunc
3. **aggfunc is powerful**: mean, sum, count, min, max, and more
4. **Always specify aggfunc**: Don't rely on default
5. **Use margins**: Add totals for complete picture

</v-clicks>

---
layout: default
---

# The Five Parameters Summary

<v-clicks>

| Parameter | Purpose | Example |
|-----------|---------|---------|
| **`data`** | Raw DataFrame | `df` |
| **`values`** | Numbers to summarize | `'Grade'`, `'Sales'` |
| **`index`** | Rows (y-axis) | `'Student'`, `'Region'` |
| **`columns`** | Columns (x-axis) | `'Subject'`, `'Month'` |
| **`aggfunc`** | How to summarize | `'mean'`, `'sum'`, `'count'` |

**Master these, and you can pivot any data!**

</v-clicks>

---
layout: default
---

# Real-World Finance Use Cases

<v-clicks>

- **Portfolio analysis**: Returns by asset and time period
- **Sales reporting**: Revenue by region and product
- **Risk analysis**: Volatility by sector and date
- **Performance tracking**: Metrics by department and quarter
- **Budget analysis**: Spending by category and month

</v-clicks>

---
layout: default
---

# In a Nutshell

<v-clicks>

> **`pd.pivot_table` turns your long, detailed list of data into a simple, easy-to-read summary table. You tell it what to look at (values), how to group things (rows and columns), and how to do the math (aggfunc).**

**Start simple**: Try summarizing small datasets first,  
just like the teacher did with grades!

</v-clicks>

---
layout: default
---

# Decision Tree

<v-clicks>

**Need to summarize data?**

→ **Group by categories?** → Use `pivot_table()`

→ **What to summarize?** → Set `values` parameter

→ **Rows?** → Set `index` parameter

→ **Columns?** → Set `columns` parameter

→ **How to summarize?** → Set `aggfunc` parameter

</v-clicks>

---
layout: default
---

# Practice Makes Perfect

<v-clicks>

**Next Steps:**
1. Try the exercises with your own data
2. Experiment with different aggregation functions
3. Practice with financial datasets
4. Build a sales or portfolio analysis report

**Remember**: Pivot tables are one of the most useful tools for data analysis!

</v-clicks>

---
layout: default
---

# Summary

## From Messy to Meaningful

<v-clicks>

**Before**: Long list of individual records  
**After**: Clean summary table revealing patterns

**Key Skill**: Knowing which aggregation function to use  
**Key Insight**: Group by what matters, summarize the numbers

**Master this, and you can analyze any dataset efficiently!**

</v-clicks>

---
layout: default
---

# Questions?

### Thank you for your attention!

**Resources:**
- Pandas documentation: https://pandas.pydata.org/docs/
- Practice datasets: Kaggle, your own financial data
- Next topic: GroupBy operations (related to pivot tables)

