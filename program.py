x = {"1": "so", "2": "by", "3": "dg", "4": {"1": "f", "2": "df", "3": "dfdf"}}
print(x["4"]["1"])
print(x["4"]["3"])
x.update({"shivani": "hjuh"})
print(x)
# x.pop("1")
print(str(x))
del x["1"]
print(x)
y=x.copy()
del y["3"]
print(y)


