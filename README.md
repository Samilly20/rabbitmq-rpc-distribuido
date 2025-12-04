# Sistema Distribuído com RabbitMQ (RPC)

Este projeto implementa um sistema distribuído simples utilizando **RabbitMQ com RPC** em Python, baseado no Tutorial 6 do RabbitMQ.  
O projeto inclui os seguintes componentes:

- ✔ Três **serviços remotos distintos**, executando em processos separados:  
  - `service_soma.py` – serviço para somar valores  
  - `service_media.py` – serviço para calcular média  
  - `service_busca.py` – serviço de consulta simulada  
- ✔ Um **cliente interativo**, onde o usuário escolhe qual serviço deseja chamar.

---

## 📦 Estrutura do Projeto



rabbitmq-rpc-distribuido/
│
├── Client/
│ └── rpc_client.py
│
├── Services/
│ ├── service_soma.py
│ ├── service_media.py
│ ├── service_busca.py
│
├── Common/
│ └── rpc_utils.py
│
├── requirements.txt
└── README.md




---

## Dependências Necessárias

Instale as dependências do projeto:

```bash
pip install -r requirements.txt

```

Pacotes utilizados:
- pika==1.3.2 — biblioteca responsável por permitir a comunicação RPC entre cliente e servidores usando RabbitMQ.

Pré-requisitos:
- RabbitMQ instalado e rodando
- Erlang instalado


3.RabbitMQ rodando:
```bash
rabbitmq-service start
```
# Como Executar (Passo a Passo)

Cada serviço precisa estar rodando em um terminal separado.
1. Rodar o serviço de SOMA
python Services/service_soma.py
2. Rodar o serviço de MÉDIA
python Services/service_media.py
3. Rodar o serviço de BUSCA
python Services/service_busca.py

Rodar o Cliente
Em outro terminal:
python Client/rpc_client.py

Fluxo de Funcionamento
1.O cliente pergunta ao usuário qual serviço deseja chamar

2.O cliente envia uma requisição para o servidor principal RPC

3.O servidor identifica o serviço correto

4.Encaminha a requisição para o serviço correspondente (soma, média ou busca)

5.O serviço processa

6.Retorna a resposta ao cliente via fila reply_to

7.O cliente exibe o resultado

Isso demonstra:
✔️ comunicação assíncrona
✔️ request/response
✔️ distribuição entre serviços diferentes

4. **Exemplos de uso**  


```
bash
# Soma
Escolha: 1
Valor 1: 10
Valor 2: 20
Resultado: 30

# Média
Escolha: 2
Valor 1: 8
Valor 2: 6
Resultado: 7.0

# Busca
Escolha: 3
ID para buscar: 4
Resultado: Carlos


## Autor
Samilly Sousa agora esta melhor?
