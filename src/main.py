import requests, json, pymsgbox, telebot
from config.auth import *

def main():
    '''
    retrieves the actual number of comments in the issue and calls
    each function to check, notify the user and save the changes
    '''
    COMMENT_URL = API_ISSUE_URL + 'comments?page={}'
    num, page, total = 1, 1, 0
    while not num == 0:
        r = requests.get(COMMENT_URL.format(str(page)))
        comments = r.json()
        num = len(comments)
        total += num
        page += 1
    print(total, 'comments in issue')
    check(total)
    save(total)

def check(total):
    '''
    Compares the actual number of comments in the issue with a previous
    count saved in a text file. Notifies the user if needed.
    '''
    try:
        with open(FILE_PATH + 'n_comments.txt', 'rt') as txt:
            num = int(txt.readline())
            if(num < total):
                print('Update')
                print('\a')
                try:
                    bot.send_message(CHAT_ID, 'New comment on issue! Check it: ' + ISSUE_URL)
                    pymsgbox.alert('New comment on issue!', 'GitHub update')
                except:
                    print('Error, no display or issue contacting bot')
                    raise
    except IOError:
        print("File not accessible")

def save(total):
    '''
    Updates the number of comments in a text file to check it the next time
    '''
    with open(FILE_PATH + 'n_comments.txt', 'wt') as txt:
        txt.write(str(total))

if __name__ == '__main__':
    bot = telebot.TeleBot(TOKEN)
    main()