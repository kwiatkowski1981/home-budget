from abc import ABC, abstractmethod
from terminaltables import AsciiTable


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
        # oprion with terminaltables
        rows = [
            ['pozycja', 'data dodania', 'kwota', 'na co', 'kategoria']
        ]
        for cost_id, created_at, amount, name, category in self.repositories['entry'].get_costs():
            # print(f'{cost_id}, {created_at}, {amount}, {category}')
            rows.append([cost_id, created_at, amount, name, category])
        table = AsciiTable(rows)
        print(table.table)


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


class Report(AbstractView):
    SHORTCUT = 'r'
    LABEL = '(R)aporty'

    def draw(self):
        print(Report.LABEL)
        repository = self.repositories['report']
        quantity, saldo = repository.get_saldo()
        print(f'ilość operacji: {quantity}  saldo: {saldo}')

        rows = [
            ['nazwa kategorii', 'ilość operacji', 'suma']
        ]
        rows += repository.get_saldo_by_category()
        table = AsciiTable(rows)
        print(table.table)


class MainMenu(AbstractView):
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),  # (D)odaj (K)oszt
        ListCosts.SHORTCUT: ListCosts(),  # (W)ypisz (K)oszta
        AddIncome.SHORTCUT: AddIncome(),  # (D)odaj (P)rzychod
        ListIncomes.SHORTCUT: ListIncomes(),  # (W)ypisz (P)rzychody
        Report.SHORTCUT: Report()  # (R)aporty
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
