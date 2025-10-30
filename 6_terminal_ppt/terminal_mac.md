---
theme: default
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
- Often more **efficient** than graphical interfaces—especially for developers

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

```bash
pwd

Prints the current directory path

⸻

⚙️ Part 2: Common Commands in Terminal

📄 Listing Files in a Directory

ls

Lists files in the current directory

ls -la

Lists all files, including hidden ones

⸻

🚶 Moving Between Directories

cd directory-name

Change to another directory

cd ..

Move up one level

cd ~

Return to home directory

cd /Users/your-username/projects

Go directly to a specific path

⸻

📦 Moving and Copying Files

Move a file:

mv file.txt ~/projects

Rename a file:

mv oldname.txt newname.txt

Copy a file:

cp file.txt ~/projects


⸻

🏗️ Creating Directories

mkdir new-folder

Creates a new directory

⸻

🗑️ Deleting Files and Directories

Delete a file:

rm file.txt

Delete an empty directory:

rmdir folder

Delete a directory and its contents:

rm -r folder


⸻

👁️ Part 3: Hidden Files

Understanding Hidden Files
	•	Files that begin with . are hidden
	•	Examples: .gitignore, .env

To list hidden files:

ls -la


⸻

✏️ Creating and Editing a .env File

Create a hidden file:

touch .env

Edit using nano:

nano .env

Type your text → Ctrl + X, then Y, then Return to save.

⸻

📖 Viewing File Contents

cat .env

Displays the contents of .env

⸻

💪 Part 4: Exercises

Try these to build confidence with the Terminal:
	1.	Print your current directory:

pwd


	2.	List all files (including hidden ones) in your home directory:

ls -la ~


	3.	Create a projects directory:

cd ~
mkdir projects


	4.	Move into it and create a file:

cd projects
touch notes.txt


	5.	Edit and save the file:

nano notes.txt


	6.	Copy and move files:

cp notes.txt backup.txt
mv backup.txt ~


	7.	Delete files:

rm ~/backup.txt


	8.	Create and view a hidden file:

touch .config
nano .config
cat .config


	9.	Remove the projects directory (carefully!):

cd ~
rm -r projects



⸻

🎉 You Did It!

You’ve learned the fundamentals of the Terminal on macOS.

Use your new command-line powers wisely. 💻

---