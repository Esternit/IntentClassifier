import tensorflow.keras
import inspect
import json
name="tensorflow.keras"
lst=inspect.getmembers(eval(name))
for elem in lst:
    print(elem)
file=open("library_templates.json",'a',encoding='utf-8')
templates={}
lstmain = []


lstfourth=[]
for elem in lst:

    if len(str(elem[1]))>1 and str(elem[1])[0]=='<' and(str(elem[1])[1]=="m" or str(elem[1])[1]=='c'):
        lstsecond = []
        lstmain.append(elem[0])
        name1=name+'.'+elem[0]
        second_lst=inspect.getmembers(eval(name1))
        for elem1 in second_lst:
            if len(str(elem1[1]))>2:
                if str(elem1[1])[0] == '<' and (str(elem1[1])[1] == "m" or str(elem1[1])[1] == 'c'):
                    lstthird = []
                    lstsecond.append(elem1[0])
                    name2 = name1 + '.' + elem1[0]
                    third_lst=inspect.getmembers(eval(name2))
                    for elem2 in third_lst:
                        if len(str(elem2[1])) > 2:
                            if str(elem2[1])[0] == '<' and (str(elem2[1])[1] == "m" or str(elem2[1])[1] == 'c' or str(elem2[1])[1] == 'f'):
                                lstthird.append(elem2[0])
                    templates.update({name2:lstthird})
                elif str(elem1[1])[0] == '<' and str(elem1[1])[1] == "f":
                    lstsecond.append(elem1[0])
        templates.update({name1:lstsecond})
    elif len(str(elem[1]))>1 and str(elem[1])[0] == '<' and str(elem[1])[1] == "f":
        lstmain.append(elem[0])



templates.update({name:lstmain})
print(templates)
json.dump(templates,file, sort_keys=True, indent=2, ensure_ascii=False)
file.close()