# SQL More Queries Project

This project covers various SQL queries and concepts such as user creation, privilege management, primary keys, foreign keys, and working with multiple tables using joins and subqueries. The tasks will be executed on a MySQL server.

## Project Structure

- **0-privileges.sql**: Lists all privileges for `user_0d_1` and `user_0d_2` on the MySQL server.
- **1-create_user.sql**: Creates the MySQL user `user_0d_1` with all privileges on the server.
- **2-create_read_user.sql**: Creates the database `hbtn_0d_2` and the user `user_0d_2` with only SELECT privileges.
- **3-force_name.sql**: Creates the `force_name` table with a `name` column that can't be null.
- **4-never_empty.sql**: Creates the `id_not_null` table where the `id` column has a default value of 1.
- **5-unique_id.sql**: Creates the `unique_id` table with a unique constraint on the `id` column.
- **6-states.sql**: Creates the `hbtn_0d_usa` database and the `states` table with a primary key.
- **7-cities.sql**: Creates the `cities` table with a foreign key reference to the `states` table.

## How to Run the SQL Scripts

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/SQL_more_queries.git
   cd SQL_more_queries
