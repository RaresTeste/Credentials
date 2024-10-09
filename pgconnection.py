import tkinter
import psycopg2
from tkinter import Entry, Button, Tk


def save_db(first_name, second_name):
    try:
        # Conectare la baza de date PostgreSQL
        conn = psycopg2.connect(
            host='localhost', 
            dbname='postgres',  
            user='postgres', 
            password='rares', 
            port='5432'
        )
        print("Conectat la baza de date cu succes!")
        
        # Crearea unui cursor
        cursor = conn.cursor()

        # Interogare SQL pentru tabelul 'names_new'
        insert_query = "INSERT INTO names_new (first_name, second_name) VALUES (%s, %s);"
        cursor.execute(insert_query, (first_name, second_name))
        
        # Confirmarea tranzacției
        conn.commit()
        
        print("Datele au fost salvate în baza de date!")
        
    except Exception as e:
        print(f"A apărut o problemă cu conexiunea sau interogarea: {e}")
        
    finally:
        # Închiderea cursorului și a conexiunii
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


def submit_button():
    first_name = entry_first_name.get()  
    second_name = entry_second_name.get()  
    print(f"Nume introdus: {first_name} {second_name}")
    save_db(first_name, second_name)  # Salvează în baza de date
    

#creearea / configurarea pagininii web 
window = Tk()
window.title("Enter your credentials")
window.geometry('400x400')


# Crearea / configurarea câmpului pentru 'first_name'
first_name_label = tkinter.Label(window, text = "First Name")
first_name_label.grid(row=1, column=0)
entry_first_name = tkinter.Entry(window, width=23) 
entry_first_name.grid(row=1, column=1)


# Crearea / configurarea câmpului pentru 'second_name'
second_name_label = tkinter.Label(window, text="Second Name")
second_name_label.grid(row=2, column=0, padx=10, pady=5)
entry_second_name = tkinter.Entry(window, width=23)
entry_second_name.grid(row=2, column=1, padx=10, pady=5)

# Crearea butonului și configurarea acestuia
button = Button(window, text="Save", command=submit_button)
button.grid(row=3, column=1)



window.mainloop()
