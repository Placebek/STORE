pip install virtualenv
virtualenv env
cd env
cd Scripts
activate
cd ..
cd ..


git clone https://git...
git add .
git config --global user.email "goblins.from.mars2003@gmail.com"
git config --global user.name "Placebek"
git commit -m "first commit"
git push origin main (дереу мастерге өзгерту керек)







D:\PythonProjects\example> 
 *  History restored 

Microsoft Windows [Version 10.0.19045.3930]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

D:\PythonProjects\example>python
Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> ^Z


D:\PythonProjects\example>pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.25.0-py3-none-any.whl (3.8 MB)
     |████████████████████████████████| 3.8 MB 819 kB/s
Collecting platformdirs<5,>=3.9.1
  Downloading platformdirs-4.2.0-py3-none-any.whl (17 kB)
Collecting distlib<1,>=0.3.7
  Downloading distlib-0.3.8-py2.py3-none-any.whl (468 kB)
     |████████████████████████████████| 468 kB 6.4 MB/s
Collecting filelock<4,>=3.12.2
  Downloading filelock-3.13.1-py3-none-any.whl (11 kB)
Installing collected packages: platformdirs, filelock, distlib, virtualenv
Successfully installed distlib-0.3.8 filelock-3.13.1 platformdirs-4.2.0 virtualenv-20.25.0
WARNING: You are using pip version 21.1.1; however, version 24.0 is available.
You should consider upgrading via the 'c:\users\jake\appdata\local\programs\python\python38\python.exe -m pip install --upgrade pip' command.

D:\PythonProjects\example>cd env
Системе не удается найти указанный путь.

D:\PythonProjects\example>virtualenv env
created virtual environment CPython3.8.10.final.0-64 in 9166ms
  creator CPython3Windows(dest=D:\PythonProjects\example\env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Jake\AppData\Local\pypa\virtualenv)      
    added seed packages: pip==23.3.1, setuptools==69.0.2, wheel==0.42.0
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

D:\PythonProjects\example>cd env

D:\PythonProjects\example\env>cd Scripts

D:\PythonProjects\example\env\Scripts>activate

(env) D:\PythonProjects\example\env\Scripts>cd..

(env) D:\PythonProjects\example\env>cd..

(env) D:\PythonProjects\example>python main.py

(env) D:\PythonProjects\example>pip install psycopg2
Collecting psycopg2
  Downloading psycopg2-2.9.9-cp38-cp38-win_amd64.whl.metadata (4.5 kB)
Downloading psycopg2-2.9.9-cp38-cp38-win_amd64.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 3.1 MB/s eta 0:00:00
Installing collected packages: psycopg2
Successfully installed psycopg2-2.9.9

[notice] A new release of pip is available: 23.3.1 -> 24.0
[notice] To update, run: python.exe -m pip install --upgrade pip

(env) D:\PythonProjects\example>pip list
Package    Version
---------- -------
pip        23.3.1
psycopg2   2.9.9
setuptools 69.0.2
wheel      0.42.0

[notice] A new release of pip is available: 23.3.1 -> 24.0
[notice] To update, run: python.exe -m pip install --upgrade pip

(env) D:\PythonProjects\example>cd env

(env) D:\PythonProjects\example\env>cd Scripts

(env) D:\PythonProjects\example\env\Scripts>deactivate.bat
D:\PythonProjects\example\env\Scripts>cd ..

D:\PythonProjects\example\env>cd ..

D:\PythonProjects\example>pip list
Package      Version
------------ -------
distlib      0.3.8
filelock     3.13.1
pip          21.1.1
platformdirs 4.2.0
pygame       2.5.2
setuptools   56.0.0
virtualenv   20.25.0
WARNING: You are using pip version 21.1.1; however, version 24.0 is available.
You should consider upgrading via the 'c:\users\jake\appdata\local\programs\python\python38\python.exe -m pip install --upgrade pip' command.

D:\PythonProjects\example>cd env

D:\PythonProjects\example\env>cd Scripts

D:\PythonProjects\example\env\Scripts>activate

(env) D:\PythonProjects\example\env\Scripts>cd ..

(env) D:\PythonProjects\example\env>cd ..

(env) D:\PythonProjects\example>git 
"git" не является внутренней или внешней
командой, исполняемой программой или пакетным файлом.

(env) D:\PythonProjects\example>
 *  History restored 

Microsoft Windows [Version 10.0.19045.3930]
(c) Корпорация Майкрософт (Microsoft Corporation). Все права защищены.

D:\PythonProjects\example>git 
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

D:\PythonProjects\example>git 
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--config-env=<name>=<envvar>] <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

D:\PythonProjects\example>git clone https://github.com/Placebek/example_repo.git
Cloning into 'example_repo'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

D:\PythonProjects\example>git add .
fatal: not a git repository (or any of the parent directories): .git

D:\PythonProjects\example>cd example_repo

D:\PythonProjects\example\example_repo>git add .

D:\PythonProjects\example\example_repo>git commit -m "first commit" 
Author identity unknown




*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

D:\PythonProjects\example\example_repo>git config --global user.email "goblins.from.mars2003@gmail.com"
D:\PythonProjects\example\example_repo>gigit config --global user.name "Placebek"  
D:\PythonProjects\example\example_repo>git config --global user.name "Placebek"   
D:\PythonProjects\example\example_repo>git commit -m "first commit"


Presentation layer -> Business logic layer