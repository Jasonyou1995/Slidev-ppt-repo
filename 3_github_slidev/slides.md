---
theme: default
class: text-center
title: Git & GitHub Tutorial
info: |
  A practical guide to version control and collaboration
  covering essential Git commands, GitHub workflows,
  and best practices for development teams.

transition: slide-left
mdc: true
lineNumbers: false
---

# Git & GitHub Tutorial

A practical guide to version control and collaboration

Press space to continue

---

# What we'll cover

<div class="grid grid-cols-2 gap-12">

<div>

## Fundamentals

- What is version control?
- Git basics
- Repository management
- Basic workflow

</div>

<div>

## Collaboration

- Branching strategies
- Pull requests
- Code review
- Team workflows

</div>

</div>

---

# What is Git?

Git is a distributed version control system that tracks changes in files.

## Key concepts

**Repository** - A project folder with Git tracking  
**Commit** - A snapshot of your files at a point in time  
**Branch** - A separate line of development  
**Remote** - A repository hosted elsewhere (like GitHub)

## Why use version control?

- Track changes over time
- Collaborate with others
- Revert to previous versions
- Work on features in parallel

---

# Git vs GitHub

<div class="grid grid-cols-2 gap-12">

<div>

## Git

- Version control system
- Runs locally on your computer
- Command line tool
- Works offline
- Free and open source

</div>

<div>

## GitHub

- Cloud hosting service
- Web interface for Git repos
- Additional collaboration tools
- Issues, pull requests, actions
- Free for public repos

</div>

</div>

Think of Git as the engine, GitHub as the garage where you park your code.

---

# Creating a repository

## Option 1: Start on GitHub

1. Go to github.com
2. Click "New repository"
3. Choose a name
4. Add README, gitignore, license
5. Clone to your computer

```bash {all}
git clone https://github.com/username/repo-name.git
```

---

# Creating a repository

## Option 2: Start locally

```bash {1-3|4-6|7-9|10-13|all}
# Create a new folder
mkdir my-project
cd my-project

# Initialize Git
git init

# Create your first file
echo "# My Project" > README.md

# Add and commit
git add README.md
git commit -m "Initial commit"
```

---

# Adding a remote

After creating a repo on GitHub, connect it to your local repo:

```bash {1-3|4-7|all}
# Add the remote
git remote add origin https://github.com/username/repo-name.git

# Push your code
git branch -M main
git push -u origin main
```

Now your local and remote repositories are connected.

---

# Daily Git workflow

The typical development cycle:

```bash {1-3|4-7|8-10|11-12|all}
# 1. Check status
git status

# 2. Add changes
git add filename.txt
git add .                    # Add all changes

# 3. Commit changes
git commit -m "Add new feature"

# 4. Push to remote
git push
```

Always write clear, descriptive commit messages.

---

# Working with branches

Branches let you work on features without affecting main code.

```bash {1-3|4-7|8-10|11-13|14-15|all}
# Create and switch to new branch
git checkout -b feature-login

# Make changes, add, commit
git add .
git commit -m "Add login form"

# Push branch to remote
git push -u origin feature-login

# Switch back to main
git checkout main

# Delete branch (after merging)
git branch -d feature-login
```

---

# Branch naming conventions

Use descriptive names that indicate the purpose:

```bash {1|2|3|4|all}
feature/user-authentication
bugfix/password-validation
hotfix/security-patch
docs/api-reference
```

Keep branch names short but meaningful.

---

# Pull requests

Pull requests let you propose changes and get code reviewed.

## Creating a pull request

1. Push your branch to GitHub
2. Go to the repository on GitHub
3. Click "Compare & pull request"
4. Add title and description
5. Request reviewers
6. Submit for review

## Pull request best practices

- Keep changes focused and small
- Write clear descriptions
- Include screenshots for UI changes
- Link related issues

---

# Code review process

## As an author

- Respond to feedback promptly
- Make requested changes
- Explain complex decisions
- Be open to suggestions

## As a reviewer

- Review within 24 hours
- Be constructive and specific
- Focus on correctness, not style
- Test changes locally if needed

---

# Merging strategies

<div class="grid grid-cols-2 gap-12">

<div>

## Merge commit

```bash {all}
git checkout main
git merge feature-branch
```

- Preserves history
- Shows when features merged
- Creates merge commits

</div>

<div>

## Squash and merge

- Combines all commits into one
- Cleaner history
- Loses individual commits
- Good for feature branches

</div>

</div>

---

# Essential Git commands

## Repository setup

```bash {1|2|3|all}
git init                     # Initialize repository
git clone <url>              # Clone repository
git remote -v                # List remotes
```

---

# Essential Git commands (cont.)

## Daily workflow

```bash {1|2|3|4|5|all}
git status                   # Check status
git add <file>               # Stage changes
git commit -m "message"      # Commit changes
git push                     # Push to remote
git pull                     # Pull from remote
```

## Branching

```bash {1|2|3|4|all}
git branch                   # List branches
git checkout <branch>        # Switch branch
git checkout -b <branch>     # Create and switch
git merge <branch>           # Merge branch
```

---

<div class="flex items-center justify-center h-[60vh]">
  <h1 class="text-5xl font-bold font-serif text-center w-full">Advanced Topics</h1>
</div>

---

# Viewing history

```bash {1-3|4-6|7-9|10-12|13-15|all}
# View commit history
git log
git log --oneline            # Compact view

git log --graph              # Visual graph

# Show specific commit
git show <commit-hash>

# See what changed
git diff                     # Unstaged changes
git diff --staged            # Staged changes

# Show file history
git log -p filename.txt
```

---

---

# Undoing changes

