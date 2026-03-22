# Fetch and push 2 remotes

Push to two remotes with one command:

```bash
# Add the second URL as an additional push URL for 'origin'
git remote set-url --add --push origin git@github.com:user/RepoName.git

cat ./.git/config
pushurl = git@github.com:user/RepoName.git
```

## [~]
