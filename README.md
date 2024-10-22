# Vacinação


| Rotas | Pts. |
|---|---|
| Utilizar **SQLAlchemy**, **Dataclass**, **Blueprint**, **Migrations** e **Padrão Flask Factory** corretamente.
| [POST] **/vaccinations**. Ao fazer requisição nessa rota passando os dados corretos deve retornar o status code **201** (**CREATED**) e fazer a inserção dos dados normalizados no banco de dados. 
| [POST] **/vaccination**. Ao fazer requisição nessa rota passando uma **string** com mais de 11 characters para a chave 'cpf', deve retornar o status code **400** (**BAD REQUEST**) com uma mensagem de erro que faça sentido. 
| [POST] **/vaccination**. Ao fazer a requisição nessa rota com o valor de qualquer uma das chaves sendo diferente de **string**, deve retornar o status code **400** (**BAD REQUEST**)) com uma mensagem de erro que faça sentido. 
| [POST] **/vaccination**. Ao fazer a requisição nessa rota faltando qualquer uma das chaves (**cpf**, **name**, **health_unit_name** e **vaccine_name**), deve retornar o status code **400** (**BAD REQUEST**) com uma mensagem de erro que faça sentido. 
| [POST] **/vaccination**. Ao fazer a requisição nessa rota passando um **CPF** que já exista no banco de dados, deve retornar o status code **409** (**CONFLICT**) com uma mensagem de erro que faça sentido. 
| [POST] **/vaccinations**. Ao fazer requisição nessa rota passando uma chave a mais, deve retornar o status code **201** (**CREATED**) e fazer a criação corretamente ignorando a chave passada. 
| [GET] **/vaccinations**. Deve retornar todas as vacinas registradas no banco de dados, status code **200** (**OK**)
| Arquivos **requirements.txt**, **.env**, **.env.example**, **.gitignore** (**venv** e .**env**) | 1 |# flask-api-vacinacao
