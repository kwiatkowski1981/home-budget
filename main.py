from views import MainMenu
from exeptions import CategoryNotFound
from repositories import EntryRepository, CategoryRepository


class Application:

    def main(self):
        menu = MainMenu()
        menu.draw()

        category_repository = self.get_category_repository()
        entry_repository = self.get_entry_repository()
        screen = menu.get_screen()
        screen.set_repository('category', category_repository)
        screen.set_repository('entry', entry_repository)
        screen.draw()

    def get_entry_repository(self):
        return EntryRepository()

    def get_category_repository(self):
        return CategoryRepository()


if __name__ == '__main__':
    try:
        app = Application()
        app.main()
    except CategoryNotFound:
        print('Nie udalo mi sie znalezc takiej kategorii. ')



