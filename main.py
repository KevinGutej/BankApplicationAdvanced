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
    elif choice == 4:
        ui.pay_in(bank)
    elif choice == 5:
        ui.pay_out(bank)

    choice = ui.show_start_page(bank)



#ui.show_start_page(bank)
#ui.show_clients(bank.clients)

