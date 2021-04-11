import ptbot
import os


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(text):
    sec = 0
    for c in text:
        if c >= '0' and c <= '9':
            sec *= 10
            sec += int(c)

    start_timer = "Таймер запущен на " + str(sec) + " секунд(ы)."
    bot.send_message(TG_CHAT_ID, start_timer)

    message_id = bot.send_message(TG_CHAT_ID, "Осталось " + str(sec) + " секунд(ы).")
    sec_at_start = sec

    id_progressbar = bot.send_message(TG_CHAT_ID,
                                      render_progressbar(sec_at_start, sec))
    sec -= 1
    for k in range(sec):
        bot.update_message(TG_CHAT_ID, message_id, "Осталось " + str(sec) + " секунд(ы).")
    sec -= 1

    bot.update_message(TG_CHAT_ID, id_progressbar, render_progressbar(sec_at_start, sec))

    bot.send_message(TG_CHAT_ID, "Время вышло...")


token = os.getenv("TOKEN")
TG_TOKEN = token
TG_CHAT_ID = '356122881'
bot = ptbot.Bot(token)
bot.send_message(TG_CHAT_ID, "На сколько секунд запустить таймер?")

bot.reply_on_message(reply)

bot.run_bot()


