Here are step-by-step instructions on how to download the GitHub repo and run the `main.py` script on your Mac:

### 1. **Install Git (if you don’t have it already)**
   - Open **Terminal** (you can find it by searching in Spotlight).
   - Type the following command to check if you have Git installed:
     ```bash
     git --version
     ```
   - If it’s not installed, your Mac will prompt you to install the command line developer tools. Just follow the on-screen instructions.

### 2. **Clone the Repository**
   - In Terminal, navigate to the directory where you want to store the project (use the `cd` command).
   - Run the following command to download the repository:
     ```bash
     git clone https://github.com/andrewjosephallen/espnapiscraper
     ```
   - After it’s cloned, navigate into the project folder:
     ```bash
     cd espnapiscraper
     ```
     
### 3. **Install Required Packages**
   - Install the `espn_api` package used in the `main.py` script. You’ll also need to install `csv`, but it’s part of Python's standard library, so no additional installation is required.
   - Run the following command to install `espn_api`:
     ```bash
     pip install espn-api
     ```

### 4. **Run the Script**
   - Now, run the `main.py` script by typing:
     ```bash
     python main.py
     ```
   - The script will prompt you for input:
     1. **League ID**: Input the ID of your fantasy league.
     2. **Year**: Input the year of the league season.
     3. **ESPN S2**: Paste your `espn_s2` cookie value.
     4. **SWID**: Paste your `swid` cookie value.

   - After providing these values, the script will generate a CSV file with weekly scores and free agents, saving it in the current directory.

This process should set up the repository and run the `main.py` script smoothly on your Mac!
