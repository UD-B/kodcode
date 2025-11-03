#יהודה גרשום ברק 324041540

def parse_line(line: str):
    list_line = line.split(";")
    
    for i in list_line:
        if i == None or i == " " or i == "" or len(list_line) != 4:
            return None
        else:
            dict_line = {}
            dict_line.update({"timestamp": str(list_line[0]), "service": str(list_line[1]), "level": str(list_line[2]), "message": str(list_line[3])})
            return dict_line

def parse_logs(lines: list[str]):
    dicted_logs = []
    for i in lines:
        a = parse_line(i)
        dicted_logs.append(a)
    return dicted_logs