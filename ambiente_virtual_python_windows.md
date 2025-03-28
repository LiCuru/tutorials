## Como instalar o Jupyter Lab e configurar um ambiente virtual do python no Windows

Esse tutorial explica como que instala o Jupyter Lab no Windows e como que se configura um ambiente virtual com qualquer versão do python para instalação de bibliotecas nas versões requeridas.

### Por que é necessário saber sobre ambientes virtuais?
As vezes é necessário configurar um ambiente virtual onde as bibliotecas estejam em versões específicas. E se você conduz mais de um projeto em sua máquina, pode ser necessário configurar um ambiente para cada projeto.

Para instalar certas versões de algumas bibliotecas, muitas vezes não é o suficiente apenas instalar a versão requisitada delas. Pode ser também necessário alterar a versão do python. Isso é porque algumas versões antigas de algumas bibliotecas, ou suas dependências, podem não ter suporte na versão atual do python. Então acaba sendo necessário trocar a versão do python para uma versão mais antiga, de quando aquela dependência, ou aquela biblioteca requisitada mesmo, ainda tinha suporte, ainda rodava, naquela versão mais antiga do python.

Esse tutorial também explica como ver quando uma versão de alguma biblioteca não tem suporte na versão atual do python, e como saber qual versão utilizar nesse caso.

No caso desse tutorial, é explicado como configurar um ambiente para o Jupyter Lab com as instalações das seguintes bibliotecasdo python nas seguintes versões:


|Biblioteca|Versão|
|---|---|
|pandas|1.5.2 ou inferior|
|numpy|1.23.5 ou inferior|
|matplotlib|3.5.2 ou inferior|
|imblearn|0.11.0|
|seaborn|0.12.2 ou inferior|
|scikit-learn|1.2.0 ou inferior|


### Passos desse tutorial:
- 1 - instalar a versão mais recente do python no Windows
- 2 - instalar o jupyter lab no Windows
- 3 - entendendo qual versão do python usar e porque
- 4 - instalar o pyenv-win
- 5 - alterar a versão do python para versões mais antigas com o pyenv-win
- 6 - instalar o Microsoft C++ Build Tools
- 7 - criar um ambiente virtual no windows com uma versão escolhida do python
- 8 - instalar as bibliotecas requeridas no ambiente virtual criado
- 9 - criar um kernel do ipython dentro do ambiente virtual
- 10 - adicionar esse kernel ao leque de opções de kernel do jupyter lab


