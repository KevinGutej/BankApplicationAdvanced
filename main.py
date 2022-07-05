from Bank import Bank
from UI import UI

bank = Bank()
ui = UI()
ui.show_clients(bank.clients)
ui.show_start_page(bank)
ui.show_clients(bank.clients)