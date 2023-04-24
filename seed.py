from models import db, FlashCard

# Creating Tables for database
db.create_tables([FlashCard])

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