# Course Project: Build a budget app

class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.withdrawal_sum = 0

    def __repr__(self):
        title = self.category.center(30, '*')
        items = []
        total = f'Total: {self.get_balance():.2f}'
        for item in self.ledger:
            desc, am = item['description'][:23], item['amount']
            items.append(f"{desc:<23}{am:>7.2f}")
        return title + '\n' + '\n'.join(items) + '\n' + total


    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            self.withdrawal_sum += amount
            return True
        return False

    def transfer(self, amount, destination):
        if self.withdraw(amount, f'Transfer to {destination.category}'):
            destination.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

def create_spend_chart(categories):
    chart = ['Percentage spent by category']
    withdrawal_total = sum(category.withdrawal_sum for category in categories)
    longest = max(len(category.category) for category in categories)
    y_range = [f'{i:>3}|' for i in range(100, -1, -10)]
    bars = [y_range]
    legend = [' ' * longest] * 4
    for category in categories:
        name = category.category.ljust(longest, ' ')
        p = int(category.withdrawal_sum / withdrawal_total * 10) * 10
        bar = ['   ' if p < r else ' o ' for r in range(100, -1, -10)]
        bars.append(bar)
        legend.append([f' {i} ' for i in name])
    for row in zip(*bars, ' ' * 11):
        chart.append(''.join(row))
    chart.append(' ' * 4 + '-' * len(categories) * 3 + '-')
    for row in zip(*legend, ' ' * longest):
        chart.append(''.join(row))
    return '\n'.join(chart)
