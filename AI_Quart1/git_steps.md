Steps for making a repo and pushing to Github :
1. git init : Initializes a new Git repository in the current directory.
2. git add : Adds files to the staging area, preparing them for a commit.
3. git commit : Creates a new commit with the changes in the staging area.
4. git status : Shows the current state of your working directory and staging area.
5. git log : Displays a log of all commits in the current branch.

Working with Branches :
1. Creating a branch : (git branch new-feature)
2. Switching branches : (git checkout new-feature
                        # Or, to create and switch in one command:
                        git checkout -b another-feature)
3. Merging branches : (git checkout main
                      git merge new-feature)


git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Dawoodayaz20/IMS.git
git push -u origin main
