# File Extensions

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (`.`) at the end of their name. For instance, file names for GIFs end with `.gif`, and file names for JPEGs end with `.jpg` or `.jpeg`. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is `image/gif`, and the media type for a JPEG is `image/jpeg`. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

See [MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types) for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
```
.gif .jpg .jpeg .png .pdf .txt .zip 
```
If the file’s name ends with some other suffix or has no suffix at all, output `application/octet-stream` instead, which is a common default.

??? Hints
    - Recall that a `str` comes with quite a few methods, per [string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods){:target="_blank"}.

## Before You Begin

From the root of your repository execute cd `conditionals` So your current working directory is ...
```
/conditionals $:
```
Next execute
```
code extensions.py
```
to make a file called `extensions.py` where you’ll write your program.

!!! success
    Your program must have a function called `extension` that takes a string argument and returns a string representing the media type. Your `main` function must call this `extension` function with the user’s input and print the result.

## How to Test

Here’s how to test your code manually:

Run your program with `python extensions.py`. Type `happy.jpg` and press ++enter++. Your program should output:
```
image/jpeg
```
Run your program with `python extensions.py`. Type `document.pdf` and press ++enter++. Your program should output:
```
application/pdf
```

Be sure to test each of the other file formats, vary the casing of your input, and “accidentally” add spaces on either side of your input before pressing enter. Your program should behave as expected, case- and space-insensitively.

### Pytest 
You can execute the below to check your code using `pytest` from the root directory.

```
pytest .\tests\conditionals\test_extensions.py
```

A green output from running the test means it was successful. A red output means there is a bug in your code that you need to fix.

## How to Submit

From github desktop or the command line, commit your changes and push them to your repository.

### Codespaces
If you are using codespaces, you can commit your changes directly from the Codespace interface. Click on the Source Control icon in the left sidebar, then click on the "..." button and select "Commit to main". Enter a commit message and click "Commit".

#### Codespace terminal or your local terminal. 

!!! Note
    You will need to have installed `git-scm` for this to work locally

At the `/datatypes $` prompt in your terminal:
```
git add -A 
```
Add all changed files in the repository to be committed
```
git commit -m "your message here"
```
Commit all changes in the REPO with the comment “your message here“ note: If the file is not complete, adjust the comment to describes what is being committed
!!! Note
    Remember to replace "your message here" with a meaningful commit message that describes your changes.

```
git push 
```
Push all changes to the repo.