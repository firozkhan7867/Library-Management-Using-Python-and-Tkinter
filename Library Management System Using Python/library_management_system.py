from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import psycopg2
from tkinter import messagebox
from datetime import *
from datetime import date

#img = ImageTk.PhotoImage(Image.open("D:\courses\\r3.jpg"))
class project():
    def __init__(self, root):
        self.main_root = root
        self.root = self.main_root
        self.root.geometry("700x550")
        self.root.title("Library Management System")
        self.db()
        # s = ttk.Style()
        self.style = ttk.Style()

        self.style.map("C.TButton",
                       foreground=[('pressed', 'red'), ('active', 'blue')],
                       background=[('pressed', '!disabled', 'black'),
                                   ('active', 'white')],
                       font=[('active', 'bold')]
                       )
        self.style.configure('C.TButton', font=('Helvetica', 15, 'bold'))
        # s.configure('.', font=('Helvetica', 22))
        # s.configure('TButton',background="wheat")

        def hi(event):
            # self.welcome_page()
            self.Home_page()

        self.mf = Frame(self.root)
        self.mf.place(relx=0, rely=0, relwidth=1, relheight=1)
        Label(self.root, text="Library Mangement System in Python", font=("bold", 28),
              fg="red", borderwidth=5, bg="Yellow", relief="sunken").place(relx=0, rely=0, relwidth=1, relheight=0.1)

        img = ImageTk.PhotoImage(Image.open("library.jpg"))
        Label(self.mf, image=img).place(
            relx=0, rely=0.12, relwidth=1, relheight=0.8)
        ttk.Button(self.mf, text="Welcome", style="C.TButton", cursor="hand2", command=self.welcome_page).place(relx=0.8,
                    rely=0.9, relwidth=0.2, relheigh=0.07)
        con = True
        if con == True:

            self.root.bind('<Return>', hi)
        con = False
        #-------------Variables----------------------
        self.branch_var = StringVar()
        self.book_title_var = StringVar()
        self.author_var = StringVar()
        self.publication_var = StringVar()
        self.total_quantity_var = IntVar()
        self.quantity_avail_var = IntVar()

        self.price_var = IntVar()
        self.book_serial_no_var = IntVar()
        self.quantity_var = IntVar()
        self.details_var = StringVar()
        self.semester_var = StringVar()
        self.pin_no_var = StringVar()
        self.std_name_var = StringVar()
        self.std_password_var = StringVar()
        self.Gender_var = StringVar()
        self.dob_day_var = StringVar()
        self.dob_mon_var = StringVar()
        self.dob_year_var = StringVar()
        self.phone_var = StringVar()

        self.library_id_var = IntVar()
        self.email_var = StringVar()
        self.address_var = StringVar()
        self.transaction_var = IntVar()
        self.penality_var = IntVar()
        self.pending_book_var = IntVar()

        #-----------------------End---------

        self.root.mainloop()

    def welcome_page(self):
        r1 = Toplevel()
        r1.geometry("350x250")
        fr = Frame(r1, bg="wheat")
        fr.place(relx=0, rely=0, relwidth=1, relheight=1)

        id_var = StringVar()
        pasw_var = StringVar()
        admin_var = IntVar()
        label_var = StringVar()
        admin_var.set("1")

        Label(fr, text="Login_page", bg="green", relief="sunken", borderwidth=3, fg="white", font=(
            'bold', 20)).place(relx=0, rely=0, relwidth=1, relheight=0.15)
        label1 = Label(fr, text="Id", font=('bold', 15), bg="wheat")
        label1.place(relx=0.1, rely=0.25)

        self.waste = "hellp"

        # textvariable=id_var,
        # id_var.set("User id")
        txt = Entry(fr, font=('bold', 15), textvariable=id_var,
                    relief="sunken", borderwidth=2)
        txt.place(relx=0.45, rely=0.25, relwidth=0.4, relheight=0.09)
        txt.focus()

        label1 = Label(fr, text="Password", font=('bold', 15), bg="wheat")
        label1.place(relx=0.1, rely=0.45)
        txt2 = Entry(fr, font=('bold', 15), show="*", textvariable=pasw_var,
                     relief="sunken", borderwidth=2)
        txt2.place(relx=0.45, rely=0.45, relwidth=0.4, relheight=0.09)

        def sub():
            i = id_var.get()
            pw = pasw_var.get()
            if i == "0000" and pw == "0000":
                messagebox.showinfo("successfully logged in!!",
                                    "Welcome Admin of the library")
                r1.withdraw()
                self.Home_page()

            else:
                messagebox.showerror(
                    "Error", "wrong id and password for admin")
                r1.withdraw()

            if admin_var.get() == 2:
                    # label_var.set("D1ent_Pin.No:")
                # label1.config(text="D1ent_Pin.No :")
                print("hello")

            else:
                label_var.set("Admin_id")

        ra1 = Radiobutton(fr, text="Admin_login", bg="wheat", variable=admin_var,
                          value=1)
        ra1.place(relx=0.35, rely=0.61)

        r2 = Radiobutton(fr, text="Student_Login", bg="wheat", variable=admin_var,
                         value=2)
        r2.place(relx=0.65, rely=0.61)
        sub1 = ttk.Button(fr, text="Login", cursor="hand2", style="C.TButton",
                          command=sub)
        sub1.place(relx=0.45, rely=0.71, relwidth=0.36, relheight=0.15)
        r1.bind('<Return>', sub)

        r1.mainloop()

    def Home_page(self):
        self.root.geometry("1000x700")
        self.root.title("Home Page (created by Firoz Khan)")
        self.mf2 = Frame(self.root, bg="wheat")
        self.mf2.place(relx=0, rely=0, relheight=1, relwidth=1)

        Label(self.root, text="Library Mangement System in Python", font=("times", 28,'bold'), fg="red",
              borderwidth=5, bg="Yellow", relief="sunken").place(relx=0, rely=0, relwidth=1)

        f2 = Frame(self.mf2, bg="light pink", relief="ridge", borderwidth=10)
        f2.place(relx=0, rely=0.1, relheight=0.9, relwidth=0.3)

        ttk.Button(f2, text="add_publication", style="C.TButton", cursor="hand2", command=self.add_publication).place(relx=0.15,
                                                                                                                      rely=0.03, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="Add_book", style="C.TButton", cursor="hand2", command=self.Add_book).place(
            relx=0.15, rely=0.14, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="View_Books", style="C.TButton", cursor="hand2", command=self.view_book).place(
            relx=0.15, rely=0.25, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="add_student", style="C.TButton", cursor="hand2", command=self.add_student).place(
            relx=0.15, rely=0.36, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="Student_report", style="C.TButton", cursor="hand2", command=self.Student_report).place(
            relx=0.15, rely=0.47, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="issue_boook", style="C.TButton", cursor="hand2", command=self.issue_book).place(
            relx=0.15, rely=0.58, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="return_book", style="C.TButton", cursor="hand2", command=self.return_book).place(
            relx=0.15, rely=0.69, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="penalty", style="C.TButton", cursor="hand2", command=self.penalty).place(
            relx=0.15, rely=0.79, relwidth=0.7, relheigh=0.07)
        ttk.Button(f2, text="log out", style="C.TButton", cursor="hand2", command=self.logout).place(
            relx=0.15, rely=0.90, relwidth=0.7, relheigh=0.07)

        self.left_fr = Frame(self.mf2, bg="wheat", borderwidth=10)
        self.left_fr.place(relx=0.31, rely=0.1, relwidth=0.67, relheight=0.9)

        self.l1 = Frame(self.left_fr, bg="plum2",
                        relief="groove", borderwidth=2)
        self.l1.place(relx=0, rely=0, relwidth=1, relheight=1)

    def add_publication(self):
        self.l1.configure(bg="salmon")
        f1 = Frame(self.l1, bg="salmon")
        f1.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(f1, text="Add Publication", font=('bold', 25), relief="ridge", borderwidth=2,
              bg="green", fg="white").place(relx=0, rely=0, relwidth=1, relheight=0.07)

        Label(f1, text="Publication Name : ", fg="white", font=('Bold', 15),
              bg="salmon").place(relx=0.1, rely=0.12, relwidth=0.32, relheight=0.074)
        # publication_name_var = StringVar()
        ent = Entry(f1, textvariable=self.publication_var,
                    borderwidth=1, font=('bold', 17))
        ent.place(relx=0.46, rely=0.13, relwidth=0.45, relheight=0.05)
        ent.focus()
        self.pub_id = 0
        conn = psycopg2.connect(
            host="localhost",
            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()

        def add():
            if self.publication_var.get() == "":
                pass
            else:
                # mylist.insert(END, publication_name_var.get())
                conn = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = conn.cursor()
                cur.execute("""SELECT * FROM publication""")
                k = cur.fetchall()
                try:
                    self.pub_id = k[-1][0]
                    print(self.pub_id)
                except:
                    self.pub_id=0
                self.pub_id += 1
                
                cur = conn.cursor()
                try:
                    cur.execute(
                        f"""INSERT INTO publication(name,pub_id) VALUES('{self.publication_var.get()}',{(self.pub_id)})""")
                    conn.commit()
                    cur.execute("""SELECT * FROM publication""")
                    s = cur.fetchall()
                    if len(s) > 1:
                        for i in s:
                            if i[1] == self.publication_var.get():
                                mylist.insert(END, i[1])
                    else:
                        mylist.insert(END, s[0][1])
                except:
                    messagebox.showerror(
                        "data_base error", "Publicaton Name already exists☻")
                cur.close()
                conn.close()
        def mismatch():
            conn = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
            cur = conn.cursor()
            cur.execute("SELECT * FROM publication")
            s = cur.fetchall()
            for i in s:
                if self.publication_var.get() == i[1]:
                    messagebox.showerror("DataBase ERROR  !!",f"{i[1]} is already exists in DAta")
            else:
                add()
            cur.close()
            conn.close()

        def delw():
            for i in range(10):
                # if mylist.get(i) == publication_name_var.get():
                #     mylist.delete(i)
                #     publication_name_var.set("")
                pass
            conn = psycopg2.connect(
                host="localhost",

                database='d3',
                user="postgres",
                password="psql",
            )
            cur = conn.cursor()
            s = self.publication_var.get()
            cur.execute(f"""DELETE FROM publication WHERE name = '{s}'""")
            mylist.delete(0, END)
            cur.execute("""SELECT * FROM publication""")
            s = cur.fetchall()
            try:
                if len(s) > 1:
                    for i in s:
                        mylist.insert(END, i[1])
                else:
                    mylist.insert(END, s[0][1])
            except:
                pass
            cur.close()
            conn.commit()
            conn.close()

        def clear():
            self.publication_var.set("")

        ttk.Button(f1, text="Add ", cursor="hand2", style="C.TButton", command=mismatch).place(
            relx=0.73, rely=0.26, relwidth=0.16, relheight=0.05)
        # ttk.Button(f1, text="Update", cursor="hand2",style="C.TButton").place(
        #     relx=0.53, rely=0.26, relwidth=0.16, relheight=0.07)
        ttk.Button(f1, text="Delete", cursor="hand2", style="C.TButton", command=delw).place(
            relx=0.53, rely=0.26, relwidth=0.16, relheight=0.05)
        ttk.Button(f1, text="Clear", cursor="hand2", style="C.TButton", command=clear).place(
            relx=0.33, rely=0.26, relwidth=0.16, relheight=0.05)

        f12 = Frame(f1, bg="white")
        f12.place(relx=0.3, rely=0.4, relwidth=0.5, relheight=0.4)

        Label(f12, text="Publications", bg="light green",
              font=('bold', 16)).pack(side=TOP, fill=X)

        scrollbar = Scrollbar(f12)
        scrollbar.pack(side=RIGHT, fill=Y)

        def get_cursor(ev):

            try:
                lb = map(int, mylist.curselection())
                d = mylist.curselection()
                d = d[0]
                self.publication_var.set(mylist.get(d))
            except:
                pass

        mylist = Listbox(f12, yscrollcommand=scrollbar.set, width=40, font=20)

        # def add():
        #     mylist.insert(END, publication_name_var.get())
        mylist.bind("<ButtonRelease-1>", get_cursor)
        mylist.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=mylist.yview)

        cur.execute("""SELECT * FROM publication""")
        s = cur.fetchall()
        try:
            if len(s) > 1:
                for i in s:
                    mylist.insert(END, i[1])
            else:
                mylist.insert(END, s[0][1])
        except:
            pass
        conn.commit()
        cur.close()
        conn.close()

    def Add_book(self):
        self.l1.configure(bg="cornsilk")
        f2 = Frame(self.l1, bg="cornsilk")
        f2.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.book_title_var.set("")
        self.author_var.set("")
        self.quantity_var.set(0)
        
        conn = psycopg2.connect(
            host="localhost",

            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()
        cur.execute("""SELECT * FROM book""")
        s = cur.fetchall()
        
        self.book_serial_no_var.set((len(s)+1))

        Label(f2, text="Add Book ", font=('bold', 25), relief="ridge", borderwidth=2,
              bg="skyblue2", fg="black").place(relx=0, rely=0, relwidth=1, relheight=0.09)

        Label(f2, text="Book Title   :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.1)
        Label(f2, text="Book Serial No:", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.18)
        Label(f2, text="Author        :", bg="cornsilk", font=(
            'bold', 15)).place(relx=0.1, rely=0.25)
        Label(f2, text="Publication  :", bg="cornsilk", font=(
            'bold', 15)).place(relx=0.1, rely=0.33)
        Label(f2, text="Branch       :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.41)
        Label(f2, text="Semester   :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.48)
        Label(f2, text="price         :", bg="cornsilk", font=(
            'bold', 15)).place(relx=0.1, rely=0.563)
        Label(f2, text="Quantity     :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.65)
        Label(f2, text="Details       :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.72)

        self.semester_var.set("select")
        self.publication_var.set("select")
        self.branch_var.set("select")
        Entry(f2, font=('bold', 15), textvariable=self.book_title_var,
              borderwidth=1, relief='sunken').place(relx=0.4, rely=0.1)
        Entry(f2, font=('bold', 15), textvariable=self.book_serial_no_var,
              borderwidth=1, relief='sunken').place(relx=0.4, rely=0.18)
        Entry(f2, font=('bold', 15), textvariable=self.author_var, borderwidth=1, relief='sunken').place(
            relx=0.4, rely=0.25)
        ttk.Combobox(f2, font=('bold', 11), textvariable=self.publication_var,
                     values=self.pub_data()).place(relx=0.4, rely=0.335)

        ttk.Combobox(f2, font=('bold', 11), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL',
            'ITI']).place(relx=0.4, rely=0.405)
        ttk.Combobox(f2, font=('bold', 11), textvariable=self.semester_var,
                     values=self.sem_data()).place(relx=0.4, rely=0.475)
        Entry(f2, font=('bold', 15), textvariable=self.price_var, borderwidth=1, relief='sunken').place(
            relx=0.4, rely=0.57)
        # Entry(f2, font=('bold', 15),textvariable=quantity_var,borderwidth=3,relief='sunken').place(relx=0.4, rely=0.62)
        Spinbox(f2, from_=0, to=100, font=15, textvariable=self.quantity_var).place(
            relx=0.4, rely=0.65, relheight=0.04)
        self.details = Text(f2, borderwidth=1)
        self.details.place(relx=0.4, rely=0.72, relwidth=0.4, relheight=0.13)
        # self.details.insert(END, "firoz is the worst programmer")

        def add_click():
            # s = self.pub_id(self.publication_var.get())
            # k = self.branch_id_fun(self.branch_var.get())
            # print(self.book_title_var.get(),self.book_serial_no_var.get(),self.author_var.get(),
            # self.publication_var.get(),s,self.sem_id_fun(self.semester_var.get()),k,
            # self.price_var.get(),self.quantity_var.get(),self.price_var.get(),self.details.get('1.0',END))
            # t = self.details.get('1.0', END)
            # print(type(t))

            conn = psycopg2.connect(
                host="localhost",

                database='d3',
                user="postgres",
                password="psql",
            )
            cur = conn.cursor()
            s = self.details.get('1.0', END)
            # s = s.split()
            # k = ""
            # for i in s:
            #     k += " " + i

            cur.execute(f"""INSERT INTO book(library_id , title ,author ,publication_id,
                        branch_id ,semester_id ,price ,total_quantity,quantity_avail ,details) VALUES
                        ({self.book_serial_no_var.get()},'{self.book_title_var.get()}','{self.author_var.get()}'
                        ,'{self.pub_id(self.publication_var.get())}','{self.branch_id_fun(self.branch_var.get())}'
                        ,'{self.sem_id_fun(self.semester_var.get())}'
                        ,{self.price_var.get()},{self.quantity_var.get()},{self.quantity_var.get()}
                        ,'{str(s)}') """)

            cur.close()
            conn.commit()
            conn.close()

        ttk.Button(f2, text="Add", style="C.TButton", cursor="hand2",
                   command=add_click).place(relx=0.8, rely=0.9, relwidth=0.15)

    def view_book(self):
        self.l1.configure(bg="rosybrown1")
        f3 = Frame(self.l1, bg="rosybrown1")
        f3.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.branch_var.set("select")
        self.publication_var.set("select")
        Label(f3, text="Select Branch  :", bg="rosybrown1", font=("bold", 15)).place(
            relx=0, rely=0.08, relwidth=0.32, relheight=0.09)
        Label(f3, text="Select Publication  :", bg="rosybrown1", font=("bold", 15)).place(
            relx=0.46, rely=0.08, relwidth=0.34, relheight=0.09)
        Label(f3, text="View Books ", font=('times', 25, 'bold'), relief="ridge", borderwidth=2,
              bg="palegreen1", fg="black").place(relx=0, rely=0, relwidth=1, relheight=0.07)
        ttk.Combobox(f3, font=('bold', 15), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL',
            'ITI']).place(relx=0.28, rely=0.1, relwidth=0.16)
        ttk.Combobox(f3, font=('bold', 12), textvariable=self.publication_var,
                     values=self.pub_data()).place(relx=0.79, rely=0.1, relwidth=0.19, relheight=0.045)

        def show_all(n):

            def fetch_data():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                cur.execute("""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                        ,a.total_quantity,a.quantity_avail,a.details
                        FROM book a,publication b,branch c,sem d 
                        WHERE a.publication_id = b.pub_id 
                        AND a.branch_id = c.branch_id AND 
                        a.semester_id = d.sem_id""")

                rows = cur.fetchall()

                if len(rows) != 0:
                    books_table.delete(*books_table.get_children())
                    for row in rows:
                        books_table.insert('', END, values=row)
                        con.commit()
                con.close()

            def sort_by():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                            ,a.total_quantity,a.quantity_avail,a.details
                            FROM book a,publication b,branch c,sem d
                            WHERE a.publication_id = b.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id AND c.branch_id = '{self.branch_id_fun(self.branch_var.get())}' 
                            AND b.name = '{self.publication_var.get()}'""")
                except:
                    messagebox.showerror("DATABASE Error","Please select the branch and publication fields")
                    return  None

                rows = cur.fetchall()

                if len(rows) != 0:
                    books_table.delete(*books_table.get_children())
                    for row in rows:
                        books_table.insert('', END, values=row)
                        con.commit()
                con.close()

            Table_Frame = Frame(f3, bd=2, bg="white")
            Table_Frame.place(relx=0.04, rely=0.4,
                              relwidth=0.94, relheight=0.6)

            scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

            books_table = ttk.Treeview(Table_Frame, columns=(
                'Serial', 'Book Title', 'Author', 'Publications', 'Branch', 'Semester', 'Price', 'Quantity', 'Quantity availabel', 'Details'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=books_table.xview)
            scroll_y.config(command=books_table.yview)

            books_table.heading("Serial", text="Serial")
            books_table.heading("Book Title", text="Book Title")
            books_table.heading("Author", text="Author")
            books_table.heading("Publications", text="Publications")
            books_table.heading("Branch", text="Branch")
            books_table.heading("Semester", text="Semester")
            books_table.heading("Price", text="Price")
            books_table.heading("Quantity", text="Quantity")
            books_table.heading("Quantity availabel",
                                text="Quantity availabel")
            books_table.heading("Details", text="Details")

            books_table['show'] = 'headings'
            books_table.column("Serial", width=70)
            books_table.column("Book Title", width=100)
            books_table.column("Author", width=100)
            books_table.column("Publications", width=120)
            books_table.column("Branch", width=100)
            books_table.column("Semester", width=100)
            books_table.column("Price", width=100)
            books_table.column("Quantity", width=150)
            books_table.column("Quantity availabel", width=150)
            books_table.column("Details", width=150)
            books_table.pack(fill=BOTH, expand=1)
            if n == 1:
                fetch_data()
            elif n == 0:
                sort_by()

            # books_table.bind("<ButtonRelease-1>", )

        ttk.Button(f3, style="C.TButton", text='Show All', cursor="hand2", command=lambda: show_all(1)).place(
            relx=0.77, rely=0.19, relwidth=0.19, relheight=0.06)
        ttk.Button(f3, style="C.TButton", text='Sort by', cursor="hand2", command=lambda: show_all(0)).place(
            relx=0.6, rely=0.19, relwidth=0.15, relheight=0.06)

    def add_student(self):
        self.l1.configure(bg="pink1")
        f4 = Frame(self.l1, bg="cornsilk")
        f4.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(f4, text="Add Student ", font=('times', 25, 'bold'), relief="ridge", borderwidth=2,
              bg="purple1", fg="black").place(relx=0, rely=0, relwidth=1, relheight=0.07)

        Label(f4, text="Pin No         :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.1)
        Label(f4, text="Full Name    :", bg="cornsilk", font=(
            'bold', 15)).place(relx=0.1, rely=0.17)
        Label(f4, text="Branch        :", bg="cornsilk", font=(
            'bold', 15)).place(relx=0.1, rely=0.24)
        Label(f4, text="Gender       :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.31)
        Label(f4, text="Date of Birth :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.38)
        Label(f4, text="library Id     :", bg="cornsilk", font=(
            'bold', 15)).place(relx=0.1, rely=0.45)
        Label(f4, text="Email          :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.52)
        Label(f4, text="Phone number        :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.59)
        Label(f4, text="Password   :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.66)
        Label(f4, text="Address     :", bg="cornsilk",
              font=('bold', 15)).place(relx=0.1, rely=0.73)
    
        conn = psycopg2.connect(
            host="localhost",

            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()
        cur.execute("""SELECT * FROM std""")
        s = cur.fetchall()
        self.price_var.set((len(s)+1))
        self.branch_var.set("select")
        Entry(f4, font=('bold', 15), textvariable=self.pin_no_var,
              borderwidth=1, relief='sunken').place(relx=0.4, rely=0.1)
        Entry(f4, font=('bold', 15), textvariable=self.std_name_var, borderwidth=1, relief='sunken').place(
            relx=0.4, rely=0.17)
        ttk.Combobox(f4, font=('bold', 11), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL',
            'ITI']).place(relx=0.4, rely=0.245)

        ra1 = Radiobutton(f4, text="Male", bg="cornsilk", variable=self.Gender_var,
                          value="Male")
        ra1.place(relx=0.4, rely=0.31)
        r2 = Radiobutton(f4, text="Female", bg="cornsilk", variable=self.Gender_var,
                         value="Female")
        r2.place(relx=0.55, rely=0.31)
        self.dob_day_var.set(1)
        self.dob_mon_var.set("Jan")
        self.dob_year_var.set(1999)
        self.pin_no_var.set("")
        self.std_name_var.set("")
        self.branch_var.set("select")
        self.Gender_var.set("Male")
        self.email_var.set("")
        self.phone_var.set("")


        ttk.Combobox(f4, font=('bold', 11), textvariable=self.dob_day_var, values=[
                     i for i in range(1, 31)]).place(relx=0.4, rely=0.38, relwidth=0.07)
        ttk.Combobox(f4, font=('bold', 11), textvariable=self.dob_mon_var, values=[
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']).place(relx=0.5, rely=0.38, relwidth=0.1)
        ttk.Combobox(f4, font=('bold', 11), textvariable=self.dob_year_var, values=[
                     i for i in range(1995, 2020)]).place(relx=0.65, rely=0.38, relwidth=0.1)
        Entry(f4, font=('bold', 15), textvariable=self.price_var, borderwidth=1, relief='sunken').place(
            relx=0.4, rely=0.45)
        Entry(f4, font=('bold', 15), textvariable=self.email_var,
              borderwidth=1, relief='sunken').place(relx=0.4, rely=0.53)
        Entry(f4, font=('bold', 15), textvariable=self.phone_var,
              borderwidth=1, relief='sunken').place(relx=0.4, rely=0.6)
        Entry(f4, font=('bold', 15), show="*", textvariable=self.std_password_var,
              borderwidth=1, relief='sunken').place(relx=0.4, rely=0.67)
        self.address = Text(f4, font=('bold'), borderwidth=1)
        self.address.place(relx=0.4, rely=0.74, relwidth=0.4, relheight=0.13)
        # self.address.insert(END, "firoz is the worst programmer")

        def add_stud():
            conn = psycopg2.connect(
                host="localhost",
                database='d3',
                user="postgres",
                password="psql",
            )
            cur = conn.cursor()
            s = self.address.get('1.0', END)
            k = str(self.dob_day_var.get()) + '-' + str(self.dob_mon_var.get()) + '-' + str(self.dob_year_var.get())
            self.zero = IntVar()
            self.zero.set(0)
        
            try:
                cur.execute(f"""INSERT INTO std(pin_no , std_name ,branch_id ,gender,
                            dob,email , phone , pass,std_address,total_transaction , pending_books , penality) VALUES
                            (
                                '{self.pin_no_var.get()}',
                                '{self.std_name_var.get()}',
                                {self.branch_id_fun(self.branch_var.get())},
                                '{self.Gender_var.get()}',
                                '{k}',
                                '{self.email_var.get()}',
                                '{str(self.phone_var.get())}',   
                                '{self.std_password_var.get()}',
                                '{str(s)}',0,0,0)""")
            # cur.execute("""INSERT INTO std(total_transaction , pending_books , penality) 
            #     Values(0,0,0) where pin_no = '{self.pin_no_var.get()}'""")
            except:
                messagebox.showerror("DataBase Error occured","Please fill all details of the student")
            
            conn.commit()
            cur.close()
            conn.close()

        ttk.Button(f4, text="Add", style="C.TButton", cursor="hand2",
                   command=add_stud).place(relx=0.84, rely=0.92, relwidth=0.15)

    def Student_report(self):
        self.l1.configure(bg="gray75")
        f5 = Frame(self.l1, bg="gray75")
        f5.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.std_name_var.set("")
        self.branch_var.set("select")
        self.pin_no_var.set("")

        Label(f5, text="Select Branch  :", bg="gray75", font=("bold", 15)).place(
            relx=0, rely=0.08, relwidth=0.32, relheight=0.09)
        Label(f5, text="Student Pin NO  :", bg="gray75", font=("bold", 15)).place(
            relx=0.46, rely=0.08, relwidth=0.34, relheight=0.09)
        Label(f5, text="Student Report ", font=('times', 25, 'bold'), relief="ridge", borderwidth=2,
              bg="aquamarine", fg="black").place(relx=0, rely=0, relwidth=1, relheight=0.07)
        ttk.Combobox(f5, font=('bold', 15), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL',
            'ITI']).place(relx=0.28, rely=0.1, relwidth=0.16)
        Entry(f5, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.pin_no_var).place(
            relx=0.79, rely=0.1, relwidth=0.19, relheight=0.04)

        def show(n):
            def fetch_data():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                cur.execute("""SELECT  a.library_id,a.pin_no,a.std_name,b.branch,a.gender,
                        a.email,a.phone,a.total_transaction,a.pending_books,a.penality,
                        a.std_address
                        FROM std a,branch b
                        WHERE a.branch_id = b.branch_id """)

                rows = cur.fetchall()

                if len(rows) != 0:
                    books_table.delete(*books_table.get_children())
                    for row in rows:
                        books_table.insert('', END, values=row)
                        con.commit()
                con.close()

            def sort_by():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  a.library_id,a.pin_no,a.std_name,b.branch,a.gender,
                            a.email,a.phone,a.total_transaction,a.pending_books,a.penality,
                            a.std_address
                            FROM std a,branch b
                            WHERE a.branch_id = b.branch_id  AND b.branch_id = {self.branch_id_fun(self.branch_var.get())} 
                                AND a.pin_no = '{self.pin_no_var.get()}' """)

                    rows = cur.fetchall()

                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            books_table.insert('', END, values=row)
                            con.commit()
                except:
                    messagebox.showerror("DataBase ERROR !!!", "Please select the  branch feild and enter correct pin no")
                con.close()

            Entry(f5, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.std_name_var).place(
                relx=0.02, rely=0.2, relwidth=0.39, relheight=0.05)
            ttk.Button(f5, style="C.TButton", text='View', cursor="hand2", command=self.view).place(
                relx=0.43, rely=0.2, relwidth=0.12, relheight=0.054)

            Table_Frame = Frame(f5, bd=2, bg="white")
            Table_Frame.place(relx=0.04, rely=0.3,
                              relwidth=0.94, relheight=0.6)

            scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

            books_table = ttk.Treeview(Table_Frame, columns=(
                'Library Id', 'Pin no', 'Name', 'Branch', 'Gender',  'Email', 'Phone', 'Total_Transaction', 'Pending book', 'Penality', 'Address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=books_table.xview)
            scroll_y.config(command=books_table.yview)
            books_table.heading("Library Id", text="Library ID")
            books_table.heading("Pin no", text="Pin no")
            books_table.heading("Name", text="Name")
            books_table.heading("Branch", text="Branch")
            books_table.heading("Gender", text="Gender")
            books_table.heading("Email", text="Email")
            books_table.heading("Phone", text="Phone")
            books_table.heading("Total_Transaction", text="Total_transaction")
            books_table.heading("Pending book", text="Pending book")
            books_table.heading("Penality", text="Penality")
            books_table.heading("Address", text="Address")

            books_table['show'] = 'headings'
            books_table.column("Library Id", width=70)
            books_table.column("Pin no", width=100)
            books_table.column("Name", width=100)
            books_table.column("Branch", width=70)
            books_table.column("Gender", width=70)
            books_table.column("Email", width=130)
            books_table.column("Phone", width=100)
            books_table.column("Total_Transaction", width=130)
            books_table.column("Pending book", width=100)
            books_table.column("Penality", width=80)
            books_table.column("Address", width=150)
            books_table.pack(fill=BOTH, expand=1)

            if n == 1:
                fetch_data()
            else:
                sort_by()

            def get_cursor(event):
                curosor_row = books_table.focus()
                contents = books_table.item(curosor_row)
                row = contents['values']
                self.std_name_var.set(row[1] + '    (' + row[2] + ')')

            books_table.bind("<ButtonRelease-1>", get_cursor)

        ttk.Button(f5, style="C.TButton", text='show', cursor="hand2", command=lambda: show(1)).place(
            relx=0.87, rely=0.19, relwidth=0.12, relheight=0.06)
        ttk.Button(f5, style="C.TButton", text='Sort by', cursor="hand2", command=lambda: show(0)).place(
            relx=0.6, rely=0.19, relwidth=0.15, relheight=0.06)

    def issue_book(self):
        self.l1.configure(bg="pale green")
        f6 = Frame(self.l1, bg="pale green")
        f6.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Label(f6, text="Select Branch  :", bg="pale green", font=("bold", 15)).place(
        #     relx=0, rely=0.08, relwidth=0.32, relheight=0.09)
        Label(f6, text="OR",fg="red", bg="pale green", font=("times", 25, 'bold')).place(
            relx=0.32, rely=0.08, relwidth=0.34, relheight=0.09)
        Label(f6, text="Issue Boook ", font=('times', 25, 'bold'), relief="ridge", borderwidth=2,
              bg="aquamarine", fg="black").place(relx=0, rely=0, relwidth=1, relheight=0.07)
        self.branch_var.set('Branch')
        self.book_serial_no_var.set("Serial_no")
        ttk.Combobox(f6, font=('times', 15, 'bold'), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL']).place(relx=0.02, rely=0.1, relwidth=0.16, relheight=0.04)
        Entry(f6, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.book_serial_no_var).place(
            relx=0.6, rely=0.1, relwidth=0.19, relheight=0.04)

        def view2():
            self.l1.configure(bg="pale green")
            vi = Frame(f6, bg="cadetblue3")
            vi.place(relx=0, rely=0, relwidth=1, relheight=0.75)

            Label(vi, text="Book Details", bg="old lace", font=('times', 25, 'bold')).place(
                relx=0, rely=0, relwidth=1, relheight=0.07)

            fr = Frame(vi, bg="light blue", borderwidth=1, relief=SUNKEN)
            fr.place(relx=0.03, rely=0.09, relwidth=0.9, relheight=0.7)

            Label(fr, text=self.std_name_var.get(), bg="chocolate", font=20).place(
                relx=0, rely=0, relwidth=1, relheight=0.07)
            Label(fr, text="Book Serial        :", font=('times', 15,
                                                         'bold'), bg="light blue").place(relx=0.1, rely=0.1)
            Label(fr, text="Book Title      :", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.1, rely=0.18)
            Label(fr, text="Author            :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.1, rely=0.26)
            Label(fr, text="Branch            :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.1, rely=0.34)
            Label(fr, text="Semester          :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.1, rely=0.42)
            Label(fr, text="Quantity          :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.1, rely=0.5)
            Label(fr, text="Price             :", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.1, rely=0.58)
            Label(fr, text="Available        :", fg="red", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.1, rely=0.66)
            Label(fr, text="Description         :", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.1, rely=0.74)

            #=-----------------------------
            con = psycopg2.connect(
                host="localhost",
                database='d3',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            cur.execute("""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                            ,a.total_quantity,a.quantity_avail,a.details
                            FROM book a,publication b,branch c,sem d
                            WHERE a.publication_id = b.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id AND a.quantity_avail > 0 """)
            s = cur.fetchall()
            t = self.book_title_var.get()
            t = t.split('(')
            for i in s:
                if  int(t[1][0])== i[0]:
                    self.book_serial_no_var.set(i[0])
                    self.book_title_var.set(i[1])
                    self.author_var.set(i[2])
                    self.branch_var.set(i[4])
                    self.semester_var.set(i[5])
                    self.price_var.set(i[6])
                    self.total_quantity_var.set(i[7])
                    self.quantity_avail_var.set(i[8])
                    self.details_var.set(i[9])

            address = "visakhapatnam"
            Label(fr, text=self.book_serial_no_var.get(), font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.4, rely=0.1)
            Label(fr, text=self.book_title_var.get(), font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.4, rely=0.18)
            Label(fr, text=self.author_var.get(), font=('times', 15,
                                                       'bold'), bg="light blue").place(relx=0.4, rely=0.26)
            Label(fr, text=self.branch_var.get(), font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.4, rely=0.34)
            Label(fr, text=self.semester_var.get(), font=(
                'times', 15, 'bold'), bg="light blue").place(relx=0.4, rely=0.42)
            Label(fr, text=self.total_quantity_var.get(), font=('times', 15,
                                                       'bold'), bg="light blue").place(relx=0.4, rely=0.5)
            Label(fr, text=self.price_var.get(), font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.4, rely=0.58)
            Label(fr, text=self.quantity_avail_var.get(), font=(
                'times', 15, 'bold'), fg="red", bg="light blue").place(relx=0.4, rely=0.66)
            Label(fr, text=self.details_var.get(), font=(
                'times', 15, 'bold'), bg="light blue").place(relx=0.4, rely=0.74)


            def back():
                self.issue_book()
                show(2)

            ttk.Button(vi, text="back", style="C.TButton",
                       cursor="hand2", command=back).place(relx=0.8, rely=0.89)

        def show(n):

            def sort_by():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                            ,a.total_quantity,a.quantity_avail,a.details
                            FROM book a,publication b,branch c,sem d
                            WHERE a.publication_id = b.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id AND c.branch_id = '{self.branch_id_fun(self.branch_var.get())}' 
                            AND a.quantity_avail > 0 
                            """)

                    rows = cur.fetchall()

                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            books_table.insert('', END, values=row)
                            con.commit()
                except:
                    messagebox.showerror(
                        "DataBase ERROR !!!", "Please select the  branch feild and enter correct pin no")
                con.close()

            def search():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                            ,a.total_quantity,a.quantity_avail,a.details
                            FROM book a,publication b,branch c,sem d
                            WHERE a.publication_id = b.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id AND a.library_id = {self.book_serial_no_var.get()}
                            AND a.quantity_avail > 0 """)

                    rows = cur.fetchall()

                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            books_table.insert('', END, values=row)
                            con.commit()
                except:
                    messagebox.showerror(
                        "DataBase ERROR !!!", "Please select the  branch feild and enter correct pin no")
                con.close()



            def fetch_all():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                            ,a.total_quantity,a.quantity_avail,a.details
                            FROM book a,publication b,branch c,sem d
                            WHERE a.publication_id = b.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id AND a.quantity_avail > 0
                            """)

                    rows = cur.fetchall()

                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            books_table.insert('', END, values=row)
                            con.commit()
                except:
                    messagebox.showerror(
                        "DataBase ERROR !!!", "Please select the  branch feild and enter correct pin no")
                con.close()
            self.book_title_var.set("")
            Entry(f6, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.book_title_var).place(
                relx=0.02, rely=0.2, relwidth=0.39, relheight=0.05)
            ttk.Button(f6, style="C.TButton", text='View', cursor="hand2", command=view2).place(
                relx=0.43, rely=0.2, relwidth=0.12, relheight=0.054)



            Table_Frame = Frame(f6, bd=2, bg="white")
            Table_Frame.place(relx=0.04, rely=0.32,
                              relwidth=0.94, relheight=0.4)

            # Entry(f6, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.pin_no_var).place(
            #     relx=0.05, rely=0.23, relwidth=0.25, relheight=0.04)
            # ttk.Button(f6, text="View", style="C.TButton", cursor="hand2", command=view2).place(
            #     relx=0.33, rely=0.23, relwidth=0.12, relheight=0.05)

            scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

            books_table = ttk.Treeview(Table_Frame, columns=(
                'Book serial', 'Book Title', 'Author', 'Publications', 'Branch', 'Semester', 'Price', 'Total_quantity' , 'Quantity_available' , 'Details'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=books_table.xview)
            scroll_y.config(command=books_table.yview)

            books_table.heading("Book serial", text="Book serial")
            books_table.heading("Book Title", text="Book Title")
            books_table.heading("Author", text="Author")
            books_table.heading("Publications", text="Publications")
            books_table.heading("Branch", text="Branch")
            books_table.heading("Semester", text="Semester")
            books_table.heading("Price", text="Price")
            books_table.heading("Total_quantity", text="Total_quantity")
            books_table.heading("Quantity_available", text="Books_available")
            books_table.heading("Details", text="Description")

            books_table['show'] = 'headings'
            books_table.column("Book serial", width=70)
            books_table.column("Book Title", width=100)
            books_table.column("Author", width=100)
            books_table.column("Publications", width=120)
            books_table.column("Branch", width=70)
            books_table.column("Semester", width=80)
            books_table.column("Price", width=70)
            books_table.column("Total_quantity", width=100)
            books_table.column("Quantity_available", width=100)
            books_table.column("Details", width=250)
            books_table.pack(fill=BOTH, expand=1)

            if n == 1:
                sort_by()
            elif n == 0:
                search()
            elif n == 2:
                fetch_all()

            def get_cursor(event):
                curosor_row = books_table.focus()
                contents = books_table.item(curosor_row)
                row = contents['values']
                self.book_title_var.set(row[1] + '    (' + str(row[0]) + ')')
                self.b = self.book_title_var.get()
            
            books_table.bind("<ButtonRelease-1>", get_cursor)

        ttk.Button(f6, style="C.TButton", text='sort_by', cursor="hand2", command=lambda: show(1)).place(
            relx=0.2, rely=0.09, relwidth=0.15, relheight=0.06)
        ttk.Button(f6, style="C.TButton", text='Search', cursor="hand2", command=lambda: show(0)).place(
            relx=0.85, rely=0.09, relwidth=0.12, relheight=0.06)
        ttk.Button(f6, style="C.TButton", text='Show_all', cursor="hand2", command=lambda: show(2)).place(
            relx=0.79, rely=0.19, relwidth=0.18, relheight=0.06)


        fr = Frame(f6, bg="cadet blue")
        fr.place(relx=0, rely=0.75, relwidth=1, relheight=0.3)

        Label(fr, bg="salmon", text="Select Stundet", fg="white", font=(
            'times', 17, 'bold')).place(relx=0, rely=0, relwidth=1, relheight=0.2)

        Label(fr, text="Select Branch  :", bg="cadet blue", font=("bold", 15)).place(
            relx=0, rely=0.3, relwidth=0.32, relheight=0.09)
        Label(fr, text="Student Pin NO  :", bg="cadet blue", font=("bold", 15)).place(
            relx=0.46, rely=0.3, relwidth=0.34, relheight=0.09)
        ttk.Combobox(fr, font=('bold', 15), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL']).place(relx=0.28, rely=0.3, relwidth=0.16)
        def issue():
            con = psycopg2.connect(
                host="localhost",
                database='d3',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            try:
                cur.execute(f"select * from std where pin_no = '{self.pin_no_var.get()}'")
            except:
                messagebox.showerror("DataBase ERROR!!","Invalid std Pin No.  ")
            s = cur.fetchall()
            # s = s[0][0]
            # print(s)
            t = self.b
            t = t.split('(')
            t = t[1]
            # print(t[:-1])
            cur.execute("""select CURRENT_DATE""")
            a = cur.fetchall()
            a = a[0][0]
            a = str(a)
            # print(int(a[-2] + a[-1]))
            cur.execute(f"""INSERT INTO issue(std_id,book_id,date1)
                 VALUES({s[0][0]},{t[:-1]},'{a}')""")
            
            cur.execute(f"""update book set quantity_avail = (quantity_avail - 1 ) where library_id = {t[:-1]}""")
            con.commit()
            cur.close()
            con.close()


        Entry(fr, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.pin_no_var).place(
            relx=0.79, rely=0.3, relwidth=0.19, relheight=0.15)
        ttk.Button(fr, text="Issue ", style="C.TButton",
                   cursor="hand2",command=issue).place(relx=0.78, rely=0.52)

    def return_book(self):
        self.l1.configure(bg="lemon chiffon")
        f7 = Frame(self.l1, bg="lemon chiffon")
        f7.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(f7, text="Select Branch  :", bg="lemon chiffon", font=("bold", 15)).place(
            relx=0, rely=0.08, relwidth=0.32, relheight=0.09)
        Label(f7, text="Book Name  :", bg="lemon chiffon", font=("bold", 15)).place(
            relx=0.46, rely=0.08, relwidth=0.34, relheight=0.09)
        Label(f7, text="Issue Boook ", font=('times', 25, 'bold'), relief="ridge", borderwidth=2,
              bg="aquamarine", fg="black").place(relx=0, rely=0, relwidth=1, relheight=0.07)
        self.branch_var.set('select')
        ttk.Combobox(f7, font=('bold', 15), textvariable=self.branch_var, values=[
            'CSE',
            'ECE',
            'MECH',
            'EEE',
            'CIVIL']).place(relx=0.28, rely=0.1, relwidth=0.16, relheight=0.04)
        Entry(f7, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.book_title_var).place(
            relx=0.73, rely=0.1, relwidth=0.19, relheight=0.04)


        def sort_by():
            def sort_by():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  a.library_id,a.title,a.author,b.name,c.branch,d.sem,a.price
                            ,a.total_quantity,a.quantity_avail,a.details
                            FROM book a,publication b,branch c,sem d
                            WHERE a.publication_id = b.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id AND c.branch_id = '{self.branch_id_fun(self.branch_var.get())}' 
                            AND a.quantity_avail > 0 
                            """)

                    rows = cur.fetchall()

                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            books_table.insert('', END, values=row)
                            con.commit()
                except:
                    messagebox.showerror(
                        "DataBase ERROR !!!", "Please select the  branch field and enter correct pin no")
                con.close()

            
            def fetch_all():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                try:
                    cur.execute(f"""SELECT  f.issue_id,b.std_name,a.title,e.name,c.branch,d.sem,a.price
                            ,f.date1,a.details
                            FROM book a,std b,branch c,sem d,publication e,issue f
                            WHERE a.publication_id = e.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id 
                            AND f.std_id = b.library_id 
                            AND f.book_id = a.library_id""")

                    rows = cur.fetchall()

                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            books_table.insert('', END, values=row)
                            con.commit()
                except:
                    messagebox.showerror(
                        "DataBase ERROR !!!", "Please select the  branch feild and enter correct pin no")
                con.close()
            
            Entry(f7, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.book_title_var).place(
                relx=0.02, rely=0.2, relwidth=0.39, relheight=0.05)
            ttk.Button(f7, style="C.TButton", text='View', cursor="hand2", command=view2).place(
                relx=0.43, rely=0.2, relwidth=0.12, relheight=0.054)

            Table_Frame = Frame(f7, bd=2, bg="white")
            Table_Frame.place(relx=0.01, rely=0.28,
                              relwidth=0.97, relheight=0.7)

            # Entry(f6, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.pin_no_var).place(
            #     relx=0.05, rely=0.23, relwidth=0.25, relheight=0.04)
            # ttk.Button(f6, text="View", style="C.TButton", cursor="hand2", command=view2).place(
            #     relx=0.33, rely=0.23, relwidth=0.12, relheight=0.05)

            scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

            books_table = ttk.Treeview(Table_Frame, columns=(
                'Issue_Id', 'Student Name' ,'Book Title', 'Publications', 'Branch', 'Semester', 'Price', 'Details'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=books_table.xview)
            scroll_y.config(command=books_table.yview)

            books_table.heading("Issue_Id", text="Issue_ID")
            books_table.heading("Book Title", text="Book Title")
            books_table.heading("Student Name", text="Student Name")
            books_table.heading("Publications", text="Publications")
            books_table.heading("Branch", text="Branch")
            books_table.heading("Semester", text="Semester")
            books_table.heading("Price", text="Price")
            books_table.heading("Details", text="Description")

            books_table['show'] = 'headings'
            books_table.column("Issue_Id", width=70)
            books_table.column("Book Title", width=100)
            books_table.column("Student Name", width=100)
            books_table.column("Publications", width=120)
            books_table.column("Branch", width=70)
            books_table.column("Semester", width=80)
            books_table.column("Price", width=70)
            books_table.column("Details", width=250)
            books_table.pack(fill=BOTH, expand=1)

            def get_cursor(event):
                curosor_row = books_table.focus()
                contents = books_table.item(curosor_row)
                row = contents['values']
                self.book_title_var.set(row[2] + '    (' + str(row[0]) + ')')
                self.b = self.book_title_var.get()
            fetch_all()
            books_table.bind("<ButtonRelease-1>", get_cursor)


        def view2():
            self.l1.configure(bg="pale green")
            vi = Frame(f7, bg="lemon chiffon")
            vi.place(relx=0, rely=0.28, relwidth=1, relheight=0.73)

            Label(vi, text="Book Details", bg="moccasin", fg="light salmon", font=(
                'times', 25, 'bold')).place(relx=0, rely=0, relwidth=1, relheight=0.07)

            fr = Frame(vi, bg="khaki", borderwidth=1, relief=SUNKEN)
            fr.place(relx=0.03, rely=0.09, relwidth=0.9, relheight=0.76)
            k = self.b
            s = self.b.split()
            self.book_title_var.set(s[0])

            Label(fr, text=self.book_title_var.get(), bg="chocolate", font=20).place(
                relx=0, rely=0, relwidth=1, relheight=0.07)
            Label(fr, text="Book Serial       :", font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.2, rely=0.1)
            Label(fr, text="Book Title        :", font=('times', 15,
                                                      'bold'), bg="khaki").place(relx=0.2, rely=0.18)
            Label(fr, text="Student_Issued  :", font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.2, rely=0.26)
            Label(fr, text="Branch            :", font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.2, rely=0.34)
            Label(fr, text="Semester          :", font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.2, rely=0.42)
            Label(fr, text="Student_id        :", font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.2, rely=0.5)
            Label(fr, text="Price               :", font=('times', 15, 'bold'),
                  bg="khaki").place(relx=0.2, rely=0.58)
            Label(fr, text="Date Issued     :", fg="red", font=('times', 15, 'bold'),
                  bg="khaki").place(relx=0.2, rely=0.66)
            Label(fr, text="Description       :", font=('times', 15, 'bold'),
                  bg="khaki").place(relx=0.2, rely=0.74)
            ttk.Button(f7, style="C.TButton", text='Return', cursor="hand2", command=view2).place(
                relx=0.87, rely=0.93, relwidth=0.12, relheight=0.06)

            #-------------------------------------------------------------------------------------
            con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
            cur = con.cursor()
            s = self.b.split('(')
            s = s[1][:-1]
            cur.execute(f"""SELECT  a.library_id,f.issue_id,b.std_name,b.library_id,a.title,c.branch,d.sem,a.price
                            ,f.date1,a.details
                            FROM book a,std b,branch c,sem d,publication e,issue f
                            WHERE a.publication_id = e.pub_id
                            AND a.branch_id = c.branch_id AND
                            a.semester_id = d.sem_id 
                            AND f.std_id = b.library_id 
                            AND f.book_id = a.library_id
                            AND f.issue_id = {s}""")
            row = cur.fetchall()
            row = row[0]
            cur.close()
            con.close()
            self.book_serial_no_var.set(row[0])
            self.book_title_var.set(row[4])
            self.std_name_var.set(row[2])
            self.branch_var.set(row[5])
            self.semester_var.set(row[6])
            self.library_id_var.set(row[3])
            self.price_var.set(row[7])
            self.dob_mon_var.set(row[8])
            self.details_var.set(row[9])


            Label(fr, text=self.book_serial_no_var.get(), font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.54, rely=0.1)
            Label(fr, text=self.book_title_var.get(), font=('times', 15,
                'bold'), bg="khaki").place(relx=0.54, rely=0.18)
            Label(fr, text=self.std_name_var.get(), font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.54, rely=0.26)
            Label(fr, text=self.branch_var.get(), font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.54, rely=0.34)
            Label(fr, text=self.semester_var.get(), font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.54, rely=0.42)
            Label(fr, text=self.library_id_var.get(), font=(
                'times', 15, 'bold'), bg="khaki").place(relx=0.54, rely=0.5)
            Label(fr, text=self.price_var.get(), font=('times', 15, 'bold'),
                  bg="khaki").place(relx=0.54, rely=0.58)
            Label(fr, text=self.dob_mon_var.get(), fg="red", font=('times', 15, 'bold'),
                  bg="khaki").place(relx=0.54, rely=0.66)
            Label(fr, text=self.details_var.get(), font=('times', 15, 'bold'),
                  bg="khaki").place(relx=0.54, rely=0.74)
            def return_book():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()
                d = self.b.split('(')
                s = d[1][:-1]
                cur.execute("select * from issue")
                k = cur.fetchall()
                l = []
                for i in k:
                    l.append(i)
                for i in l:
                    j = i[0]
                    if int(s) == int(j):
                        ik = i[2]
                        
                
                #     else:
                #         ik = 1
                cur.execute(f"""DELETE FROM issue WHERE issue_id = {s}""")
                cur.execute(f"""UPDATE book set quantity_avail = 1 where id = {ik}""")
                con.commit()
                cur.close()
                con.close()


            ttk.Button(f7, style="C.TButton", text='Return', cursor="hand2", command=return_book).place(
                relx=0.87, rely=0.93, relwidth=0.12, relheight=0.06)
        ttk.Button(f7, style="C.TButton", text='show', cursor="hand2", command=sort_by).place(
            relx=0.87, rely=0.19, relwidth=0.12, relheight=0.06)
        ttk.Button(f7, style="C.TButton", text='sort_by', cursor="hand2", command=sort_by).place(
            relx=0.67, rely=0.19, relwidth=0.13, relheight=0.06)

    def penalty(self):
        self.l1.configure(bg="light green")
        f8 = Frame(self.l1, bg="light green")
        f8.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(f8, text="Penalty  :-", fg="White", bg="green4", font=("times",
                                                                     25, 'bold')).place(relx=0, rely=0, relwidth=1, relheight=0.07)
        Label(f8, text="Branch  :-", bg="light green", font=("times", 15,
                                                             'bold')).place(relx=0.04, rely=0.09, relwidth=0.3, relheight=0.04)

        ttk.Combobox(f8, textvariable=self.branch_var, values=['CSE', 'ECE', 'EEE', 'IT', 'CIVIL', 'MECH']).place(
            relx=0.44, rely=0.09, relwidth=0.3, relheight=0.04)

        def view2():
            self.l1.configure(bg="pale green")
            vi = Frame(f8, bg="cadetblue3")
            vi.place(relx=0, rely=0, relwidth=1, relheight=0.75)

            Label(vi, text="Book Details", bg="old lace", font=('times', 25, 'bold')).place(
                relx=0, rely=0, relwidth=1, relheight=0.07)

            fr = Frame(vi, bg="light blue", borderwidth=1, relief=SUNKEN)
            fr.place(relx=0.03, rely=0.09, relwidth=0.9, relheight=0.7)

            Label(fr, text=self.std_name_var.get(), bg="chocolate", font=20).place(
                relx=0, rely=0, relwidth=1, relheight=0.07)
            Label(fr, text="Book Serial        :", font=('times', 15,
                                                         'bold'), bg="light blue").place(relx=0.2, rely=0.1)
            Label(fr, text="Book Title      :", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.2, rely=0.18)
            Label(fr, text="Author            :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.2, rely=0.26)
            Label(fr, text="Branch            :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.2, rely=0.34)
            Label(fr, text="Semester          :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.2, rely=0.42)
            Label(fr, text="Quantity          :", font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.2, rely=0.5)
            Label(fr, text="Price             :", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.2, rely=0.58)
            Label(fr, text="Available        :", fg="red", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.2, rely=0.66)
            Label(fr, text="Description         :", font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.2, rely=0.74)

            #=-----------------------------
            address = "visakhapatnam"
            Label(fr, text=self.pin_no_var.get(), font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.6, rely=0.1)
            Label(fr, text=self.std_name_var.get(), font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.6, rely=0.18)
            Label(fr, text=self.phone_var.get(), font=('times', 15,
                                                       'bold'), bg="light blue").place(relx=0.6, rely=0.26)
            Label(fr, text=self.branch_var.get(), font=('times', 15,
                                                        'bold'), bg="light blue").place(relx=0.6, rely=0.34)
            Label(fr, text=self.library_id_var.get(), font=(
                'times', 15, 'bold'), bg="light blue").place(relx=0.6, rely=0.42)
            Label(fr, text=self.email_var.get(), font=('times', 15,
                                                       'bold'), bg="light blue").place(relx=0.6, rely=0.5)
            Label(fr, text=address, font=('times', 15, 'bold'),
                  bg="light blue").place(relx=0.6, rely=0.58)
            Label(fr, text=self.transaction_var.get(), font=(
                'times', 15, 'bold'), fg="red", bg="light blue").place(relx=0.6, rely=0.66)
            Label(fr, text=self.pending_book_var.get(), font=(
                'times', 15, 'bold'), bg="light blue").place(relx=0.6, rely=0.74)

            def back():
                self.penalty()
                show()

            ttk.Button(vi, text="back", style="C.TButton",
                       cursor="hand2", command=back).place(relx=0.8, rely=0.89)

        ttk.Button(f8, text="Show All", style="C.TButton", cursor='hand2').place(
            relx=0.74, rely=0.18, relwidth=0.24, relheight=0.07)

        def show():
            def fetch_all():
                con = psycopg2.connect(
                    host="localhost",
                    database='d3',
                    user="postgres",
                    password="psql",
                )
                cur = con.cursor()

                cur.execute("""SELECT * FROM issue""")
                self.k = cur.fetchall()
                def d1(i):
                    s = i
                    k = s.replace('-',',')
                    s = k.split(',')
                    if s[1][0] == '0':
                        t = s[0] + ',' + s[1][1] + ','+ s[2]
                    else:
                        t = s[0] + ',' + s[1] + ',' + s[2]
                    t = t.split(',')
                    if t[2][0] == '0':
                        t = t[0] + ',' + t[1] + ',' + t[2][1]
                    else:
                        t = t[0] + ',' + t[1] + ',' + t[2]
                    return t

                def date2():
                    k = []
                    for i in self.k:
                        s = d1(i[3])
                        s = s.split(',')
                        # if date(int(s[0]),int(s[1]),int(s[2])) >
                        d2 = date.fromisoformat(i[3])
                        # print(date(int(s[0]),int(s[1]),int(s[2])) - date.today())
                        s = date(int(s[0]),int(s[1]),int(s[2])) - date(2020,6,15)
                        s = str(s)
                        # print(s[:3])
                        try:
                            if int(s[:3]) > 7:
                                k.append([i[0] ,i[3],int(s[:3])])
                        except: pass
                    return k

                
                # print(date2())
                s = date2()
                for i in s:
                    # print(i[0])
                    cur.execute(f"""SELECT  f.issue_id,a.library_id,a.title,b.std_name,c.branch,b.pin_no,a.price
                                    ,f.date1
                                    FROM book a,std b,branch c,sem d,publication e,issue f
                                    WHERE a.publication_id = e.pub_id
                                    AND a.branch_id = c.branch_id AND
                                    a.semester_id = d.sem_id 
                                    AND f.std_id = b.library_id 
                                    AND f.book_id = a.library_id
                                    AND f.issue_id = {i[0]}""")
                    rows = cur.fetchall()
                    if len(rows) != 0:
                        books_table.delete(*books_table.get_children())
                        for row in rows:
                            row = list(row)
                            row.append(i[2])
                            books_table.insert('', END, values=row)
                            con.commit()

                cur.close()
                con.close()

            Table_Frame = Frame(f8, bd=2, bg="white")
            Table_Frame.place(relx=0.04, rely=0.32,
                              relwidth=0.94, relheight=0.4)

            Label(f8, font=15, borderwidth=1, relief=SUNKEN, textvariable=self.book_title_var).place(
                relx=0.05, rely=0.23, relwidth=0.25, relheight=0.04)
            ttk.Button(f8, text="View", style="C.TButton", cursor="hand2", command=view2).place(
                relx=0.33, rely=0.23, relwidth=0.12, relheight=0.05)

            scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
            scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

            books_table = ttk.Treeview(Table_Frame, columns=(
                'Issue_ID', 'Book serial', 'Book Title', 'Student_name', 'Branch', 'Student_Pin_No', 'Price' , 'Date OF Issued', 'Penality'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x.config(command=books_table.xview)
            scroll_y.config(command=books_table.yview)

            books_table.heading("Issue_ID", text="Issue_ID")
            books_table.heading("Book serial", text="Book serial")
            books_table.heading("Book Title", text="Book Title")
            books_table.heading("Student_name", text="Student_name")
            books_table.heading("Branch", text="Branch")
            books_table.heading("Student_Pin_No", text="Student_Pin_No")
            books_table.heading("Price", text="Price")
            books_table.heading("Date OF Issued", text="Date OF Issued")
            books_table.heading("Penality", text="Penality")

            books_table['show'] = 'headings'
            books_table.column("Issue_ID", width=60)
            books_table.column("Book serial", width=75)
            books_table.column("Book Title", width=100)
            books_table.column("Student_name", width=100)
            books_table.column("Branch", width=60)
            books_table.column("Student_Pin_No", width=100)
            books_table.column("Price", width=60)
            books_table.column("Date OF Issued", width=100)
            books_table.column("Penality", width=70)
            books_table.pack(fill=BOTH, expand=1)

            fetch_all()

            def get_cursor(event):
                curosor_row = books_table.focus()
                contents = books_table.item(curosor_row)
                row = contents['values']
                self.book_title_var.set(row[2] + '    (' + str(row[0]) + ')')
                self.b = self.book_title_var.get()

            books_table.bind("<ButtonRelease-1>", get_cursor)

        ttk.Button(f8, text="Show All", style="C.TButton", cursor='hand2', command=show).place(
            relx=0.74, rely=0.18, relwidth=0.24, relheight=0.07)

    def logout(self):
        self.__init__(root)

    def view(self):
        self.l1.configure(bg="pale green")
        vi = Frame(self.l1, bg="cadetblue3")
        vi.place(relx=0, rely=0, relwidth=1 , relheight=1)
        

        def fetch_data():
            con = psycopg2.connect(
                host="localhost",
                database='d3',
                user="postgres",
                password="psql",
            )
            cur = con.cursor()
            cur.execute("""SELECT  a.library_id,a.pin_no,a.std_name,b.branch,a.gender,
                    a.email,a.phone,a.total_transaction,a.pending_books,a.penality,
                    a.std_address
                    FROM std a,branch b
                    WHERE a.branch_id = b.branch_id """)

            rows = cur.fetchall()
            s = self.std_name_var.get()
            s = s.split()
            for row in rows:
                if s[0] == row[1]:
                    self.std_name_var.set(row[2])
                    self.pin_no_var.set(row[1])
                    self.branch_var.set(row[3])
                    self.library_id_var.set(row[0])
                    self.email_var.set(row[5])
                    self.transaction_var.set(row[7])
                    self.pending_book_var.set(row[8])
                    self.phone_var.set(row[6])
                    self.penality_var.set(row[9])
                    self.address_var.set(row[10])

            con.close()
        fetch_data()

        Label(vi, text="Student Details", bg="old lace", font=(
            'times', 25, 'bold')).place(relx=0, rely=0, relwidth=1, relheight=0.07)

        fr = Frame(vi, bg="light blue", borderwidth=1, relief=SUNKEN)
        fr.place(relx=0.03, rely=0.09, relwidth=0.9, relheight=0.7)

        Label(fr, text=self.std_name_var.get(), bg="chocolate",fg="white", font=('times',20,'bold')).place(
            relx=0, rely=0, relwidth=1, relheight=0.07)
        Label(fr, text="Student Id            :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.1)
        Label(fr, text="Student Name      :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.18)
        Label(fr, text="Mobile                  :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.26)
        Label(fr, text="Branch                  :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.34)
        Label(fr, text="Library Id            :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.42)
        Label(fr, text="Email Id                :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.5)
        Label(fr, text="Address               :", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.58)
        Label(fr, text="Total Transactions :", fg="red", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.66)
        Label(fr, text="pending books         :", fg="red", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.74)
        Label(fr, text="penality                 :", fg="red", font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.1, rely=0.82)

        #=-----------------------------
        address = "visakhapatnam"
        Label(fr, text=self.pin_no_var.get(), font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.4, rely=0.1)
        Label(fr, text=self.std_name_var.get(), font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.4, rely=0.18)
        Label(fr, text=self.phone_var.get(), font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.4, rely=0.26)
        Label(fr, text=self.branch_var.get(), font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.4, rely=0.34)
        Label(fr, text=self.library_id_var.get(), font=(
            'times', 15, 'bold'), bg="light blue").place(relx=0.4, rely=0.42)
        Label(fr, text=self.email_var.get(), font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.4, rely=0.5)
        Label(fr, text=self.address_var.get(), font=('times', 15, 'bold'),
              bg="light blue").place(relx=0.4, rely=0.58)
        Label(fr, text=self.transaction_var.get(), font=('times', 15,
                                                         'bold'), fg="red", bg="light blue").place(relx=0.4, rely=0.66)
        Label(fr, text=self.pending_book_var.get(), font=('times', 15,
                                                          'bold'), fg="red", bg="light blue").place(relx=0.4, rely=0.74)
        Label(fr, text=self.penality_var.get(), font=('times', 15, 'bold'), fg="red",
              bg="light blue").place(relx=0.4, rely=0.82)
        def back():
            self.Student_report()
        ttk.Button(fr,text="Back",style="C.TButton",cursor="hand2",command=back).place(relx=0.8,rely=0.9)

        #---------------------------------
        #---------------------------------

        #---------------------------------
        #---------------------------------
        

    def db(self):
        import psycopg2

        conn = psycopg2.connect(
            host="localhost",
            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXiSTS book(id SERIAL PRIMARY KEY,
                library_id INT UNIQUE NOT NULL,
                title VARCHAR NOT NULL,
                author VARCHAR NOT NULL,
                publication_id int NOT NULL,
                branch_id int NOT NULL,
                semester_id int NOT NULL,
                price INT NOT NULL,
                total_quantity INT NOT NULL,
                quantity_avail INT NOT NULL,
                details VARCHAR NOT NULL
                )

        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS std(library_id Serial PRIMARY KEY,
                pin_no VARCHAR UNIQUE NOT NULL,
                std_name VARCHAR NOT NULL,
                branch_id INT NOT NULL,
                gender VARCHAR NOT NULL,
                dob VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                phone VARCHAR NOT NULL,
                pass VARCHAR NOT NULL,
                std_address VARCHAR NOT NULL,
                total_transaction INT NOT NULL,
                pending_books INT NOT NULL,
                penality INT NOT NULL
            )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS publication(
            id SERIAL PRIMARY KEY,
            name VARCHAR UNIQUE NOT NULL,
            pub_id INT UNIQUE NOT NULL
            )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS branch(
            id SERIAL PRIMARY KEY,
            branch VARCHAR UNIQUE NOT NULL,
            branch_id INT UNIQUE NOT NULL
            )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS sem(
            id SERIAL PRIMARY KEY,
            sem VARCHAR UNIQUE NOT NULL,
            sem_id INT UNIQUE NOT NULL
            )""")

        cur.execute("""CREATE TABLE IF NOT EXISTS issue(
            issue_id SERIAL PRIMARY KEY,
            std_id INT UNIQUE NOT NULL,
            book_id INT UNIQUE NOT NULL,
            date1 VARCHAR NOT NULL
            )""")

        conn.commit()
        cur.close()
        conn.close()

    def branch_id_fun(self, name):
        d = {'CSE': 1,
             'ECE': 2,
             'MECH': 3,
             'EEE': 4,
             'CIVIL': 5,
             'ITI': 6}
        return d[name]

    def sem_id_fun(self, name):
        d = {'I  Semester': 1,
             'III Semester': 2,
             'IV Semester': 3,
             'V Semester': 4
             }
        return d[name]

    def sem_data(self):
        conn = psycopg2.connect(
            host="localhost",
            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM sem")
        s = cur.fetchall()
        a = {}
        for i in s:
            a[i[1]] = i[2]
        conn.commit()
        cur.close()
        conn.close()

        return [i[1] for i in s]

    def pub_id(self, n):
        conn = psycopg2.connect(
            host="localhost",
            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM publication")
        s = cur.fetchall()
        a = {}
        for i in s:
            a[i[1]] = i[2]
        conn.commit()
        cur.close()
        conn.close()
        return a[n]

    def pub_data(self):
        conn = psycopg2.connect(
            host="localhost",
            database='d3',
            user="postgres",
            password="psql",
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM publication")
        s = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return [i[1] for i in s]



root = Tk()
s = project(root)
root.mainloop()
