---
theme: seriph
layout: cover
fonts:
  monospace: 'Monaco'
highlighter: shiki
author: Shengwei You
lineNumbers: true
transition: slide-left
info: |
  ## Introduction to the Command Prompt (Windows)
  Learn to navigate and command your system like a developer.
---

# 💻 Introduction to the Command Prompt

## HKBU FIN7830 2025

### For Windows Users (Developer Style)

Shengwei You

---

## 🧭 Part 1: Preliminaries
### What is the Command Prompt?

- The **Command Prompt** (or terminal) is a **text-based interface** for communicating with your computer.  
- It allows developers to:
  - Navigate the file system  
  - Run scripts or programs  
  - Manage files quickly and efficiently  

> Developers love it because it’s faster and more powerful than using menus or buttons.

---

### ⚙️ Opening PowerShell

To open a PowerShell prompt:

1. Press **Windows + S** to open **Search**  
2. Type **PowerShell**  
3. Press **Enter**

Alternatively, right-click the **Start Menu** → select **Windows PowerShell**

> PowerShell is a modern replacement for the old `cmd.exe`.

---

### 📂 Files and Directory Structure

- Windows organizes data into **directories** (folders).  
- The top-level drive is `C:\`  
- Your personal files live in:  
  `C:\Users\your-username`

The **home directory** can be represented as `~` (similar to Linux).

```powershell {monaco}
pwd
```

Prints the current directory path.

---

## ⚙️ Part 2: Common Commands in PowerShell

### 📄 Listing Files in a Directory

```powershell {monaco}
ls
```

Lists all files in the current folder.

For detailed information (including hidden files):

```powershell {monaco}
ls -Force
```

---

### 🚶 Moving Between Directories

```powershell {monaco}
cd directory-name
```

Change to another folder.

```powershell {monaco}
cd ..
```

Move up one level.

```powershell {monaco}
cd ~
```

Return to your home directory.

---

### 🏠 Your Home and Projects Directory

It's common for developers to keep work in:

```powershell {monaco}
cd ~/projects
```

If it doesn't exist, create it:

```powershell {monaco}
mkdir projects
```

Organizing code in projects keeps things neat.

---

### 📦 Moving and Copying Files

Move a file:

```powershell {monaco}
mv file.txt ~/projects
```

Copy a file:

```powershell {monaco}
cp file.txt ~/projects
```

Rename a file:

```powershell {monaco}
mv oldname.txt newname.txt
```

---

### 🗑️ Deleting Files and Directories

Delete a file:

```powershell {monaco}
rm file.txt
```

Delete an empty folder:

```powershell {monaco}
rmdir folder
```

Delete a folder and all its contents:

```powershell {monaco}
rm -r folder
```

Always double-check paths before removing recursively!

---

## 👁️ Part 3: Hidden Files

### What Are Hidden Files?

- Files starting with `.` are hidden.
- Common examples: `.gitignore`, `.env`

List them:

```powershell {monaco}
ls -Force
```

---

### 📝 Creating and Editing a .env File

Create a hidden file:

```powershell {monaco}
ni .env
```

Edit with Notepad:

```powershell {monaco}
notepad .env
```

View contents:

```powershell {monaco}
cat .env
```

`.env` files often store secret keys and environment settings.

---

## 🪟 Part 4: PowerShell vs. Anaconda Prompt

### Understanding the Difference

- **PowerShell:**  
  The general-purpose Windows shell: versatile for all system operations.
- **Anaconda Prompt:**  
  A specialized environment provided by Anaconda for managing Python environments and packages.

Essentially, Anaconda Prompt = PowerShell + Python setup preloaded.

You can use either, but Anaconda makes working with Python smoother.

---

## 🧩 Part 5: Exercises

Practice Commands to Build Confidence

1. Print your current directory:

<v-click>

```powershell {monaco}
pwd
```

</v-click>

---

2. List files (including hidden):

<v-click>

```powershell {monaco}
ls -Force
```

</v-click>

---

3. Navigate to your home folder:

<v-click>

```powershell {monaco}
cd ~
```

</v-click>

---

4. Create a folder named projects:

<v-click>

```powershell {monaco}
mkdir projects
```

</v-click>

---

5. Enter it and create a file:

<v-click>

```powershell {monaco}
cd projects
ni notes.txt
```

</v-click>

---

6. Edit and save the file:

<v-click>

```powershell {monaco}
notepad notes.txt
```

</v-click>

---

7. Copy and move files:

<v-click>

```powershell {monaco}
cp notes.txt backup.txt
mv backup.txt ~
```

</v-click>

---

8. Delete a file:

<v-click>

```powershell {monaco}
rm ~/backup.txt
```

</v-click>

---

9. Create and view a hidden file:

<v-click>

```powershell {monaco}
ni .config
cat .config
```

</v-click>

---

10. Remove the projects folder (carefully):

<v-click>

```powershell {monaco}
cd ~
rm -r projects
```

</v-click>

---

## 🎉 You're Ready!

You now understand the fundamentals of the Command Prompt and PowerShell.

Start exploring, automate your work, and feel the power of the terminal. 💪

---
