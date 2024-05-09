Iniciar o projeto Django

```
python -m venv venv
. venv/bin/activate
python -m pip install pip setuptools wheel --upgrade
pip install django
django-admin startproject project .
pip install django-stubs
pip install mypy
pip install flake8

```

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```