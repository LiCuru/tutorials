## Como instalar o Jupyter Lab e configurar um ambiente virtual do python no Windows

As vezes é necessário configurar um ambiente virtual onde as bibliotecas estejam em versões específicas. E se você conduz mais de um projeto em sua máquina, pode ser necessário configurar um ambiente para cada projeto.

### Por que é necessário saber isso?
Para instalar certas versões de algumas bibliotecas, muitas vezes não é o suficiente apenas instalar a versão requisitada delas. Por ser também necessário alterar a versão do python na máquina. Isso é porque algumas versões antigas de algumas bibliotecas, ou suas dependências, podem não ter suporte na versão atual do python. Então acaba sendo necessário trocar a versão do python para uma versão mais antiga, de quando aquela dependência, ou aquela biblioteca mesmo, ainda tinha suporte, ainda rodava, no python.

No caso desse tutorial, ele foi escrito porque para o eixo de IA e Ciência de Dados do AcademiaBB, um processo de certificação interna de TI do BB, são necessárias as instalações das seguintes bibliotecasdo python nas seguintes versões:



### Passos desse tutorial:
- 1 - instalar a versão mais recente do python no Windows
- 2 - instalar o jupyter lab no Windows
- 3 - instalar o pyenv-win
- 4 - alterar a versão do python para versões mais antigas com o pyenv-win
- 5 - criar um ambiente virtual no windows com uma versão escolhida do python
- 6 - instalar as bibliotecas requeridas no ambiente virtual criado
- 7 - criar um kernel do ipython dentro do ambiente virtual
- 8 - adicionar esse kernel no leque de opções de kernel do jupyter lab


## 1 - instalar a versão mais recente do python no Windows

Primeiro vá no site oficial do python, na parte de downloads, e selecione a versão:
 - para windows
 - correta para a **arquitetura da sua máquina**

Para saber a arquitetura da sua máquina, vá no cmd (*prompt de comando*). Se você não sabe como encontrar o prompt de comando, procure por "cmd" no menu do windows:

