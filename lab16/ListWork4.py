"""
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вывести указатель на пятый элемент этого списка P5. Известно, что в исходном списке не
менее 5 элементов.
"""

from GlobalTools.HandMadeList import HMList

newList = HMList()

newList.append(5)
newList.append(15)
newList.append(25)
newList.append(35)

newList.insert(3, 12)

for item in newList:
    print(item.Data)