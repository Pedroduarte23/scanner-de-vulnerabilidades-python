# 🔍 Scanner de Vulnerabilidades em Python

Projeto desenvolvido para análise de portas TCP, identificação de serviços e detecção básica de riscos em servidores.

---

## 🚀 Funcionalidades

* Scan de portas TCP
* Identificação de portas **ABERTAS**, **FECHADAS** e **FILTRADAS**
* Banner Grabbing (identificação de serviços)
* Suporte a HTTP e HTTPS
* Multithreading para melhor performance
* Detecção de possíveis riscos (FTP, Telnet, SMTP)
* Geração de relatório automático

---

## 🧠 Tecnologias utilizadas

* Python
* Socket
* Threading

---
## 🧠 Como funciona

O scanner realiza conexões TCP utilizando a biblioteca socket para verificar o estado das portas.

- Porta ABERTA: conexão aceita
- Porta FECHADA: conexão recusada
- Porta FILTRADA: ausência de resposta (possível firewall)

O uso de multithreading permite escanear múltiplas portas simultaneamente, aumentando a performance.
---
## 📊 Exemplo de execução

```
Digite o site ou IP: scanme.nmap.org

[ABERTA] Porta 22 (SSH)
[ABERTA] Porta 80 (HTTP)
[FECHADA] Porta 21 (FTP)
[FILTRADA] Porta 25 (SMTP)
```

---

## ⚠️ Análise de Segurança

O scanner identifica serviços potencialmente inseguros, como:

* FTP (sem criptografia)
* Telnet (protocolo inseguro)
* SMTP exposto

---

## 📁 Estrutura do Projeto

```
scanner.py
README.md
```

---

## ▶️ Como executar

1. Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/scanner-de-vulnerabilidades-python.git
```

2. Acesse a pasta:

```
cd scanner-de-vulnerabilidades-python
```

3. Execute o script:

```
python scanner.py
```

---

## ⚠️ Aviso

Este projeto foi desenvolvido para fins educacionais.
Utilize apenas em ambientes autorizados.

---

## 💼 Autor

Pedro Henrique Duarte de Oliveira
Estudante de Defesa Cibernética | Segurança da Informação