![Screenshot 2024-11-03 164910](https://github.com/user-attachments/assets/f3549ee6-d73c-4a1e-850e-c3eb991ea150)

Ele vai aparecer:

![Screenshot 2024-11-03 164509](https://github.com/user-attachments/assets/043723bc-6038-4bf0-9f18-fb801d4f368c)


Toda vez que for utilizar o prompt de comando, execute como administrador. Sem a autorização de administrador, o prompt de comando não vai autorizar todos os comandos necessários nesse tutorial:

![Screenshot 2024-11-03 175243](https://github.com/user-attachments/assets/66e1b913-7779-4c3b-a092-fcaa8f5e04f6)





Uma vez no prompt de comando, digite `wmic os get osarchitecture`. Ele vai devolver qual é a arquitetura da sua máquina como na figura abaixo:

![Screenshot 2024-11-03 164558](https://github.com/user-attachments/assets/0a2ed3e4-34d2-4748-8382-c491dd634266)




Sabendo a arquitetura da sua máquina, vá em downloads para Windows no site oficial do python (neste link: https://www.python.org/downloads/windows/), em "*Stable Releases*" (versões estáveis, que já passaram da "fase de teste", por assim dizer, e não tem muitos bugs), e escolha o instalador do Windows (*Windows installer*) para o python que <ins>**corresponda com a arquitetura da sua máquina**</ins>:

 ![Screenshot 2024-11-03 165114](https://github.com/user-attachments/assets/ff4fb9c5-d90c-4dde-ac4c-72c612b421cb)




Agora que fez o download, execute o instalador do python para windows como administrador:

![Screenshot (18)](https://github.com/user-attachments/assets/ec85e178-69a6-42fd-bf4f-512f33c2d959)

Antes de prosseguir com a instalação, autorize os privilégios de administrador e autorize que o python.exe seja adicionado ao PATH:

![Screenshot (19)](https://github.com/user-attachments/assets/8f34d149-612b-4198-881c-8fc7fd59240d)

clicando em "Install Now" (O meu diz "64-bit" mas o seu pode diferente, dependendo da arquitetura).:

## 2 - instalar o jupyter lab no Windows

É possível instalar o jupyter lab apenas procurando por ele na ferramenta de busca do próprio Windows:

![Screenshot 2024-11-03 163415](https://github.com/user-attachments/assets/38951be6-a3da-441e-a828-3f24ae08aa15)

Ele vai aparecer e você pode pedir pra baixar:

![Screenshot 2024-11-03 163441](https://github.com/user-attachments/assets/8157c60e-6746-44a9-bfa4-c8ff7dc84668)


### não funcionou, o que eu faço? =(
Contudo, se isso não funcionar, tem outra opção, que é via prompt de comando (não se esqueça de <ins>**executar o prompt de comando como administrador**</ins>, conforme mostrei no passo 1 deste tutorial). Pelo prompt de comando é possível instalar da forma que é recomendado pelo site oficial do Jupyter (em: https://jupyter.org/install). Nesse site é possível ver que ele recomenda que se use o gerenciador de pacotes pip. Não vá direto igual ele diz digitando `pip install`! primeiro vamos dar upgrade no gerenciador de pacotes pip pra que ele esteja atualizado:

`python -m ensurepip --upgrade`

Agora sim, com o gerenciador de pacotes pip atualizado, podemos seguir conforme recomenda o site do Jupyter Lab:

`pip install jupyterlab`

para rodar o Jupyter Lab é só digitar:

`jupyter lab`

Isso vai fazer o prompt de comando apresentar vários dados e ficar indisponível para novos comandos. Isso quer dizer que está funcionando. Repare no que ele diz:

![Screenshot 2024-11-03 165520](https://github.com/user-attachments/assets/928251cb-4977-4873-b504-a958ca521122)

"*Para acessar o servidor, abra esse arquivo em um navegador*"

"*Ou copie e cole um desses URLs*"

Eu prefiro copiar e colar um desses links no navegador do que procurar pelo arquivo. Mas isso é totalmente opcional.

O que acontece é que o Jupyter cria um servidor local, e bota pra funcionar quando ele executa. É um servidor dentro do seu próprio computador. Esse servidor é acessível através desses links que ele apresenta no prompt de comando quando você executa o Jupyter. Acessando o link no seu navegador, você acessa o servidor local com o Jupyter Lab rodando. Ou seja, copiando e colando o link apresentado no seu prompt de comando no seu navegador, você acessa o Jupyter Lab.

### as pastas para trabalhar estão esquisitas =(

só que se você rodar esse comando direto no prompt de comando assim que ele executa, você vai abrir o jupyter lab no endereço das pastas do sistema do windows:

![Screenshot (2)](https://github.com/user-attachments/assets/fdd072d5-7d50-4bc8-a41c-48b7d39113e4)


E, no fim, os arquivos que vão aparecer no Jupyter pra você "trabalhar" vão simplesmete ser arquivos do sistema do windows:

![Screenshot 2024-11-03 181618](https://github.com/user-attachments/assets/fcf14211-79a8-4ee1-9389-580c8c80f06b)


Então é necessário ir no endereço da pasta que você quer disponível nos arquivos do jupyter. Só depois de ir na pasta que você quer, é que então você roda o jupyter lab:

![Screenshot 2024-11-03 181805](https://github.com/user-attachments/assets/1167039e-aeaa-4cb6-9895-7e8e598e6859)


![Screenshot 2024-11-03 181816](https://github.com/user-attachments/assets/1896996a-5799-4cce-a234-3dbbbaba6b85)

### diretório de dados do usuário

Nesse exemplo eu decidi ir para o diretório onde fica os dados de usuário (Downloads, Desktop, Documentos, etc...). Se a gente não souber onde fica esse diretório, a gente fica meio perdido. O endereço desse diretório fica disponível para consulta quando você acessa o prompt de comando executando direto, sem executar como administrador:

![Screenshot 2024-11-03 180647](https://github.com/user-attachments/assets/95b1a2c9-3334-4a89-988a-545cf0a47d72)

### Como eu navego para algum diretório no cmd (prompt de comando)?

O endereço de onde você está no momento é o que aparece antes do sinal de '`>`', e que precede qualquer comando que você venha a executar:

![Screenshot (1)](https://github.com/user-attachments/assets/23b70d5d-d1da-46b7-ae66-b6bcb44d95af)

para voltar para um diretório acima, use o comando:

`cd ..`

para visualizar os diretórios e arquivos dentro do endereço onde você está, use o comando:

`dir`

e para acessar um diretório use o comando:

`cd nome_do_diretorio`

Veja como funciona no exemplo abaixo:

![Screenshot 2024-11-03 183414](https://github.com/user-attachments/assets/3a7485eb-a1c1-4338-91d0-af8c639e380f)


Então é isso. Se você quiser fechar o Jupyter porque ele está acessando uma pasta que não te interessa, digite `Ctrl + C` no prompt de comando onde ele está rodando e apresentando os links para acesso. Vai levar uns segundos, mas ele vai terminar o processo. Em seguida navegue até a pasta que é do seu interesse, e só então execute o `jupyter lab`.

### depois de acessar a pasta que você quer trabalhar:

use o comando:

`jupyter lab`

## 3 - instalar o pyenv-win

Agora que instalamos o jupyter, é necessário configurar um ambiente virtual.

O ambiente é criado pelo python, o que significa que a versão do python utilizada vai ser a versão do python do ambiente virtual. Trocar de versão do python no Windows, e em qualquer sistema operacional, pode ser muito desafiador e desnecessariamente difícil. Para que seja possível poder trocar de versão com facilidade e organização, foi criado o pyenv. Depois de um tempo o pyenv teve sua versão adaptada para o Windows, chamado de pyenv-win.

Esse site (https://realpython.com/intro-to-pyenv/) explica como que faz o manejo das diferentes versões do python com o pyenv. Vale a pena ler.

Para instalar o pyenv-win, acesse prompt de comando como administrador, e execute:

`pip install pyenv-win`

Uma vez instalado, ainda não tem como acessar o pyenv-win através do prompt de comando porque a pasta onde fica o binário do pyenv-win ainda não está na variável path. Então o próximo passo é adicionar a pasta do binário à variável path do Windows. Para adicionar, primeiro é necessário encontrar onde fica a pasta to pyenv-win. Se você repetir o comando: 

`pip install pyenv-win`

Ele vai informar que o pyenv-win já está instalado e onde está instalado. Vá até esse diretório, encontre o diretório do pyenv-win, entre no diretório, e depois vá no bin. A figura abaixo explica melhor:

![Captura de tela 2024-11-03 195413](https://github.com/user-attachments/assets/cff8f471-1d9f-4e59-93f3-1558d25aa3c2)

Depois vá nas variáveis do ambiente do windows, e adicione o endereço copiado à variável PATH conforme as figuras abaixo. O seu computador pode estar um pouco diferente. Se estiver um pouco diferente, não vai estar tão diferente. O importante é adicionar ao PATH:

![Captura de tela 2024-11-03 195927](https://github.com/user-attachments/assets/040727d7-55eb-487c-9809-c3a85a9d7813)

![Captura de tela 2024-11-03 195942](https://github.com/user-attachments/assets/d744a4be-48c0-4890-87a8-fd81d408a9b9)




## 4 - alterar a versão do python para versões mais antigas com o pyenv-win





