import itertools 

def bruteForce(fighters, hasil, hfighter, Koin, tPower):
    n = len(fighters)
    best_power = 0
    best_combination = []

    for r in range(1, n + 1):
        for combination in itertools.combinations(fighters, r):
            total_harga = sum(fighter.harga for fighter in combination)
            total_power = sum(fighter.power for fighter in combination)
            if total_harga <= Koin and total_power > best_power:
                best_power = total_power
                best_combination = combination
                print(best_combination)

    for fighter in best_combination:
        hasil.append(fighter.img_url)
        hfighter.append(fighter.nama)
        Koin -= fighter.harga
        

    tPower.append(best_power)
    return Koin