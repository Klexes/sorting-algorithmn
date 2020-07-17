from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort
from mergeSort import merge_sort

root = Tk()
root.title('Sorting Algorithm Visulaiser')
root.maxsize(900,600)  # sets the maximum size even after the expansion of the window
root.config(bg='grey') # main background of the window 

#variables
selected_alg = StringVar()  # set the text in tkinter
data = [] # empty data list

def drawData(data, colorArray): # draws the data into the canvas
    canvas.delete('all')
    c_height = 380
    c_width = 600
    x_width = c_width/(len(data)+1)
    offset = 150/len(data)
    spacing  = 10
    normalizedData = [i/max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height *340

        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0, anchor =SW, text = str(data[i]))

    root.update_idletasks() # blanking the screen


def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minVal,maxVal+1))
    

    drawData(data, ['purple' for x in range(len(data))])

def satrtAlgo():
    global data
    if not data:return
    if(algMenu.get() == 'Quick Sort'):
        quick_sort(data,0,len(data)-1,drawData,speedScale.get())
    elif (algMenu.get() == 'Bubble Sort'):
        bubble_sort(data, drawData,speedScale.get())
    elif (algMenu.get() == 'Merge Sort'):
        merge_sort(data,drawData,speedScale.get())
    drawData(data, ['green' for x in range(len(data))])

#frame
UI_frame = Frame(root, width = 600, height =200, bg='grey')  # root means the main window and frame is the spot where all the widgets are placed
UI_frame.grid(row =0, column = 0, padx = 10, pady =5) # table like form

canvas = Canvas(root, width = 600, height =380 , bg='white') # similar to the Frame
canvas.grid(row = 1, column=0,padx = 10, pady =5)

# UI area
# row[0]
Label(UI_frame, text = 'Algorithm :', bg='grey').grid(row =0, column=0,padx =5, pady=5,sticky = W) # creates a algorithm box in the frame
algMenu = ttk.Combobox(UI_frame,textvariable =selected_alg, values=['Bubble Sort', 'Merge Sort','Quick Sort']) # creates the dropdown menu
algMenu.grid(row = 0, column = 1,padx =5,pady =5) # sets the position in the frame
algMenu.current(0) # default element in the dropdown

speedScale = Scale(UI_frame, from_=0.1, to=2.0,length =200,digits=2,resolution = 0.2,orient = HORIZONTAL,label = 'Select Speed [s]')
speedScale.grid(row=0, column=2,padx=5,pady=5)
Button(UI_frame, text='Start', command=satrtAlgo, bg='pink').grid(row=0,column=2,padx =5,pady =5) # creates a button named Generate

#row[1]

# Label(UI_frame, text = 'Size ', bg='Grey').grid(row=1,column=0,padx=5,pady=5,sticky=W)
sizeEntry =  Scale(UI_frame, from_=3, to=25,resolution = 1,orient = HORIZONTAL, label= 'Data Size') 
sizeEntry.grid(row=1,column=0,padx=5,pady=5)

# Label(UI_frame, text = 'Min Value ', bg='Grey').grid(row=1,column=2,padx=5,pady=5,sticky=W)
minEntry = Scale(UI_frame, from_=0, to=10,resolution = 1,orient = HORIZONTAL, label ='Min Value') 
minEntry.grid(row=1,column=1,padx=5,pady=5)

# Label(UI_frame, text = 'Max Value ', bg='Grey').grid(row=1,column=4,padx=5,pady=5,sticky=W)
maxEntry =  Scale(UI_frame, from_=3, to=50,resolution = 1,orient = HORIZONTAL, label = 'Max Value') 
maxEntry.grid(row=1,column=2,padx=5,pady=5)


Button(UI_frame, text='Generate', command=Generate, bg='turquoise').grid(row=1,column=3,padx =5,pady =5) # creates a button named Generate

root.mainloop() # runs the code

# the command function in the button sets the function to be called when the button is being clicked