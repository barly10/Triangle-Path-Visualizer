import random
import math


#My variable debugger
#print("Hello World {}".format(min_path_fund))

def Hello(text):
    print("Hello World {} My name is Siraj.".format(text))

def Hellos(num,text):
    print("{} Hello World {} My name is Siraj.".format(num,text))
    
def layer(num):
    num=math.ceil(num)
    if num == 1:
        return 1
    count = 1
    while (True):
        num -= count
        count += 1
        if (num - count <= 0):
            return count

def leveler(start,level):
    if layer(start)==layer(level):
        return start
    elif (layer(level)-layer(start))%2==0:
        return leveler(start+layer(start)+layer(start)+2,level)
    else:
        return leveler(start+layer(start),level)+.5


top =[]
left_nums = []
right_nums = []
fund_array=[]

#Old Source Code
class node:
    def __init__(self, val):
        self.val = val
        self.child = []

    def add_child(self, num):
        self.child.append(num)

def rev_lst_lst(list_):

    rev_lst_lst=[]
    for edge in list_:
        rev_lst=[]
        for item in reversed(edge):
            rev_lst.append(item)
        rev_lst_lst.append(rev_lst)
        
    return rev_lst_lst

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def remove(lst1, lst2):
    return list(set(lst1) - set(lst2))

def remove_lst_lst(lst1, lst2):
    lst1_temp=lst1[:]
    for path in lst2:
        if path in lst1:
            lst1_temp.remove(path)
            
    return lst1_temp

#Returns Edges that are moves
def edges(n):

    points = []
    bottom_nums = []
    edge_num=int(3*n*(n+1)/2)

    print(n)
    points_num = (n + 1) * (n + 2) / 2
    # Creates the node objects of the graph
    for num in range(0, int(points_num)):
        points.append(node(num + 1))

    max_num = len(points)

    # Calculates the left-side numbers
    l_num = 1
    count = 0


    while (l_num < max_num - n):
        l_num += count
        left_nums.append(l_num)
        count += 1

    # Calculates the right-side numbers
    r_num = 0
    count = 1
    while (r_num < max_num):
        r_num += count
        right_nums.append(r_num)
        count += 1

    # Calculates the bottom numbers

    lleft = left_nums[-1]
    rright = right_nums[-1]
    for b_num in range(lleft, rright + 1):
        bottom_nums.append(b_num)

    top = intersection(left_nums, right_nums)
    leftdown = intersection(left_nums, bottom_nums)
    rightdown = intersection(right_nums, bottom_nums)
    left = remove(remove(left_nums, top), leftdown)
    right = remove(remove(right_nums, top), rightdown)
    down = remove(remove(bottom_nums, leftdown), rightdown)
    center = remove(range(1, max_num + 1), top + leftdown + rightdown + left + right + down)

    print(top)
    print(leftdown)
    print(rightdown)
    print(left)
    print(right)
    print(down)
    print(center)

    for num in range(1, max_num + 1):
        if num in top:
            points[num - 1].add_child(2)
            points[num - 1].add_child(3)
        elif num in leftdown:
            points[num - 1].add_child(num + 1)
            points[num - 1].add_child(left_nums[left_nums.index(num) - 1])
        elif num in rightdown:
            points[num - 1].add_child(num - 1)
            points[num - 1].add_child(right_nums[right_nums.index(num) - 1])
        elif num in left:
            points[num - 1].add_child(num + 1)
            points[num - 1].add_child(left_nums[left_nums.index(num) - 1])
            points[num - 1].add_child(left_nums[left_nums.index(num) + 1])
            points[num - 1].add_child(left_nums[left_nums.index(num) + 1] + 1)
        elif num in right:
            points[num - 1].add_child(num - 1)
            points[num - 1].add_child(right_nums[right_nums.index(num) - 1])
            points[num - 1].add_child(right_nums[right_nums.index(num) + 1])
            points[num - 1].add_child(right_nums[right_nums.index(num) + 1] - 1)
        elif num in down:
            diff = layer(num)
            points[num - 1].add_child(num - 1)
            points[num - 1].add_child(num + 1)
            points[num - 1].add_child(num - diff)
            points[num - 1].add_child(num - diff + 1)
        elif num in center:
            diff = layer(num)
            points[num - 1].add_child(num + diff)
            points[num - 1].add_child(num + diff + 1)
            points[num - 1].add_child(num - diff)
            points[num - 1].add_child(num - diff + 1)
            points[num - 1].add_child(num - 1)
            points[num - 1].add_child(num + 1)
      

    #for point in points:
        #print("Point: {}\nConnected: {}".format(point.val, point.child))

    edges = []
    for point in points:
        for childnum in point.child:
            duplicate = False
            for edge in edges:
                if all(elem in edge for elem in [point.val, childnum]):
                    duplicate = True
            if not duplicate:
                edges.append([point.val, childnum])
    return edges

