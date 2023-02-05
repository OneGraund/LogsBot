from sheet_manipulator import Logs
#available functions: Logs.amount(), Logs.get_header(), Logs.by_num(), Logs.as_dict(), Logs.__str__()
from tg_token import TOKEN, GROUP_ID
import telebot
import time

fname = "UCS r_keeper KFC Logs form (Ответы)"
wksname = 'Ответы на форму (1)'

logs = []
logs.append(Logs(fname, wksname))

bot = telebot.TeleBot(TOKEN)

def generate_message(last_log):
    elem=1
    if elem == 1:
        if last_log[elem] == '(AT) Brunn':
            last_log[elem] = '#brunn'
        elif last_log[elem] == '(AT) Columbus':
            last_log[elem] = '#donau'
        elif last_log[1] == '(AT) Floridsdorf':
            last_log[1] = '#floridsdorf'
        elif last_log[1] == '(AT) Linz Plus City':
            last_log[1] = '#linz'
        elif last_log[1] == '(AT) Lugner City':
            last_log[1] = '#lugner'
        elif last_log[1] == '(AT) Mariahilfe':
            last_log[1] = '#maria'
        elif last_log[1] == '(AT) Millennium':
            last_log[1] = '#millenium'
        elif last_log[1] == '(AT) Parndorf':
            last_log[1] = '#parndorf'
        elif last_log[1] == '(AT) SCS':
            last_log[1] = '#scs'
        elif last_log[1] == '(Bosnia) scc':
            last_log[1] = '#scc'
        elif last_log[1] == '(SK) AuPark':
            last_log[1] = '#aupark'
        elif last_log[1] == '(SK) Banska Bystrica':
            last_log[1] = '#banska'
        elif last_log[1] == '(SK) BoryMall':
            last_log[1] = '#borymall'
        elif last_log[1] == '(SK) Cisco Trnava':
            last_log[1] = '#ciscotrnava'
        elif last_log[1] == '(SK) Nivy':
            last_log[1] = '#nivy'
        elif last_log[1] == '(SK) RELAXX':
            last_log[1] = '#relaxx'
        elif last_log[1] == '(SK) Trnava Drive':
            last_log[1] = '#trnavadrive'
        elif last_log[1] == '(SK) VIVO':
            last_log[1] = '#vivo'
    return (f'{last_log[1]}, {last_log[2]}, {last_log[3]},\n'
              f'{last_log[4]}, {last_log[5]}, {last_log[6]}')

def send(msg, chat_id):
    print(f'Sending message:\n{msg}')
    bot.send_message(chat_id=chat_id, text=msg)

while 1:
    #ininite loop
    for i in range(26):
        time.sleep(5)
        print(f'Waiting {120-i*5} more seconds')
    logs.append(Logs(fname, wksname))
    print(f'Amount of logs before: {logs[0].amount()}\n'
          f'After: {logs[1].amount()}')
    if logs[0].amount()!=logs[1].amount():
        last_log=logs[1].by_num(logs[1].amount())
        send(generate_message(last_log), GROUP_ID)
    logs.pop(0)


bot.infinity_polling()