# Roku Deep Links

## What exactly is this?
Roku has the ability for you to send HTTP requests to your device on your local area network to control it.
This includes simple things such as virtualizing a keypress on your Roku remote (which is how the Roku app works).
All you need to know is your Roku's IP address and you are ready to make these requests.

### What kind of requests are there?
To list some of them:
* Home button
* Arrow key buttons
* Play/Pause buttons
* Back button

If you're in a web browser, you can even see what apps you have on it by typing this in:

`http://<YOUR_ROKUS_IP_ADDRESS>:8060/query/apps`

or you can just view the basic information on your Roku by typing this in:

`http://<YOUR_ROKUS_IP_ADDRESS>:8060`

Note that the link is HTTP instead of HTTPS. This is because of Roku's [External Control Protocol](https://developer.roku.com/docs/developer-program/debugging/external-control-api.md) (or ECP for short).
I won't go into detail about that since Roku has documentation covering that.

### How is this useful?
As I mentioned before, Roku's iOS and Android apps use this to let you control your Roku device from your phone and
there's even a [web app](http://devtools.web.roku.com/RokuRemote/) that works the same way.

With the knowledge of being able to send these sorts of requests to your own Roku device, I created this repo to help
others to apply this to their own implementations of whatever they choose.

## Goals and Contributing
I invite anyone and everyone to contribute to this repo because my goal is to have a bunch of scripts that
contain the information on how to send a deep-link through to a Roku device for more channels than just Netflix and Vudu (only 2 channels as of May 23rd, 2021)

If you want to contribute, I ask that you contribute inside a specific streaming service folder and prepend the folder name with either
`[TV SHOW]` or `[MOVIE]` that way they can be distinguished from one another. Each TV Show or Movie will have its own folder for 
the possibility that other languages may be included for each of them to implement in whichever language a person chooses to use.

### Contributing Movies
Movies are pretty simple to contribute as they consist of merely the ID of the movie itself on whichever platform it is.
There's no extra stuff that needs to be dealt with like with a TV Show that has seasons and episodes

### Contributing TV Shows
TV Shows, as mentioned just up above, are a bit more in-depth as they consist of however many episodes there are including their seasons.
It gets especially difficult with long-running shows like *Supernatural*, *The Simpsons*, and *Grey's Anatomy*, to name a few.

So to best implement these, these should consist of comments that describe where the season barriers are in addition to 
the episode numbers.
