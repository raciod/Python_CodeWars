def bouncing_ball(h, bounce, window):
    count = 1
    if h > 0 and (1 > bounce > 0) and h > window:
        while h*bounce > window :
            h *=bounce
            count += 2
        return count
    else:
        return -1
h = 2
bounce = 0.5
window = 1

print(bouncing_ball(h, bounce, window))