#Old Source Codes

#Returns [Boolean,Boolean], corresponding to [IsUp,IsRight,IsCenter]
def min_direction(start,end):
    Up=True
    Right=True
    Center=False

    if (layer(start)==layer(end)):
        Center=True
    elif (layer(start)<layer(end)):
        Up=False
    if (leveler(start,end)>end):
        Right=False
    elif (leveler(start,end)==end):
        if (random.randint(1,2)==1):
            Right=False

    return [Up,Right,Center]

#Returns an edge-path from a given point towards the end point
def min_path(start,end):
    dire=min_direction(start,end)

    if dire[2]==True:
        if dire[1]==True:
            return [start,start+1]
        else:
            return [start,start-1]
    elif dire[0]==True:
        if dire[1]==True:
            return [start,start-layer(start)+1]
        else:
            return [start,start-layer(start)]
    else:
        if dire[1]==True:
            return [start,start+layer(start)+1]
        else:
            return [start,start+layer(start)]

#Returns the min-path from the starting to the end point
def all_min_path(start,end):
    Reverse=False
    start_temp=0
    end_temp=0
    if start>end:
        start_temp=end
        end_temp=start
        Reverse=True
    else:
        start_temp=start
        end_temp=end
    print(Reverse)
    min_paths=[]
    
    while start_temp!=end_temp:
        temp_path=min_path(start_temp,end_temp)
        min_paths.append(temp_path)
        start_temp=temp_path[1]

    rev_min_paths=[]

    #Reverses the normal min-path 
    if Reverse:

        for edge in min_paths:
            rev_path=[]
            for item in reversed(edge):
                rev_path.append(item)
            rev_min_paths.append(rev_path)
        min_paths=[]
        for item in reversed(rev_min_paths):
            min_paths.append(item)

    return min_paths

#Returns the fundamental triangles a number is in
def fund_tri_num(num):
    nums=[num]

    if num is 1:
        next
    elif num in left_nums:
        nums.append(num-layer(num)+1)
    elif num in right_nums:
        nums.append(num-layer(num))
    else:
        nums.append(num-layer(num)+1)
        nums.append(num-layer(num))

    return nums

#returns the fundamental triangle an edge is in
def fund_tri_path(array):
    print(array)
    return intersection(fund_tri_num(array[0]),fund_tri_num(array[1]))[0]

#                   #
# Might get deleted #
#                   #

#returns the first fundamental triangle below that given number
def first_fund(num):
    n=layer(num)
    return (n*(n-1)/2+1)

#returns the last fundamental triangle above that given number
def last_fund(num):
    n=layer(num)
    return ((n-1)*(n-2)/2+n-1)

#returns the fundamental triangles that are in between the starting point and the end point
def funds(start,end):
    funds=[]
    for num in (first_fund(start),last_fund(end)+1):
        funds.append(num)
    return num

#                   #
# Might get deleted #
#                   #

def funds_level_edge(points_old):
    points=points_old[:]
    points.sort()
    funds=[]
    
    first=first_fund(points[0])
    
    for num in range(0,layer(points[0])):
        funds.append(first+num)

    return funds

#Determines if this edge is the upper-left edge of its fundamental  triangle
def fund_edge_left(points_old):
    points=points_old[:]
    points.sort()
    if (points[1]-layer(points[0]))==points[0]:
        return True
    else:
        return False

def fund_edge_bottom(points_old):
    points=points_old[:]
    points.sort()
    if layer(points[0])==layer(points[1]):
        return True
    else:
        return False

