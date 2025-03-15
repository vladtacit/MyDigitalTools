# Git

## Create a local repositoty for SomeProject

Change:
* "SomeProject" to your project name
* "UserLogin" to your account name


```bash
git init
git add --all
git commit -m "Initial SomeProject version"
```

## Add remote (GitHub)

### Connecting to GitHub with SSH

1. Generating a new SSH key and adding it to the ssh-agent

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
2. Adding a new SSH key to your GitHub account

```bash
cat ~/.ssh/KeyFile.pub
```

3. Testing your SSH connection

```bash
ssh -T git@github.com
> Hi UserLogin! You've successfully authenticated, but GitHub does not provide shell access.
```

### Add new origin

```bash
git remote add "origin" git@github.com:UserLogin/SomeProject.git
git remote -v
git push -u origin master
```

### Change URL for origin

If you need to change the URL of an existing remote repository:

```bash
git remote set-url "origin" git@github.com:UserLogin/SomeProject.git
```

## Ignore files for commit

[Source](https://stackoverflow.com/a/767213/26464397)

The .gitignore file should be in your repository, so it should indeed be added and committed in, as git status suggests. It has to be a part of the repository tree, so that changes to it can be merged and so on.

So, add it to your repository, it should not be gitignored.

If you really want you can add .gitignore to the .gitignore file if you don't want it to be committed. However, in that case it's probably **better to add the ignores to .git/info/exclude**, a special checkout-local file that works just like .gitignore but does not show up in "git status" since it's in the .git folder.

[See also](https://help.github.com/articles/ignoring-files)
