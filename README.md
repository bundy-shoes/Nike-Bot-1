# Nike-Bot
Bot used to buy items off of Nike.com.

Sacai.py and jordan.py will essentially just run until the cart button is found. I found it successful to just run them as soon as you see items available.


I have not tested how it will work to just have it wait but use caution. If cmd page gets stuck then its CRTL+C to kill the script but it should end gracefully when 
it gets to the paying page.


I have only accounted for a few sizes but 9, 9.5, 10, 10.5, 11.5, 12, and 12.5 is available.


These scripts will just take you all the way until you have to enter credit card info.

## Requirements
(windows) Python which can be downloaded here -> https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe


(apple) https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg


Firefox browser which can be downloaded here -> https://www.mozilla.org/en-US/firefox/new/

      
## Usage
Edit config.py to include all of your information. Read all of the steps before proceeding specifically the optional step.

Config.py is the only file you will have to edit.

### Step 1 Windows

Open 2 cmd pages and change directory into the project, type this into both cmd pages. If on apple or 

linux just open terminal and continue. CD means change directory so the following command will vary based on each system.

      cd nike-bot
            

### Step 2
Activate virtualenv to have all the dependencies, type this into both cmd pages

      env\Scripts\activate

### Step 3
At this point you should have something like this

      (env) C:\Users\damia\VS_Projects\Nike_Bot>
      
You should see this in both cmd pages now in one you will run this

      python sacai.py

And in another you will write

      python jordan.py

### Step 4 (Optional)
I strongly suggest you run test.py to make sure that script is working. To do this

you would just skip to this step from step 2.

      python test.py
