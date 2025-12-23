# GitHub Repository Setup

Your local Git repository is ready! Follow these steps to create a GitHub repository and push your code:

## Step 1: Create a New Repository on GitHub

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in:
   - **Repository name**: `premierzone` (or your preferred name)
   - **Description**: "Premier League statistics website with Python FastAPI backend"
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **"Create repository"**

## Step 2: Connect and Push to GitHub

After creating the repository, GitHub will show you commands. Use these PowerShell commands (replace `YOUR_USERNAME` and `YOUR_REPO_NAME`):

```powershell
# Add the remote repository
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Rename branch to main (if needed)
git branch -M main

# Push your code
git push -u origin main
```

## Example

If your GitHub username is `johndoe` and repo name is `premierzone`:

```powershell
git remote add origin https://github.com/johndoe/premierzone.git
git branch -M main
git push -u origin main
```

## Authentication

If prompted for credentials:
- **Username**: Your GitHub username
- **Password**: Use a Personal Access Token (not your GitHub password)
  - Create one at: https://github.com/settings/tokens
  - Select scope: `repo`

## Verify

After pushing, refresh your GitHub repository page - you should see all your files!

