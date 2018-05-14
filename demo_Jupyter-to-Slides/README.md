# Building awesome slides from a Jupyter notebook


## The "manual" way

* We assume that you made a beautiful notebook with Jupyter like this one: `xarray_intro_acinn/ACINN_workshop_xarray-slides.ipynb` (stolen from [here](http://fabienmaussion.info/2017/02/18/html-presentations-w-rise/) --- courtesy of Fabien Maussion)

* We assume that you have [Jupyter](http://jupyter.org/install) installed, as well as the notebook extension [RISE](http://rise.readthedocs.io).

### #1 Running on your machine

Then you can run this command to convert your Jupyter notebook into an awesome reveal-based web presentation served in your web browser:

```shell
cd xarray_intro_acinn
jupyter nbconvert  ACINN_workshop_xarray-slides.ipynb --to slides --post serve
```

### #2 Running on slides.com

If you want to have it on internet for others to see it, hosted by the person who created reveal.js:

* simply convert your presentation into html

```shell
cd xarray_intro_acinn
jupyter nbconvert  ACINN_workshop_xarray-slides.ipynb --to slides
```

* copy the content of the html file to a new deck on [slides.com](https://slides.com).


## The "automated" way

You can use thrid-party tools to tell it to convert your notebook into slides and to host the slides on internet every time you do modifications (`git push`) to your code.

As an example you could use:

* [Travis CI](https://travis-ci.org/), a tool usually used to automate the testing of your code, here used also to run extra commands like converting your notebook to slides every time Github receives a `git push` from you.

* Github and more specifically [Github Pages](https://pages.github.com/) to host your newly created slides, as Gitub Pages could host almost any kind of "static" website.

To do so, you can just follow the steps on this [blog post](https://jellis18.github.io/post/2017-11-20-automating-jupyter-slides/) or follow those steps:

* Visit the project associated to your Github repository on [https://travis-ci.org/DataForGood-Norway/GirlsCanDoIt](https://travis-ci.org/DataForGood-Norway/GirlsCanDoIt).

* ...