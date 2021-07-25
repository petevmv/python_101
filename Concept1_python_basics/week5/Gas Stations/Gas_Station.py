def gas_stations(distance, tank_size, stations):
    res = []
    destination = 0
    for idx, val in enumerate(stations):
        try:
            if tank_size + val <= stations[idx + 1]:
                print ([])
                return []
        except :
            pass
        if stations[-1] >= distance:
            stations.remove(stations[-1])
        if val >= (tank_size + destination):
            destination = stations[idx - 1]
            res.append(destination)
            if val == stations[-1] and tank_size + destination <= distance:
                res.append(stations[-1])
    print(res)

gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
#gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
#gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150])
#gas_stations(100, 50, [10, 90])
