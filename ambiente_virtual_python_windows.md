## Como instalar o Jupyter Lab e configurar um ambiente virtual do python no Windows

As vezes é necessário configurar um ambiente virtual onde as bibliotecas estejam em versões específicas. E se você conduz mais de um projeto em sua máquina, pode ser necessário configurar um ambiente para cada projeto.

### Por que é necessário saber isso?
Para instalar certas versões de algumas bibliotecas, muitas vezes não é o suficiente apenas instalar a versão requisitada delas. Muitas vezes também é necessário alterar a versão do python na máquina. Isso é porque algumas versões antigas de algumas bibliotecas, ou suas dependências, podem não ter suporte na versão atual do python. Então acaba sendo necessário trocar a versão do python para uma versão mais antiga, de quando aquela dependência, ou aquela biblioteca mesmo, ainda tinha suporte, ainda rodava, no python.

### Esse tutorial explica como que:
- 1 - instala a versão mais recente do python no Windows
- 2 - instala o jupyter lab no Windows
- 3 - instala o pyenv-win
- 4 - altera a versão do python para versões mais antigas com o pyenv-win
- 5 - cria um ambiente virtual no windows com uma versão escolhida do python
- 6 - instala as bibliotecas requeridas no ambiente virtual criado
- 7 - cria um kernel do ipython dentro do ambiente virtual criado para ser usado no jupyter lab
- 8 - adiciona esse kernel no leque de opções de kernel do jupyter lab


### 1 - instalando a versão mais recente do python no Windows

Primeiro vá no site oficial do python, na parte de downloads, e selecione a versão:
 - para windows
 - correta para a arquitetura da sua máquina

Para saber a arquitetura da sua máquina, vá no cmd (prompt de comando) e digite "wmic os get osarchitecture". Ele vai devolver qual é a arquitetura da sua máquina como na figura abaixo:

![Screenshot 2024-11-03 164558](https://github.com/user-attachments/assets/0a2ed3e4-34d2-4748-8382-c491dd634266)


Se você não sabe onde encontrar o prompt de comando, procure por "cmd" no menu do windows:

![Screenshot 2024-11-03 164910](https://github.com/user-attachments/assets/f3549ee6-d73c-4a1e-850e-c3eb991ea150)

Depois de saber a arquitetura da sua máquina, vá no site oficial do python, em "Stable Releases" (versões estáveis), e escolha o **instalador do windows** para o python que corresponda com a sua arquitetura:

 ![Screenshot 2024-11-03 165114](https://github.com/user-attachments/assets/ff4fb9c5-d90c-4dde-ac4c-72c612b421cb)
