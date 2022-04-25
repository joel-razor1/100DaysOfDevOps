Notes from IBM Youtube Video, FreeCodeCamp Video by Gwen

GIT
Version Control System
The Management of Changes to Documents, Computer programs, large websites, and other Collections of information

GitHub & GitLab
Hosted Git

What does it do?
Track changes
Historical Backups(Snapshot)
Team based Developments
Flexible (Part of Automated Tests/Builds)
CLI or Web
TRUNK based Development (main and branch)
/ |
| |
| |
|\_|
|

What is a respository?
It is a place to store your code and add changes to your code

Clone the repository to your local machine and create a branch
When task is completed push it back to the repository

When one person has already pushed code to git and another person pulls it to push it back then MErge Conflict Occurs

Merge Conflict
When this happens, resolve the code and then push it back

Pull Request
A request that should get approved by proper authorities so that the branch can be merged

GIT Commands

clone->Bring a repository hosted somewhere on the web to your local machine
add-> Track your files and changes in Git
commit-> Save your files to Git
push->Upload Git Commmits to a remote repo, like GitHub
pull-> Download changes from remote repo to your local machine, the opposite of push

Each commit has a unique Identifier.

Git Status-> used to display the state of the repository and staging area. It allows us to see the tracked, untracked files and changes. This command will not show any commit records or information.

git commit -m (message related to commit) -m (Description)
git push(origin -> location of git repository master->The branch to which we want to push to)

if you want to make a folder a git repository, start with git init
git init
git status
git add .
git status
git commit -m "dsds"
git push origin master(you will get a error if you haven't cloned it from a remote repository
How to solve it?
Create a same repo with the same naem

git remote add origin (copy the repository link)
git push -u origin master (u means upstream)

GIT Branch

Why Git branch? Because you may want to write a code which may have issues at first but don't want to put it on main branch

git branch -> shows what branches are available and the \* mark shows on which branch you are on

git checkout -> to switch between already created branches

git checkout -b -> to create a new branch
