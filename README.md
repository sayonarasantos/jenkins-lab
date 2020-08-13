# jenkins_lab
## Descrição
- Jenkins é um software de automação, que viabiliza a integração contínua e a entrega contínua (CI/CD) de projetos
- Versão da imagem: 2.235.4
- Link da imagem no DockerHub: https://hub.docker.com/layers/jenkins/jenkins/2.235.4/images/sha256-63af286d97cd125b7735e6dae7cb504956facf3be91c0d332f724ea528a74121?context=explore

## Instalação
Na instalação por docker-compose, suba o container da aplicação Jenkins:
```
cd dockerJenkins
docker-compose up -d
```
Verifique se o procedimento ocorreu corretamente:
```
docker             ps
```
> Saida:
>
> CONTAINER ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;IMAGE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COMMAND&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CREATED&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;STATUS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PORTS&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NAMES
> 
> ****** &nbsp;&nbsp;&nbsp;&nbsp;jenkins/jenkins:2.235.4&nbsp;&nbsp;&nbsp;&nbsp;"/sbin/tini -- /usr/…"&nbsp;&nbsp;&nbsp;&nbsp;3 hours ago&nbsp;&nbsp;&nbsp;&nbsp;Up 3 hours&nbsp;&nbsp;&nbsp;&nbsp;0.0.0.0:8080->8080/tcp, 50000/tcp&nbsp;&nbsp;&nbsp;&nbsp;jenkins_s
> 

Extraia a senha para acessar a interface web:
```
cat jenkins_home/secrets/initialAdminPassword  
```
Ao se conectar na interface web, registre um novo usuário e instale os plugis sugeridos.
** Imagem **

## Alguns testes
### 1 Push in GitHub --> Run in Node
**Descrição**

(Freesytle project - Shel script - Push in GitHub - Run in Node)

Automatizar a realização de tarefas em um nó depois que ocorre um push em um projeto no GitHub

#### 1.1 Adicionar credencial para acessar o nó
Adicionar chave privada SSH que te acesso ao nó

#### 1.2 Adicionar novo nó
- configurar nome, host, chave...

### Iniciar acesso ao nó
- Conectar-se ao Nó
Clicar em "Launch Agent"
** Imagem **
- Habilitar como confiável a identidade do host
Clicar em "Trust SSH host key">"Yes"
** Imagem **
- Verificar se o processo ocorreu corretamente
Verificar log
- Disconectar
** Imagem **

## Referências
- Como instalar o Jenkins no Ubuntu 20.04. Disponível em: https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-ubuntu-20-04-pt
- How to Connect to Remote SSH Agents?. Disponível em: https://support.cloudbees.com/hc/en-us/articles/222978868-How-to-Connect-to-Remote-SSH-Agents-
- Host Key Verification for SSH Agents. Disponível em: https://support.cloudbees.com/hc/en-us/articles/115000073552-Host-Key-Verification-for-SSH-Agents