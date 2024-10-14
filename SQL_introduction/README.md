# SQL Introduction Project

This project contains a series of SQL scripts that demonstrate basic database operations using MySQL 8.0. These scripts include tasks such as listing databases, creating and deleting databases, creating tables, inserting data, querying data, and performing basic SQL operations like counting and averaging.

## Project Structure

- **0-list_databases.sql**: Lists all databases on the MySQL server.
- **1-create_database_if_missing.sql**: Creates the database `hbtn_0c_0` if it doesn't already exist.
- **2-remove_database.sql**: Deletes the database `hbtn_0c_0` if it exists.
- **3-list_tables.sql**: Lists all tables from a specified database.
- **4-first_table.sql**: Creates a table called `first_table` with two columns: `id` (integer) and `name` (varchar).
- **5-full_table.sql**: Displays the full description of the table `first_table` using `SHOW CREATE TABLE`.
- **6-list_values.sql**: Lists all rows of the table `first_table`.
- **7-insert_value.sql**: Inserts a new row with `id = 89` and `name = 'Best School'` into the table `first_table`.
- **8-count_89.sql**: Counts the number of records in `first_table` where the `id = 89`.
- **9-full_creation.sql**: Creates a new table `second_table` with three fields (`id`, `name`, and `score`), and inserts multiple records.
- **10-top_score.sql**: Lists all records from `second_table`, ordered by the `score` field in descending order (highest score first).
- **11-best_score.sql**: Lists all records from `second_table` where the `score` is greater than or equal to 10.
- **12-no_cheating.sql**: Updates the score of the row where the `name` is "Bob" to 10, without using `id`.
- **13-change_class.sql**: Deletes all rows from `second_table` where the score is less than or equal to 5.
- **14-average.sql**: Computes the average score from all records in `second_table`.
- **15-groups.sql**: Lists the number of records that have the same `score` in `second_table`, grouped by the `score`.
- **16-no_link.sql**: Lists all records from `second_table` where the `name` field is not empty, ordered by `score` in descending order.

## Detailed File Descriptions

### 0. List Databases
- **File**: `0-list_databases.sql`
- **Description**: This script lists all databases present on the MySQL server using the `SHOW DATABASES` command.

### 1. Create Database If Missing
- **File**: `1-create_database_if_missing.sql`
- **Description**: This script creates a new database called `hbtn_0c_0` only if it doesn't already exist, using the `CREATE DATABASE IF NOT EXISTS` command.

### 2. Remove Database
- **File**: `2-remove_database.sql`
- **Description**: This script deletes the database `hbtn_0c_0` if it exists, using the `DROP DATABASE IF EXISTS` command.

### 3. List Tables in Database
- **File**: `3-list_tables.sql`
- **Description**: This script lists all tables from a specified database using the `SHOW TABLES` command.

### 4. Create First Table
- **File**: `4-first_table.sql`
- **Description**: This script creates a table named `first_table` with two fields: `id` (INT) and `name` (VARCHAR(256)) using the `CREATE TABLE` command.

### 5. Full Table Description
- **File**: `5-full_table.sql`
- **Description**: This script shows the full structure of `first_table` using the `SHOW CREATE TABLE` command, which describes how the table is structured.

### 6. List Values in Table
- **File**: `6-list_values.sql`
- **Description**: This script lists all records in the `first_table` by running the `SELECT * FROM first_table` query.

### 7. Insert Value into Table
- **File**: `7-insert_value.sql`
- **Description**: This script inserts a new row into the `first_table` with `id = 89` and `name = 'Best School'` using the `INSERT INTO` command.

### 8. Count Records with ID 89
- **File**: `8-count_89.sql`
- **Description**: This script counts how many rows in `first_table` have `id = 89` using the `SELECT COUNT(*)` query.

### 9. Full Table Creation with Multiple Rows
- **File**: `9-full_creation.sql`
- **Description**: This script creates a new table called `second_table` with fields `id`, `name`, and `score`. It also inserts multiple rows of data into the table.

### 10. List by Top Score
- **File**: `10-top_score.sql`
- **Description**: This script lists all records from `second_table`, ordered by `score` in descending order using `ORDER BY score DESC`.

### 11. Select Records with Best Score
- **File**: `11-best_score.sql`
- **Description**: This script lists all records where the `score >= 10` from `second_table`, ordered by score.

### 12. Update Bob’s Score
- **File**: `12-no_cheating.sql`
- **Description**: This script updates the `score` of the row where `name = 'Bob'` to 10 without using the `id` field.

### 13. Remove Low Scores
- **File**: `13-change_class.sql`
- **Description**: This script deletes all records from `second_table` where the `score <= 5`.

### 14. Calculate Average Score
- **File**: `14-average.sql`
- **Description**: This script calculates the average score of all rows in `second_table`.

### 15. Count Records by Score
- **File**: `15-groups.sql`
- **Description**: This script counts the number of records with the same `score` in `second_table` and groups the results by score using the `GROUP BY` clause.

### 16. List Records with Valid Names
- **File**: `16-no_link.sql`
- **Description**: This script lists all records in `second_table` where the `name` is not empty or `NULL`, ordered by `score` in descending order.

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/SQL_introduction.git
   cd SQL_introduction