## 1 - instalar a versão mais recente do python no Windows
Primeiro vá no [site oficial do python, na parte de downloads para windows](https://www.python.org/downloads/windows/), e selecione a versão correta para a **arquitetura da sua máquina**

Para saber a arquitetura da sua máquina, vá no cmd (*prompt de comando*). Se você não sabe como encontrar o prompt de comando, procure por "cmd" no menu do windows:

![Screenshot 2024-11-03 164910](https://github.com/user-attachments/assets/f3549ee6-d73c-4a1e-850e-c3eb991ea150)

Ele vai aparecer:

![Screenshot 2024-11-03 164509](https://github.com/user-attachments/assets/043723bc-6038-4bf0-9f18-fb801d4f368c)


### Execute como administrador <a name="execute_administrador" />
Toda vez que for utilizar o prompt de comando, execute como administrador. Sem a autorização de administrador, o prompt de comando não vai autorizar todos os comandos necessários nesse tutorial:

![Screenshot 2024-11-07 193630](https://github.com/user-attachments/assets/9dec437d-3536-4bf9-855a-68223338f3c2)



**Dica importante**: Toda vez que for copiar ou colar qualquer coisa no cmd (prompt de comando) do windows, utilize o botão direito do mouse. O botão direito do mouse é a mesma coisa que CTRL + C ou CTRL + V no cmd do Windows.

Uma vez no prompt de comando, digite `wmic os get osarchitecture`. Ele vai devolver qual é a arquitetura da sua máquina como na figura abaixo (a sua máquina tem uma arquitetura própria, e o resultado pode ser diferente):

![Screenshot 2024-11-07 180616](https://github.com/user-attachments/assets/757f93be-7528-44e6-bd7e-046be037bfcf)

Sabendo a arquitetura **da sua máquina**, vá em downloads para Windows no site oficial do python, em "*Stable Releases*" (versões estáveis, que já passaram da "fase de teste", por assim dizer, e não tem muitos bugs), e escolha o instalador do Windows (*Windows installer*) para o python que corresponda com a arquitetura da sua máquina:

Agora que fez o download, execute o instalador do python para windows como administrador:

![Screenshot (18)](https://github.com/user-attachments/assets/ec85e178-69a6-42fd-bf4f-512f33c2d959)

Antes de prosseguir com a instalação, autorize os privilégios de administrador e autorize que o python.exe seja adicionado ao PATH:

![Screenshot (19)](https://github.com/user-attachments/assets/8f34d149-612b-4198-881c-8fc7fd59240d)

Clique em "Install Now" (O meu diz "64-bit" mas o seu pode diferente, dependendo da sua arquitetura).

Feche o cmd (prompt de comando) e abra novamente (não esqueça de [executar como administrador](#execute_administrador))

## 2 - instalar o jupyter lab no Windows

É possível instalar o jupyter lab apenas procurando por ele na ferramenta de busca do próprio Windows:

![Screenshot 2024-11-03 163415](https://github.com/user-attachments/assets/38951be6-a3da-441e-a828-3f24ae08aa15)

Ele vai aparecer e você pode pedir pra baixar:

![Screenshot 2024-11-03 163441](https://github.com/user-attachments/assets/8157c60e-6746-44a9-bfa4-c8ff7dc84668)


### não funcionou, o que eu faço? =(
Contudo, se isso não funcionar, tem outra opção, que é via prompt de comando (não se esqueça de [<ins>**executar o prompt de comando como administrador**</ins>](#execute_administrador), conforme mostrei no passo 1 deste tutorial). Pelo prompt de comando é possível instalar da forma que é recomendado pelo [site oficial do Jupyter](https://jupyter.org/install). Nesse site é possível ver que ele recomenda que se use o gerenciador de pacotes pip. Não vá direto igual ele diz digitando `pip install`! primeiro vamos dar upgrade no gerenciador de pacotes pip pra que ele esteja atualizado:

`python.exe -m pip install --upgrade pip`

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

### as pastas no Jupyter estão esquisitas =(
Ok, você copiou o link e colou no navegador e o Jupyter funciona. Só que as pastas são totalmente "aleatórias". Isso é porque se você rodar esse comando direto no prompt de comando assim que ele executa, você vai abrir o jupyter lab no endereço das pastas do sistema do windows:

![Screenshot (2)](https://github.com/user-attachments/assets/fdd072d5-7d50-4bc8-a41c-48b7d39113e4)


E, no fim, os arquivos que vão aparecer no Jupyter pra você "trabalhar" vão simplesmente ser arquivos dessa pasta:

![Screenshot 2024-11-03 181618](https://github.com/user-attachments/assets/fcf14211-79a8-4ee1-9389-580c8c80f06b)


Então é necessário ir no endereço da pasta que você quer disponível nos arquivos do jupyter. Só depois de ir na pasta que você quer, é que então você roda o jupyter lab:

![Screenshot 2024-11-03 181805](https://github.com/user-attachments/assets/1167039e-aeaa-4cb6-9895-7e8e598e6859)


![Screenshot 2024-11-03 181816](https://github.com/user-attachments/assets/1896996a-5799-4cce-a234-3dbbbaba6b85)

### Sobre o diretório home, home directory, e como mudar de diretório no cmd
Nesse exemplo eu decidi ir para o diretório home, home directory, onde fica os dados de usuário (Downloads, Desktop, Documentos, etc...). Se a gente não souber onde fica esse diretório, a gente fica meio perdido. O endereço desse diretório é de onde parte o cmd quando você executa sem ser como administrador:

![Screenshot 2024-11-03 180647](https://github.com/user-attachments/assets/95b1a2c9-3334-4a89-988a-545cf0a47d72)

### Como eu navego para algum diretório no cmd (prompt de comando)?

O endereço de onde você está no momento é o que aparece antes do sinal de `>`, e que precede qualquer comando que você venha a executar:

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

### depois de acessar a pasta onde você quer trabalhar:

use o comando:

`jupyter lab`

## 3 - Entendendo qual versão do python usar e porque:
Ao instalar o Jupyter Lab no Windows, ele está pronto para ser usado. Contudo, a versão do python do kernel do ambiente padrão utilizado, chamado de  *"Python 3 (ipykernel)"* . Você encontra ele no canto superior direito, como na figura a seguir (ele está no modo escuro, mas é a mesma coisa que o modo claro):

![Captura de tela 2024-11-06 213004](https://github.com/user-attachments/assets/226ac221-a492-4f40-bddd-43e6551b8eea)

Se você deixar o mouse em cima dele, vai ver que ele tem a opção de trocar de kernel:

![Captura de tela 2024-11-06 213010](https://github.com/user-attachments/assets/e63fa639-f8ac-4439-9dbc-4a0a37b9fe19)

Clicando no Python 3 (ipykernel), você pode escolher qual kernel utilizar. Como o Jupyter Lab acabou de ser instalado e não tem outro kernel instalado, não tem outra opção disponível ainda. A versão do python desse kernel e seu ambiente virtual é a versão do python instalada no seu Windows. Para saber a versão do python utilizada, rode esse código em uma célula do notebook do Jupyter:

`from platform import python_version`

`print(python_version())`

No meu caso, com a última versão instalada no sistema, que veio do primeiro passo desse tutorial, a versão apresentada é a  *3.13.0* . O seu pode ser diferente, dependendo da época em que você siga este tutorial (dependendo de qual python foi instalado no passo 1).

Repare que é mesma versão que ele apresenta se você for ver qual a versão no python no cmd. Digite no cmd:

`python -V`

Desde que o pyenv-win ainda não tenha sido instalado e você não tenha alterado a versão do python global no pyenv-win, a versão do python vai ser a mesma no cmd e no Jupyter usando o kernel  *Python 3 (ipykernel)* .

### Entendendo a incompatibilidade das bibliotecas antigas com versões recentes do python
Vamos tentar instalar as bibliotecas nas versões requeridas:

|Biblioteca|Versão|
|---|---|
|pandas|1.5.2 ou inferior|
|numpy|1.23.5 ou inferior|
|matplotlib|3.5.2 ou inferior|
|imblearn|0.11.0|
|seaborn|0.12.2 ou inferior|
|scikit-learn|1.2.0 ou inferior|

Vamos instalar as bibliotecas com o python na última versão instalada usando o kernel  *"Python 3 (ipykernel)"* . No Jupyter mesmo, dentro da célula.

Toda vez que for instalar bibliotecas escolhendo versões específicas, é melhor instalar todas as bibliotecas do ambiente no mesmo comando pip, porque o pip faz o gerenciamento da compatibilidade entre versões do pandas e numpy, por exemplo. Isso é explicado melhor [nessa questão do fórum do stack overflow](https://stackoverflow.com/questions/78634235/numpy-dtype-size-changed-may-indicate-binary-incompatibility-expected-96-from). Portanto vamos rodar o seguinte código em uma célula do Jupyter com o kernel  *"Python 3 (ipykernel)"* :

`!pip install pandas==1.5.2 numpy==1.23.5 matplotlib==3.5.2 imbalanced-learn==0.11.0 seaborn==0.12.2 scikit-learn==1.2.0`

Repare na mensagem que ele devolve tentando instalar essas bibliotecas com o python versão 3.13.0:

![Captura de tela 2024-11-06 232051](https://github.com/user-attachments/assets/5d15e33f-2122-4043-8926-035c5ec5aadd)


Leia com atenção. Você vai reparar que o pip faz bem a instalação do pandas versão 1.5.2 , e que depois ele parte para a instalação do numpy versão 1.23.5. Aí ele dá erro. Esse o final da mensagem de erro:

![Captura de tela 2024-11-06 232032](https://github.com/user-attachments/assets/99502758-3143-40f4-9a5a-71aae38f6e20)

O problema está nessa dependência do numpy chamada ' *pkgutil.ImpImporter* '.

Se você procurar pelo '*pkgutil.ImpImporter*' na [documentação do python](https://docs.python.org/), vai ver nos resultados da busca que essa classe  *ImpImporter* , do módulo  *pkgutil*  foi removido na versão do python 3.12. Você pode buscar por '*pkgutil.ImpImporter*' na [página que explica o que é novo no python 3.12](https://docs.python.org/3/whatsnew/3.12.html), você vai encontrar:

![Captura de tela 2024-11-08 062029](https://github.com/user-attachments/assets/a74a2831-24e4-4169-a7a7-273a232fb8e1)

Repare que a mensagem de erro quando vai instalar a biblioteca com o python 3.13 é justamente dizendo que '*pkgutil.ImpImporter*' não existe:

*AttributeError: module 'pkgutil' has no attribute 'ImpImporter'. Did you mean: 'zipimporter'?*

E a página contando as atualizações do python 3.12 explica que essa classe foi removida.

Então, usando uma versão anterior à do python 3.12, essa função vai ter suporte no python e as bibliotecas vão funcionar. Eu decidi usar a versão 3.10.5 e deu certo com todas as outras bibliotecas com suas respectivas versões.

Para alterar a versão do python, é necessário usar o pyenv-win.

## 4 - instalar o pyenv-win

Agora que instalamos o jupyter, é necessário criar um ambiente virtual novo, com uma versão diferente do python para que as bibliotecas funcionem nas versões requisitadas. Nesse novo ambiente a gente instala as bibliotecas nas versões requisitadas e também instala o kernel para ser usado no jupyter.

### O ambiente virtual e a versão do python
O ambiente virtual é criado com uma execução de comando do python. Isso que significa que a versão do python utilizada vai ser a versão do python do ambiente virtual. Então é preciso trocar de versão do python para depois executar o comando que cria o ambiente virtual.

### Trocando a versão do python
Trocar de versão do python no Windows, e em qualquer sistema operacioal, pode ser muito desafiador e desnecessariamente difícil. Para que seja possível poder trocar de versão com facilidade e organização, foi criado o pyenv. Depois de um tempo, o pyenv teve sua versão adaptada para o Windows, chamado de pyenv-win.

[O site do Real Python](https://realpython.com/intro-to-pyenv/) explica como que faz o gerenciamento das diferentes versões do python com o pyenv. Vale a pena ler.

### Instalação do pyenv-win
A instalação do pyenv-win pode ser de formas diferentes. Seguindo as instruções no [GitHub do pyenv-win](https://github.com/pyenv-win/pyenv-win/tree/057ba9e97bc5f217ddcffc01768174495c78859a#finish-the-installation) não tem erro. Os passos a seguir são apenas um dos caminhos possíveis das instruções dadas no github do pyenv-win. Escolhi instalar com o pip:

No cmd execute:

`pip install pyenv-win --target %USERPROFILE%\.pyenv`

No **PowerShell**. <ins>Atenção, PowerShell não é cmd</ins>. Também não esqueça, quando for executar o PowerShell, de executar como administrador:

![Screenshot 2024-11-07 193112](https://github.com/user-attachments/assets/89c3570d-e561-4287-851e-31a79802fa82)


No PowerShell execute, para atualizar as variáveis de ambiente:

`[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")`

No **PowerShell** também execute, para que o cmd reconheça o comando pyenv:

`[System.Environment]::SetEnvironmentVariable('path', $HOME + "\.pyenv\pyenv-win\bin;" + $HOME + "\.pyenv\pyenv-win\shims;" + $env:Path,"User")`

Pronto. O pyenv-win está instalado.

## 5 - alterar a versão do python para uma versão mais antiga com o pyenv-win

Feche o cmd, e abra um novo [como administrador](#execute_administrador).
Vá até o diretório home no cmd.

Para instalar uma versão anterior do python (no caso, vou instalar a versão 3.10.5, mas outras versões do python 3.11 também funcionam):

`pyenv install 3.10.5`

Para dar update no shims execute [conforme explicado nesse tópico do stack overflow](https://stackoverflow.com/questions/29753592/pyenv-shim-not-created-when-installing-package-using-setup-py):

`pyenv rehash`

Defina o python global como sendo a versão instalada:

`pyenv global 3.10.5`

Ao testar a versão do python na máquina, você deverá ver a versão instalada:

`python -V`

Ele deverá retornar como mensagem o python na versão instalada, nesse caso é o python 3.10.5

## 6 - instalar o Microsoft C++ Build Tools
Se você não tiver o Microsoft C++ Build Tools instalado, apesar de não aparecer nenhuma mensagem de erro na hora de instalar as bibliotecas nas versões citadas, a biblioteca matplotlib na versão 3.5.2 simplesmente não vai funcionar quando você importar. Ao importar a biblioteca em alguma célula do Jupyter, vai aparecer o seguinte erro:

 *ImportError: DLL load failed while importing _path: The specified module could not be found.* 

Ao procurar a respeito desse erro, é possível ver nesses tópicos do [GitHub](https://github.com/matplotlib/matplotlib/issues/18292#issuecomment-792634734) e no [StackOverflow](https://stackoverflow.com/questions/66919838/matplotlib-wont-run-on-windows-10-dll-fails-to-load) que uma das soluções apontadas para o problema seria fazer um downgrade do matplotlib para a versão 3.3.0 ou 3.3.1

Só que ao tentar fazer a instalação do matplotlib 3.3.1 (depois de desinstalar o matplotlib 3.5.2), ele dá erro na hora do build e recomenda a instalação do Microsoft C++ Build Tools:

![Captura de tela 2024-11-10 155717](https://github.com/user-attachments/assets/ef711e06-d958-4407-b260-f599bb04f44c)

Ou seja, ele não consegue passar da fase do build porque não tem as ferramentas necessárias.

Indo no site recomendado: https://visualstudio.microsoft.com/visual-cpp-build-tools , é possível fazer a instalação. Vou deixar as figuras aqui para ficar mais fácil:

Vá no site e faça o download do instalador:
![Screenshot (6)](https://github.com/user-attachments/assets/21658aca-ed73-4991-a984-494a6c7f9e26)

Não esqueça de rodar o instalador como administrador:
![Screenshot (2)](https://github.com/user-attachments/assets/85778906-f15c-4edb-8f87-e831218ddfad)

Escolha o build tools e faça a instalação:
![Screenshot (4)](https://github.com/user-attachments/assets/f7ebf7ad-430e-4ee4-b3e9-063818def56d)

Com isso é possível fazer a instalação de todas as bibliotecas e o matplotlib vai funcionar ao ser importado.

## 7 - criar um ambiente virtual no windows com uma versão escolhida do python
Conforme explicado na [documentação do python](https://docs.python.org/3/library/venv.html), crie um ambiente no diretório de sua escolha:

`python -m venv \caminho\para\o\ambiente`

O ambiente não deixa de ser também um diretório por si só. No caso, resolvi gravar no diretório Desktop um ambiente chamado 'desafio':

![Captura de tela 2024-11-07 161325](https://github.com/user-attachments/assets/05329e6c-e56c-4e0a-b775-66488b3b906b)

Com isso foi criado um ambiente (e um diretório) chamado 'desafio' com o python versão 3.10.5

![Screenshot 2024-11-07 194638](https://github.com/user-attachments/assets/a898d00c-6534-4888-bf42-0300081ff6f1)


## 8 - instalar as bibliotecas requeridas no ambiente virtual criado
Para acessar no cmd o ambiente, execute:

`C:\> <venv>\Scripts\activate.bat`

O que quer dizer que, no meu caso, seria:

![Captura de tela 2024-11-07 162114](https://github.com/user-attachments/assets/e3927408-f9e3-4131-80b4-8c80cfcb06bd)

Ele sinaliza com o nome do ambiente virtual entre parenteses que está dentro do ambiente. Os comandos dados dentro do ambiente mencionado  *(desafio)* são comandos que ficam contidos dentro do ambiente  *desafio* . Uma vez dentro do ambiente, podemos fazer as instalações das bibliotecas nas versões requeridas. Repare que não precisa do caractere `!` antes do comando de instalação do pip:

`pip install pandas==1.5.2 numpy==1.23.5 matplotlib==3.5.2 imbalanced-learn==0.11.0 seaborn==0.12.2 scikit-learn==1.2.0`

## 9 - criar um kernel do ipython dentro do ambiente virtual
Para criar o kernel, primeiro precisamos instalar o Ipython. É o Ipython que provê a estrutura para que interfaces de usuário gráficas rodem, assim como o shell, e também o kernel para que o python rode no Jupyter acessando as bibliotecas instaladas. Você pode entender melhor sobre o Ipython visitando o [site oficial do Ipython](https://ipython.org/) Para instalar o Ipython, execute:

`pip install ipython`

Uma vez instalado o Ipython, podemos instalar o kernel executando:

`pip install ipykernel`

## 10 - adicionar esse kernel no leque de opções de kernel do jupyter lab
Para finalmente ter o kernel listado no Jupyter. Escolha um nome para o kernel executando:

`ipython kernel install --name "nome_do_kernel" --user`

 No meu caso, chamei o kernel de 'desafio':
 
![Captura de tela 2024-11-07 164623](https://github.com/user-attachments/assets/49ab32cf-ce19-4bca-8efe-523527a5d506)

Para se certificar de que o kernel está listado nos kernels disponíveis no Jupyter execute:

`jupyter kernelspec list`

Ele deverá listar o kernel python3 e o kernel que você acabou de criar. No exemplo do meu computador:

![Captura de tela 2024-11-07 164822](https://github.com/user-attachments/assets/984ebf5c-13e0-4ba8-acf3-7a07858b6b79)

### Fim da instalação do kernel!
Saia de dentro do ambiente com o comando:

`deactivate`

Depois de usar `deactivate`, você vai voltar para o sistema normal, e não vai estar mais dentro do ambiente virtual criado, por isso não vai mais aparecer o nome do ambiente no cmd.

Agora feche o jupyter completamente. Se o Jupyter estiver executando em um cmd, feche esse cmd e a janela do jupyter no navegador.

Inicie novamente o Jupyter (não se esqueça de fazer isso de dentro do diretório home se estiver no cmd) e selecione o kernel no canto superior direito:

![Captura de tela 2024-11-06 213004](https://github.com/user-attachments/assets/ed9ee147-f464-46e7-b206-b6a51f45d17e)

![Captura de tela 2024-11-06 213010](https://github.com/user-attachments/assets/019712ce-4388-468e-8ec4-7e072ea27c92)

Repare que ao clicar para selecionar o kernel, o kernel estará listado =D
No meu caso o nome do kernel que eu criei foi 'desafio', é o que aparece:

![Screenshot 2024-11-07 200415](https://github.com/user-attachments/assets/933daae1-fa9d-4c8d-9092-007801d44c9b)


Fim!

### Aviso importante!
Se você estiver fazendo o academIA e for mandar o notebook para validação, ele vai dar erro com um kernel de nome diferente do kernel padrão. Então, na hora de desenvolver o desafio, desenvolva com o kernel novo, mas na hora de enviar para validação, não pode esquecer de:
 - selecionar o kernel padrão, chamado de "Python 3 (ipykernel)"
 - salvar com o kernel "Python 3 (ipykernel)" padrão selecionado
 - enviar para validação


Com isso, ele vai rodar o notebook no validador com o kernel padrão. Caso contrário, o validador vai devolver a mensagem de erro dizendo no final:  *NoSuchKernel: No such kernel named nome_do_kernel* 

### =)
Aproveite seu novo ambiente de desenvolvimento!



 










