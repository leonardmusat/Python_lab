def XML(a, string, dict1, dict2, dict3):
    list_dict = [dict1, dict2, dict3]
    final = "<"
    final = final + a + " "

    for dict in list_dict:
        temp = list(dict.keys())[0]
        temp1 = dict[temp]
        temp1= '"' + temp1 + ' \ "'
        final = final + temp + "=\ " + temp1
    final = final + ' ' + string + '"' + "</a>"
    return final


dict1 ={"href":" http://python.org "}
dict2 ={"_class":" my-link "}
dict3 ={"id": " someid "}
print(XML("a", "Hello there", dict1, dict2, dict3))