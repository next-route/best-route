# 🚚[A Melhor Rota]

Para solucionar um problema que determina a melhor rota de um caminhão para carga e descarga de minério em uma mina aberta realizada através de uma malha de estradas localizadas dentro da mina, é necessário implementar um serviço que calcule o melhor trajeto que um caminhão precisará seguir para chegar ao seu destino.

## 🎯[Objetivos]

Implementar uma API que fornece operações necessárias para:

- Cadastrar/Atualizar localização e status do caminhão.
- Listar todos os caminhões com suas informações (localização e status).
- Retornar a melhor rota para o destino final (escavadeira ou área de descarga) considerando a localização e status do caminhão.
- Caso o caminhão esteja CHEIO(true), a melhor rota deve ser para a área de descarga mais próxima. Caso o caminhão esteja VAZIO(false), a melhor rota deve ser para a escavadeira mais próxima.

---

## 🗺️[Mina considerada no desafio]

- Segmentos de estradas e direções permitidas para o tráfego de caminhões
- Pontos de localização
- 3 escavadeiras
- 3 áreas de descarga

  [OBS]: Os caminhões e suas localizações devem ser cadastrados/atualizados dinamicamente via API.

---

![mapa_grapho](https://user-images.githubusercontent.com/79414170/139161335-3ab53649-9d75-47dd-8ec9-30599712a37b.png)

## 🧬[Requisitos]

Necessário ter instalado os seguintes aplicativos:

- Python 3.8.10
- MySQL 8.0
- MySQL Workbench 8.0
- Postman (ou qualquer outra ferramente para testar a API)

---

## 🔧[Instalação]

Para executar o código, deverá ser realizado alguns procedimentos de instalação e configuração do ambiente conforme orientações a seguir:

1. Python3:

- Para instalar o Python, você precisa baixar o instalador. Acesse o site oficial [neste link](https://www.python.org/downloads/), escolha o seu Sistema Operacional e execute o download da versão utilizada neste projeto (3.8.10).

- Para verificar se a instalação do Python foi bem-sucedida, abra o terminal do seu sistema operacional e digite o seguinte comando:

  ```
  python --version
  ```

- Este comando retornará a versão do python que está instalada em sua máquina:

  ```
  Python 3.8.10
  ```

2. Dependências:

- Para realizar a instalação do Flask, execute o comando:

  ```
  pip install Flask
  ```

  - Após isso, ainda será necessário a instalação da extensão SQLAlchemy do Flask, basta executar o seguinte comando:
    ```
    pip install -U Flask-SQLAlchemy
    ```
  - O Flask agora está instalado juntamente com sua extensão. Pode-se verificar a versão instalada executando o comando:
    ```
    flask --version
    ```
  - Este comando retornará a versão instalada, algo similar a:
    ```
    Flask 2.0.2
    ```
  - Com o Flask instalado, você pode seguir para o [Guia de início rápido](https://flask.palletsprojects.com/en/2.0.x/quickstart/) ou caso prefira, para a [Documentação geral](https://flask.palletsprojects.com/en/2.0.x/) a fim de executar a API.

- Próximo passo é instalar o MySQL Connector através do comando:

  ```
  pip install mysql-connector-python
  ```

  - Após execução deste comando, deverá ser exibido no terminal uma mensagem de Instalação completa com sucesso.

- Seguiremos então para a instalação do NetworkX, biblioteca dedicada a grafos. Esse processo poderá levar alguns minutos a mais que os anteriores. Para prosseguir, execute o comando:
  ```
  pip install networkx
  ```
  - Concluído a instalação do NetworkX, você já poderá acessar o [Tutorial](https://networkx.org/documentation/stable/tutorial.html) para trabalhar com o mesmo.
- Por fim, iremos instalar o pacote MatplotLib, executando o comando a seguir no Windows:
  ```
  python -m pip install -U matplotlib
  ```
  Caso esteja utilizando outro sistema operacional, você poderá recorrer ao tutorial de instalação para [Outros Sistemas Operacionais](https://matplotlib.org/stable/users/installing.html#) no site oficial.

---

## :hammer_and_wrench: [Como testar no seu computador]

Antes de realizar o teste, é necessário criar a tabela `truck` no MySQL. Abra o Workbench e rode o seguinte script a fim de criar o schema e a tabela do projeto:

```
CREATE DATABASE `melhor_rota` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
CREATE TABLE `truck` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `destination` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
```

Para testar o funcionamento da API, utilizamos o Postman. No [site oficial](https://www.postman.com/downloads/) a aplicação pode ser instalada de acordo com o sistema operacional utilizado, ou a versão Web pode ser usada como alternativa.
Para utilizar o Postman é preciso primeiramente executar o comando `python .\app.py` no terminal e como resposta será retornado algo semelhante a:

```
* Serving Flask app 'app' (lazy loading)
* Enviroment: production
    Use a production WSGI server instead
* Debug mode: off
* Running on http://127.0.0.1:5000/
```

Copie a url juntamente com a porta e cole no Postman, como mostrado na imagem abaixo:

![url postman](https://user-images.githubusercontent.com/79414170/139086976-46af510b-cbba-4242-9382-1efa37fc03f7.JPG)

Cada método possui um path correspondente que deverá vir após o `/`, vejamos os exemplos:

### **Exemplo POST**

Para cadastrar um novo caminhão, a opção POST deve ser selecionada, justamente com a URL abaixo. Os dados do caminhão devem ser informados no `Body`, onde a opção `raw` deve ser escolhida, e o formato do texto deve ser modificado para `JSON`.

```
http://127.0.0.1:5000/truck
```

![post](https://user-images.githubusercontent.com/79414170/139087765-92c052c9-dc87-4a24-93a4-3cb3344d9699.JPG)

### **Exemplo GET**

O método GET é apenas para consulta, portanto nada será inserido no Body.

```
http://127.0.0.1:5000/trucks (retorna todos os caminhões cadastrados)

http://127.0.0.1:5000/truck/1 (retorna o caminhão especificado pelo seu id na url)
```

![get](https://user-images.githubusercontent.com/79414170/139159978-ac08dd78-faac-49a5-8ab6-143c3aec5b54.JPG)

### **Exemplo GET melhor rota**

Por meio da url path/id, podemos selecionar um caminhão por meio de seu id na url, e será retornada a melhor rota a ser seguida conforme a localização previamente informada.

```
http://127.0.0.1:5000/path/8
```

![path](https://user-images.githubusercontent.com/79414170/139160177-e5b66814-470a-429e-a5d9-1c0ec2002878.JPG)

### **Exemplo PUT**

Assim como o POST, o método PUT necessita que dados sejam informados no `Body` de forma a atualizar as informações de um caminhão específico selecionado pelo seu id.

```
http://127.0.0.1:5000/truck/8
```

![put](https://user-images.githubusercontent.com/79414170/139160428-a5753307-7fe2-4268-aeea-da5ce98bac40.JPG)

### **Exemplo DELETE**

Neste método apenas o id do caminhão que será excluído deve ser informado na url.

```
http://127.0.0.1:5000/truck/8
```

![delete](https://user-images.githubusercontent.com/79414170/139160564-bf1334cb-30a5-481b-bc52-e20a8c1ddbe0.JPG)

---

## :pencil2: [Autores]

- [Ana Carla Vasconcelos](https://github.com/anacarlavgs)
- [André Barros](https://github.com/Andre1312)
- [Jéssica Nogueira](https://github.com/JessNogui)
- [Marina Gouveia](https://github.com/Marina-Gouveia)
- [Tavares Neto](https://github.com/Tavares-NT)

---

## :compass: [Mentores]

- [Ana Catarina Pereira](https://github.com/anacgfp)
- [Michael Bittencourt](https://github.com/MichaelBittencourt)

---

## :balance_scale: [Licença]

Este projeto está sob a [licença MIT](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
