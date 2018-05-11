# Building awesome slides from a Jupyter notebook

* We assume that you made a beautiful notebook with Jupyter like this one: `xarray_intro_acinn/ACINN_workshop_xarray-slides.ipynb` (stolen from [here](http://fabienmaussion.info/2017/02/18/html-presentations-w-rise/) --- courtesy of Fabien Maussion)

* We assume that you have [Jupyter](http://jupyter.org/install) installed, as well as the notebook extension [RISE](http://rise.readthedocs.io).


Then you can run this command to convert your Jupyter notebook into an awesome reveal-based web presentation served in your web browser:

```shell
cd xarray_intro_acinn
jupyter nbconvert  ACINN_workshop_xarray-slides.ipynb --to slides --post serve
```


If you want to have it on internet for other to see it:

* Convert your presentation into

