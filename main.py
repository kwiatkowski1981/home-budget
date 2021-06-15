from views import MainMenu
from repositories import EntryRepository, CategoryRepository


class Application:
    @staticmethod
    def main():
        menu = MainMenu()
        menu.draw()

        screen = menu.get_screen()
        screen.set_repository('category', CategoryRepository)
        screen.set_repository('entry', EntryRepository)
        screen.draw()

    def get_entry_repository(self):
        pass


if __name__ == '__main__':
    Application.main()

