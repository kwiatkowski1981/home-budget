import sqlite3


class EntryRepository:

    def get_costs(self):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                # 'SELECT `name`, `amount`, `created_at` FROM entry ORDER BY created_at DESC'
                '''
                SELECT
                entry.id,
                entry.created_at,
                entry.amount,
                entry.name,
                category.name 
            FROM
                entry
            LEFT JOIN category ON entry.category_id = category.id 
            ORDER BY created_at DESC
                '''
            )
            return cursor.fetchall()

    def save(self, name, category_id, amount):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO entry(`category_id`, `name`, `amount`) VALUES(?, ?, ?)', (
                    category_id,
                    name,
                    amount
                ))
            connection.commit()

# todo access do DB is not working, need to figure it out!


class CategoryRepository:
    def get_by_name(self, name):
        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT `id`, `name` FROM category WHERE `name`=?', (name,))
            return cursor.fetchone()
