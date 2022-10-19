import model
import view

def run():
    point = view.write_menu()
    if point == 1:
        num = view.number_entries()
        for i in range(num):
            info = view.creating_info()
            model.writing_csv(info)
        num = view.menu_csv()
        if num == 1:
            res = model.csv_data_open()
            view.show_res(res)
        elif num == 2:
            model.export_csv_txt()
    elif point == 2:
        num = view.number_entries()
        for i in range(num):
            info = view.creating_info()
            model.writing_txt(info)