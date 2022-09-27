def execute_file():
    try:
        table_db_file = open("table_dB.txt", "r")
    except:
        raise "No existe el archivo necesario para leer los dB."

    list_file = table_db_file.readlines()
    list_table_dB = list()
    for line in list_file:
        line_split = line.split("|")
        try:
            to_float = float(line_split[1])            
        except:
            continue
        list_table_dB.append({"dB":line_split[1], "rgb":line_split[3]})
    return list_table_dB
