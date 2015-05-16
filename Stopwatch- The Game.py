# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

message = "Welcome!"
interval = 100
time=0
score=0
total_stop=0


# Handler for mouse click
def start():
    timer.start()

def stop():
    global time,score,total_stop
    if(time>600):
        #算出分
        minute=time/600
        temp=time%600
        #算出毫秒
        Millisecond=temp%100%10
        if(Millisecond==0):
            score+=1
            total_stop+=1
        else:
            total_stop+=1

    else:
        temp=time%600
        
        #算出毫秒
        Millisecond=temp%100%10
        
        if(Millisecond==0):
            score+=1
            total_stop+=1
        else:
            total_stop+=1
        
    timer.stop()
    
def clare():
    global time,score,total_stop
    score=0
    total_stop=0
    time=0
    
# Handler for timer
def tick():
    global time
    time+=1
    
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(format(time), [50,112], 36, "Red")
    canvas.draw_text(str(score)+"/"+str(total_stop), [70,40], 36, "white")


    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Clare", clare)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)


# Start the frame animation
frame.start()

#格式
def format(time):
    minute=0
    second=0
    if(time>600):
        #算出分
        minute=time/600
        temp=time%600
        #算出毫秒
        Millisecond=temp%100%10
        
        #算出秒
        second=temp/10
        
        #如果秒小於10就多補0
        if(second<10):
            result=str(minute)+":0"+str(second)+"."+str(Millisecond)
        else:
            result=str(minute)+":"+str(second)+"."+str(Millisecond)

        return result
    else:
        temp=time%600
        
        #算出毫秒
        Millisecond=temp%100%10
        
        #算出秒
        second=temp/10

        #如果秒小於10就多補0
        if(second<10):
            result=str(minute)+":0"+str(second)+"."+str(Millisecond)
        else:
            result=str(minute)+":"+str(second)+"."+str(Millisecond)
        return result

