# Install git in your windows

## Then open git bash 

## run the following commands 

```bash
git config --global --unset user.name
git config --global --unset user.email
git config --global --unset credential.helper
```

## now go to folder where you want to clone the repo 
- Run the below command: replace "Your Name" with github name
- replace "Your-email" with your github email
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

## confirm the configuration is correct or not

```bash
git config --global --list
```

## Set Up SSH Key (Optional, But Recommended)
- in git bash run the below command
```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

- Start the SSH agent and add your key:
```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

- Copy the SSH key to GitHub:
```bash
clip < ~/.ssh/id_rsa.pub
```

- Go to GitHub > Settings > SSH and GPG Keys.
- Click New SSH Key, paste it, and save.

- Test the connection:
```bash 
ssh -T git@github.com
```

## clone the repository 
```bash 
git clone git@github.com:abhigyan-709/git-live.git
cd your-repo-location 
/path/to/repo/git-live
```

## create a new file in folders
```bash
any python file as of now, like multiply.py
add the code in that
```

# run the below command to push the changes to the repo with your own branch
```bash
git add .  # this should only be done when you have added a new file or made any changes in any file
git commit -m "your-commit message"
git checkout -b "your-branch-name-your-username"
git push origin -u "your-branch-name-your-username"
```

## confirm the changes in the git repo of 
```bash
https://github.com/abhigyan-709/git-live

you will see your branch
```