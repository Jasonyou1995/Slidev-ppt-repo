---
theme: seriph
highlighter: shiki
lineNumbers: true
author: Shengwei You
info: |
  ## Introduction to Using the Terminal on a Mac
  Learn how to navigate, manage files, and master the basics of the macOS command line.
---

# 🖥️ Introduction to Using the Terminal on a Mac

## HKBU FIN7830 (2025)

### Become fluent with the command line

Shengwei You

---

## 🧭 Part 1: Preliminaries

### What is the Command Prompt?

- A **text-based interface** for interacting with your computer  
- Execute commands to:
  - Navigate the filesystem  
  - Manage files  
  - Run programs  
- Often more **efficient** than graphical interfaces, especially for developers

---

### 🪄 Opening the Terminal

To open **Terminal** on a Mac:

1. Press **Command + Space** to open **Spotlight Search**
2. Type **Terminal** and press **Return**
3. Or navigate to:  
   **Applications → Utilities → Terminal**

---

### 🗂️ Files and Directory Structure

- macOS organizes files into **directories (folders)**
- The top-level directory is `/` (the **root**)
- Your personal files live in `/Users/your-username`  
  → also represented as `~` (**home directory**)

```bash {monaco}
pwd
```

Prints the current directory path

---

## ⚙️ Part 2: Common Commands in Terminal

### 📄 Listing Files in a Directory

```bash {monaco}
ls
```

Lists files in the current directory

```bash {monaco}
ls -la
```

Lists all files, including hidden ones

---

### 🚶 Moving Between Directories

```bash {monaco}
cd directory-name
```

Change to another directory

```bash {monaco}
cd ..
```

Move up one level

```bash {monaco}
cd ~
```

Return to home directory

```bash {monaco}
cd /Users/your-username/projects
```

Go directly to a specific path

---

### 📦 Moving and Copying Files

Move a file:

```bash {monaco}
mv file.txt ~/projects
```

Rename a file:

```bash {monaco}
mv oldname.txt newname.txt
```

Copy a file:

```bash {monaco}
cp file.txt ~/projects
```

---

### 🏗️ Creating Directories

```bash {monaco}
mkdir new-folder
```

Creates a new directory

---

### 🗑️ Deleting Files and Directories

Delete a file:

```bash {monaco}
rm file.txt
```

Delete an empty directory:

```bash {monaco}
rmdir folder
```

Delete a directory and its contents:

```bash {monaco}
rm -r folder
```

---

## 👁️ Part 3: Hidden Files

### Understanding Hidden Files

- Files that begin with `.` are hidden
- Examples: `.gitignore`, `.env`

To list hidden files:

```bash {monaco}
ls -la
```

---

### ✏️ Creating and Editing a .env File

Create a hidden file:

```bash {monaco}
touch .env
```

Edit using nano:

```bash {monaco}
nano .env
```

Type your text → Ctrl + X, then Y, then Return to save.

---

### 📖 Viewing File Contents

```bash {monaco}
cat .env
```

Displays the contents of .env

---

## 💪 Part 4: Exercises

Try these to build confidence with the Terminal:

1. Print your current directory:

<v-click>

```bash {monaco}
pwd
```

</v-click>

---

2. List all files (including hidden ones) in your home directory:

<v-click>

```bash {monaco}
ls -la ~
```

</v-click>

---

3. Create a projects directory:

<v-click>

```bash {monaco}
cd ~
mkdir projects
```

</v-click>

---

4. Move into it and create a file:

<v-click>

```bash {monaco}
cd projects
touch notes.txt
```

</v-click>

---

5. Edit and save the file:

<v-click>

```bash {monaco}
nano notes.txt
```

</v-click>

---

6. Copy and move files:

<v-click>

```bash {monaco}
cp notes.txt backup.txt
mv backup.txt ~
```

</v-click>

---

7. Delete files:

<v-click>

```bash {monaco}
rm ~/backup.txt
```

</v-click>

---

8. Create and view a hidden file:

<v-click>

```bash {monaco}
touch .config
nano .config
cat .config
```

</v-click>

---

9. Remove the projects directory (carefully!):

<v-click>

```bash {monaco}
cd ~
rm -r projects
```

</v-click>

---

## 🎉 You Did It!

You've learned the fundamentals of the Terminal on macOS.

Use your new command-line powers wisely. 💻

