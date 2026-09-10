## 1. Conferir a instalação do Python
Abra o CMD e execute:

python
Pressione Enter e verifique a versão do Python instalada. Para sair do interpretador Python, execute:

exit()
Para esta atividade, utilize uma versão do Python compatível com a versão do Django adotada no ambiente da disciplina.

Consulte as versões suportadas pelo Django: Django — Supported Versions

## 2. Instalar o virtualenv
O virtualenv permite criar ambientes virtuais isolados para projetos Python.

Execute no CMD:

pip install virtualenv
Caso o comando pip não seja reconhecido, verifique se o pip está disponível por meio do Python:

python -m pip --version
Se o comando funcionar, instale o virtualenv utilizando:

python -m pip install virtualenv
Material de apoio: Python Academy — Python e virtualenv

## 3. Criar a pasta do projeto
Crie uma pasta para o projeto de teste:

mkdir helloworld_raiz
Entre na pasta:

cd helloworld_raiz
## 4. Criar o ambiente virtual
Dentro da pasta helloworld_raiz, crie o ambiente virtual:

py -m venv .venv
Será criada uma pasta chamada .venv, que conterá o ambiente virtual do projeto.

## 5. Ativar o ambiente virtual
No CMD, execute:

.venv\Scripts\activate
Quando o ambiente estiver ativo, você perceberá que (.venv) aparecerá no início da linha de comando.

(.venv) C:\Users\1017591\helloworld_raiz>
Isso indica que o ambiente virtual está ativo.

## 6. Desativar o ambiente virtual
Para sair do ambiente virtual, execute:

deactivate
Para continuar a atividade, caso tenha desativado o ambiente, ative-o novamente:

.venv\Scripts\activate

## 7. Instalar o Django
Com o ambiente virtual ativado, instale o Django:

pip install django
Caso o comando pip não seja reconhecido:

python -m pip install django
Verifique a versão instalada:

django-admin --version

## 8. Conhecer os comandos do Django
Para visualizar os comandos disponíveis no django-admin:

django-admin
Observe especialmente os comandos:

startproject — criar um projeto;
startapp — criar uma aplicação;
runserver — executar o servidor de desenvolvimento.

## 9. Criar o projeto Django
Ainda dentro da pasta helloworld_raiz, execute:

django-admin startproject helloworld
Será criada a estrutura inicial do projeto:

helloworld_raiz/
└── helloworld/
    ├── manage.py
    └── helloworld/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py

## 10. Executar o servidor de desenvolvimento
Entre na pasta do projeto, onde está localizado o arquivo manage.py:

cd helloworld
Execute o servidor:

py manage.py runserver
Se tudo estiver correto, será apresentada uma mensagem semelhante a:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

Django version 6.1, using settings 'helloworld.settings'
Starting WSGI development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
A mensagem sobre unapplied migrations pode aparecer neste momento. Ela não impede o teste inicial do servidor e será trabalhada posteriormente na disciplina.

Acessar a aplicação
Abra o navegador e acesse:

http://localhost:8000
Se a página inicial do Django for apresentada, o servidor está funcionando corretamente.

Para interromper o servidor, pressione: CTRL + BREAK.

## 11. Criar o primeiro app
Com o servidor interrompido e estando na pasta que contém o arquivo manage.py, execute:

python manage.py startapp website
Será criada a aplicação website:

helloworld/
├── manage.py
├── helloworld/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── website/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py

## 12. Checklist
Antes de finalizar, verifique se você realizou todas as etapas:

☐ Conferiu a versão do Python;
☐ Criou a pasta helloworld_raiz;
☐ Criou o ambiente virtual .venv;
☐ Ativou o ambiente virtual;
☐ Instalou o Django;
☐ Conferiu a versão do Django;
☐ Criou o projeto helloworld;
☐ Executou o servidor Django;
☐ Acessou http://localhost:8000;
☐ Criou o app website;
☐ Identificou a estrutura do projeto e do app.