```bash {1-2|3-4|5-6|7-8|9-10|all}
# Discard unstaged changes
git checkout -- filename.txt

# Unstage files
git reset HEAD filename.txt

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Revert a commit (safe for shared repos)
git revert <commit-hash>
```

---

---

# Working with remotes

```bash {1-2|3-4|5-6|7-8|9-10|11-12|all}
# List remotes
git remote -v

# Add remote
git remote add origin <url>

# Change remote URL
git remote set-url origin <new-url>

# Fetch from remote
git fetch origin

# Pull changes
git pull origin main

# Push changes
git push origin main
```

---

# Merge conflicts

Conflicts happen when Git can't automatically merge changes.

## Example conflict

```javascript {1-2|3-4|5-6|7-8|all}
function greetUser(name) {
&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD
    return `Hello, ${name}!`;
=======
    return `Hi ${name}!`;
&gt;&gt;&gt;&gt;&gt;&gt;&gt; feature-branch
}
```

## Resolving conflicts

1. Edit the file to keep what you want
2. Remove conflict markers (`&lt;&lt;&lt;&lt;&lt;&lt;&lt;`, `=======`, `&gt;&gt;&gt;&gt;&gt;&gt;&gt;`)
3. Add and commit the resolved file

```bash {1|2|3|all}
git add filename.js
git commit -m "Resolve merge conflict"
```

---

# GitHub features

## Issues

- Track bugs and feature requests
- Assign to team members
- Label and organize
- Link to pull requests

## Projects

- Kanban boards
- Track progress
- Organize work
- Automate workflows

## Actions

- Continuous integration
- Automated testing
- Deploy applications
- Custom workflows

---

# Protected branches

Protect important branches like `main` from direct pushes.

## Branch protection rules

- Require pull request reviews
- Require status checks to pass
- Restrict who can push
- Require up-to-date branches

## Setting up protection

1. Go to Settings > Branches
2. Add branch protection rule
3. Configure requirements
4. Save changes

---

# Best practices

## Commit messages

```bash {1|2|3|4|5|6|7|8|9|10|11|12|all}
# Good
git commit -m "Add user login validation"
git commit -m "Fix memory leak in image processing"
git commit -m "Update API documentation"

# Avoid
git commit -m "fix"
git commit -m "changes"
git commit -m "stuff"
```

## Repository organization

- Keep README up to date
- Use .gitignore files
- Add license information
- Include contributing guidelines

---

# Git workflow strategies

## GitHub Flow

1. Create branch from main
2. Make changes and commit
3. Open pull request
4. Review and discuss
5. Merge to main
6. Delete branch

Simple and effective for most teams.

## Git Flow

More complex branching model with:

- `main` - production code
- `develop` - integration branch
- `feature/*` - feature branches
- `release/*` - release preparation
- `hotfix/*` - emergency fixes

---

# Common mistakes to avoid

- Committing sensitive data (passwords, API keys)
- Working directly on main branch
- Writing unclear commit messages
- Not pulling before pushing
- Committing too many changes at once
- Not using .gitignore files
- Force pushing to shared branches

---

# Authentication

## Personal Access Tokens

GitHub requires tokens instead of passwords:

1. Go to Settings > Developer settings > Personal access tokens
2. Generate new token
3. Select necessary scopes
4. Use as password when prompted

## SSH Keys (recommended)

```bash {1|2|3|4|5|6|7|8|9|10|11|12|all}
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to SSH agent
ssh-add ~/.ssh/id_ed25519

# Copy public key and add to GitHub
cat ~/.ssh/id_ed25519.pub
```

---

# Troubleshooting

## Repository not found

- Check repository name and URL
- Verify you have access
- Ensure repository exists

## Permission denied

- Check authentication (token/SSH key)
- Verify you're a collaborator
- Test SSH connection: `ssh -T git@github.com`

## Merge conflicts

- Keep branches up to date
- Make smaller, focused commits
- Communicate with team members

## Lost work

- Use `git reflog` to find lost commits
- Check stash: `git stash list`
- Look in other branches

---

# Resources for learning more

## Official documentation

- [Git documentation](https://git-scm.com/doc)
- [GitHub documentation](https://docs.github.com)
- [Pro Git book](https://git-scm.com/book) (free online)

---

# Resources for learning more (cont.)

## Interactive learning

- [GitHub Skills](https://skills.github.com)
- [Learn Git Branching](https://learngitbranching.js.org)

## Tools

- [GitHub Desktop](https://desktop.github.com) - GUI client
- [GitHub CLI](https://cli.github.com) - Command line tool
- [GitLens](https://gitlens.amod.io) - VS Code extension

---

# Summary

## Key takeaways

- Git tracks changes to your files over time
- GitHub provides hosting and collaboration tools
- Use branches for parallel development
- Pull requests enable code review
- Clear commit messages are essential
- Protect important branches
- Practice makes perfect

## Next steps

- Create your first repository
- Practice basic Git commands
- Try collaborating on an open source project
- Set up your development workflow

---

layout: center
class: text-center

---

# Thanks!

Questions?

Learn by doing - start using Git and GitHub in your next project.

---

# Content Overflow Solutions

## When slides have too much content:

### 1. Use smaller text classes

```yaml
---
layout: default
class: text-sm
---
```

### 2. Split content across multiple slides

- Break long sections into parts
- Use "(cont.)" in titles
- Maintain logical flow

### 3. Use grid layouts for side-by-side content

```html
<div class="grid grid-cols-2 gap-12">
  <div>Left content</div>
  <div>Right content</div>
</div>
```

### 4. Monaco Editor animations

- Use `{1|2|3|all}` syntax for line-by-line reveals
- Keeps audience engaged
- Prevents information overload

### 5. Alternative layouts

- `layout: center` for focused content
- `layout: two-cols` for comparisons
- `layout: image-right` for visual balance
