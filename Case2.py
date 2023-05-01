# В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.

ids = ['1111:271', '1111:190', '1231:106', '1211:104', '1111:201', '1231:120', '1001:205',
'1001:223', '1001:127', '1001:236', \
'1111:229', '1231:286', '1231:195', '1001:279', '1001:124', '1111:292', '1505:219', '1231:259',
'1231:253', '1001:220', '1001:202',\
'1231:103', '1211:249', '1212:275']
count = [111, 3, 13, 111, 9, 5, 17, 10, 13, 3, 16, 4, 16, 11, 18, 12, 14, 4, 3, 2, 14, 14, 10, 10]
items_count = dict( zip(ids, count) )
 
count_of_unique_categories = len( ( unique_categories := set( [ x.partition(':')[0] for x in items_count ] ) ) )
print( f'Количество уникальных категорий: { count_of_unique_categories }' )
 
average_number_of_items_per_category = dict()
for cat in unique_categories:
    cat_names      = ( [x for x in items_count if x.startswith( cat ) ] )
    cat_values_sum = sum( [ items_count[x] for x in cat_names ] )
    average_number_of_items_per_category[cat] = round( cat_values_sum / len( cat_names ), 1 )
print( f'Среднее количество единиц товара на складе в категории: { average_number_of_items_per_category }')
 
id = [ x for x in items_count if items_count[x] == max( items_count.values() ) ]
print( f'ID товаров с максимальным количеством единиц на складе: {id}' )
