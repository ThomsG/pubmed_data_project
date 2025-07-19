/*
    Ventes par meubles et déco réalisés par client et sur la période allant du 1er janvier 2019 au 31 décembre 2019.
    
    P.I : On pourrait aussi utiliser la notion de PIVOT pour avoir les types de produits en tant que colonne, 
    mais le PIVOT a des syntaxes différentes selon le SGBD utilisé. On choisit donc d'utiliser des CASE WHEN plus simples et largement compatibles.
*/

SELECT
    t.client_id,
    SUM(CASE WHEN pn.product_type = 'MEUBLE' THEN t.prod_price * t.prod_qty) AS ventes_meuble,
    SUM(CASE WHEN pn.product_type = 'DECO' THEN t.prod_price * t.prod_qty) AS ventes_deco
FROM
    TRANSACTIONS t
    JOIN PRODUCT_NOMENCLATURE pn
        ON t.prod_id = pn.product_id
WHERE
    pn.product_type IN ('MEUBLE','DECO')
    AND t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY
    t.client_id;