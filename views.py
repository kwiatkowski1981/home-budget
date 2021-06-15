from abc import ABC, abstractmethod
from repositories import EntryRepository, CategoryRepository


class AbstractView(ABC):
    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class AddCost(AbstractView):
    SHORTCUT = 'dk'
    LABEL = '(D)odaj (K)oszt'

    def draw(self):
        print(AddCost.LABEL)
        title = input('Tytul: ')
        category_name = input('Kategoria: ')
        amount = float(input('Wartosc'))

        category = self.repositories['category'].get_by_name(category_name)
        self.repositories['entry'].save(title, category, amount)


class ListCosts(AbstractView):
    SHORTCUT = 'wk'
    LABEL = '(W)ypisz (K)oszta'

    def draw(self):
        print(ListCosts.LABEL)


class AddIncome(AbstractView):
    SHORTCUT = 'dp'
    LABEL = '(D)odaj (P)rzychod'

    def draw(self):
        print(AddIncome.LABEL)


class ListIncomes(AbstractView):
    SHORTCUT = 'wp'
    LABEL = '(W)ypisz (P)rzychody'

    def draw(self):
        print(ListIncomes.LABEL)


class MainMenu(AbstractView):
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),        # (D)odaj (K)oszt
        ListCosts.SHORTCUT: ListCosts(),      # (W)ypisz (K)oszta
        AddIncome.SHORTCUT: AddIncome(),      # (D)odaj (P)rzychod
        ListIncomes.SHORTCUT: ListIncomes(),    # (W)ypisz (P)rzychody
    }

    def get_screen(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcje: ')
        return MainMenu.OPTIONS[option]

    def draw(self):
        print('Powiedz co chcesz zrobic: ')
        for shortcut, screen in MainMenu.OPTIONS.items():
            print(f' [{shortcut}] - {screen.LABEL}')
        print("\n")


