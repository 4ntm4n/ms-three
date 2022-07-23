# Battle Ships
- An entertaining command line application. 

## Project outline
This is a game of Battle Ships that is written in Python and executed in the command line.

- **Game Features:**

  - User can choose name for himself and the opponent
  - user can read the rules before starting a new game
  - user can choose coordinates manually while computer makes random guesses.
  - error handling if user does something not allowed or that will break the game
  - cheat code that reveals position of the opponents ships
  - if the user wins, user can choose to append her name to a list of winners
  - make notes prioritized and have them showed up first in the list of notes


## Approach
  ![image of flow chart](assets/img/readme/responsive.png)
  > This game is built fom the functionality and control flow outlined in this flow chart.
  > you can for example see that if the user wants to see the rules before playing, an external txt-file is printed out to the terminal.

<br>
<br>

**In this game, I have created 3 main classes:**

- a board
- a player
- an articial player

The player has access to everything the board contains, I saw this as logical since a player of a physical game, has access to the board.
So a player in this game is a subclass of the board, which inherits the attributes and methods that the board has. 

An artificial player is exactly like a player, but has another method for guessing since he can not use a keyboard like a human player. The artificial player class is there for a subclass of a player that inherits all methods and attributes of a player but has another method of guessing.


**Aside from the classes, this game has 2 main functions:**

- play function
- hit finder

The play function handles the flow of the game play and also evaluate if the game should end becuse somebody won.
the hit finder is a global function that checks position on the opponents board and returns information to the play function which is then presented to the user during the game play.

Aside from these two main function there are several calls to methods and creations of classes, that are all wrapped inside a third main function called main(). 


these five items is really all thats needed for the game to work, but I have also added some smaller functions to bring more functionality to the game. 

- if a player wins, he/she can choose to append its username to a list of previous winners. 
- if a player wants to read the rules, there is a function that prints out a text file containing the rules.

<br>
<br>


Here follows some information on the three classes that makes up the majority of this game.

### **The BoardMaker class**

> This is the class that creates a board for the Player class.
> it stores information such as board size, ship location and previous guesses. it has a method that prints the board in a human friendly way to the console.  It also has a method to reveal the ships, this is standard for a normal player, and with a cheat code you can also reveal the position of the opponents ships by calling the reveal ships method on the opponent if a the cheat code is entered. 


``` python
const handleSubmit = (event) => {
 class BoardMaker:
    def __init__(self, name, type):
        """
        Initializing a playing board
        """
        self.name = name
        self.board = [["."] * 5 for times in range(5)]
        self.type = type
        self.ship_locations = []
        self.guesses = []

    def place_ships(self):
        """
        method that creates a coordinate in tuple format and
        append it until the self.ship_locations list contains
        5 unique coordinates
        """
        while len(self.ship_locations) < 4:
            random_coordinate = (randint(0, 4), randint(0, 4))
            if random_coordinate not in self.ship_locations:
                self.ship_locations.append(random_coordinate)

    def print_board(self):
        """
        Method that prints the board to the console.
        """
        print(f"\n{self.name}'s board: \n")
        print("   A B C D E")
        row_count = 1
        for row in self.board:
            print(
                f"{row_count}  " + " ".join(row),
            )
            row_count += 1
        print("\n")

    def reveal_ships(self):
        """
        method that update ship_location list so that
        remaining ships can be printed
        """
        for ship in self.ship_locations:
            self.board[ship[0]][ship[1]] = "@"

```
<br>
<br>

### **The Player class**

> The player class inherits all the methods from the board, and adds a couple of new methods for itself.
> A player can update his board with correct or incorrect guesses from his opponent, he can make guesses based on input from a keyboard, and he can answer yes or no question prompted by the game, and return true or false, so that the game understands what the player wants. 

