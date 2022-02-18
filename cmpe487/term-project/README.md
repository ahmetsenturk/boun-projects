# Online Connect Four Game

<img width="251" class="center" alt="Screen Shot 2022-02-18 at 23 01 17" src="https://user-images.githubusercontent.com/35606355/154753397-24c662a3-81b1-4e6d-8650-0438e2fd29ae.png">

In this project, we have implemented an online version of the famous Connect Four Game. Users can also chat with each other while playing the game!

## Network Fundamentals

The project is implemented using python's socket library and designed as client-server model. The packages between users (i.e., chat messages and game actions) are sent/received with both TCP and UDP.

## Required packages
 | package | version |
 | ------- | ------- |
 | Numpy   | 1.20.0  |
 | Pygame  | 2.0.1  |
 | PySimpleGUI  | 4.34.0  |

##  Execution
To run the program, execute the following from terminal, inside the project folder:
```
python3 main.py
```
You'll be directed to the login page. After entering your username, the home page (waiting room)
will be shown. At the waiting room you can:
- See the list of other online players, and refresh the list by pressing update button
- Select a user from that list and either chat or play with her

Note that you will be able to chat with your opponent when you're playing the game.

## Notes
- You need to connect to the same Wi-Fi with your opponent
- The default port is 12345 for UDP and TCP packets(except for the message packets during the game)
- The game chat port is 1234 for TCP packets(just for the message packets during the game)
- Selected development platform is MacOS using Python 3.8.5
- Required packages can be found in requirements.txt file detaily

## Team
- Me, [Ahmet Senturk](https://github.com/ahmetsenturk/), and my friend [Sertay Akpınar](https://github.com/sertayy)
implented this program together. 

## License
- [BSD 3](https://github.com/ahmetsenturk/CMPE487-ConnectFourGame/blob/sertay/LICENSE)

## Extras
- [PySimpleGui some infos](https://pysimplegui.readthedocs.io/en/latest/cookbook/)
