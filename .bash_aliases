# .bash_aliases

## git
alias ga='git add -A && git diff --cached --name-only'
alias gb='git branch'
alias gc='git commit -m '
alias gp='git push'
alias gdf='git diff --cached --name-only'
alias gl='git log --oneline'
alias gs='git status'
alias gsv='git status -v'

# Kubernetes
alias k='kubectl'
alias kc='kubectl config use-context'
alias kns='kubectl config set-context --current --namespace'
alias kcv='kubectl config view --minify'
alias kg='kubectl get'
alias kd='kubectl describe'
alias ka='kubectl apply -f'
