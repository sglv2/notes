# .bash_aliases

## git
alias ga='git add -A && git diff --cached --name-only'
alias gb='git branch'
alias gc='git commit -m '
alias gp='git push'
alias gdc='git diff --cached'
alias gdcn='git diff --cached --name-only'
alias gl='git log --oneline'
alias gs='git status'
alias gsv='git status -v'

# Kubernetes
alias k='kubectl'
alias ka='kubectl apply -f'
alias kc='kubectl config use-context'
alias kd='kubectl describe'
alias kcv='kubectl config view --minify'
alias kns='kubectl config set-context --current --namespace'
alias kg='kubectl get'
alias kl='kubectl logs -f'