#Returns a list of fundamental triangles left and right to the min-paths
def funds_lr(min_paths):

    #fundamental triangles to the left of the min-paths
    left_fund=[]
    #fundamental triangles to the right of the min-paths
    right_fund=[]
    for min_path in min_paths:
        
        funds=funds_level_edge(min_path)
        min_path_fund=fund_tri_path(min_path)

        
        if layer(min_path[0])==layer(min_path[1]):
            next
        elif fund_edge_left(min_path):
            for fund in funds:
                if fund<min_path_fund:
                    left_fund.append(int(fund))
                else:
                    right_fund.append(int(fund))
        else:
            for fund in funds:
                if fund<=min_path_fund:
                    left_fund.append(int(fund))
                else:
                    right_fund.append(int(fund))
                    
    return [left_fund,right_fund]

#Returns fundamental triangle of start min_path and end min_path with respective rotations
def rot(paths):
    first_fund=fund_tri_path(paths[0])
    last_fund=fund_tri_path(paths[1])
    
    first_fund_rot=fund_rot(paths[0],first_fund)
    last_fund_rot=fund_rot(paths[1],last_fund)

    return [first_fund_rot,last_fund_rot]

#Interface, Returns the numbers of that fundamental triangle
def fund_nums(fund):
    global fund_array
    return fund_array[fund-1]
            
#Returns: [Fundamental triangle number int, "Rotation"]
def fund_rot(path,fund):
    rots="CC"
    nums=fund_nums(fund)

    start_index=nums[1].index(path[0])
    end_index=nums[1].index(path[1])
    
    if start_index is 0:
        if end_index is 2:
            rots="C"
    elif start_index is 1:
        if end_index is 0:
            rots="C"
    elif start_index is 2:
        if end_index is 1:
            rots="C"
    return [fund,rots]

#assigns C or CC rotation to all fundamental triangles that need correction, left or right 
def real_rotate(TrueRots,LeftRight,RotData):
    if TrueRots[0][1]=="CC":
        if TrueRots[0][0] in LeftRight[0]:
            for fund in LeftRight[0]:
                RotData[fund-1][0]="CC"
        else:
            for fund in LeftRight[1]:
                RotData[fund-1][0]="CC"
                
    elif TrueRots[1][1]=="CC":
        if TrueRots[1][0] in LeftRight[0]:
            for fund in LeftRight[0]:
                RotData[fund-1][0]="CC"
        else:
            for fund in LeftRight[1]:
                RotData[fund-1][0]="CC"
                
#Creates the list of edges that have been corrected in rotation based from fund_array
def correct_edge(fund_array):
    edges=[]
    for fund_data in fund_array:
        if fund_data[0]=="CC":
            edges.append([fund_data[1][2],fund_data[1][1]])
            edges.append([fund_data[1][0],fund_data[1][2]])
            edges.append([fund_data[1][1],fund_data[1][0]])
        else:
            edges.append([fund_data[1][1],fund_data[1][2]])
            edges.append([fund_data[1][2],fund_data[1][0]])
            edges.append([fund_data[1][0],fund_data[1][1]])
    return edges

def max_possible_paths(start,possible_paths):
    return_possible_paths=[]
    for path in possible_paths:
        if path[0]==start:
            return_possible_paths.append(path)
    return return_possible_paths
#Returns [Boolean,Boolean], corresponding to [IsUp,IsRight,IsCenter]

def level_range(top,bottom):
    layer_diff=layer(bottom)-layer(top)
    leveled_start=leveler(top,bottom)
    return [int(leveled_start-layer_diff/2),int(leveled_start+layer_diff/2)]

def distance(path):
    distance=0
    minimum=min(path)
    maximum=max(path)
    
    if layer(minimum)==layer(maximum):
        distance=maximum-minimum
    else:
        leveled_range= level_range(minimum,maximum)
        leveled_point=leveler(minimum,maximum)
        standard_distance=layer(maximum)-layer(minimum)
        
        if (maximum<leveled_range[0]):
            distance=leveled_range[0]-maximum+standard_distance
        elif (maximum>leveled_range[1]):
            distance=maximum-leveled_range[1]+standard_distance
        else:
            distance=standard_distance
            
            
    return distance
            
        
