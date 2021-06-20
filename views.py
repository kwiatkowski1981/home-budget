from abc import ABC, abstractmethod
from exeptions import CategoryNotFound


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
        name = input('Tytul: ')
        amount = float(input('Wartosc: '))
        found_category = False

        while not found_category:
            try:
                category_name = input('Kategoria: ')
                category_id, _ = self.repositories['category'].get_by_name(category_name)
                found_category = True
            except TypeError:
                found_category = False
        self.repositories['entry'].save(name, category_id, amount * -1)


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


