def cooking_time(eggs):
    if eggs:
        return (eggs // 8 + 1) * 5 if eggs % 8 else eggs // 8 * 5
    return 0
