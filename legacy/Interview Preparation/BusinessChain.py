from operator import attrgetter

class Business(object):

    def __init__(self, chain_name, location, id):
        self.chain_name = chain_name
        self.location = location
        self.id = id

class Chain(object):

    def __init__(self, chain_name, frequency):
        self.chain_name = chain_name
        self.frequency = frequency

# remove duplicate elements from the sorted list
def remove_duplicate(arr):
    if not arr or len(arr) <= 1:
        return arr

    i, j = 0, 1
    while j < len(arr):
        if arr[i].id != arr[j].id:
            arr[i + 1] = arr[j]
            i += 1
        j += 1

    return arr[:i + 1]

def get_chain_freq(biz_list, location):

    if not biz_list or len(biz_list) == 0 or not location:
        return []

    # sort by id and then remove the duplicate elements from list
    biz_list.sort(key=attrgetter('id'))
    biz_list = remove_duplicate(biz_list)

    # sort the list by location and chain name
    biz_list.sort(key=attrgetter('location', 'chain_name'))
    for i in range(0, len(biz_list)):
        print("(" + str(biz_list[i].id) + ", " + biz_list[i].location + ", " + biz_list[i].chain_name + ")")

    # locate the starting and ending index of the chain that was located in the given location
    for i in range(0, len(biz_list)):
        if biz_list[i].location == location: break
    for j in range(i, len(biz_list)):
        if biz_list[j].location != location: break

    # corner case, deal the case that the last element happen to be a qualified chain
    j = j + 1 if j == len(biz_list) - 1 and biz_list[j].location == location else j

    # if the given location can not be found in current chain, return a empty list
    if i == j == len(biz_list) - 1:
        return []

    # count the id frequency wrt to each chain name
    chain_list = []
    c_name, freq = biz_list[i].chain_name, 0
    for k in range(i, j):

        if c_name == biz_list[k].chain_name:
            freq += 1

        if c_name != biz_list[k].chain_name:

            # add the previous chain's stat into the chain list
            chain_list.append(Chain(c_name, freq))

            # reset the chain name and frequency for new chain
            c_name = biz_list[k].chain_name
            freq = 1

    # append the last qualified chain into the list
    chain_list.append(Chain(c_name, freq))

    # sort the list in ascending order of frequency and chain name
    chain_list.sort(key=attrgetter('frequency', 'chain_name'))

    return chain_list

def get_chain_freq_1(biz_list, location):

    if not biz_list or len(biz_list) == 0 or not location:
        return []

    # loc_count store the (location, count) pairs, ids use to track the duplicate cases
    loc_count = dict()
    ids = set()
    for i in range(0, len(biz_list)):

        cursor = biz_list[i]
        if cursor.location == location:
            # check if the new biz is duplicate
            if cursor.id not in ids:
                # calculate the frequency of each chain under the given location
                if cursor.chain_name in loc_count.keys():
                    loc_count[cursor.chain_name] += 1
                else:
                    loc_count[cursor.chain_name] = 1

                ids.add(cursor.id)

    # create the chain_list and order the element in ascending order of freq and chain_name
    chain_list = []
    for key in loc_count:
        chain_name = key
        freq = loc_count[key]
        chain_list.append(Chain(chain_name, freq))
    chain_list.sort(key=attrgetter('frequency', 'chain_name'))

    return chain_list


# location Austin, output whole food 2, Peets Coffe 1, Starbucks 1
b1 = Business("Starbucks", "Seattle", 101)
b2 = Business("Peets Coffee", "San Francisco", 102)
b3 = Business("Amazon", "Austin", 103)
b4 = Business("Starbucks", "San Francisco", 104)
b5 = Business("Peets Coffee", "Austin", 105)
b6 = Business("Starbucks", "Austin", 106)
b7 = Business("Amazon", "Austin", 103)
b8 = Business("Amazon", "Austin", 107)
b9 = Business("Starbucks", "Austin", 108)
b10 = Business("Starbucks", "Austin", 109)


biz_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
for i in range(0, len(biz_list)):
    print("(" + str(biz_list[i].id) + ", " + biz_list[i].location + ", " + biz_list[i].chain_name + ")")
print()

arr1 = get_chain_freq_1(biz_list, "Austin")
# arr1 = get_chain_freq(biz_list, "Austin")
for i in range(0, len(arr1)):
    print(arr1[i].chain_name + ", " + str(arr1[i].frequency))
