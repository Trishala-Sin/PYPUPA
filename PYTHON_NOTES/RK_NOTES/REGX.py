import re

r = """SELECT * FROM  
latest_slice::sale_order so INNER JOIN latest_slice::res_partner rp ON  so.id = rp.id"""


def replace_latest_slice(str):
    a = {}
    for i in re.finditer("latest_slice::", str):
        st = i.start()
        f = str.find(" ", i.end() + 1)
        f = len(str) if f == -1 else f
        tab = r[st:f].split('::')[-1]
        print(tab)
        rep = "(SELECT * FROM " + tab + " WHERE DS = 'LATEST')"

        a[str[st:f]] = rep

    for key, val in a.items():
        #print(key)
        #print(val)
       str = str.replace(key, val)
    return str


#print("orignal) :" + r)
print( replace_latest_slice(r))
