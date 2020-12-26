## add
Update the index by adding all files in the working directory (`-n` for dry-run)
```
git add -A
```
## checkout
Create a new branch
```
git checkout -b <branch>
```
Switch to an existing branch
```
git checkout <branch>
```

## cleanup
Remove untracked files from the working tree (`-n` for dry-run)
```
git clean -df
```

## diff
View the changes you staged for the next commit
```
git diff --cached
```
Diff between local and remote branch
```
git diff <branch>..origin/<branch>
```
## push
Use `-n` for dry-run
```
git push -u origin <branch>
```
Delete a remote branch
```
git push -d origin <branch>
```
Push tags
```
git push --tags
```
## reset
```
git reset --mixed
```
```
git reset --hard
```
```
git reset --hard HEAD^
```
## stash 

```
git stash
```

```
git stash apply
```
## status 
List of modified files (using `-vv` will also list contents)
```
git status -v
```

## tag
Tag current commit
```
git tag -a -m <message> <tag>
```
Delete a tag
```
git tag -d <tag>
```
