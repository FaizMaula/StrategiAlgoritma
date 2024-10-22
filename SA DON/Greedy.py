
def insertionSortAsc(arr, keyPower=lambda x: x):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and keyPower(key_item) < keyPower(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def insertionSortDesc(arr, keyPower=lambda x: x):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and keyPower(key_item) > keyPower(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def insertionSortDens(arr, keyPower=lambda x: x):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and keyPower(key_item) > keyPower(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item



def greedyABC(fighters, hasil, hfighter, Koin, tPower):
    best_power = 0
    for fighter in fighters:
            if fighter.harga <= Koin:
                hasil.append(fighter.img_url)
                hfighter.append(fighter.nama)
                Koin -= fighter.harga
                best_power += fighter.power

    tPower.append(best_power)

    return Koin
