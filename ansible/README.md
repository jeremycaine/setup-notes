# Red Hat Ansible
https://docs.ansible.com/ansible/2.9/installation_guide/intro_installation.html#from-pip

Pre-req of pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user
pip install --upgrade pip
```

Install Ansible
```
pip install --user ansible
```
.zshrc
```
export PATH=$HOME/bin:/usr/local/bin:$HOME/.local/bin:$PATH
```
check anisble working
```
. ~/.zshrc
ansible --version
```

Install in a virtual env
```
python -m virtualenv ansible  # Create a virtualenv if one does not already exist
source ansible/bin/activate   # Activate the virtual environment
pip install ansible
```