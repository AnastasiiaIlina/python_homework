# 1. Show the category_name and description from the categories table sorted by category_name.
SELECT categories.category_name, categories.description FROM categories
order BY category_name ASC

# 2. Show the product_name and unit_price from the products table sorted by unit_price in descending order.
SELECT products.product_name, products.unit_price FROM products
order BY unit_price desc 

# 3. Show all the contact_name, address, city of all customers which are not from 'Germany', 'Mexico', 'Spain'
SELECT customers.contact_name, customers.address, customers.city, customers.country
FROM customers WHERE NOT country IN ('Mexico', 'Germany', 'Spain')
# 4. Show all the contact_name, city, and country of customers from countries other than 'USA', 'Canada', and 'Mexico'.
SELECT customers.contact_name, customers.city, customers.country
FROM customers WHERE NOT country IN ('USA', 'Canada', 'Mexico')
# 5. Show order_date, shipped_date, customer_id, Freight of all orders placed between '2019-05-01' and '2019-06-30'.
select orders.order_date, orders.shipped_date, orders.customer_id, orders.freight 
FROM orders 
WHERE order_date between '2018-05-01' and '2018-06-30'
# 6. Show order_date, shipped_date, customer_id, Freight of all orders placed on 2018 Feb 26
SELECT orders.order_date, orders.shipped_date, orders.customer_id, orders.freight 
FROM orders 
WHERE order_date == '2018-02-19'
# 4. Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders shipped later than the required date
select orders.employee_id, orders.order_id, orders.customer_id, orders.required_date, orders.shipped_date
from orders
WHERE shipped_date > required_date
# 5. Show the company_name, contact_name, fax number of all customers that has a fax number. 
select customers.company_name, customers.contact_name, customers.fax
FROM customers 
WHERE fax IS NOT NULL
# 6. Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders where shipped_date is earlier than required_date.
SELECT orders.employee_id, orders.order_id, orders.customer_id, orders.required_date, orders.shipped_date 
from orders 
where shipped_date < required_date
# 7. Show the supplier_name, contact_name, phone number of all suppliers that have a phone number.
select suppliers.contact_name, suppliers.contact_name, suppliers.phone
from suppliers 
WHERE phone IS NOT NULL
# 8. Show the first_name, last_name, hire_date of employees hired before '2022-01-01'.
SELECT employees.first_name, employees.last_name, employees.hire_date
FROM employees
WHERE hire_date < '2022-01-01'
# 9. Show the product_name, quantity_per_unit, units_in_stock of all products that have less than 10 units in stock.
SELECT products.product_name, products.quantity_per_unit, products.units_in_stock
FROM products
WHERE units_in_stock < 10

# 10. Show the company_name, contact_name, contact_title of customers that have a contact_title.
SELECT customers.company_name, customers.contact_name, customers.contact_title
FROM customers 
WHERE contact_title IS NOT NULL
# 11. Show the order_id, ship_country, ship_region of orders where ship_country is not 'USA' and ship_region is not empty.
SELECT orders.order_id, orders.ship_country, orders.ship_region
FROM orders 
where ship_country is not 'USA' and ship_region is not NULL

# 12. Show the employee_id, last_name, first_name of the employees who have the title 'Sales Representative'.
SELECT employees.employee_id, employees.last_name, employees.first_name
FROM employees
WHERE title == 'Sales Representative'
# 13. List the products that were ordered more than once in a single order. Display the product name, order ID, and quantity ordered.

SELECT
    products.product_name,
    order_details.order_id,
    order_details.quantity
FROM
    order_details
Inner JOIN
    products ON order_details.product_id = products.product_id
where order_details.quantity > 1


# 14. Retrieve the top 10 most ordered categories of products. Display the category name and the total quantity of products ordered within each category.


SELECT categories.category_name, products.product_name, order_details.quantity,
SUM(order_details.quantity) as avg_price 
FROM categories
Inner JOIN products on products.category_id = categories.category_id
inner join order_details on products.product_id == order_details.product_id
group by categories.category_name
ORDER BY COUNT(order_details.quantity) DESC limit 10


# 15. Find the employees who have never handled any orders. Display their names and hire dates.


select employees.first_name, employees.hire_date, orders.order_id
from employees
left join orders on employees.employee_id = orders.employee_id
where orders.order_id is Null


# 16. Retrieve a list of orders with the customer's company name and the employee's first and last names. Include only orders placed after January 1, 2010

select customers.company_name, employees.first_name, employees.last_name, orders.order_date
from orders
inner join employees on employees.employee_id = orders.employee_id
Inner join customers on customers.customer_id = orders.customer_id
where orders.order_date > '2010-01-10'


# 17. Retrieve a list of customers and suppliers who are located in the same city. Display the company name and city for both customers and suppliers. If a city doesn't have any customers or suppliers, show "No Data" for the missing side.
select suppliers.city as supplier_city, customers.city as customer_city from customers
inner join orders on customers.customer_id = orders.customer_id
inner join order_details on order_details.order_id = orders.order_id
Inner join products on products.product_id = order_details.product_id
inner join suppliers on products.supplier_id = suppliers.supplier_id 
where supplier_city = customers.city


# 18. Generate a detailed report that showcases product details, product categories, and customer orders. Display the product name, category name, customer's company name, and the order date for all orders containing products from a specific category.

# 19. Create a report that combines supplier information, product details, and employee territories. Display the supplier's company name, product name, and the territory description for employees responsible for orders containing these products.