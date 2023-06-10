import math
import numpy as np
import pandas as pd
import re

int_2_ascii={
    0:".",
    1:":",
    2:"-",
    3:"[",
    4:"8",
    5:"&",
    6:"$",
    7:"*",
    8:"#",
    9:"M",
    10:"@"
}

# def MathEngine(currx,xdiameter,ydiameter,circlesize):
#     centroidx=xdiameter/2
#     centroidy=ydiameter/2
#     circlesize=int(circlesize)
#     pos=((-((-currx+centroidx)**2)+circlesize**2)**0.5)+centroidy
#     if isinstance(pos,complex):
#         pos=centroidy-pos.imag
#     pos=round(pos)
#     if pos==0:
#         pos=True
#     return pos

def TestMathEngine(x,r):
    expression=-((x-r)**2)+(r**2)
    try:
        return round(expression**0.5)
    except TypeError:
        try: return round((-expression)**0.5)
        except ValueError: return "OOB"
    except ValueError: return "OOB"

def Shader(array):
    for key in reversed(int_2_ascii.keys()):
        for x in range(len(array)-1):
            for y in range(len(array[0])-1):
                if int(array[x,y])<key:
                    if x<=0:
                        minilist=[array[x+1,y],array[x,y+1],array[x,y-1]]
                    else:
                        minilist=[array[x+1,y],array[x-1,y],array[x,y+1],array[x,y-1]]
                    if max(minilist)<key: continue
                    array[x,y]=max(minilist)-1
    return array

def TestEngineWrapper(r):
    arc=[]
    buffer=len(int_2_ascii)-1
    for i in range((r*2)+1): arc.append(TestMathEngine(i,r))
    canvas_y=(max(arc)*2)-1+buffer
    canvas_x=len(arc)
    array=np.zeros((canvas_x+buffer*2,canvas_y)).astype("object")
    for x in range(canvas_x): 
        array[x+buffer,arc[x]]=10
        print(x)
    print(array)
    return array

def Symmetry(array):
    outarray=[]
    for inte in range(len(array)):
        curr=array[inte]
        smallist=np.array(list(reversed(list(curr[1:]))))
        outarray.append(np.append(smallist,curr))
    return outarray

def convert_to_ascii(array):
    for i in range(len(int_2_ascii)):
        array[array==i]=int_2_ascii[i]
    return array

def write_to_html(array,location):
    longinsert=""
    insert='<p style="font-size:8px;line-height:0%">{}</p>\n'
    for line in array:
        longinsert=longinsert+insert.format(" ".join(line))
    boiler="""
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="stylesheet" href="styles.css">
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
    <center>
    {}
    <center>
</body>
</html>
    """
    with open(location,"w") as file:
        file.write(boiler.format(longinsert))


#MathEngine(100)
# def CircleSketch(xdiameter,ydiameter):
#     array=np.zeros((xdiameter,ydiameter)).astype('object')
#     for x in range(100):
#         pos=round(math.sin(x*10))
#         if pos==True:
#             continue
#         array[x,pos]=int_2_ascii[10]
        
#         for inte in range(1,10):
#             if (x-inte>=0) and (array[x-inte,pos] in [0," "]):
#                 array[x-inte,pos]=int_2_ascii[10-inte]
#             if (x+inte<len(array[0])) and (array[x+inte,pos] in [0," "]):
#                 array[x+inte,pos]=int_2_ascii[10-inte]
#     array[array==0]=int_2_ascii[0]
#     return array

array=Symmetry(convert_to_ascii(Shader(TestEngineWrapper(10))))
#print(len(array),len(array[0]))
write_to_html(array,"C:\\Users\\desjardav\\Downloads\\pythonscripts\\test.html")
#df=pd.DataFrame(array)
# df.to_html("C:\\Users\\desjardav\\Downloads\\pythonscripts\\test.html")
# html = re.sub(r'<tr.*>', '<tr>', "C:\\Users\\desjardav\\Downloads\\pythonscripts\\test.html".replace('border="1" ', ''))
# #df.to_html("C:\\Users\\desjardav\\Downloads\\pythonscripts\\test.html")
