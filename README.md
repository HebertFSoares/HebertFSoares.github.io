# Friendly_Host-DJANGO

O Sistema de Adoção de Estudantes é uma plataforma desenvolvida para conectar estudantes e anfitriões, permitindo que estudantes fiquem mais próximos de uma instituição. O sistema permite o cadastro de estudantes, instituições e anfitriões, bem como o registro de adoção de estudantes pelos anfitriões.

## Funcionalidades
- Cadastro de estudantes, instituições e anfitriões
- Registro de adoção de estudantes pelos anfitriões
- Listagem de estudantes disponíveis para adoção
- Listagem de estudantes adotados
- Pesquisa de estudantes por instituição ou nome
- Perfil do usuário logado
- Gerenciamento de permissões de acesso

## Tecnologias Utilizadas
- Python
- Django
- Sqlite
- HTML/CSS/JavaScript
- Bootstrap

## Requisitos
### Para executar o projeto em sua máquina local, você precisará ter o Python 3 instalado. Além disso, recomendamos utilizar um ambiente virtual para instalar as dependências necessárias.

## Instalação

### Clone este repositório em sua máquina local.

- Crie um ambiente virtual:
```
python3 -m venv myenv
```
- Ative o ambiente virtual:
```
source myenv/bin/activate
```
- Instale as dependências:
```
pip install -r requirements.txt
```
- Execute as migrações do banco de dados:
```
python manage.py migrate
```
- Crie um superusuário:
```
python manage.py createsuperuser
```
- Execute o servidor:
```
python manage.py runserver
```

## Contribuição
Este projeto é de código aberto e contribuições são bem-vindas. Se você quiser contribuir com o projeto, por favor, abra uma issue ou um pull request.

## Autor
- Hebert Ferreira Soares - hebertsoaresof@gmail.com

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
