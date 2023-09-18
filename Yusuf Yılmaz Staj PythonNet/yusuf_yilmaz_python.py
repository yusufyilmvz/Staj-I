import json
from sqlite3 import connect
# Adli Analiz Yazılımı projesinde bu işlem otomatize bir şekilde yapılmaktadır.
def veritabani_mesajlar_al() -> list:
    baglanti = connect("chat.sqlite")
    imlec = baglanti.cursor()
    # SQL Query
    imlec.execute('''SELECT cm.messageBody as mesaj, cm.timestamp, c.realName as isim,
    c.username as kullanici_isimi FROM ChatMessage as cm
    LEFT JOIN Contact as c on c.userID = cm.userID;''')
    tupple_sonuc = imlec.fetchall()
    liste_sonuc = []
    for sonuc in tupple_sonuc:
        gecici_dictionary = {
            "mesaj_govdesi": sonuc[0],
            "timestamp": sonuc[1],
            "isim": sonuc[2],
            "kullanici_adi": sonuc[3]
        }
        liste_sonuc.append(gecici_dictionary)

    baglanti.close()
     # .NET tarafına göndermek için serialize etme işlemi
    return json.dumps(liste_sonuc)

# print(veritabani_mesajlar_al())