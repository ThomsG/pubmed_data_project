/*
    CA (= montant total des ventes) jour par jour, du 1er janvier 2019 au 31 décembre 2019. 
    Trié par date.
*/

SELECT
    t.date AS "date",
    SUM(t.prod_price * t.prod_qty) AS ventes
FROM
    TRANSACTIONS t
WHERE
    t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY
    t.date
ORDER BY
    t.date;