def number(bus_stops):
    get_on = 0
    get_off = 0
    for b in bus_stops:
        get_on  += b[0]
        get_off += b[-1]

    return get_on - get_off