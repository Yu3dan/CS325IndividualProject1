# URL Source Code to a Text File
### CS325 Individual Project 1

This project is focused on using Python to write a text file with the contents of a page's source code provided by the user.

If you are interested in using my code above, the first thing you must do is clone this repository by using this command in your terminal:

```
git clone https://github.com/Yu3dan/CS325IndividualProject1
```

Once you have done this, make sure you are in the correct directory the repository (and its content) was downloaded to using cd (file location) in your terminal.

The requirement.yaml file included is all the neccesary libraries in the environment I coded this project under while using miniconda.
In order to use the packages needed to run this program, you must create a new environment using the .yaml file given. Before you do this, you must remember to deactivate your current environment using

```
conda deactivate
```

The command to create the new environment is:

```
conda create --name my_yaml_env --file requirement.yaml
```

My_yaml_env would be the name of the new environment in that instance (You may use any name you would like to). Next, activate the new environment with the commmand:

```
conda activate my_yaml_env
```

Once everything is set, the syntax to use this program is:

```
python IDProject1.py (URL)
```

The output of this project should be a text file where all the source code of the URL you provided is neatly written to a text file (output.txt).
The output.txt file included here is my output using the Reddit URL https://www.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/. 

My command would look like this:

```
python IDProject1.py https://www.reddit.com/r/OnePiece/comments/16e71cy/how_close_is_zoro/
```

If ran correctly, you should see your updated output.txt file in the same folder with all the new data of the Reddit post you provided.
