# Data_Pirates_challenge
O objetivo desse programa é coletar dados do site dos Correios e salvar como .json.

> Windowns >=7 <br>
> Python versão >=3.7 <br>
> Não Foi testado em Linux <br>

<img src="https://sn3301files.storage.live.com/y4mfbpTHhFWCBkoxP01hhTo5Ui5ffRnSwb5h3pCrv3FognnqmNmm83EM9Y44qvv_xZyzsGXOJFsYdjBKeMG6FOLIziGNdorjgArp3pwOi2zjb2Dcp3ywfTIDblibPMVqg-VoT7eOElTRzHJ6uhm5j7khhnNYSvLOgfCvCBgkvFloCpJhwe6wjI8MzidllzWzb6O?width=256&height=256&cropmode=none" width="256" height="256" />

## Instalando ambiente
Para executar a aplicação é necessário configurar um ambiente com todas bibliotecas dependentes.

1. Primeiro abra um prompt de comando python/anconda e instale o virtualenv:

```bash
 pip install virtualenv
```
2. Crie uma pasta para instalar o ambiente.

```bash
 python -m virtualenv <nome_ambiente>
```
3. Navegue pelo terminal até a pasta "Script" dentro do ambiente criado.

```bash
 cd ./nome_ambiente/Scripts
```
4. Ative o ambiente.
```bash
 activate.bat
```

5. Volte a raiz do projeto.
```bash
 cd ../../
```

6. Instale as bibliotecas com base no arquivo "requirements.txt".
```bash
 pip install -r requirements.txt
```

## Rodando o spider

```shell
scrapy crawl Correios -O Correios.json
```

# Melhorias

* Testes
* Arrumar o Docker

# Referências

* https://scrapy.org/
* https://www.youtube.com/watch?v=s4jtkzHhLzY
* https://www.youtube.com/watch?v=wyE4oDxScfE
* https://www2.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm
* https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md
* https://shinesolutions.com/2018/09/13/running-a-web-crawler-in-a-docker-container/


