from playsound import playsound
import time


Genres = ("restart")

first_date = (r"C:\Users\pc\Downloads\Frad - first date.mp3")
the_girl_i_have_a_crush_on = (r"C:\Users\pc\Downloads\Frad - the girl i have a crush on.mp3")
im_so_tired = (r"C:\Users\pc\Downloads\Lauv & Troye Sivan - i'm so tired... [Official Visualizer].mp3")
mean_it = (r"C:\Users\pc\Downloads\Lauv & LANY - Mean It [Official Video].mp3")
there_for_you = (r"C:\Users\pc\Downloads\Martin Garrix & Troye Sivan - There for You (Official Video).mp3")
when_i_was_your_man = (r"C:\Users\pc\Downloads\Bruno Mars - When I Was Your Man (Official Video).mp3")
christmas_is_YOUU = (r"C:\Users\pc\Downloads\All I Want For Christmas Is You X Crank That Soulja Boy - Mariah Carey Soulja Boy.mp3")
kahoot_dreams = (r"C:\Users\pc\Downloads\sweet dreams but i put kahoot music over it but I fixed the tempo.mp3")
my_nocturnal_serenade = (r"C:\Users\pc\Downloads\YOHIO - My Nocturnal Serenade (OFFICIAL MUSIC VIDEO).mp3")
merry_go_round = (r"C:\Users\pc\Downloads\YOHIO - Merry Go Round (OFFICIAL MUSIC VIDEO).mp3")

def LofiQ():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")
        playsound(the_girl_i_have_a_crush_on)
        LofiQM2()
    elif b == "repeat":
        playsound(first_date)
        LofiQ()

    elif b == Genres:
        player()
    else:
        LofiQ()

def LofiQ2():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")

    elif b == "repeat":
        playsound(the_girl_i_have_a_crush_on)
        LofiQ2()

    elif b == Genres:
        player()
    else:
        LofiQ()

def LofiQM():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(first_date)
            LofiQ()
    elif a == "next":
        playsound(the_girl_i_have_a_crush_on)
        LofiQM2()
    elif a == Genres:
        player()
    else:
        LofiQM()

def LofiQM2():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(the_girl_i_have_a_crush_on)
            LofiQ()

    elif a == Genres:
        player()
    else:
        LofiQM2()

def lofi():
    playsound(first_date)
    time.sleep(1)
    LofiQM()

def sad_stuff():
    playsound(when_i_was_your_man)
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(when_i_was_your_man)

def PopQ():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")
        playsound(mean_it)
        PopQM2()

    elif b == "repeat":
        playsound(im_so_tired)
        PopQ()

    elif b == Genres:
        player()
    else:
        PopQ()

def PopQ2():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")
        playsound(there_for_you)
        PopQM3()
    elif b == "repeat":
        playsound(mean_it)
        PopQ2()
    elif b == Genres:
        player()

def PopQ3():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")

    elif b == "repeat":
        playsound(there_for_you)
        PopQ3()
    elif b == Genres:
        player()

def PopQM():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(im_so_tired)
            PopQ()
    elif a == "next":
        playsound(mean_it)
        PopQM2()
    elif a == Genres:
        player()
    else:
        PopQM()

def PopQM2():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(mean_it)
            PopQ2()
    elif a == "next":
        playsound(there_for_you)
        PopQM3()
    elif a == Genres:
        player()
    else:
        PopQM2()

def PopQM3():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(there_for_you)
            PopQ3()

    elif a == Genres:
        player()
    else:
        PopQM3()

def pop():
    playsound(im_so_tired)
    PopQM()

def RandQ():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")
        playsound(christmas_is_YOUU)
        RandQM2()
    elif b == "repeat":
        playsound(kahoot_dreams)
        RandQ()
    elif b == Genres:
        player()
    else:
        RandQ()

def RandQ2():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")

    elif b == "repeat":
        playsound(christmas_is_YOUU)
        RandQ2()
    elif b == Genres:
        player()
    else:
        RandQ2()

def RandQM():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(kahoot_dreams)
            RandQ()
    elif a == "next":
        playsound(christmas_is_YOUU)
        RandQM2()
    elif a == Genres:
        player()
    else:
        RandQM()

def RandQM2():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(christmas_is_YOUU)
            RandQ2()

    elif a == Genres:
        player()
    else:
        RandQM2()

def haha():
    playsound(kahoot_dreams)
    RandQM()

def AltRockQ():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")
        playsound(merry_go_round)
        AltRockQM2()
    elif b == "repeat":
        playsound(my_nocturnal_serenade)
        AltRockQ()
    elif b == Genres:
        player()
    else:
        AltRockQ()

def AltRockQ2():
    b = input("next or repeat?")
    if b == "next":
        print("Understood")

    elif b == "repeat":
        playsound(merry_go_round)
        AltRockQ2()
    elif b == Genres:
        player()
    else:
        AltRockQ2()

def AltRockQM():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(my_nocturnal_serenade)
            AltRockQ()
    elif a == "next":
        playsound(merry_go_round)
        AltRockQM2()
    elif a == Genres:
        player()
    else:
        AltRockQM()

def AltRockQM2():
    a = input("loop or next?")
    if a == "loop":
        while a == "loop":
            playsound(merry_go_round)
            AltRockQ2()

    elif a == Genres:
        player()
    else:
        AltRockQM2()

def altrock():
    playsound(my_nocturnal_serenade)
    AltRockQM()

# H = 450
# W = 400

# def gui():
#  root = Tk()
#  root.title("Musica")
#
#  canvas = Canvas(root, height = H, width = W)
#  canvas.grid()
#
#  frame = Frame(root, bg = "white")
#  frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
#
#  label = Label(frame, text = "what genre playlist would you like to listen to?")
#  label.grid()
#
#  button1 = Button(frame, text = "Pop", command = pop)
#  button1.grid()
#
#  button2 = Button(frame, text = "Lofi", command = lofi)
#  button2.grid()
#
#  button3 = Button(frame, text = "Sad Stuff", command = sad_stuff)
#  button3.grid()
#
#  root.mainloop()

def player():
 print("Lofi, Pop, Sad Stuff, Random, AltRock")
 a = input("what genre playlist would you like to listen to?")

 if a == ("Sad Stuff"):
     sad_stuff()

 if a == ("Lofi"):
     lofi()

 if a == ("Pop"):
     pop()

 if a == ("Random"):
     haha()

 if a == ("AltRock"):
     altrock()

player()
