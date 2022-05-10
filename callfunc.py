import outputdata as fl
import inputdata as fl2
import updatedata as fl3

def callfunc (call):

    if call == 'вывести':
        chooze = input ("введите параметр поиска ")
        if chooze == 'Наименование' or chooze == "наименование":
            fl.selectdataname (input('Введите наименование товара: '))

        elif chooze == "Размер" or chooze == "размер":
            fl.selectdatasize (input('Введите размер: '))
    
        elif chooze == "Цвет" or chooze == "цвет":
            fl.selectdatacolor (input('Введите цвет: '))
    
    elif call == 'ввести':
        fl2.inputdata (list(map(str,input('Введите даннные через пробел: ').split())))
        
    elif call == 'обновить':
        fl3.updatedata(list(map(str,input('введите количество, наименование, цвет и размер через пробел: ').split())))    

callfunc (input ('введите команду: (ввести, вывести, обновить): '))