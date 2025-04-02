Teste de Transformação de Dados
Objetivo: Extrair dados do PDF, transformar para CSV, compactar e processar abreviações.

Passos Realizados:

Extração de Dados do PDF: O código lê todas as páginas do Anexo I, extraindo as tabelas de dados.

Transformação em CSV: Após a extração, os dados são organizados em uma tabela CSV.

Compactação: O arquivo CSV gerado é compactado em um arquivo ZIP com o nome Teste_{seu_nome}.zip.

Substituição de Abreviações: As colunas "OD" e "AMB" foram processadas para substituir abreviações pelas descrições completas, conforme o rodapé do PDF.

Tecnologias Utilizadas:

Python (Bibliotecas: PyPDF2, csv, zipfile).

Como Rodar o Código:

Execute o script main.py dentro do diretorio transformacao para extrair, transformar e compactar os dados.

O arquivo final Teste_Ernesto_Orlando_Uanicela.zip será gerado na pasta de saída.

Resultados Esperados: O arquivo CSV será gerado com os dados corretamente estruturados e compactados.

