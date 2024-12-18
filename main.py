import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7683636155:AAHJGfelgE7ZWu6bP0SIwdvT-Johe5HJ_gU')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, text='Привет! Рыжий хвостик здесь! '
                               'Если хочешь новую историю, то нажимай /hist')
    hist_tread = threading.Thread(target=send_hist, args=(message.chat.id,))
    hist_tread.start()



@bot.message_handler(commands=['hist'])
def hist_message(message):
    list = [
        'Сегодня Рыжик проснулся чуть раньше всех, чтобы увидеть, как на листьях расцветают жемчужины лунной росы. Подбежав к папоротнику, он потрогал один хрупкий шарик лапкой, и тот заиграл радужным светом. Лисёнок улыбнулся: теперь весь день будет наполнен тихим волшебством.',
        'Пробегая по лесу, Рыжик услышал звонкий смех. Это был пёстрый дятел, барабанивший по стволу дуба. Он показал лисёнку новое дерево с сокрытой полой, где можно спрятаться от дождя. Рыжик поблагодарил дятла и понял, что в лесу друзья встречаются на каждом шагу',
        'Вечером Рыжик вышел на поляну и увидел, как над травой порхают светлячки. Они кружились, образуя мерцающие нити света. Лисёнок замер, наблюдая за этим танцем, и почувствовал, что даже в тёмном лесу всегда есть место радости и красоте.',
        'Сегодня Рыжик встретил енотика, который загадочно подмигнул и скрылся за кустом малины. Лисёнок последовал за ним и обнаружил тайную полянку, усыпанную ягодами. Енотик не сказал ни слова, но Рыжик понял: иногда дружба выражается в добром жесте без лишних слов.',
        'Сегодня ветер принёс листочек с далёкой поляны. Прислушавшись, Рыжик уловил в его шелесте тихую историю о другом лисёнке, который тоже искал приключения. Поняв, что лес полон незримых связей и историй, Рыжик улыбнулся, ощущая себя частью большого мира.',
        'Рыжик заметил мышонка, который пытался переплыть неглубокий ручей. Лисёнок подтолкнул ему тонкую веточку, и тот смог перейти по ней, словно по мосту. Мышонок поблагодарил Рыжика взглядом, и лисёнок почувствовал, что героем можно стать просто подарив поддержку.',
        'Сегодня ночью Рыжик услышал странную мелодию. Приглядевшись, он увидел, что это сова тихо подпевает лунному свету. Лисёнок понял: каждая ночь — концерт, каждая тень — танцор, и в этом волшебстве лес делится с ним своими тайнами.',
        'После ночного дождя на ветке берёзы осталась капелька воды. В ней отражалось всё вокруг: и голубое небо, и листва, и сам Рыжик, подошедший полюбоваться. Лисёнок понял, что порой целый мир можно увидеть в одной крохотной капле.',
        'Сегодня Рыжик задремал под шепот ветра и проснулся от мягкого прикосновения листа, опустившегося на его мордочку. Он улыбнулся, понимая, что даже короткий сон может подарить новые силы и свежий взгляд на день.',
        'Вечером лисёнок наблюдал, как перелётные птицы выстраиваются клином в небе. Их крики звучали, будто они пересчитывают друг друга перед долгим путешествием. Рыжик пожелал им счастливого пути, зная, что лес всегда будет рад их возвращению.',
        'Сегодня на заре Рыжик забрался на пригорок и прислушался к тишине. Он понял, что даже в молчании лес говорит с ним — о покое, о мире и о том, что настоящий ответ иногда приходит, когда перестаёшь задавать вопросы.',
        'На окраине леса лисёнок увидел опавший лист, который ветер подхватил и закружил. Наблюдая за ним, Рыжик осознал: всё в мире меняется, но перемены — это не конец, а лишь начало нового пути.',
        'Прислонив ухо к стволу векового дерева, Рыжик услышал шёпот прошлого. Он подумал, что мудрость леса — как глубокие корни, соединяющие поколения, а мы можем учиться, если будем слушать сердцем.',
        'Старая белка собирала орехи не только для зимы, но и для памяти о жарких днях лета. Рыжик понял, что воспоминания — это наша невидимая корзинка, в которую мы складываем уроки и радость каждого прожитого дня.',
        'В сумерках Рыжик увидел одинокого светлячка. Он подумал: даже крохотный огонёк может осветить темноту, а значит, каждый из нас, делая доброе дело, становится лучиком, который преодолевает мрак.',
        'Вода в роднике оставалась чистой, несмотря на палые листья. Рыжик задумался, что так и душа может быть светлой, если научиться пропускать через себя переживания, не задерживая обиду и страх.',
        'Наблюдая за тем, как птицы, насекомые и звери уживаются в одном лесу, лисёнок понял: разные голоса могут звучать вместе, создавая мелодию согласия. Мы все разные, но в этом и есть секрет общего счастья.',
        'Вечером лисёнок сидел у ручья, глядя, как свет луны отражается в воде. Он понял, что смотреть спокойно — значит уметь видеть глубже. Чем ровнее твой взгляд, тем яснее становятся истины, скрытые за рябью повседневности.']
    random_hist = random.choice(list)
    bot.reply_to(message,  text=f'Пришло время новой истории:  {random_hist}')

