# GitHubIssueAlertBot

## Description

Extremely simple Telegram Bot that notifies you whenever there is an update in the issue you want to focus on.
Plus, as a previous feature (90% of the code comes from another project of mine): if the computer it's running on has a DISPLAY, it will try to show up a dialog, that way it can be twice as annoying.

**THE BOT IS NOT PUBLIC FOR NOW, AND IF YOU WANT TO USE IT YOU'LL HAVE TO CREATE YOUR OWN BOT AND TWEAK IT**

## How to get it to work
Modify __auth.py.template__ to your needs, it is pretty self-explanatory, and do not forget to change the name of the file to __auth.py__, or it won't work (duh).

If you are in Linux, all you'd need to do is to add the execution of the Bot to crontab.

If on the contrary, you are in Windows, I believe to recall there was some way to run Scheduled Tasks but... For now, you are on your own, Internet has the answer. Maybe, if someone needs it, I'll explain here how to.

**Notice:** You don't want the bot to notify you more than once per minute, trust me on this one, if you use this bot to make anonymous requests to the GitHub API (as it is now the code on its actual state) the limit is on 60, I think. Check it here:
https://developer.github.com/v3/#rate-limiting

## Disclaimer

I'm aware that it is pretty awkward to use for now. The reason is that it's initially supposed for my use only, but anyone can.

This is the first "useful" Telegram Bot I make, but as in: it's not the first Telegram Bot made by me following a tutorial...
So please, be merciful, and if you have any issues or ideas I'll be happy to know.

Oh, and English is not my first language, so feel free to let me know when something I wrote is incomprehensible.

In the near (-ish) future I will have the next features added so it can be much useful.

## To-Do:
 - Get more details of the update in the Issuew
 - Find a better way to run the Bot without having to execute the program from crontab
 - Let the bot take the chat_id from the chat instead of the actual static implementation
 - Let the user select the issue he wants to be watching
 - Let the user watch various issues and not just one
 - Let the user remove issues to watch
 - Let the user decide if he wants to be notified using the dialog as well
 - Increase the limit of searches in GitHub API (I will do this one only if there is a considerable number of people interested)
