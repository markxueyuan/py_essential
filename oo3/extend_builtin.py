
# inherit built-in class list, adding a new method to it.
class ContractList(list):
    def search(self, name):
        """Return all contracts that contain the search value
        in their name."""
        matching_contracts = []
        for contract in self:
            if name in contract.name:
                matching_contracts.append(contract)
        return matching_contracts


class Contract():
    all_contracts = ContractList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contract.all_contracts.append(self)


def main():
    c1 = Contract("John A", "johna@example.net")
    c2 = Contract("John B", "johnb@example.net")
    c3 = Contract("Jenna C", "jennac@example.net")
    [c.name for c in Contract.all_contracts.search('John')]


if __name__ == "__main__":
    main()


"""
[Think that in our used ways we will define a function
which effects on the built-in class objects.
Now we extend that built-in class by adding a new method
in the extended class.

This gives a different type of world view in which every
function (method) comes into exist only when it is necessary
to serve the special characteristics of a certain object.

It is not valid to think about a method that works without
considering class, which may represent the failure to
achieve economy by fully utilizing what already realized.]
"""

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


def main():
    lk = LongNameDict()
    lk["hello"] = 1
    lk['longest yet'] = 5
    lk['hello2'] = 'world'
    lk.longest_key()






