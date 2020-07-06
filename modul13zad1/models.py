import json
import sqlite3
import logging


class ItemDB:

    def __init__(self, table_name: str):
        self.table_name = table_name

    def all(self):
        return self.execute("SELECT * FROM {self.table_name}")

    def delete(self, condition_param_name: str, condition_param_value):
        return self.execute(f"DELETE FROM {self.table_name} WHERE {condition_param_name}={condition_param_value}")

    def execute(self, sql_query: str, print_error: bool = True):
        try:
            connection = self.connect_to_database(self.database_name)
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
            logging.debug(f"OK - {sql_query}")
            return cursor.fetchall()
        except (sqlite3.OperationalError, sqlite3.IntegrityError) as error:
            if print_error:
                logging.error(f"Error - {sql_query} [{error}]")

    def _create_table(self):
        self.execute("CREATE TABLE todos (title varchar(255) PRIMARY KEY, description varchar(255), done bool);",
                     print_error=False)

    @staticmethod
    def sql_normalize_bool_value(bool_value: bool):
        return 1 if bool_value else 0

    @staticmethod
    def sql_normalize_string_value(string_value: str):
        return f"\"{string_value}\""

    @staticmethod
    def connect_to_database(database_name: str):
        try:
            return sqlite3.connect(database_name)
        except sqlite3.Error:
            logging.exception(f"Cannot connect to database {database_name}")


class TodosDB(ItemDB):

    def __init__(self, database_name: str, table_name: str):
        super().__init__(table_name=table_name)
        self.database_name = database_name
        self._create_table()

    def get(self, title: str):
        return self.execute(f"SELECT * FROM todos WHERE title=\"{title}\"")

    def create(self, title: str, description: str, done: bool):
        return self.execute(f"INSERT INTO todos (title, description, done) "
                            f"VALUES (\"{title}\", \"{description}\", {self.sql_normalize_bool_value(done)});")

    def update(self, title: str, description: str = None, done: bool = None):
        def generate_query(id: str, param_name: str, param_value):
            sql_update_query_template = "UPDATE todos SET {} = {} WHERE title = \"{}\""
            if isinstance(param_value, str):
                param_value = self.sql_normalize_string_value(param_value)
            if isinstance(param_value, bool):
                param_value = self.sql_normalize_bool_value(param_value)
            return sql_update_query_template.format(param_name, param_value, id)

        if description is not None:
            self.execute(generate_query(title, param_name="description", param_value=description))

        if done is not None:
            self.execute(generate_query(title, param_name="done", param_value=done))

    def delete(self, title: str):
        return super().delete("title", title)

    @staticmethod
    def save_all():
        logging.warning("Depreciated method")


class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos

    def get(self, id):
        return self.todos[id]

    def create(self, data):
        data.pop('csrf_token')
        self.todos.append(data)

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

    def delete(self, id):
        todo = self.get(id)
        if todo:
            self.todos.remove(todo)
            self.save_all()
            return True
        return False


todos = Todos()

if __name__ == '__main__':
    todosDB = TodosDB("kodilla.sqlite3")
    # todosDB.create("test", "test_desc", True)
    # todosDB.update("test", description="updated_test_desc")
    # print("# GET ONE \n", todosDB.get("test"))
    # todosDB.update("test", done=False)
    # print("# GET ALL \n", todosDB.all())
    # todosDB.delete("test")
    print("# GET ALL \n", todosDB.all())
