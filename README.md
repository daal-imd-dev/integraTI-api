 # IntegraTI

Api para a plataforma IntegraTI.É a API que irá fornecer os dados para o sistema IntegraTI.

Veja nossa [wiki](https://github.com/daal-imd/integraTI-api/wiki). E se você pretende ajudar no desenvolvimento, leia e siga nosso [arquivo de contribuição](./CONTRIBUTING.md).

# Instruções

> **Atenção***: as configurações de desenvolvimento são instáveis e se atualizando constantemente, não sendo adequadas para produção

## Configurando ambiente de desenvolvimento

- Instale os seguintes programas e certifique-se de que as **versões** usadas estão sempre corretas e os serviços estão **ativos**:
    - [Docker](https://docs.docker.com/install/) 
    - [Docker Compose](https://docs.docker.com/compose/install/)
- Prepare o ambiente de desenvolvimento:
    - Construa as imagens dando ```make up``` (atalho para o comando ```docker-compose build```)
    - Copie o arquivo ```env.example``` com o novo nome ```.env```

## Rodando o servidor

Considerando que todo o ambiente foi corretamente instalado e configurado:

- Inicie o servidor com ```make up``` (atalho para o comando ```docker-compose up -d```)
    - Por padrão, o servidor irá rodar no ip ```0.0.0.0:8000```, que significa que está aberto para toda sua rede interna
- Não se esqueça de que essa aplicação é apenas o lado do servidor e precisa da instalação do [repositório web do IntegraTI](https://github.com/daal-imd/integraTI-Web) para se "materializar" para um usuário comum.
