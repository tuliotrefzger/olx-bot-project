# OLX Webscrapper

## Instalação:

Crie uma conta na OLX para poder usar essa automação.

Antes de rodar o GUI você deverá instalar os seguintes programas:
- Git ([aqui](https://git-scm.com/downloads))
- Python V3.10.11 ([aqui](https://www.python.org/downloads/release/python-31011/))

Na tela de instalação selecione a opção "Add python.exe to PATH" e depois instale o programa:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/ea8cf1be-2523-4acf-bf5a-1d95d6707813)

Abra uma janela do powershell e digite `cd .\Desktop`.

Em seguida clone o repositório do projeto digitando `git clone https://github.com/tuliotrefzger/olx-bot-project.git`, conforme imagem:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/583a8c6a-e2ef-49d6-a873-df7c002dc50f)

Entre no repositório recém criado usando `cd .\olx-bot-project`.

Crie o ambiente virtual com o comando `python -m venv project-venv`.

Ative o ambiente virtual com o comando `.\project-venv\Scripts\activate.ps1` (Válido somente para windows powershell, para outro shell ver [documentação](https://dev.to/shriekdj/how-to-create-and-activate-the-virtual-environment-for-python3-project-3g4l)
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/32baa51a-a171-40cc-af2e-b49cb921ed62)

Instale os pacotes necessários utilizando `pip install -r requirements.txt`.

Cole o arquivo **credentials.json** na mesma pasta em que foi clonado o repositório ("\Desktop\olx-bot-project" se você tiver seguido o que fiz nesse passo-a-passo).


## Utilização:

Vá até a pasta onde foi clonado o diretório: `cd .\Desktop\olx-bot-project\`.

Ative o ambiente virtual: `.\project-venv\Scripts\activate.ps1`

Execute o GUI: `python .\gui.py`. Uma janela como essa deverá aparecer:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/fa5c1681-8db9-48a0-b595-4c56d369ce56)

Selecione o modelo, marca, etc e escreva uma mensagem a ser enviada aos vendedores e clique em **Buscar**. O scrapping começará.

Logo de cara você será redirecionado para a página de login:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/2f310143-f1f7-4566-9bf0-64c8be5add2c)

Você terá 2 minutos para fazer o login. Após fornecer seu email, selecione a opção **E-mail** e forneça à OLX o código que eles te enviaram por email. Aguarde até que esses dois minutos acabem e a busca inicie automaticamente.

