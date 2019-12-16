# Arquitetura Definitiva para Projetos Flask

Tutorial em texto em: https://codeshow.com.br/arquitetura-web-python-flask/

Video: https://youtu.be/-qWySnuoaTM
Slides: http://bit.ly/codeshow-003-arquitetura-flask ou [googledrive](https://docs.google.com/presentation/d/e/2PACX-1vTZfj2xF3-Nf4NZO8V4HNr2rQNt0ci2kP19OT3Uhrzljl7MZj5Txl_AVlNt4upnCl3aYEJDAfiELpd7/pub?start=false&loop=false&delayms=15000)

Código parte da apresentação na https://pyjamas.live conference

---

## Clone

```bash
git clone https://github.com/codeshow/003-arquitetura-flask.git
```

## ou faça o download

https://github.com/codeshow/003-arquitetura-flask/archive/new.zip

ou

```bash
wget https://github.com/codeshow/003-arquitetura-flask/archive/new.zip
```

## Ambiente

Python 3.6+
Ative a sua virtualenv

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
pip install -r requirements_test.txt
```

## Testando

```bash
pytest pydaria/tests
```

## Executando

```bash
flask create-db  # rodar uma vez
flask populate-db # rodar uma vez
flask add-user -u admin -p 1234  # adiciona usuario admin
flask run
```

Acesse:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
- API GET:
  - https://localhost:5000/api/v1/product/
  - https://localhost:5000/api/v1/product/1
  - https://localhost:5000/api/v1/product/2
  - https://localhost:5000/api/v1/product/3


## Structure

```bash
.
├── Makefile
├── pydaria  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi  (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   └── webui  (FRONT END)
│   │       ├── __init__.py
│   │       ├── templates
│   │       │   ├── index.html
│   │       │   └── product.html
│   │       └── views.py
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── appearance.py
│   │   ├── auth.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py  (DATABASE MODELS)
│   └── tests  (TESTS)
│       ├── conftest.py
│       ├── __init__.py
│       └── test_api.py
├── README.md
├── requirements_dev.txt
├── requirements_test.txt
├── requirements.txt
└── settings.toml  (SETTINGS)

7 directories, 26 files
```
