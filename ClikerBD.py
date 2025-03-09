import flet as ft
import sqlite3
import time

def main(page: ft.Page):

    page.window.height = 900
    page.window.width = 400
    page.theme = ft.Theme(hint_color=ft.Colors.WHITE)
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    

    #БД создание
    
    db = sqlite3.connect("Orange3.db")

    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                name TEXT,
                token TEXT,
                lvl INTEGER,
                score INTEGER,
                EXP INTEGER
                )""")
    
    db.commit()
    db.close()
    #вход

    #БД
    def basareg(e):
        db = sqlite3.connect("Orange3.db")

        cur = db.cursor()

        cur.execute(f"INSERT INTO user VALUES(NULL, '{field1.value}', '{field2.value}', 1, 0, 0)")

        db.commit()
        db.close()
    
    def basavh(e):
        db = sqlite3.connect("Orange3.db")

        cur = db.cursor()

        cur.execute(f"SELECT * FROM user WHERE name = '{field1.value}' AND token = '{field2.value}'")
        data = cur.fetchone()

        #передаем данные в UI
        
        if data != None:
        
            for el in data:
                print(el)
                star.value = data[4]
                lvl.value = data[3]
                page.clean() 
                page.add(playUI)
                page.update()
        else:
            basareg(e)

        db.commit()
        db.close()




    field1 = ft.TextField(hint_text="Имя", width=200, border_color=ft.Colors.ORANGE, border_radius=10)
    field2 = ft.TextField(hint_text="Ваш токен", width=200, border_color=ft.Colors.ORANGE, border_radius=10)
    button = ft.ElevatedButton(text="Вход", bgcolor=ft.Colors.BLACK,width=200, on_click=basavh)
    register = ft.Column([
        ft.Image(src="https://github.com/Egor698/Orange/blob/main/2025-03-07_10-53-34%201%20(1).png?raw=true"),
        ft.Row([field1], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([field2], alignment=ft.MainAxisAlignment.CENTER),
        button
        
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
   

    #обновление счета в БД
    def score_upBD(e):

        db = sqlite3.connect("Orange3.db")

        cur= db.cursor()
        
        cur.execute(f"UPDATE user SET score = score + 10 WHERE name = '{field1.value}' AND token = '{field2.value}' ")

        db.commit()
        db.close()
    #мехфника lvlbar 
    def mexlvlbar(e):
        if lvlbar.value == 1:
            lvlbar.value = 0
            db = sqlite3.connect("Orange3.db")

            cur = db.cursor()

            cur.execute(f"UPDATE user SET lvl = lvl + 1 WHERE name = '{field1.value}' AND token = '{field2.value}'")
            db.commit()
            db.close()
            lvl.value += 1
            page.update()
    
   
    #механика
    def score_up(e):
        n = score.data / 100
        image.scale = 0.9 #анимация
        score.data += 1 #логика очков
        score.value = str(score.data)
        progressBar.value += 0.1
        if score.data % 10 == 0: #and score.data / 10 < 10:
            snackBar10 = ft.SnackBar(content=ft.Row([ft.Text("🍪 +10", size=20, color=ft.Colors.BROWN_800, weight=ft.FontWeight.W_500)], alignment=ft.MainAxisAlignment.CENTER), bgcolor=ft.Colors.BLACK26)
            progressBar.value = 0
            lvlbar.value += 0.5
            mexlvlbar(e)
            score_upBD(e)
            page.update()
            page.open(snackBar10)
        elif n.is_integer() and n != 0:
            snackBar100 = ft.SnackBar(content=ft.Row([ft.Text("🍪 +100", size=20, color=ft.Colors.BROWN_800, weight=ft.FontWeight.W_500)], alignment=ft.MainAxisAlignment.CENTER), bgcolor=ft.Colors.BLACK26)
            progressBar.value = 0
            lvlbar.value += 0.1
            mexlvlbar(e)
            page.update()
            page.open(snackBar100)
        page.update()
        time.sleep(0.1) #анимация
        image.scale = 1
        page.update()
   
                 
        
    #UI
    star = ft.Text(value="", weight=ft.FontWeight.W_500)
    #контейнер с прогрессом

    #lvl.value - левел, lvlbar.value, gifebocks
    lvl = ft.Text(value="1", weight=ft.FontWeight.W_700)
    lvlbar = ft.ProgressBar(color=ft.Colors.BROWN_300, width=200, value=0, border_radius=20, height=15)
    gifebocks = ft.Image(src="https://cdn-icons-png.flaticon.com/128/8146/8146553.png", width=40, height=40, fit=ft.ImageFit.CONTAIN)
    lvlcontainer = ft.Container(
        width=40, 
        height=40, 
        border_radius=20, 
        content=lvl, 
        alignment=ft.alignment.center, 
        border=ft.border.all(1.5, ft.colors.BROWN_900))
    
    progress = ft.Container(
        width=400, 
        height=45, 
        bgcolor=ft.colors.BLACK,
        border_radius=20, 
        content=ft.Row([lvlcontainer,lvlbar, gifebocks], alignment=ft.MainAxisAlignment.CENTER))
    
        
    progressBar = ft.ProgressBar(color=ft.Colors.BROWN_300, value=0, width=page.window.width - 60, height=20, border_radius=10)
    image = ft.Image(src="https://github.com/Egor698/Orange/blob/main/808851%201.png?raw=true")
    score = ft.Text("0", weight=ft.FontWeight.W_500, size=100, data=0)
    playUI = ft.Column([
    progress,
    ft.Row([score], alignment=ft.MainAxisAlignment.CENTER),
    ft.Container(content=image, alignment=ft.alignment.center, on_click=score_up),
        
    ft.Row([progressBar], alignment=ft.MainAxisAlignment.CENTER)
        ])
    


    #панельуправления

    #UIbottomBar = ft.BottomAppBar(bgcolor=ft.Colors.BLACK12, content=
        
            #ft.Row([
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/686/686589.png"), on_click=UI),
            #ft.VerticalDivider(thickness=2),
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/2948/2948037.png"), on_click=menu),
            #ft.VerticalDivider(thickness=2),
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/3094/3094830.png"), on_click=competition),
            #ft.VerticalDivider(thickness=2),
            #ft.IconButton(content=ft.Image(src="https://cdn-icons-png.flaticon.com/128/2976/2976215.png"), on_click=setting)
            #], alignment=ft.MainAxisAlignment.SPACE_AROUND)
            
            
    #)




    page.add(register)









ft.app(target=main)
