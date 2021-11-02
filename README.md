Graduate CLI Exercise
=====================

A small python exercise to pair on with a graduate interviewee and a couple of Cloudsmith engineers.

Welcome! Today your mission if you choose to accept it, is to implement a Python CLI application to speak to the Cloudsmith API, and pull some things out, and present to a user.

### Sounds great, what's an API?

An API is an 'application program interface'. Basically, a fancy way of saying 'how to speak' to a web service. When using Cloudsmith, our users can interact using the user interface, the API directly, or the 'CLI'.

For reference, the [Cloudsmith API Docs are here](https://api.cloudsmith.io).

### That sounds...OK, i guess! What's a CLI?

A CLI is a 'command line interface'. In the Cloudsmith world, we provide a little Python application that speaks to our API, and allows users to do a bunch of different things. Such things include uploading packages, listing repository contents, that kind of thing. It's pretty sweet, really.

### So, what do I have to do? How Do I do it? Aghhhhhh!!11

Firstly:

![Don't panic gif](https://media1.giphy.com/media/JkADkL9786mQBORwCS/giphy.gif)

We're here with you throughout. You can bounce ideas around, Google stuff, hit up stack overflow, no worries. We're human, it's how we work day to day, so we don't expect you to work any differently.

The code is structured, with a little utility in `utils.py`, which will help make a call to a URL. Your job is to write some logic in each function in the `namespace.py`, `package.py`, `repository.py`, and `user.py` files. These should call through to endpoints in the Cloudsmith API, and get some data out.

You'll need to consider authentication, too. The utility does handle this, but you'll need a way to pass the API key / password to Cloudsmith, too.

### How to run the files

#### Natively
You can run the python script by executing `python -m cli_exercise` in your terminal.

#### Docker
Alternatively, if you have Docker set up, we have a docker container set up which you can use by running `docker run --rm -it $(docker build -q .)`.

## Good Luck!

Remember, you got this!