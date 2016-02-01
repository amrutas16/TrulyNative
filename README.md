We have used data science distribution of python named Anaconda. Detailed installation steps are as follows:

Download this version from https://www.continuum.io/downloads

Go through the GUI Installer on Windows or Mac.

After the installer finishes follow these steps:

Note: While running the commands mentioned below you may run into permission issues. To avoid those run the cmd as administrator or change user to root user in Terminal(by running 'su root' and then entering your password)

1. Open Command Prompt/Terminal and navigate to folder where Anaconda is installed.
2. Run command 'conda update conda'
3. Run command 'conda update anaconda'
4. Now that Ananconda is updated run this command to install some extra python packages that we might use later.
  'conda create -n alda cython distribute ipython-notebook ipython-qtconsole jinja2 lxml matplotlib nose numba numexpr pandas pip pygments pytables pywin32 scipy statsmodels xlrd xlwt csvkit'
5. After all the new packages get installed there will be a message on the cmd/terminal that will ask you to activate the environment 'alda' that we created above. To do this run 'cd Scripts' and then 'activate alda'

After this your job on the command line is done. Now comes the part of setting up the anaconda interpreter in the IDE. The recommended IDE is PyCharm/ LiClipse. You can use any one you want. 

The following packages need to be installed:
1. TextBlob: Command - 
   "import textblob
   download textblob()"
2. BeautifulSoup
   Using easy_install or pip - 
   "$ easy_install beautifulsoup4" or "$ pip install beautifulsoup4"
3. nltk: Command - 
   "import nltk
   nltk.download()"
4. pandas
5. numpy
6. sklearn

Except for TextBlob, nltk and beautifulSoup other packages should be easily present with Anaconda.

In order to run the code, you need to provide 3 parameters to trulynative.py:
1. Input directory: Give it same as the 2nd parameter - output directory
2. Output directory - (Eg: "C:/Users/Isha/Desktop/AldaSampling/output) 
3. Training file name: "train_v2.csv"

Eg. of the parameters: "C:/Users/Isha/Desktop/AldaSampling/output" "C:/Users/Isha/Desktop/AldaSampling/output" "train_v2.csv"

This Output directory has a few things:
   - Folder where the training samples are kept. Keep the training sample folders(sponsored and unsponsored) inside a folder called "train"
	 Eg: "C:/Users/Isha/Desktop/AldaSampling/output/train"  -- This directory had two folders - sponsored and unsponsored
   - Folder where "testDataCSV.CSV" and "test" folder is kept
     Eg: "C:/Users/Isha/Desktop/AldaSampling/output/test" and "C:/Users/Isha/Desktop/AldaSampling/output/testDataCSV.CSV"
   - Folder that contains the file "train_v2.csv" 
     Eg: "C:/Users/Isha/Desktop/AldaSampling/output/train_v2.csv"

