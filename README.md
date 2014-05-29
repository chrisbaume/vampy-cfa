# Continuous Frequency Activation Vampy Plugin
This is a [Vampy plugin](http://www.vamp-plugins.org/vampy.html) that wraps
the Continuous Frequency Activation (CFA) output of the
[CBA-YAAFE-extension](https://github.com/mcrg-fhstp/cba-yaafe-extension)
[SP2007], which can be used as a speech/music discriminator.

[SP2007] Seyerlehner, Pohle, et al., Automatic Music Detection in Television
Productions., Proc. of the 10th Int. Conference on Digital Audio Effects
(DAFx-07), Bordeaux, France, September 10-15, 2007, pp. 221-228.

## Installation
Firstly, install [Yaafe](http://yaafe.sourceforge.net/) and then
[CBA-YAAFE-extension](https://github.com/mcrg-fhstp/cba-yaafe-extension) as per
the instructions in their respective README files.

Download [Vampy](http://www.vamp-plugins.org/vampy.html) and place it in your
[Vamp system plugin folder](http://www.vamp-plugins.org/download.html#install).

Finally, copy PyCFA.py into the Vamp system plugin folder. You should then be
able to extract CFA using your favourite Vamp host, such as [Sonic
Visualiser](http://www.sonicvisualiser.org/) or [Sonic
Annotator](http://www.vamp-plugins.org/sonic-annotator/).

## Usage
Parameters should be set through the Vamp host. Please see the
CBA-YAAFE-extension [features
page](https://github.com/mcrg-fhstp/cba-yaafe-extension/blob/master/FEATURES.md)
for an explanation of what the parameters do.
