
depth_data = []

crate_data = []
move_data = []

with open("Day5\data.txt") as file:
    data = file.read()
    data_into_list = (data.split("\n"))
    for ixd, i in enumerate(data_into_list):
        if len(i) == 0:
            crate_data = data_into_list[:ixd]
            move_data = data_into_list[ixd+1:]
            break
            
            
    crate= {}
    for i in crate_data[:-1]:
        
        for j in range(1, len(i), 4):
            index = j//4 +1
            if i[j] != " ":
                if index not in crate.keys():
                    crate[index] = []
                
                crate[index].append(i[j])
    
    for key, value in crate.items():
        key =  value.reverse()
        
    move = []
    for i in move_data:
        temp = i.replace("move ", "").replace("from ", "").replace("to ", "")
        move.append(temp.split(" "))
        for idx, st in enumerate(move[-1]):
            move[-1][idx] = int(st)
        
    
    # # Uncomment for part 1
    
    # for m in move:
    #     for i in range(m[0]):
    #         crate[m[2]].append(crate[m[1]].pop())
            
    # for i in range(1, len(crate)+1):
    #     print(crate[i][-1], end="")
        
         
    # Uncomment for part 2
    for m in move:
        # tempArr
        crate[m[2]] += crate[m[1]][(-1 * m[0]):]
        del crate[m[1]][len(crate[m[1]]) - m[0]:]
            # tempAr
            
    print(crate)
    for i in range(1, len(crate)+1):
        # if(len(crate[i].value()) > 0):
        print(crate[i][-1], end="")
    
        
    
    
