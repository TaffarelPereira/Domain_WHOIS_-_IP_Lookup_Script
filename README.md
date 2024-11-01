# Domain WHOIS & IP Lookup Script

Este repositório contém um script em Python que realiza consultas de IP e WHOIS a partir de um domínio. A ferramenta utiliza o serviço DNS do Google para resolver o domínio e a biblioteca `IPWhois` para coletar informações detalhadas de WHOIS, oferecendo dados como o bloco de rede, o número de sistema autônomo (ASN) e outras informações pertinentes.

## Funcionalidades

### 🔹 Resolução de IP via Domínio
   - O script recebe um domínio como entrada e utiliza a API do Google DNS para resolver e obter o IP associado.
   
### 🔹 Consulta WHOIS
   - Com o IP em mãos, o script faz uma consulta WHOIS, coletando dados sobre a rede a qual pertence, ASN, bloco de IPs (CIDR) e identificadores de rede.
   - Útil para identificar a origem e o proprietário do IP, facilitando análises de rede e segurança cibernética.

### 🔹 Exibição de Informações Formatadas
   - Os dados são exibidos de forma organizada no terminal, apresentando:
     - **Netblock (CIDR)**: bloco de endereços IP ao qual pertence o domínio.
     - **Inetnum (Identificador de Rede)**: identificador da rede no banco de dados WHOIS.
     - **Aut-num (ASN)**: número do sistema autônomo ao qual o IP está associado.

## Exemplo de Uso

### 1. Configuração Inicial
   - Clone este repositório para o seu ambiente local.
   - Instale as dependências com o comando abaixo:
     ```bash
     pip install requests ipwhois
     ```

### 2. Execução do Script
   - Execute o script e insira um domínio quando solicitado:
     ```bash
     python domain_lookup.py
     ```
   - Exemplo de entrada:
     ```
     Digite o domínio: exemplo.com
     ```
   - O script exibirá o IP correspondente e as informações WHOIS, se disponíveis.

### Exemplo de Saída
```plaintext
IP do domínio exemplo.com: xx.xxx.xxx.xx

Informações WHOIS:
Netblock: xx.xxx.xxx.x/24
Inetnum: NET-xx-xxx-xxx-x-x
Aut-num: ASxxxxx
```

## Implementação

### Estrutura do Código

- **Função `get_ip(domain)`**: Faz a resolução de IP utilizando a API do Google DNS e retorna o endereço IP.
- **Função `get_whois_info(ip)`**: Utiliza a biblioteca `IPWhois` para buscar e retornar informações WHOIS relacionadas ao IP fornecido.
- **Função `display_info(whois_info)`**: Formata e exibe as informações WHOIS no terminal.
- **Função `main()`**: Executa o fluxo do programa, coordenando as etapas de input, resolução de IP, consulta WHOIS e exibição dos dados.

### Dependências

- **Python 3.x**: Linguagem de programação.
- **Bibliotecas**:
  - `requests`: Para realizar a consulta à API DNS do Google.
  - `ipwhois`: Para consultar dados WHOIS a partir de um endereço IP.

## Observações

- A API DNS do Google permite resolver domínios com facilidade, mas, dependendo da configuração de rede, pode haver restrições de acesso.
- As consultas WHOIS são realizadas de forma RDAP, garantindo maior integridade e padronização nos dados, mas a disponibilidade dos dados pode variar dependendo da política da RIR.

## Aplicações

Esta ferramenta é útil para:
- **Análises de Segurança**: Investigações e análises de domínios suspeitos, ajudando a mapear redes e verificar a integridade e origem de IPs.
- **Auditoria de Redes**: Auxilia em auditorias de segurança, onde o mapeamento de endereços IP e informações de rede são fundamentais.
- **Educação e Aprendizado**: Boa opção para profissionais e estudantes em cibersegurança para entender melhor a estrutura e informações disponibilizadas em consultas de WHOIS.

## Licença

Este projeto é distribuído sob a licença MIT. 

