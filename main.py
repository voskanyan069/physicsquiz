# Imports
from tkinter import *
from datetime import datetime
from tkinter.messagebox import *
from tkinter import simpledialog

# Scores array
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

font = "Arial"


# Alert Links and Copy it to Clipboard
def Alert(title, text):
    alert = Tk()

    alert.geometry("300x100")
    alert.resizable(False, False)
    alert.title(title)

    link = Button(alert, text=text, width=35, height=5)
    link.configure(borderwidth=0)
    link.grid(row=0, column=0)

    text = text
    alert.clipboard_clear()
    alert.clipboard_append(text)
    clip_text = alert.clipboard_get()

    alert.mainloop()


# Menu of the Game Start
def Menu():
    # Window settings
    menu = Tk()

    menu.geometry("900x600")
    menu.resizable(False, False)
    menu.title("Ֆիզիկաի Հացաշար")

    def btn_start_func(event):
        menu.destroy()
        Questions()

    def btn_info_func(event):
        showinfo('Խաղի մասին', '1. Խաղը ֆիզիկա առարկայի մասին է\n'
                               '2. «Մարմինների փոխազդեցութիւն» եւ «Նիւտոնի \n աւրենքները» թեմաներով\n'
                               '3. Բոլոր թուերը գրել թուերով\n'
                               '4. Սկսել մեծատառով\n'
                               '5․ Վերջակէտ չդնել')

    def btn_feedback_func(event):
        showinfo('Յետադարձ կապ', 'Խաղի ստեղծողը։ Անդրանիկ Ոսկանեան\n'
                                 'Հարցերի եւ առաջարկների համար\n'
                                 'կարող էք կապուել այս էլ․ հասցէին\n'
                                 'andranik.voskanyan@realschool.am')

    mini_title = Button(menu, text="Ֆիզիկա", width=40, height=2, background="#0e263d", foreground="#fff",
                        font=(font, 30))
    mini_title.place(relx=0, rely=0)

    btn_start = Button(menu, text="Սկսել", width=15, height=2, background="#1d2228", foreground="#fb8122",
                       font=(font, 16))
    btn_start.place(relx=.38, rely=.35)
    btn_start.bind("<Button-1>", btn_start_func)

    btn_info = Button(menu, text="Ինֆորմացիայ", width=20, height=2, background="#1d2228", foreground="#fb8122",
                      font=(font, 16))
    btn_info.place(relx=.35, rely=.48)
    btn_info.bind("<Button-1>", btn_info_func)

    btn_feedback = Button(menu, text="Յետադարձ կապ", width=25, height=2, background="#1d2228", foreground="#fb8122",
                          font=(font, 16))
    btn_feedback.place(relx=.32, rely=.61)
    btn_feedback.bind("<Button-1>", btn_feedback_func)

    # # YouTube Alert
    # def yt(event):
    #     Alert("YouTube", "https://youtube.com\n"
    #                      "Link are copied to clipboard")

    # YouTube button
    # try:
    #     ytPhotoOriginal = PhotoImage(file=r"res/yt.png")
    #     ytPhoto = ytPhotoOriginal.subsample(5)
    #     ytImgBtn = Button(menu, image=ytPhoto)
    #     ytImgBtn.place(relx=.93, rely=.9)
    #     ytImgBtn.bind("<Button-1>", yt)
    # except Exception as e:
    #     showwarning(title='Files and folders', message='Please don\'t touch files and folders')  # , **options)


    # Menu Window Launch
    menu.mainloop()


