-- Active: 1743445982447@@localhost@5432@intuitive

#Criando a tabela de operadoras
CREATE TABLE operadoras (
    id_operadora SERIAL PRIMARY KEY,
    registro_ans VARCHAR(500) NOT NULL UNIQUE,
    cnpj VARCHAR(17) NULL  UNIQUE,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),      
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_comercializacao VARCHAR(255),
    data_registro_ans DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



#Criando a tabela de demonstrativos contábeis
CREATE TABLE demonstrativos_contabeis (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(10) NOT NULL,
    cd_conta_contabil VARCHAR(20) NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    vl_saldo_inicial DECIMAL(18,2) NOT NULL,
    vl_saldo_final DECIMAL(18,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_operadora FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans) ON DELETE CASCADE
);


