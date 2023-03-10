import tkinter as tk
import math
import fastguess
window= tk.Tk()
window.geometry("700x500")
window.config(bg="#a5a5a5")
window.resizable(width=False,height=False)
window.title('GUESSING GAME')
count = 1
guess = 1
max = 0
maxtries = 0



title=tk.Label(window,text="GUESSING GAME",font=("Arial",45),fg="#373fad",bg="#a5a5a5")

display = tk.Label(window,text = "Click on \"PLAY\" button to start a new game", font=("Arial", 10, "normal"),fg = "White", bg = "Black",justify=tk.LEFT)


def yes():
  global logs,count,guess,maxtries
  higher_button.config(state='disabled')
  lower_button.config(state='disabled')
  yes_button.config(state='disabled')
  if count<maxtries:
    display=(f"**************** I won the challenge ****************\nNumber {guess} Guessed in {maxtries} tries \nThank you for playing ")
  else:
   display=("You Won the challenge")
  filename = "logs.txt"

  try:
      file_handle=open(filename)
      lines=file_handle.readlines()
      file_handle.close()
      if not len(lines):
        header="{} : No logs!".format(filename)
      else:
        header="\n ***************** Log Contents *****************\n"
        for l in lines:
          pass
  except:
    header="No stat file"
    display+="\n"+header
  statnow=f'Guess:{guess},count:{count},response:{"yes"}\n'
  display+="\n score:- {}".format(statnow)
  file_handle=open(filename, ("a+"))
  file_handle.write(statnow)
  file_handle.close()
  update_result(display)
 
def play_game():
  global max,maxtries,guess
  challenge_button.config(state='normal')
  max=int(number_form.get())
  max_button.config(state='disabled')
  number_form.config(state='disabled')
  guess=fastguess.fguesser('init',max)
  if max>2:
    maxtries=math.ceil(math.log2(max))
  elif max==2:
    maxtries=1
  challenge="I shall guess within{} tries.".format(maxtries)
  update_result(text="{} \n Click the \ 'CHALLENGE\'button to start the Game".format(challenge))

def high():
    global count,guess,max,maxtries
    count+=1
    guess = fastguess.fguesser('h',max)
    count_left=maxtries-count
    if count_left<0:
      if guess==max:
        display=("You are cheating!!")
    else:    
      display=("Guesses Left : {}\nIs it {}?".format((count_left),guess))
    update_result(display)

def low():
    global count,guess,max,maxtries
    count+=1
    guess = fastguess.fguesser('l',max)
    display= ("Guesses Left : {}\nIs it{}?".format((maxtries-count),guess))
    update_result(display)  
def new_game():
  max_button.config(state='normal')
  number_form.config(state='normal')
  number_form.delete(0,"end")
  global count,guess,max
  count=1
  guess=1
  update_result(text="Please Enter the Maximum Value of your choice")
  max=number_form.get()

def update_result(text):
  display.configure(text=text)
def challenge():
    global guess,count,maxtries
    higher_button.config(state='normal')
    lower_button.config(state='normal')
    yes_button.config(state='normal')
    display=("Guesses Left : {}\
    \nIs it {}?".format((maxtries-count),guess))
    update_result(display)
    challenge_button.config(state='disabled')
 


yes_button = tk.Button(window,text='YES',font=("Arial",9),state="disabled",fg="Black",bg="#1378ab",command=yes)
play_button = tk.Button(window,text="PLAY",font=(("Arial",9,"bold")),fg="Black",bg="#07aa07",command=new_game)
higher_button=tk.Button(window,text="HIGHER",font=("Arial",9),state='disabled',fg="Black",bg="#2231b5",command=high)
lower_button = tk.Button(window,text="LOWER",font=("Arial",9),state='disabled',fg="Black",bg="#2231b5",command=low)
max_button=tk.Button(window,text="MAXIMUM VALUE",font=("Arial",9),state='disabled',fg="Black",bg="#4144e6",command=play_game)
challenge_button=tk.Button(window,text='CHALLENGE',font=("Arial",9),state='disabled',fg="Black",bg="#4144e6",command=challenge)
exit_button=tk.Button(window,text="EXIT",font=("Arial",9,"bold"),fg="Black",bg="#ff0000",command=exit)


max=tk.StringVar()
number_form=tk.Entry(window,font=("Arial",9),textvariable=max,width=15)
number_form.config(state="disabled")


title.place(x=90, y=30)
display.place(x=100, y=250)


#Place of button
exit_button.place(x=340,y=160)
play_button.place(x=265,y=160)
challenge_button.place(x=350,y=210)
max_button.place(x=180,y=210)
higher_button.place(x=385,y=370)
lower_button.place(x=150,y=370)
yes_button.place(x=280,y=370)
number_form.place(x=270, y=125)
window.mainloop
