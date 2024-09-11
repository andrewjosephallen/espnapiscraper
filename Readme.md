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


---

## How to Obtain ESPN Cookies (`espn_s2` and `SWID`)

To access data from private ESPN Fantasy Football leagues, you'll need to provide authentication cookies (`espn_s2` and `SWID`). Follow these steps to retrieve them from your browser.

### Step 1: Log In to ESPN Fantasy Football
1. Visit [ESPN Fantasy Football](https://fantasy.espn.com/).
2. Log in with your ESPN account credentials.

### Step 2: Access Browser Developer Tools

#### For Google Chrome or Microsoft Edge:
1. Right-click anywhere on the page and select **Inspect**.
2. In the Developer Tools window, click on the **Application** tab.
3. In the left sidebar under **Storage**, expand **Cookies** and select `https://fantasy.espn.com`.

#### For Mozilla Firefox:
1. Right-click anywhere on the page and select **Inspect**.
2. Click on the **Storage** tab.
3. In the left sidebar, expand **Cookies** and select `https://fantasy.espn.com`.

### Step 3: Locate the Cookies
1. In the list of cookies, find `espn_s2` and `SWID`.

   - **espn_s2**: A long alphanumeric string.
   - **SWID**: A string formatted as `{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}` (including the curly braces).

### Step 4: Copy the Values
1. Double-click on the value for `espn_s2` to highlight it, then right-click and select **Copy**.
2. Repeat the process for `SWID`.

Now you have the `espn_s2` and `SWID` cookies, which you can use in your code to authenticate and access private ESPN Fantasy Football league data.

---
