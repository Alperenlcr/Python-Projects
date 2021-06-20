import collections.abc


class Permissions:
    def __init__(self):
        self.permissions = {
            "brand": {
                "edit": {
                    "read": True,
                    "write": True,
                    "k":{
                        "a":True
                    }
                },
            }
        }


class Role(Permissions):
    def __init__(self):
        super().__init__()

    def is_granted(self, transaction: list) -> bool:
        """

        Parameters
        ----------
        transaction yapılacak işlem için gelen dizidir. Örneğin ["brand","edit","read"]

        Returns
        -------

        """
        g = dict(self.permissions)
        for key in transaction:
            g = g[key]
        return g

    def toggle_grant(self, transaction):
        g = self.permissions
        for key in transaction:
            g = g[key]

a = Role()
a.toggle_grant(["brand", "edit", "read"])
print(a.permissions)

#names = ["brand", "edit"]
names = ["brand", "edit", "read"]

#sayilar = [i for i in range(len(names))]
# g = a.permissions
# for i in range(len(names)):
#     g = g[names[i]]
#print(g)
dictionary = a.permissions
for i in range(len(names)):
    for key, values in dictionary.items():
        #print(key,"**",values)
        if key == names[len(names)-1]:
            dictionary[key] = False
        if type(values) == dict:
            dictionary = values
# print(dictionary)
print(a.permissions)

# def recursive_items(dictionary):
#     for key, value in dictionary.items():
#         if type(value) is dict:
#             yield (key, value)
#             yield from recursive_items(value)
#         else:
#             yield (key, value)
#
# a = {'a': {1: {1: 2, 3: 4}, 2: {5: 6}}}
#
# for key, value in recursive_items(a):
#     print(key, value)


#print(a.permissions[names[sayilar[0]]][names[sayilar[1]]][names[sayilar[2]]])
#print(a.permissions[names[sayilar[0]]][names[sayilar[1]]])

# ------------------------------------------
# >>> a.permissions["brand"]["edit"]["read"]
# >>> False