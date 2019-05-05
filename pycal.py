#SIMPLE CALCULATOR SYSTEM USING PYTHON CODES WITH EXPLANATION
 #!/usr/bin/env python 
 #---------------------------------------------------------------------------------------------------------------- 
 # SIMPLE CALCULATOR SYSTEM in Python 
 # Tested with Python 3.6.3 # --------------------------------------------------------------------------------------------------------------------- 
 # Import the math module for root,factorial,sin,cos and tan calculation 
 import math
 # Import all the components from tkinter 
 from tkinter import* 
# ---------------------------------------------------------------------------------------------------------------
 # Creat the root window 
 root = Tk()
 # Set the window size 
 root.geometry("1500x600") 
# Set window title 
root.title("Scientific Calculator")
 # Set the background colour of window 
root.configure(background = 'blue')
 # -------------------------------------Set the title bar----------------------------------------------------- 
 # bd = Border width in pixels. Default is 2. 
 # Raise is used to express the 3-D effects of the text 
 Tops = Frame(root, width = 1000, height = 50, bd = 12, relief = "raise") 
 # side = top indicates the top site of the window 
 Tops.pack(side = TOP) 
 # -------------------------Set the left and right portion of the window---------------------------- 
 # Set the Left side of the window 
 inBotto1 = Frame(root, width = 900, height = 600, bd = 10, bg = "pink", relief ="raise") 
 inBotto1.pack(side=LEFT) 
 # Right side of the window 
 inBotto2 = Frame(root, width = 600, height = 600, bd = 10, relief ="raise") 
 inBotto2.pack(side=RIGHT) 
 #--------------------------------------------------------------------------------------------------------- 
 Tops.configure(background = 'black') 
 inBotto2.configure(background = 'black') 
 # ("Helvetica", "50") for a 50-point Helvetica regular. 
 # Anchors are used to define where text is positioned... 
 lblInfo = Label(Tops, font = ('Helvetica', 70, 'bold'), text = "Simple Calculator System", bd = 16, anchor = 'w') 
 # Relative to a reference point.Here w = 'west' corner of the window 
 lblInfo.grid(row = 0, column = 0) 
 # -------------------------Function perform the different calculation---------------------------- 
 def Sum(): 
 # For ADDITION calculation 
     if var.get() == 1: 
         Qty1 = float(firstnumber.get()) 
         Qty2 = float(secondnumber.get()) 
         Sumup = Qty1 + Qty2 
         Total.set(Sumup) 
 # For SUBSTRUCTION calculation 
     elif var.get() == 2: 
         Qty1 = float(firstnumber.get()) 
         Qty2 = float(secondnumber.get()) 
         Sumup = Qty1 - Qty2 
         Total.set(Sumup) 
 # For MULTIPLICATION calculation 
     elif var.get() == 3: 
         Qty1 = float(firstnumber.get()) 
         Qty2 = float(secondnumber.get()) 
         Sumup = Qty1 * Qty2 
         Total.set(Sumup) 
  # For DIVISION calculation 
      elif var.get() == 4: 
          Qty1 = float(firstnumber.get()) 
          Qty2 = float(secondnumber.get()) 
          Sumup = Qty1 / Qty2 
          Total.set(Sumup) 
  # For MODULO DIVISION 
      elif var.get() == 5: 
          Qty1 = float(firstnumber.get()) 
          Qty2 = float(secondnumber.get()) 
          Sumup = Qty1 % Qty2
          Total.set(Sumup) 
  # For EXPONENTIAL calculation 
      elif var.get() == 6: 
          Qty1 = float(firstnumber.get()) 
          Qty2 = float(secondnumber.get()) 
          Sumup = Qty1 ** Qty2 
          Total.set(Sumup) 
   # For FLOOR DIVISION calculation 
       elif var.get() == 7: 
           Qty1 = float(firstnumber.get()) 
           Qty2 = float(secondnumber.get()) 
           Sumup = Qty1 // Qty2 
           Total.set(Sumup) 
   # For LOGARITHM calculation(Here only the first number column is used) 
       elif var.get() == 8: 
           Qty1 = float(firstnumber.get()) 
           Sumup = math.log(Qty1) 
           Total.set(Sumup) 
   # For DECIMAL -> BINARY conversation(Here only the first number column is used) 
       elif var.get() == 9: 
           Qty1 = float(firstnumber.get()) 
           # Call the binary() function 
           Sumup = binary(Qty1) 
           Total.set(Sumup) 
   # For SQUARE ROOT of number(Here only the first number column is used) 
           elif var.get() == 10: 
               Qty1 = float(firstnumber.get()) 
               Sumup = math.sqrt(Qty1) 
               Total.set(Sumup) 
   # For FACTORIAL(Here only the first number column is used) 
           elif var.get() == 11: 
               Qty1 = float(firstnumber.get()) 
               Sumup = factorial(Qty1) 
               Total.set(Sumup) 
    # For SINE value of degree(Here only the first number column is used) 
           elif var.get() == 12: 
               Qty1 = float(firstnumber.get()) 
               Sumup = math.sin(math.radians(Qty1)) 
               Total.set(Sumup) 
    # For COSINE value of degree 
           elif var.get() == 13: 
               Qty1 = float(firstnumber.get())
               Sumup = math.cos(math.radians(Qty1)) 
               Total.set(Sumup) 
    # For TANGENT value of degree 
           elif var.get() == 14: 
               Qty1 = float(firstnumber.get()) 
               Sumup = math.tan(math.radians(Qty1)) 
               Total.set(Sumup) 
     # For PARCENTAGE calculation 
           elif var.get() == 15: 
               Qty1 = (firstnumber.get()) 
               Qty2 = (secondnumber.get()) 
               Sumup = (Qty2/Qty1) * 100 
               Total.set(Sumup) 
     # FUNCTION for evaluate the factorial of a number 
            def factorial(n): 
                if n == 0: 
                    return 1 
                else: 
                    return n * factorial(n-1) 
     # the function which is called from 
            elif var.get() == 9: 
                def binary(f): 
                    if f >= 1: 
                        g = int(math.log(f, 2)) 
                    else: 
                        g = -1 
                        h = g + 1 
                        ig = math.pow(2, g) 
                        st = " " 
                        while f > 0 or ig >= 1: 
                            if f < 1: 
                                if len(st[h:]) >= 10: 
                                # 10 fractional digits max break 
                                if f >= ig: 
                                    st += "1" 
                                    f -= ig 
                                else: 
                                    st += "0" 
                                    ig /= 2 
                                    st = st[:h] + "." + st[h:] 
                            return st 
    # FUNCTION that set 1st, 2nd and Total as '0.0' if the RESET button is pressed 
           def Reset(): 
               firstnumber.set("0.0") 
               secondnumber.set("0.0")
               Total.set("0.0") 
               # Function show a meggagebox that ask the user if he wants to exit.. 
           def Exit(): 
           # if the EXIT button is pressed 
               qExit = messagebox.askyesno("System","Do you want to exit ?") 
               if qExit > 0: 
                   # root.destroy() --> use for closing the window screen 
                   root.destroy() 
                   return 
            # ----------------------------------------------------------------------------------------------------- 
     # Create a tkinter() variable of Integer type 
           var = DoubleVar() 
           firstnumber = DoubleVar() 
           secondnumber = DoubleVar() 
           Total = DoubleVar() 
     # ---------------------------Radio Buttons for different operation--------------------- 
           rb1 = Radiobutton(inBotto1, text = "Addition", variable = var, value = 1, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 0, column = 0, sticky = W) 
           rb2 = Radiobutton(inBotto1, text = "Substraction", variable = var, value = 2 bg = "pink", font = ('Helvetica', 21, 'bold')) .grid(row = 1, column = 0, sticky = W) 
           rb3 = Radiobutton(inBotto1, text = "Multiplication", variable = var, value = 3 bg = pink , font = ( Halvetica , , 21 bold ) .grid(row = 2, column = 0, sticky = W) 
           rb4 = Radiobutton(inBotto1, text = "Division", variable = var, value = 4, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 3, column = 0, sticky = W) 
           rb5 = Radiobutton(inBotto1, text = "Modulus", variable = var, value = 5, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 4, column = 0, sticky = W) 
           rb6 = Radiobutton(inBotto1, text = "Exponent", variable = var, value = 6, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 0, column = 1, sticky = W) 
           rb7 = Radiobutton(inBotto1, text = "Floor Division", variable = var, value = 7, bg = pink , font = ('Helvetica', 21, 'bold')) .grid(row = 3, column = 1, sticky =W) 
           rb8 = Radiobutton(inBotto1, text = "Logarithm", variable = var, value = 8, bg = pink font = ('Helvetica', 21, 'bold')) .grid(row = 2, column = 1, sticky =W) 
           rb9 = Radiobutton(inBotto1, text = "Binary", variable = var, value = 9, bg = "pink",font = ('Helvetica', 21, 'bold')).grid(row = 4, column = 1, sticky =W) 
           rb10 = Radiobutton(inBotto1, text = "Root", variable = var, value = 10, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 1, column = 1, sticky =W) 
           rb11 = Radiobutton(inBotto1, text = "Factorial", variable = var, value = 11, bg = "pink", font = ('Helvetica', 21, 'bold')) .grid(row = 0, column = 2, sticky =W) 
           rb12 = Radiobutton(inBotto1, text = "Sine", variable = var, value = 12, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 2, column = 2, sticky =W) 
           rb13 = Radiobutton(inBotto1, text = "Cosine", variable = var, value = 13, bg = "pink", font = ('Helvetica', 21, 'bold')).grid(row = 3, column = 2, sticky =W) 
           rb14 = Radiobutton(inBotto1, text = "Tangant", variable = var, value = 14, bg = pink , font = ('Helvetica', 21, 'bold')) .grid(row = 4, column = 2, sticky =W) 
           rb15 = Radiobutton(inBotto1, text = "Percentage", variable = var, value = 15, bg = pink , font = ('Helvetica', 21, 'bold')) .grid(row = 1, column = 2, sticky =W) 
           # -----------------------------Set first, second and total column--------------------------- 
           lblfirstnumber = Label(inBotto1, font = ('Helvetica',23, 'bold'), text = "Enter First Number", bg = "pink", fg = "black", bd = 16) .grid(row = 5, column = 0, sticky = W) 
           textfirstnumber = Entry(inBotto1, font = ('Helvetica',23, 'bold'), bd = 4, width = 13, bg = "orange , textvariable = firstnumber) .grid(row = 5, column = 1, sticky = W) 
           lblsecondnumber = Label(inBotto1, font = ('Helvetica', 23, 'bold') , text = "Enter Second Number", bg = "pink", fg = "black", bd = 16) 
           lblsecondnumber.grid(row = 6, column = 0, sticky = W) 
           textsecondnumber = Entry(inBotto1, font = ('Helvetica', 23, 'bold'), bd = 4, width = 13, bg = "orange", textvariable = secondnumber) .grid(row = 6, column = 1, sticky = W) 
           lblTotal = Label(inBotto1, font = ('Helvetica', 23, 'bold'), text = "Answer", fg = "black", bg = "pink", bd = 16, justify = "left") 
           lblTotal.grid(row = 7, column = 0, sticky = W) 
           lblAnswer = Label(inBotto1,font = ('Helvetica', 23, 'bold'), bd = 4, width = 20,bg = "orange", textvariable = Total, relief ='sunken') .grid(row = 7, column = 1, sticky = W) 
           # -----------------------------Set the Result, Reset and Exit Button--------------------------- 
           btnTotal = Button(inBotto2, pady = 8, bd = 8, fg = "black", font = ('Helvetica', 25, 'bold'), width = 16, height = 2 , text = "Result", bg = "light green",command = Sum) .grid(row = 0, column = 0) 
           btnReset = Button(inBotto2, pady = 8, bd = 8, fg = "black", font = ('Helvetica', 25, 'bold'), width = 16, height = 2, text = "Reset", bg = "yellow", command = Reset).grid(row = 1, column = 0) 
           btnExit = Button(inBotto2, pady = 8, bd = 8, fg = "black", font = ('Helvetica', 25, 'bold'), width = 16, height = 2, text = "Exit", bg = "red",command =Exit) .grid(row = 2, column = 0) 
           # --------------------------------------Display the ultimate result------------------------------- 
    # Wait and watch for any events that may take place in the root window root.mainloop ()OUTPUTCONCLUSION 
