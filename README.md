# TOWAN Project (The One Without A Name)

### Presentation

Little raspberry pi project that allow a user to transform a complicate bitcoin address in a readable human URL.

### Explication

TOWAN offer a endpoint that send a new bitcoin address everytime it is called (HD). It also offer a little interface for the owner.

### TODO ##

* Create a proper module call `ìnterface` with the views for the GUI.
* Slackbot !
* ~~Check if on the last 20 addresses there is a transaction.~~ (Use Blocktrail will offer other solution later)
* Add accounts, authorization, ...
* Docs
* Tests
* Blockstore integration and onename assocation.

### Notes ##

#### Generate Public Testnet Master Key

You can use [Copay](https://copay.io/). It allow Tesnet wallet and you can get the Public Master key.

Once you have it, you can change it in address/models.py (Need to create a script to ask it automatically the first time).

#### The .env file

The `.env` file contain all the environement variable needed and that you don't want to put in the `settings.py`.

Take the `_.env` rename it in `.env` and replace the dummy key with your own.

#### Start docker

```
$ docker build -t towan .
$ docker run --name towan -p 80:8000 -d towan
```
