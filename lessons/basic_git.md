# Version Control with Git #
[initiate with GitHub example]

## Automated Version Control ##
**Questions**
- What is version control and why should I use it?

**Objectives**
- Understand the benefits of an automated version control system.
- Understand the basics of how Git works.

KEYWORDS:
`distributed version control`, `commits`,

```yml
$ git --help
$ git config --list
```

## Setting Up Git ##
**Questions**
- How do I get set up to use Git?

**Objectives**
- Configure git the first time it is used on a computer.
- Understand the meaning of the `--global` configuration flag.


```sh
$ git config --global user.name "knielbo"
$ git config --global user.email "kln@cas.au.dk"
$ git config --global color.ui "auto"
```

```yml
# w/wait flag result is to wait until the file is closed in the editor
$ git config --global core.editor "atom --wait" # atom
$ git config --global core.editor "subl -n -w" # sublime
$ cat ~/.gitconfig
```

## Creating a Repository ##
**Questions**
- Where does Git store information?

**Objectives**
- Create a local Git repository.

**intiate repo**
```yml
$ mkdir planets
$ cd planets
$ git init
$ ls -la
$ git status
```

**nested repos are redundant**
```yml
$ mkdir moons
$ cd moons
$ git init
$ cd ..
$ rm -rf moons/.git # recursive and force
```

## Tracking Changes ##
**Questions**
- How do I record changes in Git?
- How do I check the status of my version control repository?
- How do I record notes about what changes I made and why?

**Objectives**
- Go through the modify-add-commit cycle for one or more files.
- Explain where information is stored at each stage of that cycle.
- Distinguish between descriptive and non-descriptive commit messages.

**add a file**
```yml
$ echo "Cold and dry, but everything is my favorite color" >> mars.txt
$ git status # untracked file(s)
$ git add mars.txt
$ git status # new file
$ git commit -m "Start notes on Mars as base" # store copy in .git/ with id 32dea69
$ git status # nothing to commit
$ git log # display recent git activities
```

**modify a file**

```yml
$ echo "The two moons may be a problem for Wolfman" >> mars.txt
$ git status # no changes added to commit
$ git diff # compare versions
```

*break down diff*
- The first line tells us that Git is producing output similar to the Unix diff command comparing the old and new versions of the file.
- The second line tells exactly which versions of the file Git is comparing; df0654a and 315bf3a are unique computer-generated labels for those versions.
- The third and fourth lines once again show the name of the file being changed.
- The remaining lines are the most interesting, they show us the actual differences and the lines on which they occur. In particular, the + marker in the first column shows where we added a line.

**add and commit modification**
```yml
$ git commit -m "concerns about moon's effects on Wolfman" # ERROR
$ git status #

$ git add mars.txt
$ git commit -m "concerns about moon's effects on Wolfman"
```

**add sends to staging area and commit changes**

```yml
$ echo "But the Mummy will appreciate the lack of humidity" >> mart.txt
$ git diff # nothing
$ git add mars.txt
$ git diff
$ git diff --staged # shows difference in staging area
$ git commit -m "Discuss concerns about Mars' climate for Mummy"
$ git status
$ git log
```

**sudos**

```yml
$ git diff --staged --color-words # requires word level modification

$ git log -1 # only get last log entry

$ git log --format=full

$ git commit -m "some messages" --author="kln-courses <kln@cas.au.dk>"
```

## Exploring History ##
**Questions**
- How can I identify old versions of files?
- How do I review my changes?
- How can I recover old versions of files?

**Objectives**
- Explain what the HEAD of a repository is and how to use it.
- Identify and use Git commit numbers.
- Compare various versions of tracked files.
- Restore old versions of files.


`HEAD` identifier for **most recent commit**
```yml
$ echo "An ill-considered change" >> mars.txt
$ cat mars.txt
$ git diff HEAD mars.txt
# compare (identifcal)
$ git diff
```
using `HEAD~n` identifiers

```yml
$ git diff HEAD~1 mars.txt
$ git diff HEAD~2 mars.txt
```
other uses of `HEAD`
```yml
# include commit comments
$ git show HEAD~1 mars.txt
# using commit (short) id
$ git diff df0654a mars.txt
```
**rolling a file back** to previous version commit with `checkout`

```yml
$ echo "We will need to manufacture our own oxygen" >> mars.txt
$ git status
$ cat mars.txt

$ git checkout HEAD mars.txt
$ cat mars.txt
```
`revert` is `checkout` for group repos

## Ignoring things ##

ignoring files with `.gitignore`

```yml
$ mkdir results/
$ touch a.dat b.dat results/a.out results/b.out
$ git status
```
clutter repository by putting all files under version control

```yml
$ echo "*.dat" >> .gitignore
$ echo "results/" >> .gitignore
$ git status
$ git add .gitignore
$ git commit -m "add ignore file"
$ git status
$ git status --ignored
```

ignore file sudos
```yml
$ echo "*.out" >> .gitignore
$ echo "results/!b.out" >> .gitignore
```

## Remotes in GitHub ##


```yml
$ mkdir <local-repository>
$ cd <local-repository>
$ echo "# shakespeare" >> README.md
$ git init
$ git add README.md
$ git commit -m "initialized with README"
$ git remote add origin https://github.com/kln-courses/<remote-repository>.git
$ git push -u origin master
```
Confirm that remote is added
```yml
git remote -v
```
`-u` flag for `git push` associates the current branch with a remote branch so that the git pull command can be used without any arguments

Pull remote changes to local repo
```yml
git pull origin master
```

branching
```yml
git branch <branch-name>
git checkout <branch-name>
```

## Collaborating ##

**collaborative workflow**
1. update your local repo with `git pull origin master`,
2. make your changes and stage them with `git add`,
3. commit your changes with git `commit -m`, and
4. upload the changes to GitHub with `git push origin master`



```yml
```
```yml
```
```yml
```
```yml
```
