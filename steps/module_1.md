# Adding locally hosted code to GitHub
If your code is stored locally on your computer and is tracked by Git or not tracked by any version control system (VCS), you can import the code to GitHub using GitHub CLI or Git commands.

##  Initializing a Git repository
Initialize the local directory as a Git repository. By default, the initial branch is called master.
If you’re using Git 2.28.0 or a later version, you can set the name of the default branch using -b
```
git init -b main
```
>Note: When you initialize a local git repository you should create an	empty new file at least (example the standard	README.md).
Pushing an empty repository does'nt work.

Add the files in your new local repository. This stages them for the first commit.
```
 git add .
```
>Note: To unstage a file, use 'git reset HEAD YOUR-FILE. 'git reset HEAD YOUR-FILE'

Commit the files that you've staged in your local repository.
```
 git commit -m "First commit"
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
git push origin master
```
> Note:If your default branch is not named "main," replace "main" with the name of your default branch.
>Source : https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-with-github-cli

# Setting up a django project


Create a virtual environment :
```
python -m venv venv
```
>Note:In a virtual environment you can install python package(example:django) just for this project

Now activate the virtual environment with the following command.
```
# windows machine
venv\Scripts\activate
```
Packages and requirements - Our project will rely on a whole bunch of 3rd party packages (requirements) to function. We will be using a Python package manager to install packages throughout this course. 
I have already created a requirements.txt file. Check out requirements.txt:
```
django
```
Let's go ahead and install our project requirements. Add the following code to you terminal.
```
pip install -r requirements.txt  
```
Django - You can now go ahead and create a new Django project. Installing Django has given you access to a handy 'startproject' command. Use the following command to create our new project.
```
django-admin startproject puddle
```
Let's see inside our django project, we should have two files:
```
cd puddle
ls
```
The state of your repository should be :
```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        26/02/2025     07:02                puddle
-a----        26/02/2025     07:02            684 manage.py
```
manage.py is a script for runNing adminstrative task such like updating the database structure, managing the developement server...
puddle is a folder with the same name as the project which contains configurations files

# run django server to see if everything is Okay : 
```
python manage.py runserver
```
You should obtain the following page by clicking on the Starting development server url:
![result](django_welcome_page.png)


Add the files in your new local repository. This stages them for the first commit.
```
 git add .
```
Commit the files that you've staged in your local repository.
```
 git commit -m "commit description"
```
Send the file on your remote branch called master:
```
git push origin master
```
Then create a branch called module_1 by copying the work already done on it:
````
git checkout -b module_1
````
Send this branch on the remote:

```
git push origin module_1
```

>Note : this project each step will have one module and each module will have one branch on the remote
# Fusion d’une demande de tirage
Fusionnez une demande de tirage (pull request) dans la branche en amont quand le travail est terminé. Toute personne disposant d’un accès en poussée (push) au dépôt peut effectuer la fusion
## À propos des fusions de demande de 
Dans une demande de tirage, vous proposez que les modifications que vous avez apportées sur une branche de tête doivent être fusionnées dans une branche de base. Par défaut, toute demande de tirage peut être fusionnée à tout moment, sauf si la branche principale est en conflit avec la branche de base.
Si la demande de tirage présente des conflits de fusion ou si vous souhaitez tester les modifications avant de fusionner, vous pouvez extraire la demande de tirage localement et la fusionner à l’aide de la ligne de commande.
Vous ne pouvez pas fusionner un brouillon de demande de tirage. Pour plus d’informations sur les brouillons de demande de tirage, consultez À propos des demandes de tirage (pull requests).
# Fusion d’une demande de tirage
1)Under your repository name, click  Pull requests.

2)In the "Pull Requests" list, click the pull request you'd like to merge. (or make new pull request and create yours)

3)If prompted, type a commit message, or accept the default message.
and clik on pull request button

4)Scroll down to the bottom of the pull request. Depending on the merge options enabled for your repository, you can:
Merge all of the commits into the base branch by clicking Merge pull request. If the Merge pull request option is not shown, click the merge dropdown menu and select Create a merge commit.

5)Click Confirm merge, Confirm squash and merge, or Confirm rebase and merge.

6)Optionally, delete the branch (manually). This keeps the list of branches in your repository tidy.
# Merging via command line
Step 1 Clone the repository or update your local repository with the latest changes
```
git pull origin branch_name
```
Step 2 Switch to the base branch of the pull request.
```
git checkout master
```
Step 3 Merge the head branch into the base branch.
```
git merge module_1
```
Step 4 Push the changes.
```
git push -u origin master

```
step 5 Puis aller sur la branch master et la mettre à jour en local :
```
git checkout master

git pull origin master
```

> Note: by merging on web browser you have more option like deleting the branch after merging or not
> Source:https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/checking-out-pull-requests-locally?tool=webui

# Then create the next branch called module_2 by and switch on it to prepare the next module:
```
git checkout -b module_2
```

