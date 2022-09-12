songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
print(songsdict)
# 1. Выведите общее время звучания всех песен.
print(sum(songsdict.values()))
# 2. Создайте список песен, время звучаниях которых больше 5 минут
songsdict_2 = {k:v for (k,v) in songsdict.items() if v>5}
print(songsdict_2)
# 3.Создайте новый словарь тех песен, в название которых состоит из одного слова
songsdict_3 = {k:songsdict[k] for k in songsdict.keys() if not ' ' in k}
print(songsdict_3)