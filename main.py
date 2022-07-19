from Bank import Bank
from UI import UI
import sys

bank = Bank()
ui = UI()

ui.show_clients(bank.clients)
choice = ui.show_start_page(bank)

while True:
    if choice == 3:
        sys.exit()
    elif choice == 2:
        ui.sign_up(bank)
    elif choice == 1:
        ui.login(bank)
    choice = ui.show_start_page(bank)

#ui.show_start_page(bank)
#ui.show_clients(bank.clients)