def max_path(start,end,possible_paths):
    
    possible_paths=max_possible_paths(start,possible_paths)
    #print(possible_paths)
    distance_possible_paths=[]
    #Hellos(7,possible_paths)
    for path in possible_paths:
        path_dist=distance([path[1],end])
        distance_possible_paths.append([path,path_dist])
    #Hellos(14,distance_possible_paths)
        
    sort_paths=sorted(distance_possible_paths, key=lambda dist_path: dist_path[1])
        
    #print(sort_paths)

    return sort_paths[-1]


        
#Returns the Max Path
def all_max_paths(start,end,min_paths,correct_paths):
    #Hello(correct_paths)
    #Hello(min_paths)
    possible_paths=remove_lst_lst(correct_paths,rev_lst_lst(min_paths))

##    print("\n************** Data for all_max_paths **************")
##    print("possible_paths:\n{}\n:possible_paths".format(str(possible_paths).replace("[","{").replace("]","}")))
##    print("****************************************************\n")
    
    start_temp=start
    end_temp=end
    max_paths=[]

    
    while (len(possible_paths)!=0):
        temp_path=max_path(start_temp,end_temp,possible_paths)
        max_paths.append(temp_path[0])
        start_temp=temp_path[0][1]
        #Hellos(49,max_paths)
        possible_paths.remove(temp_path[0])



    return max_paths

start=0
end=0
min_pathss=[]
corrected_edges=[]

def main():
    global start,end,min_pathss,corrected_edges
    
    f = open("[0] init.txt", "r")
    init_config=[]
    for num in range(0,3):
        init_config.append(f.readline())
    f.close()
    print(init_config)
    tri_size=eval(init_config[0].split(":")[1])#4#eval(input("Please enter Triangle size: (Minimum size is 1)\n>>>"))
    start=eval(init_config[1].split(":")[1])#2#eval(input("Please enter number of starting point:\n>>>"))
    end=eval(init_config[2].split(":")[1])#6#eval(input("Please enter number of ending point:\n>>>"))
    # Number of fundamental triangles in given triangle size
    fund_tri=tri_size*(tri_size+1)/2
    # Array of numbers of all fundamental triangles + generator

    for num in range(1,int(fund_tri+1)):
        add=layer(num)
        fund_array.append(["C",[num+add,num,num+add+1]])


    min_paths=all_min_path(start,end)
    min_pathss=all_min_path(start,end)
    
    #Important code to determine left and right nums
    print(fund_array)
    
    print(edges(tri_size))

    #for num in range(1,8):
        #print(fund_tri_num(num))

    print(fund_tri_path([2,5]))

    #fundamental triangles that are in between the starting point and the end point
    fund=[]
    fund=funds_lr(min_paths)

    print("Left and Right Funds: {}".format(fund))

    
    Hello(min_paths)

    #print(rot([min_paths[0],min_paths[-1]]))

    real_rotate(rot([min_paths[0],min_paths[-1]]),fund,fund_array)

    #print(fund_array)
    corrected_edges=correct_edge(fund_array)
    Hellos(84,corrected_edges)

    max_paths=all_max_paths(start,end,min_pathss,corrected_edges)
    
    print("\n************** Data for all_max_paths **************")
    print("start:\n{}\n:start\n".format(start))
    print("end:\n{}\n:end\n".format(end))
    print("corrected_edges:\n{}\n:corrected_edges\n".format(str(corrected_edges).replace("[","{").replace("]","}")))
    print("min_path:\n{}\n:min_path\n".format(str(min_pathss))) #.replace("[","{").replace("]","}")
    print("max_path:\n{}\n:max_path\n".format(max_paths))
    print("****************************************************\n")

    f = open("{1}_output.txt", "w")
    f.write("{}\n".format(str(min_pathss)))
    f.write(str(max_paths))
    f.close()

    with open('js/sketch.js') as fin, open('js/template_sketch.js', 'w') as fout:
        for line in fin:
            if 'var max_paths=' in line:
                line = 'var max_paths={}\n'.format(str(max_paths))
            if 'var min_paths=' in line:
                line = 'var min_paths={}\n'.format(str(min_pathss))
            fout.write(line)



main()
#

#Error is in fund
# Input: fund_tri_path([2,4])
# Output:
#357 Hello World [2, 1, 0] My name is Siraj.
#357 Hello World [4, 2, 1] My name is Siraj. #Error Output
#Fix: fund_tri_num(4)
#Error in fund_tri_num(num)


