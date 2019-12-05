f = open("call_graph_85_no_param.txt");
new_f = open("call_graph_85_no_param_modified.txt", "w")
for line in f:
    if line[0:2] == "M:":
        rest = line[2:].split('*')
        if rest[0][0:4] == "java" or rest[2][0:4] == "java":
            continue
        s =  "depends " + rest[0] + " " + rest[2]
        s = s.replace(":",".")
        new_f.write(s)