``` python
class Player(BoardMaker):
    """
    Subclass of the BoardMaker that represents a human player.
    Player has access to the board made in BoardMaker, a guess method and
    that collects user input and stores old guesses.
    """

    def __init__(self, name, type):
        super().__init__(name, type)

    def guess(self):
        """
        Method that collects a human guess, appends it to
        self.guesses and returns the current guess as a tuple.
        """
        letters = "abcde"
        numbers = "12345"
        false_input = "''"

        col = input("select a column [A-E]: ").lower()
        while col not in letters or col in false_input:
            print("\n...a column on the board would be preferable. [A-E]")
            col = input("select a column [A-E]: ").lower()

        row = input("select a row [1-5]: ")
        while row not in numbers or row in false_input:
            print("\n the ships are hiding within row 1-5... try again.")
            row = input("select a row [1-5]: ")

        guess = (int(row) - 1, letters.index(col))
        return guess

    def update_guesses(self, guess):
        self.guesses.append(guess)

    def miss(self, guess):
        self.board[guess[0]][guess[1]] = "0"

    def hit(self, guess):
        self.board[guess[0]][guess[1]] = "x"

    def answer(self, question):
        """
        answer is a Player method that
        returns yes or no to a question asked to it.
        """
        if self.type == "human":
            check = input(f"{question} [Y/N]").lower()
            try:
                if check == "y":
                    return True
                elif check == "n":
                    return False
                else:
                    print("Invalid input")
                    return self.answer(question)
            except Exception:
                print(f"enter 'y' for yes or 'n' for no. you entered {self.answer}")
        else:
            print("I am not real, you cant ask me questions, I don't care...")

```
<br>
<br>


### **The ArtificialPlayer class**

> The ArtificialPlayer class origins from a player, and has all those methods, but he can't guess based on keyboard input so instead his guess method is random.

``` python
class ArtificialPlayer(Player):
    """
    Subclass of the Player that represents a artificial player.
    ArtificialPlayer is a player that but with a random guess function.
    """

    def __init__(self, name, type):
        super().__init__(name, type)

    def guess(self):
        guess = (randint(0, 4), randint(0, 4))
        return guess
```
<br>
<br>

## Testing

Here follows some pictures how the game looks and handles. 


### **playboard:**

> ![](assets/img/readme/large-screen-landing.png)
>
> > This is what the viewer sees when visiting the website device with a large screen
> > you can for example see that the "add" button is not yet visible. it will appear if the user scrolls down more than 200px




### **Validator Tests**

To extend the validation of the HTML and CSS, external validators from w3c has been checking the code as well.

- HTML

  - No errors were returned when passing the index page through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2F4ntm4n.github.io%2Fms-two%2Findex.html)

- CSS

  - No errors were found when passing the single CSS file through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2F4ntm4n.github.io%2Fms-two%2Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

