from tkinter import *

root = Tk()
root.title('Подбор игрушек')
root.geometry('500x400')

Label(root, text='Стоимость игрушки не более:').grid(row=0, column=0, columnspan=2)
Label(root, text='Возраст ребенка от:').grid(row=1, column=0, columnspan=2)
Label(root, text='До:').grid(row=1, column=2)

def find_toys():
    toys_list = []
    with open('toys_file.txt') as toys_file:
        for line in toys_file:
            line = line.split(' - ')
            toy_name = line[0]
            toy_cost = line[1]
            toy_age_from = line[2]
            toy_age_to = line[3]
            # Здесь нужно добавить проверки на то, что параметры в пределах заданных ограничений:
            if int(toy_cost) <= int(costEntry.get()) and int(toy_age_to) <= int(ageToEntry.get()) and int(toy_age_from) >= int(ageFromEntry.get()):
                toys_list.append(toy_name)
    # Отображаем найденые игрушки в виджет-списке:
    for i, toy in enumerate(toys_list):
        toysList.insert(i, toy)

costEntry = Entry(root)
ageFromEntry = Entry(root)
ageToEntry = Entry(root)
costEntry.grid(row=0, column=2)
ageFromEntry.grid(row=1, column=1)
ageToEntry.grid(row=1, column=3)

submitButton = Button(root, text='Найти', command=find_toys)
submitButton.grid(row=2, column=0)

toysList = Listbox(root)
toysList.grid(row=2, column=1, columnspan=2)



root.mainloop()