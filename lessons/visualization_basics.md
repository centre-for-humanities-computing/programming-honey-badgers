# Basic viusalization in Python #

This is an introduction to Object-Oriented Programming and classes in Python

Learning goals:

* How to create a visualization in Python
* How to add and modify axis attributes figure objects
* How to organize several plots into one figure

## Set up data and environment ##

First we set up the data and environment for working with `matplotlib`.

```sh
$ mkdir infovis
$ cd infovis
$ git clone https://github.com/CHCAA-EDUX/Programming-for-the-Humanities-E21.git
$ mv Programming-for-the-Humanities-E21/dat/series/ data
$ rm -rf Programming-for-the-Humanities-E21
$ mkdir figures
```

If you want to use a virtual environment (not necessary in [UCloud](https://cloud.sdu.dk/)).

```sh
$ sudo pip3 install virtualenv
$ virtualenv -p /usr/bin/python3 ivis
$ source ivis/bin/activate
$ pip install matplotlib
$ pip install numpy
```

Check that we have the data `dat` and environment `ivis` subdirectories

```sh
$ ls -l
data  figures ivis
```

## Ten Rules of Visualization ##

1. Know you Audience
2. Identify your Message
3. Adapt the Figure to the Support Medium
4. Captions are not optional
5. Do not Trust the Defaults
6. Use Color Effectively
7. Do not Mislead the Reader
8. Avoid 'chartjunk'
9. Message Trumps Beauty
10. Get the Right Tool

### Data-Ink Ratio ###


<img src="https://render.githubusercontent.com/render/math?math=\text{Data-Ink Ratio}=\Huge\frac{\text{Data-Ink}}{\text{Total ink used to print the graphic}}">


The Data-Ink ratio is a concept introduced by _Edward Tufte_, the expert whose work has contributed significantly to designing effective data presentations. In his 1983 book, 'The Visual Display of Quantitative Data', he stated the goal:

"Above all else show the data"
(Tufte, 1983)

"A large share of ink on a graphic should present data-information, the ink changing as the data change. Data-ink is the non-erasable core of a graphic, the non-redundant ink arranged in response to variation in the numbers represented."
(Tufte, 1983)

Tufte refers to data-ink as the non-erasable ink used for the presentation of data. If data-ink would be removed from the image, the graphic would lose the content. Non-Data-Ink is accordingly the ink that does not transport the information but it is used for scales, labels and edges. The data-ink ratio is the proportion of Ink that is used to present actual data compared to the total amount of ink (or pixels) used in the entire display. (Ratio of Data-Ink to non-Data-Ink).

### Read series data ###

Start by maling a `series_visualization.py` file and read one of the tabular files from `data/` as a `numpy` array.

```py
import numpy

data = np.loadtxt(fname='data/series-01.csv', delimiter=',')
```

And run the script in interactive mode, inspect the data and check the dimensions

```sh
$ python -i series_visualization.py
>>> data
array([[0., 0., 1., ..., 3., 0., 0.],
       [0., 1., 2., ..., 1., 0., 1.],
       [0., 1., 1., ..., 2., 1., 1.],
       ...,
       [0., 1., 1., ..., 1., 1., 1.],
       [0., 0., 0., ..., 0., 2., 0.],
       [0., 0., 1., ..., 1., 1., 0.]])
>>> data.shape
(60, 40)
```

We see that the array has 60 objects measured on 40 variables. In this case each object is a person and each variable is a persons' inflammation rate (over 40 days). In other words, we have a inflammation rate time series and each variable (columns) represent the rate of inflammation at a given day. 

#### Visual inspection of a numpy array ####

Add simple array visualization to `series_visualization.py` and save the files to your `figures` subdirectory

```py
import matplotlib.pyplot as plt
image = plt.imshow(data)
plt.savefig('figures/my_array.png')
```

And execute. Now you can open you `my_array.png` file and you can inpect the matplotlib object

```sh
$ python -i series_visualization.py 
>>> image
<matplotlib.image.AxesImage object at 0x7f836fc249b0>
>>> dir(image)
['_A', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_checker', '_agg_filter', '_alpha', '_animated', '_axes', '_check_unsampled_image', '_check_update', '_clipon', '_clippath', '_contains', '_default_contains', '_extent', '_filternorm', '_filterrad', '_get_clipping_extent_bbox', '_get_scalar_alpha', '_gid', '_imcache', '_in_layout', '_interpolation', '_label', '_make_image', '_mouseover', '_oid', '_path_effects', '_picker', '_propobservers', '_rasterized', '_remove_method', '_resample', '_rgbacache', '_scale_norm', '_set_gc_clip', '_sketch', '_snap', '_stale', '_sticky_edges', '_transform', '_transformSet', '_update_dict', '_url', '_visible', 'add_callback', 'add_checker', 'autoscale', 'autoscale_None', 'axes', 'callbacksSM', 'can_composite', 'changed', 'check_update', 'clipbox', 'cmap', 'colorbar', 'contains', 'convert_xunits', 'convert_yunits', 'draw', 'eventson', 'figure', 'findobj', 'format_cursor_data', 'get_agg_filter', 'get_alpha', 'get_animated', 'get_array', 'get_children', 'get_clim', 'get_clip_box', 'get_clip_on', 'get_clip_path', 'get_cmap', 'get_contains', 'get_cursor_data', 'get_extent', 'get_figure', 'get_filternorm', 'get_filterrad', 'get_gid', 'get_in_layout', 'get_interpolation', 'get_label', 'get_path_effects', 'get_picker', 'get_rasterized', 'get_resample', 'get_size', 'get_sketch_params', 'get_snap', 'get_tightbbox', 'get_transform', 'get_transformed_clip_path_and_affine', 'get_url', 'get_visible', 'get_window_extent', 'get_zorder', 'have_units', 'is_transform_set', 'make_image', 'mouseover', 'norm', 'origin', 'pchanged', 'pick', 'pickable', 'properties', 'remove', 'remove_callback', 'set', 'set_agg_filter', 'set_alpha', 'set_animated', 'set_array', 'set_clim', 'set_clip_box', 'set_clip_on', 'set_clip_path', 'set_cmap', 'set_contains', 'set_data', 'set_extent', 'set_figure', 'set_filternorm', 'set_filterrad', 'set_gid', 'set_in_layout', 'set_interpolation', 'set_label', 'set_norm', 'set_path_effects', 'set_picker', 'set_rasterized', 'set_resample', 'set_sketch_params', 'set_snap', 'set_transform', 'set_url', 'set_visible', 'set_zorder', 'stale', 'stale_callback', 'sticky_edges', 'to_rgba', 'update', 'update_dict', 'update_from', 'write_png', 'zorder']
>>> 
```








---

This material has been adapted from [Software Carpentries](https://software-carpentry.org/) [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/) lesson by [CHCAA](https://chcaa.io/#/). 