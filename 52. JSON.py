import json

#python'da böyle yazıyoruz
person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["Engineer","Programmer"]}
print(person)

#json' a çevirecek olursak; (string olarak çevirir)
personJSON = json.dumps(person, indent=4, separators=(";","="), sort_keys=True)
print(personJSON)

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

"""
indent kodu paragrafa girintileme yapar
separators ise : ve , işaretlerini ; ve = ile değiştirdi
sort_keys kodu ise alfabetik sıralama yaptı
son olarak json dosyayı oluşturduk ve datayı içerisine yazdık

"""

""" 
dump ve dumps farkı şudur:

dumps string ve python file olarak kayıt altına alır ama diske kaydetmez.
dump ise bir dosya oluşturur ve datayı oraya tuple olarak kaydeder.
bir json dosyasını kaydederken tuple, 
geri çağırdığında ise list olarak geri verecektir.

"""