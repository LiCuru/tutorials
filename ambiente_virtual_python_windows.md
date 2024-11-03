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

Vai aparecer:

![Screenshot 2024-11-03 164509](https://github.com/user-attachments/assets/56a81792-124c-46c2-96a6-86fed4f808a2)

Não se esqueça de executar como administrador:
![Screenshot 2024-11-03 175243](https://github.com/user-attachments/assets/66e1b913-7779-4c3b-a092-fcaa8f5e04f6)





Uma vez no prompt de comando, digite `wmic os get osarchitecture`. Ele vai devolver qual é a arquitetura da sua máquina como na figura abaixo:

![Screenshot 2024-11-03 164558](https://github.com/user-attachments/assets/0a2ed3e4-34d2-4748-8382-c491dd634266)




Sabendo a arquitetura da sua máquina, vá em downloads para Windows no site oficial do python (neste link: https://www.python.org/downloads/windows/), em "*Stable Releases*" (versões estáveis, que já passaram da "fase de teste", por assim dizer, e não tem muitos bugs), e escolha o instalador do Windows (*Windows installer*) para o python que <ins>**corresponda com a arquitetura da sua máquina**</ins>:

 ![Screenshot 2024-11-03 165114](https://github.com/user-attachments/assets/ff4fb9c5-d90c-4dde-ac4c-72c612b421cb)




Agora que fez o download, simplesmente prossiga com a instalação clicando em "Install Now" (O meu diz "64-bit" mas o seu pode diferente, dependendo da arquitetura):
 
![Screenshot 2024-11-03 172148](https://github.com/user-attachments/assets/1a5361d0-aa21-407c-8ad7-37dd8201eda1)
