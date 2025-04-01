

#Comando para importar dados das operadoras cadastradas
COPY operadoras (
    registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro,
    numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax,
    endereco_eletronico, representante, cargo_representante, regiao_comercializacao, data_registro_ans
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER
ENCODING 'UTF8'
NULL 'NULL';



#====================================================================================================================================================================


#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/1T2023.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;


#====================================================================================================================================================================


#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/2t2023.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;



#====================================================================================================================================================================




#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/3T2023.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;





#====================================================================================================================================================================




#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/4T2023.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;






#====================================================================================================================================================================


#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/1T2024.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;





#====================================================================================================================================================================


#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/2T2024.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;






#====================================================================================================================================================================



#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/3T2024.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;







#====================================================================================================================================================================



#Comando para importar dados dos demonstrativos contábeis
COPY demonstrativos_contabeis (
    data, 
    registro_ans, 
    cd_conta_contabil, 
    descricao, 
    vl_saldo_inicial, 
    vl_saldo_final
)
FROM '/home/uanicode/Documents/Entrevistas/Intuitive-care/-teste-nivelamento-intuitivecare/database/arquivos/3T2024.csv'
DELIMITER ';' 
CSV HEADER 
ENCODING 'UTF8' 
NULL '' 
QUOTE '"' 
ESCAPE '"' 
;
