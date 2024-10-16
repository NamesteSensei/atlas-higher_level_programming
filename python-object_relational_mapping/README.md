# Python - Object-Relational Mapping (ORM)

This project demonstrates the use of Python with MySQL databases. It includes a set of scripts to interact with MySQL databases, both using raw SQL queries and SQLAlchemy, an Object-Relational Mapper (ORM). The goal of the project is to become familiar with how to manipulate databases programmatically.

## Learning Objectives

By the end of this project, you will understand:

- How to connect to a MySQL database using Python.
- How to execute SQL queries from Python scripts.
- What Object-Relational Mapping (ORM) means and how to use it.
- How to define Python classes that map to MySQL tables using SQLAlchemy.

## Project Structure

### Files

- `0-select_states.py`: Lists all states from a MySQL database.
- `1-filter_states.py`: Lists states with names starting with `N` from a MySQL database.
- `2-my_filter_states.py`: Filters states by a user-provided input.
- `3-my_safe_filter_states.py`: Safely filters states using MySQL escape parameters (prevents SQL injection).
- `4-cities_by_state.py`: Lists all cities in a specific state from a MySQL database.
- `5-filter_cities.py`: Lists all cities in a user-provided state.
- `6-model_state.py`: Defines a `State` class and connects to the MySQL database using SQLAlchemy.
- `7-model_state_fetch_all.py`: Lists all `State` objects using SQLAlchemy.
- `8-model_state_fetch_first.py`: Prints the first `State` object from the database.
- `9-model_state_filter_a.py`: Lists all `State` objects that contain the letter 'a'.
- `10-model_state_my_get.py`: Prints the `State` object with the name passed as an argument.
- `11-model_state_insert.py`: Adds a new `State` object to the database.
- `12-model_state_update_id_2.py`: Changes the name of a `State` object where `id = 2` to "New Mexico".
- `13-model_state_delete_a.py`: Deletes all `State` objects containing the letter 'a'.
- `14-model_city.py` and `14-model_city_fetch_by_state.py`: Defines the `City` class and lists all cities in a state.

### How to Run

To run any of the Python scripts, use the following command:

```bash
python3 script_name.py <mysql_username> <mysql_password> <database_name>