def Questions():
    # Window settings
    root = Tk()

    root.geometry("900x600")
    root.resizable(False, False)
    root.title("Ֆիզիկաի Հացաշար")

    # Information
    def information(event):
        info = Tk()
        info.geometry("600x400")
        info.resizable(False, False)
        info.title('Ինֆորմացիայ')

        infoInfoTitle = Label(info, text='Ինֆորմացիայ', font=(font, 20))
        infoInfoTitle.place(relx=.33, rely=.05)

        infoCreator = Label(info,
                            text='Խաղի ստեղծողը։ Անդրանիկ Ոսկանյան\nՀարցերի եւ առաջարկների համար\nկարող եք կապուել այս էլ․ հասցէին\nandranik.voskanyan@realschool.am',
                            font=(font, 12))
        infoCreator.place(relx=.2, rely=.15)

        infoGameTitle = Label(info, text='Խաղի մասին', font=(font, 20))
        infoGameTitle.place(relx=.33, rely=.45)

        infoGameText = Label(info,
                             text='1. Խաղը ֆիզիկա առարկայի մասին է\n2. «Մարմինների փոխազդեցութիւն» եւ «Նիւտոնի \n աւրենքները» թեմաներով\n3. Բոլոր թուերը գրել թուերով\n4. Սկսել մեծատառով\n5․ Վերջակէտ չդնել',
                             font=(font, 12))
        infoGameText.place(relx=.15, rely=.55)

    # Home
    def home(event):
        root.destroy()
        Menu()

    # Questions
    def ask_question1(event):
        answer = askquestion("Հարց 1",
                             "Թիթեղը ճկուած եւ կապուած է թելով։ Սայլակը սեղանի նկատմամբ գտնուում է դադարի վիճակում։ Կը սկսի՞ արդեօք շարժուել սայլակը, եթէ թիթեղը կտրուկ ուղղուի։")
        if answer == 'no':
            scores[0] = 5
        else:
            scores[0] = -1

    def ask_question2(event):
        answer = askquestion("Հարց 2",
                             "Եթէ ֆուտբոլիստը վազելով բախուում է այլ ֆուտբոլիստի, երկուսի արագութիւնն էլ փոխուու՞մ է։")
        if answer == 'yes':
            scores[1] = 5
        else:
            scores[1] = -1

        
    def ask_question3(event):
        answer = simpledialog.askstring("Հարց 3",
                                        "Եթէ փոխազդեցութեան ժամանակ մի մարմին իր արագութիւնն աւելի քիչ է փոխում, քան միւսը, ասում են, որ այն աւելի ․․․ է։")
        if answer.lower() == 'իներտ':
            scores[2] = 5
        else:
            scores[2] = -1

    def ask_question4(event):
        answer = simpledialog.askstring("Հարց 4",
                                        "Մարմնի իներտութեան քանակական չափը անուանում են ․․․։")
        if answer.lower() == 'զանգուած':
            scores[3] = 5
        elif answer.lower() == 'զանգված':
            scores[3] = 5
        else:
            scores[3] = -1

    def ask_question5(event):
        answer = askquestion("Հարց 5",
                                        "Որքան իներտ է մարմինը, այնքան փոքր է նրա զանգուածը։")
        if answer == 'no':
            scores[4] = 5
        else:
            scores[4] = -1

    def ask_question6(event):
        answer = askquestion("Հարց 6",
                                        "Եթէ մի մարմնի զանգուածը յայտնի լինի, կարելի՞ է փորձի միջոցով չափել միւսի զանգուածը։")
        if answer == 'yes':
            scores[5] = 5
        else:
            scores[5] = -1

    def ask_question7(event):
        answer = simpledialog.askstring("Հարց 7",
                                        "․․․ մեխանիկայի այն բաժինն է, որն ուսումնասիրում է մեխանիկական շարժման առաջացման պատճառները։")
        if answer.lower() == 'դինամիկան':
            scores[6] = 5
        else:
            scores[6] = -1

    def ask_question8(event):
        answer = simpledialog.askstring("Հարց 8",
                                        "Նիւտոնի աւրենքների քանակը")
        if answer == '3':
            scores[7] = 5
        elif answer.lower() == 'երեք':
            scores[7] = 5
        else:
            scores[7] = -1

    def ask_question9(event):
        answer = askquestion("Հարց 9",
                                        "Եթէ մարմնի վրայ այլ մարմիններ չեն ազդում, ապա այն չի պահպանում իր դադարի կամ ուղղագիծ հաւասարաչափ շարժման վիճակը։")
        if answer == 'no':
            scores[8] = 5
        else:
            scores[8] = -1

    def ask_question10(event):
        answer = askquestion("Հարց 10",
                                        "Եթէ մարմնի վրայ սկսում է ինչ֊որ ուժ ազդել, նրա դադարի վիճակը խախտուում է։")
        if answer == 'yes':
            scores[9] = 5
        else:
            scores[9] = -1

    def ask_question11(event):
        answer = askquestion("Հարց 11",
                                        "Մարմնի շարժման արագացման պատճառը նրա վրայ ազդող ուժն չէ։")
        if answer == 'no':
            scores[10] = 5
        else:
            scores[10] = -1

    def ask_question12(event):
        answer = simpledialog.askstring("Հարց 12",
                                        "Դադարի վիճակում գնուող մարմինների փոխազդեցութեան հետեւանքով նրանց ձեռք բերած արագութիւնները եւ զանգուածները կապուած են (բանաձեւ) առնչութեամբ։")
        if answer == 'm1V1 = m2V2':
            scores[11] = 5
        elif answer == 'm1V1 = m2V2':
            scores[11] = 5
        elif answer == 'm1 V1 = m2 V2':
            scores[11] = 5
        elif answer == 'm1V1=m2V2':
            scores[11] = 5
        elif answer == 'm1 V1=m2 V2':
            scores[11] = 5
        if answer == 'm 1 V 1 = m 2 V 2':
            scores[11] = 5
        elif answer == 'm 1 V 1 = m 2 V 2':
            scores[11] = 5
        elif answer == 'm 1 V 1 = m 2 V 2':
            scores[11] = 5
        elif answer == 'm 1 V 1=m 2 V 2':
            scores[11] = 5
        elif answer == 'm 1 V 1=m 2 V 2':
            scores[11] = 5
        else:
            scores[11] = -1

    def ask_question13(event):
        answer = simpledialog.askstring("Հարց 13",
                                        "Որերո՞րդ աւրենքն է գրուած։ Մարմինները միմեանց հետ փոխազդում են նոյն բնոյթի՝ մոդուլով հաւասար եւ ուղղութեամբ հակադիր ուժերով։")
        if answer == '3':
            scores[12] = 5
        elif answer.lower() == '3-րդ':
            scores[12] = 5
        elif answer.lower() == 'երրորդ':
            scores[12] = 5
        else:
            scores[12] = -1

    def ask_question14(event):
        answer = simpledialog.askstring("Հարց 14",
                                        "Որերո՞րդ աւրենքն է գրուած։ Ամէն մի մարմին շարունակում է պահպանել դադարի կամ հաւասարաչափ ուղղագիծ շարժման վիճակը, քանի դեռ հարկադրուած չէ փոփոխել այդ վիճակը կիրառուած ուժերի ազդեցութեամբ:")
        if answer == '1':
            scores[13] = 5
        elif answer.lower() == '1-ին':
            scores[13] = 5
        elif answer.lower() == 'առաջին':
            scores[13] = 5
        else:
            scores[13] = -1

    def ask_question15(event):
        answer = simpledialog.askstring("Հարց 15",
                                        "Որերո՞րդ աւրենքն է գրուած։ Մարմնի վրայ ազդող ուժի ազդեցութեամբ նրա ձեռք բերած արագացումը հաւասար է այդ ուժի եւ մարմնի զանգուածի յարաբերութեանը։")
        if answer == '2':
            scores[14] = 5
        elif answer.lower() == '2-րդ':
            scores[14] = 5
        elif answer.lower() == 'երկրորդ':
            scores[14] = 5
        else:
            scores[14] = -1

    def ask_question16(event):
        answer = simpledialog.askstring("Հարց 16",
                                        "... այն է, որ մարմինը պահպանում ոչ միայն իր արագութիւնը այլ նաեւ մարմինների ազդեցութեան բացակայութեան։")
        if answer.lower() == 'ընդհանրացում':
            scores[15] = 5
        else:
            scores[15] = -1

    def ask_question17(event):
        answer = simpledialog.askstring("Հարց 17",
                                        "Մարմնի վրայ տարբեր ուժերի ազդեցութիւնների արդիւնքը ․․․։")
        if answer.lower() == 'տարբեր':
            scores[16] = 5
        elif answer.lower() == 'տարբեր է':
            scores[16] = 5
        else:
            scores[16] = -1

    def ask_question18(event):
        answer = simpledialog.askstring("Հարց 18",
                                        "Եթէ մարմնի վրայ միաժամանակ ազդում է մի քանի ուժ, ապա բանաձեւում F-ը դրանց ․․․ է։")
        if answer.lower() == 'համազոր':
            scores[17] = 5
        elif answer.lower() == 'համազորն':
            scores[17] = 5
        elif answer.lower() == 'համազօր':
            scores[17] = 5
        elif answer.lower() == 'համազօրն':
            scores[17] = 5
        else:
            scores[17] = -1

    def ask_question19(event):
        answer = simpledialog.askstring("Հարց 19",
                                        "Ուժերը, որոնցով մարմինները փոխազդում են միմեանց հետ, մոդուլով ․․․ են, իսկ ուղղութեամբ՝ ․․․։ (աւրինակ, աւրինակ)")
        if answer.lower() == 'հաւասար, հակադիր':
            scores[18] = 5
        elif answer.lower() == 'հավասար, հակադիր':
            scores[18] = 5
        elif answer.lower() == 'հաւասար,հակադիր':
            scores[18] = 5
        elif answer.lower() == 'հավասար,հակադիր':
            scores[18] = 5
        else:
            scores[18] = -1

    def ask_question20(event):
        answer = askquestion("Հարց 20",
                                         "Ճիշտ է արդեօք, որ Նիւտոնի երրորդ աւրենքից բխում է, որ ինչ ուժով մարդը քաշում է սահնակը, նոյն ուժով սահնակը նրան յետ է քաշում։")
        if answer == 'yes':
            scores[19] = 5
        else:
            scores[19] = -1

    def check(event):
        # Try sum scores for info
        try:
            # scores_summ = scores[0:20]
            scores_res = sum(scores)
        # if don't working :(
        except Exception as e:
            pass

        # Scores info
        showinfo("Միաւորներ", "Դուք հաւաքել եք " + str(scores_res) + " միաւոր")
        root.destroy()

    # Info button
    try:
        infoPhotoOriginal = PhotoImage(file=r"res/info_2.png")
        infoPhoto = infoPhotoOriginal.subsample(2)
        infoImgBtn = Button(root, image=infoPhoto)
        infoImgBtn.place(relx=.02, rely=.03)
        infoImgBtn.bind("<Button-1>", information)
    except Exception as e:
        showwarning(title='Files and folders', message='Please don\'t touch files and folders')  # , **options)

        infoBtn = Button(root, text='Ինֆորմացիայ')
        infoBtn.place(relx=.01, rely=.03)
        infoBtn.bind("<Button-1>", information)

    # Home button
    try:
        homePhotoOriginal = PhotoImage(file=r"res/home.png")
        homePhoto = homePhotoOriginal.subsample(2)
        homeImgBtn = Button(root, image=homePhoto)
        homeImgBtn.place(relx=.9, rely=.03)
        homeImgBtn.bind("<Button-1>", home)
    except Exception as e:
        showwarning(title='Files and folders', message='Please don\'t touch files and folders')  # , **options)

        homeBtn = Button(root, text='Յետ')
        homeBtn.place(relx=.9, rely=.03)
        homeBtn.bind("<Button-1>", home)

    # Mini title
    label_title = Label(root, text="Ֆիզիկաի հարցաշար", font=(font, 30))
    label_title.place(relx=.25, rely=.03)

    # Buttons X 1
    btn_question1 = Button(root, text="1", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question1.place(relx=.15, rely=.15)
    btn_question1.bind("<Button-1>", ask_question1)

    btn_question2 = Button(root, text="2", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question2.place(relx=.3, rely=.15)
    btn_question2.bind("<Button-1>", ask_question2)

    btn_question3 = Button(root, text="3", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question3.place(relx=.45, rely=.15)
    btn_question3.bind("<Button-1>", ask_question3)

    btn_question4 = Button(root, text="4", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question4.place(relx=.6, rely=.15)
    btn_question4.bind("<Button-1>", ask_question4)

    btn_question5 = Button(root, text="5", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question5.place(relx=.75, rely=.15)
    btn_question5.bind("<Button-1>", ask_question5)

    # Buttons X 2
    btn_question6 = Button(root, text="6", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question6.place(relx=.15, rely=.35)
    btn_question6.bind("<Button-1>", ask_question6)

    btn_question7 = Button(root, text="7", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question7.place(relx=.3, rely=.35)
    btn_question7.bind("<Button-1>", ask_question7)

    btn_question8 = Button(root, text="8", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question8.place(relx=.45, rely=.35)
    btn_question8.bind("<Button-1>", ask_question8)

    btn_question9 = Button(root, text="9", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question9.place(relx=.6, rely=.35)
    btn_question9.bind("<Button-1>", ask_question9)

    btn_question10 = Button(root, text="10", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question10.place(relx=.75, rely=.35)
    btn_question10.bind("<Button-1>", ask_question10)

    # Buttons X 3
    btn_question11 = Button(root, text="11", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question11.place(relx=.15, rely=.55)
    btn_question11.bind("<Button-1>", ask_question11)

    btn_question12 = Button(root, text="12", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question12.place(relx=.3, rely=.55)
    btn_question12.bind("<Button-1>", ask_question12)

    btn_question13 = Button(root, text="13", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question13.place(relx=.45, rely=.55)
    btn_question13.bind("<Button-1>", ask_question13)

    btn_question14 = Button(root, text="14", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question14.place(relx=.6, rely=.55)
    btn_question14.bind("<Button-1>", ask_question14)

    btn_question15 = Button(root, text="15", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question15.place(relx=.75, rely=.55)
    btn_question15.bind("<Button-1>", ask_question15)

    # Buttons X 4
    btn_question16 = Button(root, text="16", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question16.place(relx=.15, rely=.75)
    btn_question16.bind("<Button-1>", ask_question16)

    btn_question17 = Button(root, text="17", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question17.place(relx=.3, rely=.75)
    btn_question17.bind("<Button-1>", ask_question17)

    btn_question18 = Button(root, text="18", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question18.place(relx=.45, rely=.75)
    btn_question18.bind("<Button-1>", ask_question18)

    btn_question19 = Button(root, text="19", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question19.place(relx=.6, rely=.75)
    btn_question19.bind("<Button-1>", ask_question19)

    btn_question20 = Button(root, text="20", width=5, height=3, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_question20.place(relx=.75, rely=.75)
    btn_question20.bind("<Button-1>", ask_question20)

    # Button for Results Check
    btn_check = Button(root, text="Ստուգել", width=7, height=1, background="#1d2228", foreground="#fb8122", font=(font, 16))
    btn_check.place(relx=.435, rely=.92)
    btn_check.bind("<Button-1>", check)

    # Root Window Launcher
    root.mainloop()


# Launch all app
Menu()
