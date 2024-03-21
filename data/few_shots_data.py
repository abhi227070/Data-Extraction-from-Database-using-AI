few_shots = [
            {
                'Question': 'What is the total profit we can earn by selling all products excluding the discounts?',
                'SQLQuery':'SELECT SUM(price*stock_quantity) FROM t_shirts',
                'SQLResult':'Result of the SQL query',
                'Answer':'85513',
            },
            {
                'Question': 'How many quantity of peter england products are there?',
                'SQLQuery':"SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Peter England'",
                'SQLResult':'Result of the SQL query',
                'Answer':'874',
            },
            {
                'Question': 'How many number of nike products are there?',
                'SQLQuery':"SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike'",
                'SQLResult':'Result of the SQL query',
                'Answer':'517',
            },
            {
                'Question': 'How many number of nike products are there?',
                'SQLQuery':"SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Nike'",
                'SQLResult':'Result of the SQL query',
                'Answer':'517',
            },
            {
                'Question': 'How many number of peter england products are there?',
                'SQLQuery':"SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Peter England'",
                'SQLResult':'Result of the SQL query',
                'Answer':'874',
            },
            {
                'Question': 'How many number of peter england products are there?',
                'SQLQuery':"SELECT SUM(stock_quantity) FROM t_shirts WHERE brand = 'Peter England'",
                'SQLResult':'Result of the SQL query',
                'Answer':'874',
            },
            {
                'Question': 'How many discount is there for the Nike products?',
                'SQLQuery':"select distinct(pct_discount) from discounts d join t_shirts t on d.discount_id = t.discount_id where brand = 'Nike' ",
                'SQLResult':'Result of the SQL query',
                'Answer':'15',
            },
            {
                'Question': 'How many only extra small size products are present in the inventory?',
                'SQLQuery':"SELECT sum(stock_quantity) FROM t_shirts WHERE size = 'XS'; ",
                'SQLResult':'Result of the SQL query',
                'Answer':'425',
            },
            {
                'Question': 'what is the discount id for the brand NIKE?',
                'SQLQuery':"SELECT DISTINCT(`discount_id`) FROM `t_shirts` WHERE `brand` = 'Nike'; ",
                'SQLResult':'Result of the SQL query',
                'Answer':'3',
            }
            
            
        ]