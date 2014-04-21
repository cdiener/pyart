pyart
=====

This repository contains some small python programs which convert images to some
artistic representation. 

## asciinator

Converts an image into ascii art. 

### Required python modules

* PIL or pillow
* numpy

### Usage

Convert the script into an executable by
```bash
chmod u+x asciinator.py
```

Basic usage:

```bash
./asciinator.py image_file scale gamma_factor
```
Here the *image_file* denotes the path to your image, *scale* is a scale factor for the image
size (0.5 = half size, 2 = double size, etc.) and *gamma_factor* is a gamma correction factor
for the image intensities. A value of 1 for *gamma_factor* will use the original intensities,
a value >1 will diminish lower intensities and favor high intensities and a value <1 will increase
lower intensities.
 
And an example:

Using an image of Franz Kafka and calling

```bash
./asciinator kafka.jpg 1 2
```

leads to

![Franz Kafka](examples/kafka.jpg) -> ![Franz Kafka](examples/kafka_ascii.jpg) 

## polygonator

Converts an image into polygon art.

### Required python modules

* PIL or pillow
* matplotlib
* numpy

### Usage

Convert the script into an executable by
```bash
chmod u+x polygonator.py
```

Basic usage:

```bash
./polygonator.py image_file scale space plot_object
```

Here the *image_file* denotes the path to your image and *scale* is a scale factor for the image
size (0.5 = half size, 2 = double size, etc.). *space* is the spacing between the individual polygons
relative to the polygon size (0.1 = 10% of the polygon size is used as spacing and so on) and the 
*plot_object* is the polygon shape used to convert the image. It can be any matplotlib marker symbol
as listed [here](http://matplotlib.org/api/markers_api.html).
 
And an example:

Using an image of Franz Kafka and calling

```bash
./asciinator kafka.jpg 0.15 0.25 o
```

leads to

![Franz Kafka](examples/kafka.jpg) -> ![Franz Kafka](examples/kafka_poly.png) 




