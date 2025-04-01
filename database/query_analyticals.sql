SELECT 
    d.registro_ans, 
    o.nome_fantasia, 
    SUM(CASE 
            WHEN d.data >= (CURRENT_DATE - INTERVAL '3 meses') THEN 
                COALESCE(d.vl_saldo_final, 0) - COALESCE(d.vl_saldo_inicial, 0) 
            ELSE 0 
        END) AS despesas_trimestre,
    SUM(CASE 
            WHEN d.data >= (CURRENT_DATE - INTERVAL '1 ano') THEN 
                COALESCE(d.vl_saldo_final, 0) - COALESCE(d.vl_saldo_inicial, 0) 
            ELSE 0 
        END) AS despesas_ano
FROM demonstrativos_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE d.descricao ILIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
GROUP BY d.registro_ans, o.nome_fantasia
ORDER BY despesas_trimestre DESC, despesas_ano DESC
LIMIT 10;
