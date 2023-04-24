from models import db, FlashCard

# Creating Tables for database
db.drop_tables([FlashCard])
db.create_tables([FlashCard])


# Seed the database with data
card1 = FlashCard(russian_word = 'да (da)', english_word = 'yes')
card1.save()

card3 = FlashCard(russian_word = 'нет (net)', english_word = 'no')
card3.save()

card4 = FlashCard(russian_word = 'спасибо (spa-si-bo)', english_word = 'thank you')
card4.save()

card5 = FlashCard(russian_word = 'русский (rus-skiy)', english_word = 'russian')
card5.save()

card6 = FlashCard(russian_word = 'любить (lyu-bit)', english_word = 'to love')
card6.save()

card7 = FlashCard(russian_word = 'писать (na-pi-sat)', english_word = 'to write')
card7.save()

card7 = FlashCard(russian_word = 'писать (na-pi-sat)', english_word = 'to write')
card7.save()

card9 = FlashCard(russian_word = 'думать (du-mat)', english_word = 'to think')
card9.save()

card10 = FlashCard(russian_word = 'читать (chit-at)', english_word = 'to read')
card10.save()

card11 = FlashCard(russian_word = 'говорить (go-vo-rit)', english_word = 'to speak')
card11.save()

card12 = FlashCard(russian_word = 'играть (ig-rat)', english_word = 'to play')
card12.save()

card13= FlashCard(russian_word = 'слышать (sly-shat)', english_word= 'to hear')
card13.save()

card14 = FlashCard(russian_word = 'смотреть (smo-tr-et)', english_word = 'to look')
card14.save()

card15 = FlashCard(russian_word = 'видеть (vi-det)', english_word = 'to see')
card15.save()

card16 = FlashCard(russian_word = 'понимать (po-ni-mat)', english_word = 'to understand')
card16.save()

card17 = FlashCard(russian_word = 'давать (da-va-t)', english_word = 'to give')
card17.save()

card18 = FlashCard(russian_word = 'работать (ra-bo-ta-t)', english_word = 'to work')
card18.save()

card19 = FlashCard(russian_word = 'спать (sp-a-t)', english_word = 'to sleep')
card19.save()

card20 = FlashCard(russian_word = 'знать (z-n-at)', english_word = 'to know')
card20.save()

card21 = FlashCard(russian_word = 'сидеть (si-de-t)', english_word = 'to sit')
card21.save()

card22 = FlashCard(russian_word = 'слушать (sl-u-sh-at)', english_word = 'to listen')
card22.save()

card23 = FlashCard(russian_word = 'пить (p-i-t)', english_word = 'to drink')
card23.save()

card24 = FlashCard(russian_word = 'открывать (ot-kr-y-vat)', english_word = 'to open')
card24.save()

card25 = FlashCard(russian_word = 'хотеть (k-ho-te-t)', english_word = 'to want')
card25.save()

card26 = FlashCard(russian_word = 'входить (v-kh-od-it)', english_word = 'to enter')
card26.save()

card27 = FlashCard(russian_word = 'плакать (pl-ak-a-t)', english_word = 'to cry')
card27.save()

card28 = FlashCard(russian_word = 'брать (b-r-a-t)', english_word = 'to take')
card28.save()

card29 = FlashCard(russian_word = 'бежать (b-ez-ha-t)', english_word = 'to run')
card29.save()

card30 = FlashCard(russian_word = 'забывать (za-b-y-vat)', english_word = 'to forget')
card30.save()

card31 = FlashCard(russian_word = 'рассказывать (ras-sk-az-y-va-t)', english_word = 'to tell')
card31.save()

card32 = FlashCard(russian_word = 'учиться (u-chi-ts-ya)', english_word = 'to study')
card32.save()

card33 = FlashCard(russian_word = 'помогать (po-mo-ga-t)', english_word = 'to help')
card33.save()

card34 = FlashCard(russian_word = 'покупать (po-ku-pa-t)', english_word = 'to buy')
card34.save()

card35 = FlashCard(russian_word = 'стоять (st-oy-a-t)', english_word = 'to stand')
card35.save()

card36 = FlashCard(russian_word = 'верить (ver-i-t)', english_word = 'to believe')
card36.save()

card37 = FlashCard(russian_word = 'лежать (le-zha-t)', english_word = 'to lie down')
card37.save()

card38 = FlashCard(russian_word = 'петь (p-et)', english_word = 'to sing')
card38.save()

card39 = FlashCard(russian_word = 'уходить (uk-ho-di-t)', english_word = 'to leave')
card39.save()

card40 = FlashCard(russian_word = 'кушать (ku-sh-a-t)', english_word = 'to eat')
card40.save()

card41 = FlashCard(russian_word = 'спрашивать (sp-ra-shi-va-t)', english_word = 'to ask')
card41.save()

card42 = FlashCard(russian_word = 'ждать (zh-da-t)', english_word = 'to wait')
card42.save()

card43 = FlashCard(russian_word = 'приходить (pr-ik-ho-di-t)', english_word = 'to come')
card43.save()

card44 = FlashCard(russian_word = 'решать (re-sh-a-t)', english_word = 'to solve')
card44.save()

card45 = FlashCard(russian_word = 'улыбаться (u-lyb-at-s-y-a)', english_word = 'to smile')
card45.save()

card46 = FlashCard(russian_word = 'смеяться (sme-ya-ts-y-a)', english_word = 'to laugh')
card46.save()

card47 = FlashCard(russian_word = 'терять (ter-ya-t)', english_word = 'to lose')
card47.save()

card48 = FlashCard(russian_word = 'нравиться (nr-av-it-sy-a)', english_word = 'to like')
card48.save()

card49 = FlashCard(russian_word = 'обещать (ob-esh-ch-a-t)', english_word = 'to promise')
card49.save()

card50 = FlashCard(russian_word = 'получать (poluchat)', english_word = 'to receive')
card50.save()

card50 = FlashCard(russian_word = 'называть (na-zyv-a-t)', english_word = 'to name')
card50.save()

card50 = FlashCard(russian_word = 'вести (vesti)', english_word = 'to lead')
card50.save()