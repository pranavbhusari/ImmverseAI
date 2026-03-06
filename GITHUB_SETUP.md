# 📤 GitHub Setup Instructions

Follow these steps to upload your ImmverseAI project to GitHub.

## ✅ Prerequisites

- GitHub account (create at https://github.com)
- Git installed on your computer
- Project ready (already cleaned up ✓)

---

## 🚀 Step-by-Step Guide

### Step 1: Create a New Repository on GitHub

1. Go to https://github.com/new
2. Enter repository name: `ImmverseAI`
3. Add description: "Multilingual QnA Generation System"
4. Choose visibility: **Public** (so others can see it)
5. **DO NOT** initialize with README (we already have one)
6. Click **Create repository**

### Step 2: Initialize Git in Your Project

Open PowerShell in your project directory:

```powershell
# Navigate to project
cd c:\Users\Rutika\Desktop\ImmverseAI

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Multilingual QnA Generation System"
```

### Step 3: Add Remote and Push to GitHub

Replace `YOUR-USERNAME` with your GitHub username:

```powershell
# Add GitHub repository as remote
git remote add origin https://github.com/YOUR-USERNAME/ImmverseAI.git

# Verify remote added
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 4: Verify Upload

1. Go to https://github.com/YOUR-USERNAME/ImmverseAI
2. Verify all files are there
3. Check that `.env` is in `.gitignore` (not uploaded) ✓

---

## 📋 What Gets Uploaded

✅ **Uploaded:**
- app.py
- qna_generator.py
- translator.py
- document_parser.py
- excel_exporter.py
- requirements.txt
- README.md
- QUICKSTART.md
- .gitignore
- .env.example

❌ **NOT Uploaded (ignored):**
- venv/ (virtual environment)
- __pycache__/ (Python cache)
- .env (sensitive API keys) ✓ Important!
- output/ (generated files)
- *.xlsx (Excel files)

---

## 🔐 Security Check

Verify `.env` file is protected:

```powershell
# Check git status
git status

# Should show:
# nothing to commit, working tree clean
```

**Important**: `.env` should never be pushed! It contains your Groq API key.

---

## 📝 After Upload - Updating

To push future changes:

```powershell
# Make changes to files...

# Stage changes
git add .

# Commit changes
git commit -m "Your commit message here"

# Push to GitHub
git push origin main
```

---

## 🎯 Common Git Commands

```powershell
# Check status
git status

# View commit history
git log --oneline

# View remotes
git remote -v

# Create a new branch
git checkout -b feature-branch

# Switch to main branch
git checkout main

# Delete local branch
git branch -d branch-name
```

---

## 🆘 Troubleshooting

### "fatal: not a git repository"
```powershell
# Run 'git init' again in correct directory
cd c:\Users\Rutika\Desktop\ImmverseAI
git init
```

### "Permission denied (publickey)"
- Use HTTPS instead of SSH:
```powershell
git remote set-url origin https://github.com/YOUR-USERNAME/ImmverseAI.git
```

### "src refspec main does not match any"
```powershell
# Make sure you have commits first
git commit -m "Initial commit"
# Then push
git push -u origin main
```

### Accidentally pushed .env
```powershell
# Remove from git history
git rm --cached .env
git commit -m "Remove .env file"
git push origin main
```

---

## 📚 Git Configuration (Optional)

Set your Git credentials:

```powershell
# Set username
git config --global user.name "Your Name"

# Set email
git config --global user.email "your.email@example.com"

# Verify
git config --global --list
```

---

## 🎉 Complete!

Your project is now on GitHub! 🚀

You can:
- Share the link: `https://github.com/YOUR-USERNAME/ImmverseAI`
- Invite collaborators
- Track issues and pull requests
- Showcase your work

---

## Next Steps

1. Add a GitHub profile picture and bio
2. Pin this repository to your profile
3. Share on LinkedIn/Twitter
4. Add topics to repository (multilingual, qna, streamlit, etc.)

Happy coding! 💻
