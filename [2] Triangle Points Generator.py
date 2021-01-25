import math

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

top_down_l=math.sqrt(3)
left_right_l=2

f = open("[0] init.txt", "r")
init_config=[]
for num in range(0,6):
    init_config.append(f.readline())
f.close()

triangle_size=eval(init_config[0].split(":")[1])
length=eval(init_config[3].split(":")[1])
width=eval(init_config[4].split(":")[1])
padding=eval(init_config[5].split(":")[1])
top_down_real=0
left_right_real=0

points_num = (triangle_size + 1) * (triangle_size + 2) / 2

adj_width=width-2*padding
adj_length=length-2*padding

if ((adj_width)/2<(adj_length)/math.sqrt(3)):
    left_right_real=adj_width/triangle_size
    top_down_real=left_right_real/2*math.sqrt(3)
else:
    top_down_real=adj_length/triangle_size
    left_right_real=top_down_real/math.sqrt(3)*2

Points=[]
temp_arr=[]

print(points_num)
for point in range(1,int(points_num+1)):
    if point is 1:
        temp_arr.append([point,[width/2,(width-top_down_real*(layer(points_num)-1))/2]])
    elif layer(temp_arr[0][0])!=layer(point):
        Points=Points+temp_arr
        new_focal_point=[point,[temp_arr[0][1][0]-left_right_real/2,temp_arr[0][1][1]+top_down_real]]
        temp_arr=[new_focal_point]
    else:
        temp_arr.append([point,[temp_arr[-1][1][0]+left_right_real,temp_arr[-1][1][1]]])
    if point==points_num:
        Points=Points+temp_arr

print("\n************** Data for Triangle Path Visualizer **************")
print("points:\n{}\n:points\n".format(Points))
print("***************************************************************\n")

f = open("{2}_output.txt", "w")
f.write(str(Points))
f.close()

with open('js/template_sketch.js') as fin, open('js/sketch.js', 'w') as fout:
    for line in fin:
        if 'var points=' in line:
            line = 'var points={}\n'.format(str(Points))
        if '  createCanvas(' in line:
            line = '  createCanvas({}, {});\n'.format(width,length)
        fout.write(line)

    
        
