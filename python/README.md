# Python

```
brew install pyenv
```

Add to your ~/.zshrc:
```
eval "$(pyenv init - zsh)"
```

Install versions
```
pyenv install 3.12.3
pyenv install 3.11.9
pyenv install 3.10.14
```

Set a global default:
```
pyenv global 3.11.9
```

Or per-project
```
cd myproject
pyenv local 3.11.9
```