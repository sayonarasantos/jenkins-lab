# jenkins_lab
## 1 Descrição
- **Jenkins** é um software de automação, que viabiliza a integração contínua e a entrega contínua (CI/CD) de projetos
- Versão da imagem utilizada neste projeto: [2.235.4](https://hub.docker.com/layers/jenkins/jenkins/2.235.4/images/sha256-63af286d97cd125b7735e6dae7cb504956facf3be91c0d332f724ea528a74121?context=explore)
---

## 2 Instalação
Na instalação por docker-compose, suba o container da aplicação Jenkins:
```console
cd jenkins_lab/dockerJenkins
docker-compose up -d
```
Verifique se o procedimento ocorreu corretamente:
```console
docker ps
```
> Saída:
>
> CONTAINER ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COMMAND&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CREATED&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STATUS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PORTS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAMES
> 
> ****** &nbsp;&nbsp;&nbsp;&nbsp;jenkins/jenkins:2.235.4&nbsp;&nbsp;&nbsp;&nbsp;"/sbin/tini -- /usr/…"&nbsp;&nbsp;&nbsp;&nbsp;3 hours ago&nbsp;&nbsp;&nbsp;&nbsp;Up 3 hours&nbsp;&nbsp;&nbsp;&nbsp;0.0.0.0:8080->8080/tcp, 50000/tcp&nbsp;&nbsp;&nbsp;&nbsp;jenkins_s
> 
Extraia a senha para acessar a interface web:
```console
cat jenkins_home/secrets/initialAdminPassword  
```
E acesse a interface pelo endereço http://localhost:8080/

Ao se conectar ao Jenkins, registre um novo usuário e instale os plugis sugeridos.
*Imagem*
---

## 3 Configurações
### 3.1 Configurar acesso a um nó via SSH
#### 3.1.1 Adicionar credencial SSH para acessar o nó
Adicionar chave privada SSH que tem acesso ao nó...

#### 3.1.2 Adicionar o novo nó
Configurar nome, host, chave...

#### 3.1.3 Iniciar acesso ao nó
- Conectar-se ao Nó
Clicar em "Launch Agent"
*Imagem*
- Habilitar como confiável a identidade do host
Clicar em "Trust SSH host key">"Yes"
*Imagem*
- Verificar se o processo ocorreu corretamente
Verificar log
- Disconectar
*Imagem*
---

## 4 Alguns testes
### 4.1 Executa comandos Shell em um nó
#### 4.1.1 Descrição

_(Freesytle project - Shel script - SSH)_

Depois de realizar o tópico 3.1, você pode criar um projeto que execute uma sequência de comando em Shell em um nó.

#### 4.1.2 Passos
1. Na página inicial do Jenkins, clique em "New item".
2. Na ṕágina de criação em será aberta automaticamente, dê um nome ao projeto e escolha o tipo "Freestyle project" e clique em "OK" no canto inferior da página.
3. Na página de configuração em será aberta automaticamente, faça a seguinte configuração:
- General
    - Selecione "Restrict where this project can be run"
    - Logo abaixo, em "Label Expression", procure pelo nome do nó e o selecione
- Source Code Management:
    - Selecione "None"
- Build:
    - Adicione um passo, clicando em "Add step build"
    - Clique em "Execute Shell"
    - Cole o seguinte código:
        ```shell
        pwd
        cd ~
        pwd
        echo "Hello World"
        ```
4. Na página do projeto, clique em "Build Now"
5. Na mesma página, na seção "Build History", clique no build criado "#1"
6. Por fim. na página do build, clique em "Console Output" e verifique se os comando em shell executaram corretamente.
*Imagem*


### 4.2 Executar trabalhos depois de um push
#### 4.2.1 Descrição
_(Freesytle project - Shel script - Python - GitHub - SSH)_

Automatizar a realização de tarefas em um nó depois que ocorre um push em um projeto no GitHub.

#### 4.2.2 Passos
##### 4.2.2.1 Na máquina do nó
1. Acesse o nó, clone o projeto do GitHub e escolho o branch que deseja utilizar
```console
git clone https://github.com/your_user/jenkins_lab.git
git checkout master
```
2. Fique com a conexão aberta para verificar se a execução automática, feita pelo Jenkins, ocorreu corretamente.

##### 4.2.2.2 Na interface do Jenkins
1. Na página inicial do Jenkins, clique em "New item".
2. Na ṕágina de criação em será aberta automaticamente, dê um nome ao projeto e escolha o tipo "Freestyle project" e clique em "OK" no canto inferior da página.
3. Na página de configuração em será aberta automaticamente, faça a seguinte configuração:
- General
    - Selecione "Restrict where this project can be run"
    - Logo abaixo, em "Label Expression", procure pelo nome do nó e o selecione
- Source Code Management:
    - Selecione "Git"
        - Repositories: https://github.com/your_user/jenkins_lab.git
        - Credentials: Adicione as credenciais que tem acesso ao GitHub. No meu caso, adicionei um token (ver [Com criar token no GitHub](https://))
        - Branch Specifier: */master
---

## Referências
- Como instalar o Jenkins no Ubuntu 20.04. Disponível em: https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-20-04-pt
- How to Connect to Remote SSH Agents?. Disponível em: https://support.cloudbees.com/hc/en-us/articles/222978868-How-to-Connect-to-Remote-SSH-Agents-
- Host Key Verification for SSH Agents. Disponível em: https://support.cloudbees.com/hc/en-us/articles/115000073552-Host-Key-Verification-for-SSH-Agents
- How To Set Up Continuous Integration Pipelines in Jenkins on Ubuntu 16.04. Disponível em: https://www.digitalocean.com/community/tutorials/how-to-set-up-continuous-integration-pipelines-in-jenkins-on-ubuntu-16-04#create-a-personal-access-token-in-github
- GitHub Permissions and API token Scopes for Jenkins. Disponível em: https://support.cloudbees.com/hc/en-us/articles/234710368-GitHub-Permissions-and-API-token-Scopes-for-Jenkins