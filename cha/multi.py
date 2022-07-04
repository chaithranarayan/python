def multiple(table: object, start: object, end: object) -> object:
    for i in range(start,end+1):
        print(f"{table}*{i}={table*i}")
 multiple(7,1,4)