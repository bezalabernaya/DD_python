# TODO Напишите функцию для поиска индекса товара
def search_goods(List, product):
    for i in range(len(List)):
        if List[i] == product:
            a = i
            break
        else:
            a = None
    return a


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_goods(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
