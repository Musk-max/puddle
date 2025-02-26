# Adding locally hosted code to GitHub
If your code is stored locally on your computer and is tracked by Git or not tracked by any version control system (VCS), you can import the code to GitHub using GitHub CLI or Git commands.

##  Initializing a Git repository
Initialize the local directory as a Git repository. By default, the initial branch is called main.
If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b
```
git init -b main
```
>Note: When you initialize a local git repository you should create an	empty new file at least (example the standard	README.md).
Pushing an empty repository does'nt work.

Add the files in your new local repository. This stages them for the first commit.
```
 $ git add .
```
>Note: To unstage a file, use 'git reset HEAD YOUR-FILE. 'git reset HEAD YOUR-FILE'

Commit the files that you've staged in your local repository.
```
$ git commit -m "First commit"
```
>Note: To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

## Adding a local repository to GitHub using Git
Create a new repository on GitHub.
To avoid errors, do not initialize the new repository with README, license, or gitignore files.

copy the remote repository URL.
Add the URL for the remote repository where your local repository will be pushed :
```
 git remote add origin REMOTE-URL
```
verify that you set the remote URL correctly:
```
git remote -v
```
To push the changes in your local repository to GitHub, run the following command.
```
git push origin main
```
> Note:If your default branch is not named "main," replace "main" with the name of your default branch.

# Setting up a django project

Create a virtual environment :
```
python -m venv venv
```
>Note:In a virtual environment you can install python package(example:django) just for this project
