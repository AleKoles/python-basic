dict_homework = {
    "key1":{
        "d":44,
        "f":None,
        "s":{
            8:44,
            9:None,
            10:{"mm":["s", "GET ME", 7]},
        },
    },
    "key2":{
        "fff1":44,
        "f":None,
    },
}

# solution1
key1 = dict_homework['key1']
s = key1['s']
ten = s[10]
final = ten['mm']
print(final[1])

# solution2
print(dict_homework['key1']['s'][10]['mm'][1])

