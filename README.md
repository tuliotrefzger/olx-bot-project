# OLX Webscrapper

## Instalação:

Crie uma conta na OLX para poder usar essa automação.

Antes de rodar o GUI você deverá instalar os seguintes programas:
- Git ([aqui](https://git-scm.com/downloads))
- Python V3.10.11 ([aqui](https://www.python.org/downloads/release/python-31011/))

Na tela de instalação selecione a opção "Add python.exe to PATH" e depois instale o programa:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/ea8cf1be-2523-4acf-bf5a-1d95d6707813)

Abra uma janela do powershell e digite:
```
cd .\Desktop
```

Em seguida clone o repositório do projeto digitando 
```
git clone https://github.com/tuliotrefzger/olx-bot-project.git
```
, conforme imagem:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/583a8c6a-e2ef-49d6-a873-df7c002dc50f)

Entre no repositório recém criado usando:
```
cd .\olx-bot-project
```

Crie o ambiente virtual com o comando:
```
python -m venv project-venv
```

Ative o ambiente virtual com o comando:
```
.\project-venv\Scripts\activate.ps1
```
(Válido somente para windows powershell, para outro shell ver [documentação](https://dev.to/shriekdj/how-to-create-and-activate-the-virtual-environment-for-python3-project-3g4l)
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/32baa51a-a171-40cc-af2e-b49cb921ed62)

Instale os pacotes necessários utilizando: 

```
pip install altgraph==0.17.4 async-generator==1.10 attrs==22.1.0 beautifulsoup4==4.12.3 black==24.2.0 cachetools==5.3.3 certifi==2022.9.24 cffi==1.16.0 charset-normalizer==2.1.1 click==8.1.7 customtkinter==5.2.2 darkdetect==0.8.0 et-xmlfile==1.1.0 exceptiongroup==1.0.0rc9 google-api-core==2.17.1 google-api-python-client==2.130.0 google-auth==2.28.1 google-auth-httplib2==0.2.0 google-auth-oauthlib==1.2.0 googleapis-common-protos==1.62.0 h11==0.14.0 httplib2==0.22.0 idna==3.4 lxml==5.2.1 MouseInfo==0.1.3 mypy-extensions==1.0.0 numpy==1.26.4 oauthlib==3.2.2 opencv-python==4.9.0.80 openpyxl==3.0.10 outcome==1.2.0 packaging==23.2 pandas==1.5.0 pathspec==0.12.1 pefile==2023.2.7 pillow==10.2.0 platformdirs==4.2.0 protobuf==4.25.3 pyasn1==0.5.1 pyasn1-modules==0.3.0 PyAutoGUI==0.9.54 pycparser==2.21 PyGetWindow==0.0.9 pyinstaller==6.0.0 pyinstaller-hooks-contrib==2023.9 PyMsgBox==1.0.9 pyparsing==3.1.1 PyPDF2==2.11.0 pyperclip==1.8.2 PyRect==0.2.0 PyScreeze==0.1.30 PySimpleGUI==4.60.3 PySocks==1.7.1 python-dateutil==2.8.2 python-dotenv==1.0.0 python3-xlib==0.15 pytweening==1.2.0 pytz==2022.4 pywin32-ctypes==0.2.2 requests==2.28.1 requests-oauthlib==1.3.1 rsa==4.9 selenium==4.9.0 six==1.16.0 sniffio==1.3.0 sortedcontainers==2.4.0 soupsieve==2.5 tk==0.1.0 tomli==2.0.1 trio==0.22.0 trio-websocket==0.9.2 typing_extensions==4.9.0 undetected-chromedriver==3.5.5 uritemplate==4.1.1 urllib3==1.26.12 webdriver-manager==4.0.1 websockets==12.0 wsproto==1.2.0 zenrows==1.3.2
```

Cole o arquivo **credentials.json** na mesma pasta em que foi clonado o repositório ("\Desktop\olx-bot-project" se você tiver seguido o que fiz nesse passo-a-passo).


## Utilização:

Vá até a pasta onde foi clonado o diretório: 
```
cd .\Desktop\olx-bot-project\
```

Ative o ambiente virtual:
```
.\project-venv\Scripts\activate.ps1
```

Execute o GUI:
```
python .\gui.py
```
 Uma janela como essa deverá aparecer:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/fa5c1681-8db9-48a0-b595-4c56d369ce56)

Selecione o modelo, marca, etc e escreva uma mensagem a ser enviada aos vendedores e clique em **Buscar**. O scrapping começará.

Logo de cara você será redirecionado para a página de login:
![image](https://github.com/tuliotrefzger/olx-bot-project/assets/51811381/2f310143-f1f7-4566-9bf0-64c8be5add2c)

Você terá 2 minutos para fazer o login. Após fornecer seu email, selecione a opção **E-mail** e forneça à OLX o código que eles te enviaram por email. Aguarde até que esses dois minutos acabem e a busca inicie automaticamente.