def send_hist(chat_id):
    first_hist = "10:00"
    second_hist = "16:00"
    end_hist = "20:00"
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_hist or now == second_hist or now == end_hist:
            list = [
                'Сегодня Рыжик проснулся чуть раньше всех, чтобы увидеть, как на листьях расцветают жемчужины лунной росы. Подбежав к папоротнику, он потрогал один хрупкий шарик лапкой, и тот заиграл радужным светом. Лисёнок улыбнулся: теперь весь день будет наполнен тихим волшебством.',
                'Пробегая по лесу, Рыжик услышал звонкий смех. Это был пёстрый дятел, барабанивший по стволу дуба. Он показал лисёнку новое дерево с сокрытой полой, где можно спрятаться от дождя. Рыжик поблагодарил дятла и понял, что в лесу друзья встречаются на каждом шагу',
                'Вечером Рыжик вышел на поляну и увидел, как над травой порхают светлячки. Они кружились, образуя мерцающие нити света. Лисёнок замер, наблюдая за этим танцем, и почувствовал, что даже в тёмном лесу всегда есть место радости и красоте.',
                'Сегодня Рыжик встретил енотика, который загадочно подмигнул и скрылся за кустом малины. Лисёнок последовал за ним и обнаружил тайную полянку, усыпанную ягодами. Енотик не сказал ни слова, но Рыжик понял: иногда дружба выражается в добром жесте без лишних слов.',
                'Сегодня ветер принёс листочек с далёкой поляны. Прислушавшись, Рыжик уловил в его шелесте тихую историю о другом лисёнке, который тоже искал приключения. Поняв, что лес полон незримых связей и историй, Рыжик улыбнулся, ощущая себя частью большого мира.',
                'Рыжик заметил мышонка, который пытался переплыть неглубокий ручей. Лисёнок подтолкнул ему тонкую веточку, и тот смог перейти по ней, словно по мосту. Мышонок поблагодарил Рыжика взглядом, и лисёнок почувствовал, что героем можно стать просто подарив поддержку.',
                'Сегодня ночью Рыжик услышал странную мелодию. Приглядевшись, он увидел, что это сова тихо подпевает лунному свету. Лисёнок понял: каждая ночь — концерт, каждая тень — танцор, и в этом волшебстве лес делится с ним своими тайнами.',
                'После ночного дождя на ветке берёзы осталась капелька воды. В ней отражалось всё вокруг: и голубое небо, и листва, и сам Рыжик, подошедший полюбоваться. Лисёнок понял, что порой целый мир можно увидеть в одной крохотной капле.',
                'Сегодня Рыжик задремал под шепот ветра и проснулся от мягкого прикосновения листа, опустившегося на его мордочку. Он улыбнулся, понимая, что даже короткий сон может подарить новые силы и свежий взгляд на день.',
                'Вечером лисёнок наблюдал, как перелётные птицы выстраиваются клином в небе. Их крики звучали, будто они пересчитывают друг друга перед долгим путешествием. Рыжик пожелал им счастливого пути, зная, что лес всегда будет рад их возвращению.',
                'Сегодня на заре Рыжик забрался на пригорок и прислушался к тишине. Он понял, что даже в молчании лес говорит с ним — о покое, о мире и о том, что настоящий ответ иногда приходит, когда перестаёшь задавать вопросы.',
                'На окраине леса лисёнок увидел опавший лист, который ветер подхватил и закружил. Наблюдая за ним, Рыжик осознал: всё в мире меняется, но перемены — это не конец, а лишь начало нового пути.',
                'Прислонив ухо к стволу векового дерева, Рыжик услышал шёпот прошлого. Он подумал, что мудрость леса — как глубокие корни, соединяющие поколения, а мы можем учиться, если будем слушать сердцем.',
                'Старая белка собирала орехи не только для зимы, но и для памяти о жарких днях лета. Рыжик понял, что воспоминания — это наша невидимая корзинка, в которую мы складываем уроки и радость каждого прожитого дня.',
                'В сумерках Рыжик увидел одинокого светлячка. Он подумал: даже крохотный огонёк может осветить темноту, а значит, каждый из нас, делая доброе дело, становится лучиком, который преодолевает мрак.',
                'Вода в роднике оставалась чистой, несмотря на палые листья. Рыжик задумался, что так и душа может быть светлой, если научиться пропускать через себя переживания, не задерживая обиду и страх.',
                'Наблюдая за тем, как птицы, насекомые и звери уживаются в одном лесу, лисёнок понял: разные голоса могут звучать вместе, создавая мелодию согласия. Мы все разные, но в этом и есть секрет общего счастья.',
                'Вечером лисёнок сидел у ручья, глядя, как свет луны отражается в воде. Он понял, что смотреть спокойно — значит уметь видеть глубже. Чем ровнее твой взгляд, тем яснее становятся истины, скрытые за рябью повседневности.']
            random_hist = random.choice(list)
            bot.send_message(chat_id, text=f'А вот и новая история: {random_hist} ')
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True)