- JavaScript:
  - _109 warnings_ for using ES 6 syntax, but *No errors* were found when testing the javaScript code through [JSHint](https://jshint.com/)

### Unfixed Bugs

> No bugs has been found in the testing of the application. tests has been made extensively throughout the coding of the app. if you find any errors, please let me know. anton.askling[a]gmail(.)com
---

## **Testing User stories**

> In this section we are testing the user stories stated in the outlined before this website was created in order to check if we have met all user needs.
>
> > We are testing the user stories one by one. Click the list items to view its correlating solution.

- **Typical users wants to have the ability:**

  - <details>
      <summary>
        create new sticky notes.
      </summary>
      <img src="assets/img/readme/small-screen-landing.png">  
    </details>

  - <details>
      <summary>
        remove completed / irrelevant notes from the view.
      </summary>  
      <img src="assets/img/readme/remove-note.png">
    </details>

  - <details>
      <summary>
        sort notes by title name from A-Z or Z-A
      </summary>
      <img src="assets/img/readme/sorting-az.png">
      <img src="assets/img/readme/sorting-za.png">  
    </details>

  - <details>
      <summary>
        make notes prioritized and have them showed up first in the list of notes.
      </summary>
      <img src="assets/img/readme/make-important.png">    
    </details>

  - <details>
      <summary>
        have a view for the prioritized notes only.
      </summary>
      <img src="assets/img/readme/starrred-notes.png">  
    </details>

  - <details>
      <summary>
        toggle between priority status on a note AFTER it has been created.
      </summary>
      <img src="assets/img/readme/star-existing.png">  
    </details>


  - <details>
      <summary>
        restore notes that has been removed.
      </summary>
      <img src="assets/img/readme/restore-note.png">  
    </details>

  - <details>
      <summary>
        delete notes permanently.
      </summary>  
      <img src="assets/img/readme/permanent-delete-note.png">
    </details>

  - <details>
      <summary>
        click a button that takes them to the note generator, instead of having to scroll up and down if many notes have been created.
      </summary>
      <img src="assets/img/readme/add-button.png"> 
    </details>

  - <details>
      <summary>
        view all the notes that have been removed
      </summary>
      <img src="assets/img/readme/removed-notes.png">  
    </details>

---

## Deployment

- The site was deployed to GitHub pages using the following steps:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

> You can visit the live website form any device by following this link:
>
> https://4ntm4n.github.io/ms-two/index.html

## Credits

In this section I want to give credits to resources I have used when creating this website.

### **Technical**

> #### **Codecademy**
>
> On Codecademy.com I took a course in JavaScript called "Learn JavaScript", as well as one called "building interactive JavaScript websites". Prior writing this web application in javascript, codecademy let me try my abilities by working with small isolated projects on specific topics. This was a great way for me to get the ability to both understand and write this application fluently with very few moments where I had too look at external resources. 
>
> > Here is a link to the tracks on codecademy:
> > https://www.codecademy.com/learn/build-interactive-websites
> > https://www.codecademy.com/learn/introduction-to-javascript


> #### **tips and tricks**
>
> Here I will are some things I picked up after googling and reading forums
>
> **Concat arrays (used when a note was made prio):**
>
> > https://www.w3schools.com/jsref/jsref_concat_array.asp#:~:text=The%20concat()%20method%20concatenates,not%20change%20the%20existing%20arrays
>
> **prevent button malfunction when using icons inside buttons:**
>
> > https://stackoverflow.com/questions/21653978/font-awesome-icon-preventing-click-in-parent-button
>
> **scroll to the top of the page ('add' button)**
>
> > https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
>
> **How to sort objects in an array**
> 
> > https://www.youtube.com/watch?v=qy8TcQSGuoI&t=2s
>
> **How to target a list item by clicking a button inside it**
> > https://stackoverflow.com/questions/65321786/how-to-target-an-item-inside-a-list-element-by-class?fbclid=IwAR0GF2tT65JqtKLRhaWEcw6XcTXMsR6D4S9FZmv7d6aCXyb7cwS7awWkPsk
> 
> **inspiration for my filter functions**
> > https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

### **Content**
>
> - Fonts for text and heading has been imported through [Google Fonts](https://fonts.google.com/)
>   >
> - All icons comes from [Font Awesome](https://fontawesome.com/)
>
> **image in header**
>
> > bought from Adobe stock photos and available on https://adobestock.com/
>
> **image in footer**
>
> > created myself, using imagination and adobe illustrator
> 
> **color scheme**
>
> >https://www.schemecolor.com/city-by-night.php
> 
> 
>  **favicon**
>  favicons where generated using favicon.io
> >http://favicon.io/

---

### Some final words from the developer

Thank you for taking the time to read through this website documentation.

This project is the second of five milestone projects in a full stack developer course that I have enrolled through [Code Institute](https://codeinstitute.net).

- There are many ways to approach a project like this, but in this case I wanted to:

  - **A**: limit myself to **pure** html and CSS and JavaScript and not use any frameworks.

  - **B**: work from my own idea to create something unique and that way challange myself to take something from my mind into reality.

The notes in this application has been viewed by me as placeholders for potentially different content on a more advanced website that I could build in the future. The ability for a user to create, sort and remove objects to give a more customized experience in a website is something that appeals to me. I think I have learned some very valuable lessons by building this application regardless of if _this_ application will be viewed as valuable or not. 


> Notes - a study in JavaScript
>
> By Anton Askling 2022