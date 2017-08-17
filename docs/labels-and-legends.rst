
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _labels-and-legends:

Labels and Legends
==================

Of course, most figures must be properly labelled before they can be of
value, so Toyplot provides several mechanisms to help:

Coordinate System Labels
------------------------

First, :ref:`cartesian-coordinates`, :ref:`numberline-coordinates`,
and :ref:`table-coordinates` provide labels that can be specified when
they are created. In all cases the ``label`` parameter provides a
top-level label for the coordinate system:

.. code:: python

    import numpy
    import toyplot
    
    canvas = toyplot.Canvas(width=600, height=600)
    canvas.cartesian(grid=(2,2,0), label="Cartesian Coordinates").plot(numpy.linspace(0, 1)**2)
    canvas.numberline(grid=(2,2,1), label="Numberline Coordinates").scatterplot(numpy.random.normal(size=100))
    canvas.table(grid=(2,2,2), label="Table Coordinates", data = numpy.random.random((4, 3)));



.. raw:: html

    <div class="toyplot" id="t73c923f3fb634112b1285e16463c1a16" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600.0px" id="t27599829bfa549c89c3215c1ec8fa539" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 600.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="tebee5411f7ef42dcb40397aa574e8a5e"><clipPath id="t13305132a6d0451a92f3e3ddb449ebb8"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t13305132a6d0451a92f3e3ddb449ebb8)"><g class="toyplot-mark-Plot" id="t0b816b8f60414aeb8582c9c06a91c48c" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.0 249.9167013744273 L 58.0 249.66680549770928 L 62.0 249.25031236984589 L 66.0 248.66722199083716 L 70.0 247.91753436068305 L 74.0 247.0012494793836 L 78.0 245.91836734693877 L 82.0 244.6688879633486 L 86.0 243.25281132861306 L 90.0 241.6701374427322 L 94.0 239.92086630570594 L 98.0 238.00499791753435 L 102.0 235.92253227821743 L 106.0 233.67346938775512 L 110.0 231.25780924614745 L 114.0 228.67555185339444 L 118.0 225.92669720949604 L 122.0 223.01124531445231 L 126.0 219.92919616826322 L 130.0 216.68054977092879 L 134.0 213.26530612244898 L 138.0 209.68346522282383 L 142.0 205.93502707205332 L 146.0 202.01999167013744 L 150.0 197.93835901707621 L 154.0 193.69012911286964 L 158.0 189.27530195751771 L 162.0 184.69387755102045 L 166.0 179.94585589337777 L 170.0 175.03123698458978 L 174.0 169.95002082465641 L 178.0 164.7022074135777 L 182.0 159.2877967513536 L 186.0 153.70678883798416 L 190.0 147.9591836734694 L 194.0 142.04498125780927 L 198.0 135.96418159100375 L 202.0 129.7167846730529 L 206.0 123.30279050395671 L 210.0 116.72219908371514 L 214.0 109.97501041232822 L 218.0 103.06122448979593 L 222.0 95.980841316118301 L 226.0 88.733860891295336 L 230.0 81.320283215326981 L 234.0 73.740108288213264 L 238.0 65.993336109954186 L 242.0 58.079966680549774 L 246.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t91b0342c12c348609caa5d7c987475bf" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te3b28f7464e5490fbb22b3907d128e07" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g><g transform="translate(150.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-74.683" y="-4.823">Cartesian Coordinates</text></g></g><g class="toyplot-coordinates-Numberline" id="t33f972af8f3b438d952dbce5abb56456"><clipPath id="tffcf0109a024452f8d9e753f152fa91f"><rect height="40.0" width="200.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tffcf0109a024452f8d9e753f152fa91f)" transform="translate(350.0,150.0)"><g class="toyplot-mark-Scatterplot" id="t093a36bd03ed4865bb6e514e9e98b394"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(64.035841359590506, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(25.577204105492669, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(96.201505242525371, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(82.615449064880764, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(84.568420307352056, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(110.74128222549797, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(52.09646156042578, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(144.59449947861543, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(98.540375164340745, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(27.970181580271191, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.64817477904595, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(183.7963698439105, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(155.01434408820464, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(124.78276862515689, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(57.834637817660997, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(114.10906636211318, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(106.08276328006636, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(130.84184286694074, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(66.727980836830923, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(19.865064984532605, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(144.92473847010891, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(85.688324025848047, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(109.20014269112572, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(17.871283467088681, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(29.045009233183084, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(58.349129044141691, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(100.94913431696423, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(10.721748343987542, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(121.15511857362995, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(47.507240338302594, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(64.086889754958037, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(64.102471791888007, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(57.929354901590436, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(122.86618642223866, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(48.020765834543404, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(40.676503743818863, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(74.615032563900272, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.650581719444006, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(52.199990220688662, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(80.461198213287545, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(57.619455518901965, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(2.324455917610087, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(54.167491311221418, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.32361462714142, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(62.952906093014668, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(104.39541268789512, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(65.990907379815667, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(115.40182742948019, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(59.613583212898433, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(49.829956529040146, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(82.198424085322259, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(126.54660048617146, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(87.722455058359543, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(67.897150463761989, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(106.51484300362841, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(94.64236381200854, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(118.94141123150111, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(114.11348484473376, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(41.529733065959114, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(78.729766897045067, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(60.356929877641996, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(120.23787523800419, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(195.59024711853257, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(74.526466733462087, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(74.077250966365327, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(95.841784301844982, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(108.84505865151341, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(98.228667509455676, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(48.127252545144827, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(66.428609807666646, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(82.072400578962373, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(42.172847939693064, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(52.580453675558594, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(75.048593519025573, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(113.59120097679383, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(67.246625711489145, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(43.829075496013026, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(74.343054612084075, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(78.796001199174768, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(70.557076214263958, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(78.031671517135081, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(71.661504757633338, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(52.974379064041003, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(47.637628441602004, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(0.0, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(132.99940636159505, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(31.454902822784049, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(58.930529683888643, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(122.00390203950332, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(125.32663949931435, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(81.695996090443472, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(99.416241176967617, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(43.245444704379629, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(57.231425204573426, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(157.01974010986601, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(147.26766836279631, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(86.910080473804925, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(101.37580627523026, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(190.16827771768695, 0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0" transform="translate(139.69002622100282, 0)"><circle r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="td4113dd5db104b748816ebd521871371" transform="translate(350.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="195.59024711853257" y1="0" y2="0"></line><g><g transform="translate(4.188434239755594,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.445" y="8.555">-2</text></g><g transform="translate(43.350747391804475,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-4.445" y="8.555">-1</text></g><g transform="translate(82.51306054385334,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(121.67537369590222,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">1</text></g><g transform="translate(160.83768684795112,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">2</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">3</text></g></g><g transform="translate(100.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-69.678" y="10.266">Numberline Coordinates</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Table" id="t82c4f95c9dfe4cc6b97bb6ce8b110f94"><g transform="translate(150.0,350.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-61.068" y="-10.423">Table Coordinates</text></g><g transform="translate(83.333333333333343,370.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">0</text></g><g transform="translate(150.0,370.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">1</text></g><g transform="translate(216.66666666666669,370.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-3.336" y="3.066">2</text></g><g transform="translate(81.333333333333343,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(83.333333333333343,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(85.333333333333343,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">324154</text></g><g transform="translate(148.0,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(150.0,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(152.0,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">449922</text></g><g transform="translate(214.66666666666669,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(216.66666666666669,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(218.66666666666669,410.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">010407</text></g><g transform="translate(81.333333333333343,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(83.333333333333343,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(85.333333333333343,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">385135</text></g><g transform="translate(148.0,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(150.0,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(152.0,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">628724</text></g><g transform="translate(214.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(216.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(218.66666666666669,450.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">445777</text></g><g transform="translate(81.333333333333343,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(83.333333333333343,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(85.333333333333343,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0352872</text></g><g transform="translate(148.0,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(150.0,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(152.0,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">00931193</text></g><g transform="translate(214.66666666666669,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(216.66666666666669,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(218.66666666666669,490.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">377721</text></g><g transform="translate(81.333333333333343,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(83.333333333333343,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(85.333333333333343,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0536664</text></g><g transform="translate(148.0,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(150.0,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(152.0,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">317433</text></g><g transform="translate(214.66666666666669,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.672" y="3.066">0</text></g><g transform="translate(216.66666666666669,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-1.668" y="3.066">.</text></g><g transform="translate(218.66666666666669,530.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">0163758</text></g><line style="stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:0.5" x1="50.0" x2="250.0" y1="390.0" y2="390.0"></line></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t73c923f3fb634112b1285e16463c1a16";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t27599829bfa549c89c3215c1ec8fa539";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0b816b8f60414aeb8582c9c06a91c48c","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t91b0342c12c348609caa5d7c987475bf",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te3b28f7464e5490fbb22b3907d128e07",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t093a36bd03ed4865bb6e514e9e98b394","data","scatterplot data",["x0"],[[-0.47181123118352286, -1.4538430408159364, 0.3495310566954055, 0.002614465612127935, 0.05248310424153705, 0.7208006731381695, -0.7766803473874028, 1.5852342197900564, 0.40925352285144273, -1.3927389516502195, 0.4630756657499383, 2.586244303466488, 1.8513023799912645, 1.0793465625278593, -0.6301574329988533, 0.8067962098047522, 0.6018465417173625, 1.234063527745397, -0.4030681141263635, -1.5997011033563822, 1.5936667909257636, 0.081079569270248, 0.6814480555236606, -1.6506118222841177, -1.365293492830184, -0.6170200265212745, 0.4707605932655784, -1.833173436950311, 0.9867154138660713, -0.8938649785481156, -0.4705077230079628, -0.47010983954103214, -0.6277388556395003, 1.03040710904162, -0.8807522317538434, -1.0682861514743212, -0.20167419501725403, -0.30290546879478003, -0.774036768601315, -0.05239379815485843, -0.6356520598847468, -2.0475962263747944, -0.7237971138880227, 0.9654831658305638, -0.4994637159172845, 0.5587604608308724, -0.42188910292121706, 0.83980654457093, -0.584732501424188, -0.8345549939279645, -0.00803416430764726, 1.1243855737365809, 0.1330206031058621, -0.3732136562859462, 0.6128795908093426, 0.30971876510620844, 0.9301889432887575, 0.8069090346678655, -1.0464991513339679, -0.09660546945017082, -0.5657513278183927, 0.9632938316917876, 2.8873980486202027, -0.20393570163700642, -0.21540631537099791, 0.34034567126416787, 0.6723810722166813, 0.4012941448219873, -0.8780331198824893, -0.41071247946305744, -0.011252143436474493, -1.030077371771636, -0.7643217281900714, -0.19060332304291525, 0.7935726450140638, -0.38982464526780664, -0.9877860099235857, -0.20861908488523095, -0.09491419289373881, -0.3052931087898182, -0.11443116266700427, -0.2770917985382659, -0.7542629406268092, -0.8905355505137404, -2.106950634491223, 1.2891563790352967, -1.3037574548478392, -0.6021741046910282, 1.0083888901640095, 1.0932341710571578, -0.020863539143809104, 0.4316185452960133, -1.0026888781317898, -0.6455603181845565, 1.9025096724174126, 1.6534929274359051, 0.11227681860568361, 0.48165555640550967, 2.748949398261, 1.4599997057160068]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td4113dd5db104b748816ebd521871371",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 3.0, "min": -2.106950634491223}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t82c4f95c9dfe4cc6b97bb6ce8b110f94","data","table data",["0", "1", "2"],[[0.32415371886704303, 0.3851352808278521, 0.035287196001215326, 0.053666415257604405], [0.44992190551548794, 0.6287240372617962, 0.009311933646016679, 0.31743333816495223], [0.010406989628544694, 0.4457772374601374, 0.3777214548101341, 0.01637583329593406]],"toyplot");
    })();</script></div></div>


Naturally, some coordinate systems - such as Cartesian - allow you to
specify additional, axis-specific labels:

.. code:: python

    canvas = toyplot.Canvas(width=300, height=300)
    axes = canvas.cartesian(label="Cartesian Coordinates", xlabel="Days", ylabel="Users")
    axes.plot(numpy.linspace(0, 1)**2);



.. raw:: html

    <div class="toyplot" id="t1c71a737353044738e6c057fb69fcff6" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t24c8c2782e5a4130ba060e15dd9933dc" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 300.0 300.0" width="300.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t9ef4463c73cd4a6c95dbc9d5c6757518"><clipPath id="t94411d8245de4fcf91db3cd05f49a1b8"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t94411d8245de4fcf91db3cd05f49a1b8)"><g class="toyplot-mark-Plot" id="t57ee660f03de438cb40367929e8520c2" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 250.0 L 54.0 249.9167013744273 L 58.0 249.66680549770928 L 62.0 249.25031236984589 L 66.0 248.66722199083716 L 70.0 247.91753436068305 L 74.0 247.0012494793836 L 78.0 245.91836734693877 L 82.0 244.6688879633486 L 86.0 243.25281132861306 L 90.0 241.6701374427322 L 94.0 239.92086630570594 L 98.0 238.00499791753435 L 102.0 235.92253227821743 L 106.0 233.67346938775512 L 110.0 231.25780924614745 L 114.0 228.67555185339444 L 118.0 225.92669720949604 L 122.0 223.01124531445231 L 126.0 219.92919616826322 L 130.0 216.68054977092879 L 134.0 213.26530612244898 L 138.0 209.68346522282383 L 142.0 205.93502707205332 L 146.0 202.01999167013744 L 150.0 197.93835901707621 L 154.0 193.69012911286964 L 158.0 189.27530195751771 L 162.0 184.69387755102045 L 166.0 179.94585589337777 L 170.0 175.03123698458978 L 174.0 169.95002082465641 L 178.0 164.7022074135777 L 182.0 159.2877967513536 L 186.0 153.70678883798416 L 190.0 147.9591836734694 L 194.0 142.04498125780927 L 198.0 135.96418159100375 L 202.0 129.7167846730529 L 206.0 123.30279050395671 L 210.0 116.72219908371514 L 214.0 109.97501041232822 L 218.0 103.06122448979593 L 222.0 95.980841316118301 L 226.0 88.733860891295336 L 230.0 81.320283215326981 L 234.0 73.740108288213264 L 238.0 65.993336109954186 L 242.0 58.079966680549774 L 246.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tedbe1e26d82b4074aac14afad368f101" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g transform="translate(100.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-14.34" y="10.266">Days</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t4eba57677183475180ca6236595d7489" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g transform="translate(100.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-16.674" y="0.0">Users</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g><g transform="translate(150.0,42.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:14.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-74.683" y="-4.823">Cartesian Coordinates</text></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t1c71a737353044738e6c057fb69fcff6";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t24c8c2782e5a4130ba060e15dd9933dc";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t57ee660f03de438cb40367929e8520c2","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tedbe1e26d82b4074aac14afad368f101",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t4eba57677183475180ca6236595d7489",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Coordinate System Text
----------------------

Another option for labelling a figure is to insert text using the same
domain as the data. For example, we can label individual series in a
plot:

.. code:: python

    def series(x):
        return numpy.cumsum(numpy.random.normal(loc=0.05, size=len(x)))
    
    numpy.random.seed(1234)
    x = numpy.arange(100)
    y = numpy.column_stack([series(x) for i in range(5)])

.. code:: python

    label_style = {"text-anchor":"start", "-toyplot-anchor-shift":"5px"}
    canvas, axes, mark = toyplot.plot(x, y)
    for i in range(y.shape[1]):
        axes.text(x[-1], y[-1,i], "Series %s" % i, style=label_style)



.. raw:: html

    <div class="toyplot" id="t2dc5b458fcd44b7ba84fb36bdeaeb671" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="600px" id="tf4a5509532ba412390f11ce38f184bf0" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600 600" width="600px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t2b9fb9df174d4a6198cc166f2bbc8de0"><clipPath id="t7ddb02317f27464c8a2cba2d2820c613"><rect height="520.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t7ddb02317f27464c8a2cba2d2820c613)"><g class="toyplot-mark-Plot" id="te59cfd7a894843cab2ce911c5389c012" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 343.33002059537489 L 54.641871792837946 358.7920369979883 L 59.283743585675886 338.69902399829283 L 63.925615378513818 342.25837056841618 L 68.567487171351772 351.3459033202555 L 73.209358964189704 338.645870513082 L 77.85123075702765 326.31951593973241 L 82.493102549865583 334.26783253218389 L 87.134974342703543 333.37754329294927 L 91.776846135541476 363.09187540771052 L 96.418717928379408 346.82950264602482 L 101.06058972121735 332.70949416307025 L 105.7024615140553 319.11287313250273 L 110.34433330689323 345.82647843101597 L 114.98620509973117 349.67617383654868 L 119.62807689256911 348.96988796792573 L 124.26994868540707 342.79777741991239 L 128.91182047824501 338.20254793539988 L 133.55369227108292 319.62119641700792 L 138.1955640639209 339.90662258741213 L 142.83743585675882 341.97522053052802 L 147.47930764959676 350.18705885629316 L 152.12117944243471 346.88831609324103 L 156.76305123527266 338.71076911964946 L 161.4049230281106 320.17016227750582 L 166.04679482094852 325.85240881431139 L 170.68866661378647 316.02000903823063 L 175.33053840662444 339.96600901716192 L 179.97241019946233 341.76983923118337 L 184.61428199230031 326.74156137410824 L 189.25615378513822 331.45534391905619 L 193.89802557797617 326.20495393882919 L 198.53989737081415 311.33103683791296 L 203.18176916365206 296.47934861757261 L 207.82364095649001 284.09704124947649 L 212.46551274932796 285.07399555091905 L 217.10738454216587 282.70636005311985 L 221.74925633500382 286.40315901074212 L 226.3911281278418 274.31956327587511 L 231.03299992067969 241.24070655410159 L 235.67487171351766 239.53050351805496 L 240.31674350635558 246.52915869095634 L 244.95861529919353 245.36179987328694 L 249.60048709203147 272.8034333998005 L 254.24235888486942 268.76788040910606 L 258.88423067770736 280.24818814691611 L 263.52610247054531 281.4243947407773 L 268.16797426338326 280.4989687201691 L 272.80984605622115 269.58434164747058 L 277.45171784905915 265.98953487895074 L 282.09358964189704 253.91496338192485 L 286.73546143473499 272.83038673960164 L 291.37733322757293 291.15175252455737 L 296.01920502041088 291.84177427213211 L 300.66107681324888 298.59374362393095 L 305.30294860608672 299.875986880472 L 309.94482039892466 294.40087550655176 L 314.58669219176267 294.20455419855818 L 319.22856398460061 285.86033106372054 L 323.87043577743856 264.23664291281534 L 328.51230757027645 276.76149985665938 L 333.15417936311439 277.03720496146769 L 337.79605115595234 272.18616357938197 L 342.43792294879029 274.33407127479313 L 347.07979474162829 259.64686559487825 L 351.72166653446624 291.49921162485907 L 356.36353832730407 263.30375797759905 L 361.00541012014202 278.11063159573075 L 365.64728191298002 274.56169953634054 L 370.28915370581797 264.33404725003658 L 374.93102549865591 274.30035184363931 L 379.57289729149386 267.36113649325932 L 384.21476908433175 257.1401569864081 L 388.8566408771697 249.3682213985208 L 393.49851267000764 261.24284645102972 L 398.14038446284565 233.35583570526822 L 402.78225625568354 229.60255736184212 L 407.42412804852148 244.54532372648018 L 412.06599984135937 235.30342889360318 L 416.70787163419737 234.09039110820942 L 421.34974342703532 227.11956552076202 L 425.99161521987327 274.73324606582531 L 430.63348701271116 256.15260704391358 L 435.2753588055491 253.40664414882914 L 439.91723059838705 250.49943120200186 L 444.559102391225 255.65032603189297 L 449.200974184063 244.57369323610104 L 453.84284597690089 230.54890055625543 L 458.48471776973884 226.20106985300572 L 463.12658956257673 206.65988744320293 L 467.76846135541473 204.90031974793388 L 472.41033314825268 209.64289061264935 L 477.05220494109057 222.89430468552675 L 481.69407673392851 230.14057802127687 L 486.33594852676651 218.3968664165042 L 490.9778203196044 218.82979924903583 L 495.61969211244235 222.82434266348673 L 500.2615639052803 214.98762814843693 L 504.90343569811824 228.79652991325702 L 509.54530749095619 235.05574858979216" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 345.77241809643766 L 54.641871792837946 337.41741617132186 L 59.283743585675886 329.91537655782139 L 63.925615378513818 325.37159231958105 L 68.567487171351772 318.13114749557167 L 73.209358964189704 298.97624837605395 L 77.85123075702765 308.88387562867604 L 82.493102549865583 314.54867291005473 L 87.134974342703543 297.27618439277626 L 91.776846135541476 313.95963911664523 L 96.418717928379408 301.41798946214669 L 101.06058972121735 323.92329584101935 L 105.7024615140553 329.35429373785217 L 110.34433330689323 318.52436639336611 L 114.98620509973117 320.61039899826847 L 119.62807689256911 322.40158385231877 L 124.26994868540707 312.50004504055596 L 128.91182047824501 336.46598973535095 L 133.55369227108292 335.15051629923988 L 138.1955640639209 329.1221771390492 L 142.83743585675882 331.8112437807626 L 147.47930764959676 339.50456235356603 L 152.12117944243471 348.08113657811043 L 156.76305123527266 341.49158073647703 L 161.4049230281106 363.89250544122621 L 166.04679482094852 357.87952848323721 L 170.68866661378647 363.69754442881595 L 175.33053840662444 367.07210711601681 L 179.97241019946233 356.9883364513949 L 184.61428199230031 347.11425760939903 L 189.25615378513822 343.19031815565188 L 193.89802557797617 340.46338062558135 L 198.53989737081415 328.72599344801444 L 203.18176916365206 302.38804255524963 L 207.82364095649001 293.04243322653912 L 212.46551274932796 305.40185930721685 L 217.10738454216587 332.98291198707494 L 221.74925633500382 306.14745165095258 L 226.3911281278418 328.98658140813075 L 231.03299992067969 311.90639853549379 L 235.67487171351766 300.42231485506068 L 240.31674350635558 304.89177005586697 L 244.95861529919353 294.69336749086438 L 249.60048709203147 305.53931910711293 L 254.24235888486942 288.9140795735637 L 258.88423067770736 295.34208030423804 L 263.52610247054531 285.16609872449595 L 268.16797426338326 271.15122269594832 L 272.80984605622115 272.12325552406656 L 277.45171784905915 239.38578851461097 L 282.09358964189704 231.9846923098543 L 286.73546143473499 220.51199944227363 L 291.37733322757293 226.25814985423378 L 296.01920502041088 226.34888735082578 L 300.66107681324888 207.27101882356885 L 305.30294860608672 217.50020379083847 L 309.94482039892466 245.60102176007211 L 314.58669219176267 249.44292602192195 L 319.22856398460061 260.78179012966382 L 323.87043577743856 255.57530349110402 L 328.51230757027645 247.62345914636654 L 333.15417936311439 257.02595262579234 L 337.79605115595234 260.6876404940279 L 342.43792294879029 272.42599834246033 L 347.07979474162829 283.39827811412948 L 351.72166653446624 279.65824040556248 L 356.36353832730407 270.45975965586285 L 361.00541012014202 267.25488902030088 L 365.64728191298002 253.66972968057473 L 370.28915370581797 239.60133155018622 L 374.93102549865591 239.90770978676753 L 379.57289729149386 246.69166728143193 L 384.21476908433175 258.72753303286197 L 388.8566408771697 274.84132414166538 L 393.49851267000764 272.27081724306936 L 398.14038446284565 274.61549675573735 L 402.78225625568354 245.15855057222734 L 407.42412804852148 242.82397440324957 L 412.06599984135937 261.24641403841355 L 416.70787163419737 241.28513610037388 L 421.34974342703532 269.71437359670438 L 425.99161521987327 287.29798129237003 L 430.63348701271116 281.69353065371808 L 435.2753588055491 281.21586629332609 L 439.91723059838705 263.2953317104425 L 444.559102391225 282.26166198653402 L 449.200974184063 297.78531158346476 L 453.84284597690089 305.12840768765227 L 458.48471776973884 310.06802199817156 L 463.12658956257673 328.71220594857601 L 467.76846135541473 325.196998325626 L 472.41033314825268 332.5539581057958 L 477.05220494109057 351.83942529841215 L 481.69407673392851 363.31192503759343 L 486.33594852676651 347.66864447485142 L 490.9778203196044 352.83924091672918 L 495.61969211244235 354.34532093769542 L 500.2615639052803 341.6182587878501 L 504.90343569811824 337.03271994253396 L 509.54530749095619 350.60514883160675" style="stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 354.04926895194819 L 54.641871792837946 361.77357238155702 L 59.283743585675886 358.96841859363479 L 63.925615378513818 366.03495930000844 L 68.567487171351772 351.02478640478773 L 73.209358964189704 361.07312677495736 L 77.85123075702765 367.50507431066967 L 82.493102549865583 365.85343505787398 L 87.134974342703543 339.28205885170655 L 91.776846135541476 327.92631855364709 L 96.418717928379408 320.29566928201024 L 101.06058972121735 327.0228911708947 L 105.7024615140553 312.19821937000114 L 110.34433330689323 282.95683449160532 L 114.98620509973117 262.49494069724642 L 119.62807689256911 248.0570199417397 L 124.26994868540707 237.22681079220558 L 128.91182047824501 245.70361131008457 L 133.55369227108292 239.05973009087751 L 138.1955640639209 229.04549839724237 L 142.83743585675882 232.11691013178165 L 147.47930764959676 205.35887600079386 L 152.12117944243471 199.10883564830323 L 156.76305123527266 186.35998985707465 L 161.4049230281106 182.61483316997763 L 166.04679482094852 210.10579839612799 L 170.68866661378647 214.68468862589557 L 175.33053840662444 215.1875464701919 L 179.97241019946233 199.24566711020435 L 184.61428199230031 195.21933574315332 L 189.25615378513822 192.8996883799532 L 193.89802557797617 188.17040680048191 L 198.53989737081415 189.62176866411457 L 203.18176916365206 198.97871062638708 L 207.82364095649001 215.2087926752603 L 212.46551274932796 211.15070320848463 L 217.10738454216587 202.59866649117504 L 221.74925633500382 164.46665060434779 L 226.3911281278418 158.37758375662938 L 231.03299992067969 148.64093826200127 L 235.67487171351766 151.7005276221945 L 240.31674350635558 144.24061794047694 L 244.95861529919353 131.86715204054451 L 249.60048709203147 145.44078596124783 L 254.24235888486942 163.62773092043105 L 258.88423067770736 147.31268975155993 L 263.52610247054531 130.61790820411991 L 268.16797426338326 124.6366304198452 L 272.80984605622115 135.89862647338131 L 277.45171784905915 131.22224990972393 L 282.09358964189704 105.28723345729669 L 286.73546143473499 127.8136613251782 L 291.37733322757293 146.20429278504744 L 296.01920502041088 143.80862948096251 L 300.66107681324888 143.08009893270241 L 305.30294860608672 159.59938963235871 L 309.94482039892466 170.28945274822894 L 314.58669219176267 162.10536930195525 L 319.22856398460061 168.25836273296486 L 323.87043577743856 178.26538943680865 L 328.51230757027645 156.86202453739085 L 333.15417936311439 153.40020921577093 L 337.79605115595234 148.48080998517639 L 342.43792294879029 136.06051185732977 L 347.07979474162829 131.33005679216228 L 351.72166653446624 116.06365804749782 L 356.36353832730407 110.46445470376295 L 361.00541012014202 84.124533981925779 L 365.64728191298002 90.029669482045222 L 370.28915370581797 84.098491766660914 L 374.93102549865591 83.101670376246176 L 379.57289729149386 91.371240546533301 L 384.21476908433175 95.012344215563772 L 388.8566408771697 104.12797561793714 L 393.49851267000764 101.04652769474927 L 398.14038446284565 87.040803604785339 L 402.78225625568354 86.044700779895805 L 407.42412804852148 77.862572467648619 L 412.06599984135937 72.390863056473307 L 416.70787163419737 75.44801184748097 L 421.34974342703532 81.417257772809506 L 425.99161521987327 85.813884324157328 L 430.63348701271116 117.62625785030562 L 435.2753588055491 96.065297513791023 L 439.91723059838705 94.532824031356668 L 444.559102391225 97.709864276057772 L 449.200974184063 114.18316474916836 L 453.84284597690089 89.275648001397997 L 458.48471776973884 93.40222025070301 L 463.12658956257673 94.144319654763507 L 467.76846135541473 88.232395562745836 L 472.41033314825268 76.40491561942504 L 477.05220494109057 84.993765211667025 L 481.69407673392851 69.989417487445422 L 486.33594852676651 68.879814977730618 L 490.9778203196044 50.0 L 495.61969211244235 50.007313642783224 L 500.2615639052803 54.262642759371886 L 504.90343569811824 74.635297513429961 L 509.54530749095619 78.284706565918469" style="stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 342.57640012896741 L 54.641871792837946 332.26212923098922 L 59.283743585675886 334.53263418525466 L 63.925615378513818 298.10883306528859 L 68.567487171351772 321.03996115252613 L 73.209358964189704 321.64212273171904 L 77.85123075702765 301.56975170848142 L 82.493102549865583 292.85936314403295 L 87.134974342703543 289.87399349524634 L 91.776846135541476 312.9347873397237 L 96.418717928379408 308.34647754138388 L 101.06058972121735 315.0217052481085 L 105.7024615140553 312.01864420042591 L 110.34433330689323 298.02233710049518 L 114.98620509973117 297.68827592599666 L 119.62807689256911 300.90748548878832 L 124.26994868540707 287.70225099678714 L 128.91182047824501 287.85465606011007 L 133.55369227108292 297.08372970526619 L 138.1955640639209 310.26634441635071 L 142.83743585675882 296.09149341996823 L 147.47930764959676 282.46460082252008 L 152.12117944243471 272.11335619215907 L 156.76305123527266 269.62839105367038 L 161.4049230281106 279.8874516080013 L 166.04679482094852 283.84465728740707 L 170.68866661378647 257.30011006959518 L 175.33053840662444 254.50952578191934 L 179.97241019946233 243.53745968995972 L 184.61428199230031 248.59228114571314 L 189.25615378513822 245.45275082543336 L 193.89802557797617 241.055365784994 L 198.53989737081415 239.45746776459742 L 203.18176916365206 239.28106441890114 L 207.82364095649001 240.91810850911702 L 212.46551274932796 236.62262234933547 L 217.10738454216587 217.20325428614103 L 221.74925633500382 216.83005577941069 L 226.3911281278418 214.37186306205686 L 231.03299992067969 207.80697676619792 L 235.67487171351766 203.54454510699478 L 240.31674350635558 195.20140558024374 L 244.95861529919353 186.5950140573955 L 249.60048709203147 188.2794496554402 L 254.24235888486942 202.12060264793837 L 258.88423067770736 202.09974003456523 L 263.52610247054531 212.87717649124423 L 268.16797426338326 206.57433192064997 L 272.80984605622115 200.13014398724283 L 277.45171784905915 212.74292386393267 L 282.09358964189704 217.86306230055902 L 286.73546143473499 196.87750217159729 L 291.37733322757293 201.08061185079953 L 296.01920502041088 206.61291164073458 L 300.66107681324888 224.06691057288282 L 305.30294860608672 223.9501846282584 L 309.94482039892466 212.14611391291473 L 314.58669219176267 183.04003298944554 L 319.22856398460061 164.97668964008102 L 323.87043577743856 160.63560657832872 L 328.51230757027645 146.36389717405231 L 333.15417936311439 131.06859417620731 L 337.79605115595234 125.77328030153625 L 342.43792294879029 127.77992905412417 L 347.07979474162829 93.474683255608596 L 351.72166653446624 74.024720788811564 L 356.36353832730407 88.993802360344716 L 361.00541012014202 105.50055506666901 L 365.64728191298002 96.585487058627919 L 370.28915370581797 110.54491563607422 L 374.93102549865591 118.15116570997353 L 379.57289729149386 116.09085065598636 L 384.21476908433175 134.88110977655626 L 388.8566408771697 131.34798338220256 L 393.49851267000764 142.82486780622662 L 398.14038446284565 165.51552929174991 L 402.78225625568354 140.54893358783238 L 407.42412804852148 157.66067809886721 L 412.06599984135937 149.45008540332529 L 416.70787163419737 158.01307158728795 L 421.34974342703532 136.02235340765731 L 425.99161521987327 136.76296826093181 L 430.63348701271116 111.00958708348054 L 435.2753588055491 114.84943132066562 L 439.91723059838705 111.55010777307584 L 444.559102391225 117.60420479643869 L 449.200974184063 102.93160116529373 L 453.84284597690089 125.83110214126683 L 458.48471776973884 135.39664555126348 L 463.12658956257673 146.65951758458309 L 467.76846135541473 140.64407879654235 L 472.41033314825268 152.84084130985011 L 477.05220494109057 147.65727456656154 L 481.69407673392851 139.81166664742307 L 486.33594852676651 154.31891096932418 L 490.9778203196044 152.98727631108972 L 495.61969211244235 151.46965655204963 L 500.2615639052803 164.7165323998255 L 504.90343569811824 167.26877301595641 L 509.54530749095619 140.40713914140326" style="stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0;stroke-width:2.0"></path></g><g class="toyplot-Series"><path d="M 50.0 352.78993330575952 L 54.641871792837946 364.63171485392746 L 59.283743585675886 359.13195770322034 L 63.925615378513818 375.66573804802579 L 68.567487171351772 377.63711819370337 L 73.209358964189704 383.23960171856362 L 77.85123075702765 369.1538946413516 L 82.493102549865583 349.65795838647 L 87.134974342703543 334.24014665110207 L 91.776846135541476 327.61612023080193 L 96.418717928379408 339.96976533170925 L 101.06058972121735 322.41221157091451 L 105.7024615140553 314.9192005775065 L 110.34433330689323 322.79806906651567 L 114.98620509973117 331.66421400760021 L 119.62807689256911 334.2455521740776 L 124.26994868540707 325.63218116478924 L 128.91182047824501 320.17359962245376 L 133.55369227108292 344.0996851006974 L 138.1955640639209 355.75571692689567 L 142.83743585675882 365.2218700818857 L 147.47930764959676 366.00955431635987 L 152.12117944243471 361.60828991693353 L 156.76305123527266 357.71424835869078 L 161.4049230281106 360.55796068252471 L 166.04679482094852 364.11446523100574 L 170.68866661378647 357.35887363396256 L 175.33053840662444 357.48804675771305 L 179.97241019946233 363.17990852499457 L 184.61428199230031 357.76514990611292 L 189.25615378513822 371.01139118729139 L 193.89802557797617 374.48924655751881 L 198.53989737081415 354.75576804573757 L 203.18176916365206 371.01354747536936 L 207.82364095649001 391.47844168710731 L 212.46551274932796 369.69567369724973 L 217.10738454216587 377.05900801766461 L 221.74925633500382 378.68910667735889 L 226.3911281278418 355.34480224433526 L 231.03299992067969 361.99591208961039 L 235.67487171351766 370.58934897546209 L 240.31674350635558 361.78133975917825 L 244.95861529919353 364.04715105339176 L 249.60048709203147 358.8768662592791 L 254.24235888486942 363.39448099047507 L 258.88423067770736 373.31174076207247 L 263.52610247054531 369.02622618522605 L 268.16797426338326 364.56195797825421 L 272.80984605622115 380.4122269783731 L 277.45171784905915 389.54529550362156 L 282.09358964189704 412.37669318095203 L 286.73546143473499 408.01768330270193 L 291.37733322757293 405.99698079116712 L 296.01920502041088 410.23984178398695 L 300.66107681324888 417.53366104738768 L 305.30294860608672 416.50453130728852 L 309.94482039892466 423.58255019218933 L 314.58669219176267 407.92252811081391 L 319.22856398460061 423.6154619514603 L 323.87043577743856 441.09294085576772 L 328.51230757027645 412.29333384403793 L 333.15417936311439 431.79960073063165 L 337.79605115595234 446.71924751907238 L 342.43792294879029 440.3627486588739 L 347.07979474162829 434.08287782693952 L 351.72166653446624 423.68100232949433 L 356.36353832730407 419.4566401396645 L 361.00541012014202 422.06899425863043 L 365.64728191298002 428.18438769159758 L 370.28915370581797 436.96755542279425 L 374.93102549865591 417.52673641090092 L 379.57289729149386 420.73067287092329 L 384.21476908433175 413.27636425966637 L 388.8566408771697 386.15826594236142 L 393.49851267000764 389.25300446602716 L 398.14038446284565 388.07691407190634 L 402.78225625568354 381.35733220819543 L 407.42412804852148 399.79222598038695 L 412.06599984135937 393.01642142245515 L 416.70787163419737 385.35328379293111 L 421.34974342703532 400.31535886189192 L 425.99161521987327 418.34130187570173 L 430.63348701271116 424.38304077637639 L 435.2753588055491 429.3060439591145 L 439.91723059838705 451.9279120851416 L 444.559102391225 451.6509301491086 L 449.200974184063 461.35439751946626 L 453.84284597690089 459.32325948901286 L 458.48471776973884 468.30827761016764 L 463.12658956257673 497.79809628525146 L 467.76846135541473 487.28594864270531 L 472.41033314825268 474.18189811899879 L 477.05220494109057 481.14591966936666 L 481.69407673392851 501.09626967313972 L 486.33594852676651 500.61219103875305 L 490.9778203196044 503.27806758273277 L 495.61969211244235 504.8409635023288 L 500.2615639052803 502.54920287589448 L 504.90343569811824 529.99087550520369 L 509.54530749095619 542.90220820189268" style="stroke:rgb(65.1%,84.7%,32.9%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g><g class="toyplot-mark-Text" id="t256e38c21f93436bb0579b81f8b3f2bc"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(509.54530749095619,235.05574858979216)"><text style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 0</text></g></g></g><g class="toyplot-mark-Text" id="t627f6bde24704406b8a0bf0090b0301c"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(509.54530749095619,350.60514883160675)"><text style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 1</text></g></g></g><g class="toyplot-mark-Text" id="t7e9732288d97424eade6577f136a59bc"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(509.54530749095619,78.284706565918469)"><text style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 2</text></g></g></g><g class="toyplot-mark-Text" id="t268d62b447c048a18669b332e7f0d301"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(509.54530749095619,140.40713914140326)"><text style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 3</text></g></g></g><g class="toyplot-mark-Text" id="t89e081dd0c8046ec827613c278f0a438"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(509.54530749095619,542.90220820189268)"><text style="fill:rgb(65.1%,84.7%,32.9%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="5.0" y="3.066">Series 4</text></g></g></g></g><g class="toyplot-coordinates-Axis" id="t2a414d536ac342958a1dea809fb26dc8" transform="translate(50.0,550.0)translate(0,10.0)"><line style="" x1="0" x2="459.5453074909562" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(232.09358964189704,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g><g transform="translate(464.1871792837941,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">100</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="tffda1d72f8cd4a88a573c20ebd31e603" transform="translate(50.0,550.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="7.09779179810732" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(64.08797363935915,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-7.225" y="-4.4408920985e-16">-10</text></g><g transform="translate(199.6037122685794,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.4408920985e-16">0</text></g><g transform="translate(335.11945089779965,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.4408920985e-16">10</text></g><g transform="translate(470.6351895270198,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.4408920985e-16">20</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t2dc5b458fcd44b7ba84fb36bdeaeb671";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tf4a5509532ba412390f11ce38f184bf0";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"te59cfd7a894843cab2ce911c5389c012","data","plot data",["x", "y0", "y1", "y2", "y3", "y4"],[[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0, 50.0, 51.0, 52.0, 53.0, 54.0, 55.0, 56.0, 57.0, 58.0, 59.0, 60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0], [0.5214351637324931, -0.6195405309739713, 0.8631664374521261, 0.6005145413604132, -0.07007419200459841, 0.8670887483031402, 1.7766771620205568, 1.190153657603208, 1.255850029717637, -0.9368349244677687, 0.2632008002520494, 1.3051468225947271, 2.3084709507071572, 0.3372161305121868, 0.05313876470408979, 0.10525712938757628, 0.5607105409577673, 0.8998024819378025, 2.2709606740671884, 0.7740551208379483, 0.6214087962087664, 0.015439452069832549, 0.2588608285401908, 0.8622997394969327, 2.2304512936770697, 1.8111460089711702, 2.536700094093551, 0.7696728675033542, 0.6365643273243555, 1.745533514895506, 1.3976932866955147, 1.785130940309487, 2.882709513202209, 3.978647768829874, 4.892365060514713, 4.820273485667039, 4.994986439435255, 4.722191633826959, 5.613866346823101, 8.054826862286134, 8.18102645012337, 7.664580519658414, 7.750722456342487, 5.725744855652458, 6.023537055401005, 5.176380270961306, 5.0895854376999585, 5.157874629049178, 5.963288611447313, 6.228557192416756, 7.119565987348147, 5.723755910303841, 4.371782628802997, 4.320864428854083, 3.822621979667228, 3.728002471297844, 4.132022803497081, 4.146509778218941, 4.762248084281536, 6.3579068889070935, 5.433670555139778, 5.413325678035675, 5.77129453325171, 5.61279577014583, 6.696596502701329, 4.346142868889033, 6.426746489727833, 5.334115200705069, 5.59599858748277, 6.350719211799879, 5.615284000036682, 6.12734373719873, 6.881571962660905, 7.455079930554715, 6.5788256170244885, 8.636668567802488, 8.913631109673384, 7.8109720004224314, 8.492951446231562, 8.582464132924928, 9.096856457975823, 5.583339797351088, 6.954445412821293, 7.157075965025828, 7.371605507958226, 6.991509817081739, 7.80887855283415, 8.843798394744047, 9.16463424357085, 10.606620437017257, 10.736462750025886, 10.386498169329364, 9.408647610647458, 8.87392939938667, 9.740523325934511, 9.708576274107847, 9.413810259853202, 9.992098405150596, 8.973109621670464, 8.511228312543649], [0.3412053597430635, 0.9577390560966359, 1.511330815207839, 1.8466264999896962, 2.380914612739446, 3.7943961251655915, 3.0632908415401996, 2.645273175202714, 3.919847530328888, 2.6887392551848457, 3.6142147594591703, 1.9534994354296413, 1.5527343322933669, 2.351898138212432, 2.1979652721111806, 2.0657898604454465, 2.796445864826903, 1.0279468744352886, 1.1250185097609997, 1.569862719088204, 1.3714306647073573, 0.8037240167103407, 0.17084002026100675, 0.6570976246019236, -0.9959151495113143, -0.5522045503726491, -0.9815285539481464, -1.2305448469142268, -0.4864415592354625, 0.24218811447439403, 0.5317441094782909, 0.7329707387727407, 1.5990979721327816, 3.5426324397289823, 4.232265202922685, 3.3202363710174936, 1.2849707288973837, 3.2652174963629594, 1.5798686218925668, 2.8402523267970814, 3.687687746224955, 3.357876962177576, 4.1104391861791765, 3.3100929145240614, 4.53690536462899, 4.062569261996534, 4.813476992912138, 5.847665063634553, 5.775936654967732, 8.19170528380777, 8.737848210055365, 9.584443076720317, 9.160422186594632, 9.153726470103702, 10.56152372821076, 9.806690004044057, 7.733069754951127, 7.449567314517879, 6.612847962032501, 6.99704589293151, 7.58382971783426, 6.8899993498980585, 6.6197954676571795, 5.753596606390639, 4.943928306408898, 5.219913793142653, 5.8986896196809475, 6.135183968454022, 7.137662313563144, 8.175799896156454, 8.153191582193777, 7.652588658630358, 6.764436044537254, 5.5753644819424615, 5.7650477559737565, 5.592028774091281, 7.765720662684833, 7.937994096943662, 6.578562357020893, 8.051548309793136, 5.9536932721495255, 4.656160758691771, 5.0697253154984185, 5.104973203693824, 6.4273682822400335, 5.027801673376646, 3.8822779317096754, 3.3404149585624263, 2.9759101150302367, 1.6001153815922153, 1.8595101691281393, 1.3166241652892139, -0.10649224817643343, -0.9530728634783044, 0.20127870638200818, -0.1802708091340366, -0.29140771737809545, 0.6477497766947783, 0.9861266244100437, -0.015412313159994362], [-0.2695613998402315, -0.8395544875614336, -0.6325561111147446, -1.1540114621945339, -0.04637827898991964, -0.7878670884678051, -1.2624944343962752, -1.1406163950259065, 0.8201430322512764, 1.6581077153888908, 2.221189859855883, 1.724773579582289, 2.818718235077612, 4.976503387870983, 6.486430869456276, 7.551836327268797, 8.351020928192995, 7.725499449756306, 8.215765841425036, 8.954737697751979, 8.72809157047499, 10.70262489049028, 11.163828911197506, 12.104593867370623, 12.38095709462233, 10.352339200920154, 10.014452968952979, 9.97734599898898, 11.153731821126254, 11.45084353728399, 11.622015342615532, 11.970999278157578, 11.863900141310927, 11.173431118530209, 9.975778195478975, 10.275233410631424, 10.90630673125203, 13.720150811101597, 14.169476248081173, 14.887964417286979, 14.662190688630673, 15.212673588785046, 16.12573844937567, 15.124110589910458, 13.782056512417372, 14.985978753029597, 16.21792285902883, 16.65929430745076, 15.828247215249192, 16.173327175035432, 18.087128237167935, 16.42485431269668, 15.067769766953456, 15.244550953280427, 15.298310801075923, 14.07931654500253, 13.29047362358224, 13.89439487502196, 13.440352156939998, 12.701911972422119, 14.28131264690605, 14.53676750083203, 14.89978062981289, 15.81630134198119, 16.165371871575566, 17.29191251542169, 17.70508986296614, 19.648769688517984, 19.213016944235175, 19.650691400012775, 19.72424901040533, 19.11401950836105, 18.845334578783035, 18.172672385108662, 18.40005910449326, 19.433571833836425, 19.50707641972182, 20.110853397585185, 20.514622691581824, 20.28902905781414, 19.84854546633546, 19.52410886614268, 17.176604890003862, 18.7676348732818, 18.880719412239106, 18.64627872831281, 17.4306781907116, 19.26865782316735, 18.964149115097975, 18.90938799203087, 19.34564168121992, 20.218417054985295, 19.584627232554286, 20.691830563768416, 20.773710537337447, 22.166892994866387, 22.166353305317614, 21.852343349010503, 20.349001009579442, 20.07970320775928], [0.5770464509549642, 1.338158850319787, 1.1706133698293109, 3.8584045805331746, 2.1662669499382092, 2.121832142196765, 3.603015894451329, 4.245774341001998, 4.466071236328286, 2.7643652885362617, 3.1029466108794694, 2.61036709397269, 2.8319694759586853, 3.86478730520179, 3.889438403139021, 3.651885953854913, 4.626328821198279, 4.615082521331964, 3.934049178746758, 2.9612754740516154, 4.007268444297368, 5.0128263769248225, 5.7766671481198655, 5.960038110313987, 5.202999801841174, 4.910989019961959, 6.869768678053146, 7.075691939506273, 7.885344471599235, 7.512338243179987, 7.7440109885036685, 8.068503559250072, 8.186415916630828, 8.19943310175491, 8.078632071057287, 8.395605302597154, 9.82860255145008, 9.856141677938654, 10.03753704516457, 10.521974230266801, 10.8365082985838, 11.452166642857625, 12.087250922359349, 11.962952769607261, 10.941584098152171, 10.943123595599788, 10.147833206033544, 10.612933764415125, 11.088464355812983, 10.157739998312397, 9.779913888340378, 11.328483843478915, 11.018327272609888, 10.610086883272395, 9.322118481321425, 9.330731941706553, 10.201779897814468, 12.34958067858616, 13.682513925460682, 14.002851851200054, 15.055992213244986, 16.18466576456539, 16.575418449695157, 16.42734349007159, 18.958801912947244, 20.39405678913645, 19.28945582374678, 18.0713867733697, 18.72924895957918, 17.699152476421588, 17.137870801625827, 17.289905913918158, 15.90333197714604, 16.164049029651697, 15.317144858954185, 13.642751779962351, 15.485090976609294, 14.222378270017064, 14.828255696402689, 14.196374390911558, 15.819117136667362, 15.764465561819597, 17.664863363429497, 17.381512936680096, 17.624977170499967, 17.178232232635057, 18.260955448370918, 16.57115165084836, 15.865289475225453, 15.034177742577517, 15.478070005490192, 14.578044470693909, 14.960551092856159, 15.539495501712207, 14.468974507719482, 14.56723871464514, 14.679227165166918, 13.70171149194905, 13.513376126481724, 15.49555429606307], [-0.17663229367683592, -1.050463013853759, -0.6446240163809387, -1.8646874947672272, -2.010159907463986, -2.4235793066814493, -1.3841644593955986, 0.0544829222361185, 1.1921966587602597, 1.6809979217946505, 0.7693956809134145, 2.0650056180612606, 2.617931135731893, 2.036532357353374, 1.3822803102651138, 1.1917977735067715, 1.8273970844366292, 2.2301976445450356, 0.46463995211294984, -0.39548389358219205, -1.0940118469212514, -1.1521367734015144, -0.8273579363493466, -0.5400081718399214, -0.74985186620331, -1.0122940433597098, -0.5137843008473031, -0.5233162655517036, -0.9433310789494903, -0.5437643073218248, -1.5212331544954376, -1.7778716383650484, -0.3216954988707805, -1.5213922716651334, -3.031541160550366, -1.4241435099013435, -1.9674999048778317, -2.087788417207332, -0.3651616087526257, -0.8559614164025009, -1.4900897451690853, -0.8401276591870923, -1.0073267843317304, -0.6258002659795775, -0.9591648461304054, -1.6909809342035165, -1.37474352737568, -1.0453155028429428, -2.214941198016713, -2.8888901147722175, -4.573668422316152, -4.252007637942128, -4.102895620993038, -4.415985527430296, -4.954212255718815, -4.878270542194683, -5.4005728929398416, -4.24498593014268, -5.403001522972327, -6.692702562947243, -4.567517156215461, -6.006926857546471, -7.107879923172435, -6.638820098498469, -6.175414822073972, -5.407837889485689, -5.096113049805784, -5.2888843209061465, -5.740152453657814, -6.388281432626669, -4.953701271787595, -5.19012668572335, -4.640057100695124, -2.638953864155063, -2.8673213257480716, -2.780535067117361, -2.2846825608563597, -3.645033318537029, -3.145032017841554, -2.5795524870476556, -3.683636427430258, -5.013809822502097, -5.4596428277152595, -5.822921900134131, -7.49223856806168, -7.471799470814765, -8.187839354337594, -8.037957277834966, -8.70098123446471, -10.877098855442297, -10.101384702320342, -9.134408419251107, -9.648298659662363, -11.120478216485534, -11.084757005113095, -11.28147781193198, -11.39680728844926, -11.227693305850918, -13.252673792020966, -14.205429009037882]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t2a414d536ac342958a1dea809fb26dc8",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 107.71516799999999, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tffda1d72f8cd4a88a573c20ebd31e603",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 22.166892994866387, "min": -14.729190445894108}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that we are using the last point in each series as the anchor for
the corresponding label - by default, Toyplot renders text centered on
its anchor, so in this case we've chosen a text style that left-aligns
the text and offsets it slightly to avoid overlapping the data.

Canvas Text
-----------

When adding text to axes, you specify the text coordinates using the
same domain as your data. Naturally, this limits the added text to the
bounds defined by the axes. For the ultimate in labeling flexibility,
you can add text to the canvas directly, using canvas units, outside
and/or overlapping coordinate systems:

.. code:: python

    label_style={"font-size":"18px", "font-weight":"bold"}
    
    canvas = toyplot.Canvas(width=600, height=300)
    canvas.cartesian(grid=(1,2,0)).plot(numpy.linspace(1, 0)**2)
    canvas.cartesian(grid=(1,2,1), yshow=False).plot(numpy.linspace(0, 1)**2)
    canvas.text(300, 120, "This label overlaps two sets of axes!", style=label_style);



.. raw:: html

    <div class="toyplot" id="t94cd2a1c113b482f8010267add122b7b" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="tbb39975be11a4e5d9f8efdbddc3c2e03" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t085c218c36fe45e2ab8702b8b1e206d3"><clipPath id="t4a3810e348094853afd3d2b36f5a31eb"><rect height="220.0" width="220.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t4a3810e348094853afd3d2b36f5a31eb)"><g class="toyplot-mark-Plot" id="t4d1130193d584df7a52fd1d62b0e0464" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 50.0 L 54.0 58.079966680549774 L 58.0 65.993336109954186 L 62.0 73.740108288213221 L 66.0 81.320283215326938 L 70.0 88.733860891295294 L 74.0 95.980841316118301 L 78.0 103.0612244897959 L 82.0 109.97501041232817 L 86.0 116.72219908371511 L 90.0 123.30279050395669 L 94.0 129.7167846730529 L 98.0 135.96418159100375 L 102.0 142.04498125780924 L 106.0 147.9591836734694 L 110.0 153.70678883798413 L 114.0 159.2877967513536 L 118.0 164.70220741357767 L 122.0 169.95002082465641 L 126.0 175.03123698458975 L 130.0 179.94585589337777 L 134.0 184.69387755102045 L 138.0 189.27530195751768 L 142.0 193.69012911286964 L 146.0 197.93835901707621 L 150.0 202.01999167013744 L 154.0 205.93502707205329 L 158.0 209.68346522282383 L 162.0 213.265306122449 L 166.0 216.68054977092876 L 170.0 219.92919616826322 L 174.0 223.01124531445231 L 178.0 225.92669720949601 L 182.0 228.67555185339441 L 186.0 231.25780924614742 L 190.0 233.67346938775509 L 194.0 235.9225322782174 L 198.0 238.00499791753435 L 202.0 239.92086630570594 L 206.0 241.67013744273217 L 210.0 243.25281132861306 L 214.0 244.6688879633486 L 218.0 245.91836734693877 L 222.0 247.00124947938357 L 226.0 247.91753436068305 L 230.0 248.66722199083716 L 234.0 249.25031236984589 L 238.0 249.66680549770925 L 242.0 249.9167013744273 L 246.0 250.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t86675d512e7542338fcdfd8d43a4fa43" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="td2c89aaa4c064d2dbc7b0d8a0a7da31a" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(100.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(200.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t9f1ab5853fcf4b7ca9834dce5747f954"><clipPath id="t27d2c906398543399a7dec129fa622fd"><rect height="220.0" width="220.0" x="340.0" y="40.0"></rect></clipPath><g clip-path="url(#t27d2c906398543399a7dec129fa622fd)"><g class="toyplot-mark-Plot" id="t1cb11046853448d7a1b1856ed23f2825" style="fill:none"><g class="toyplot-Series"><path d="M 350.0 250.0 L 354.0 249.9167013744273 L 358.0 249.66680549770928 L 362.0 249.25031236984589 L 366.0 248.66722199083716 L 370.0 247.91753436068305 L 374.0 247.0012494793836 L 378.0 245.91836734693877 L 382.0 244.6688879633486 L 386.0 243.25281132861306 L 390.0 241.6701374427322 L 394.0 239.92086630570594 L 398.0 238.00499791753435 L 402.0 235.92253227821743 L 406.0 233.67346938775512 L 410.0 231.25780924614745 L 414.0 228.67555185339444 L 418.0 225.92669720949604 L 422.0 223.01124531445231 L 426.0 219.92919616826322 L 430.0 216.68054977092879 L 434.0 213.26530612244898 L 438.0 209.68346522282383 L 442.0 205.93502707205332 L 446.0 202.01999167013744 L 450.0 197.93835901707621 L 454.0 193.69012911286964 L 458.0 189.27530195751771 L 462.0 184.69387755102045 L 466.0 179.94585589337777 L 470.0 175.03123698458978 L 474.0 169.95002082465641 L 478.0 164.7022074135777 L 482.0 159.2877967513536 L 486.0 153.70678883798416 L 490.0 147.9591836734694 L 494.0 142.04498125780927 L 498.0 135.96418159100375 L 502.0 129.7167846730529 L 506.0 123.30279050395671 L 510.0 116.72219908371514 L 514.0 109.97501041232822 L 518.0 103.06122448979593 L 522.0 95.980841316118301 L 526.0 88.733860891295336 L 530.0 81.320283215326981 L 534.0 73.740108288213264 L 538.0 65.993336109954186 L 542.0 58.079966680549774 L 546.0 50.0" style="stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tfb3600a2a16a47509d044517423ef6de" transform="translate(350.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="196.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(40.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(80.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(120.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(160.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-mark-Text" id="tf631b2cf832f422cb6b23c73dcd2f4f2"><g class="toyplot-Series"><g class="toyplot-Datum" transform="translate(300.0,120.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:18.0px;font-weight:bold;opacity:1.0;stroke:none;vertical-align:baseline;white-space:pre" x="-156.06" y="4.599">This label overlaps two sets of axes!</text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t94cd2a1c113b482f8010267add122b7b";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tbb39975be11a4e5d9f8efdbddc3c2e03";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t4d1130193d584df7a52fd1d62b0e0464","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t86675d512e7542338fcdfd8d43a4fa43",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td2c89aaa4c064d2dbc7b0d8a0a7da31a",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1cb11046853448d7a1b1856ed23f2825","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tfb3600a2a16a47509d044517423ef6de",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


... remember when placing labels directly on the canvas that, unlike
Cartesian coordinates, canvas coordinates increase from top-to-bottom.

Coordinate System Color Scales
------------------------------

Since we often use color in visualization to add an additional dimension
to our plots, we need a way to help viewers map between colors and
values. For this case, Toyplot allows a color scale to be added to a set
of :ref:`cartesian-coordinates`:

.. code:: python

    data = toyplot.data.read_csv("cars-clean.csv", convert=True)
    
    colormap = toyplot.color.brewer.map(
        name="BlueGreenBrown",
        reverse=True,
        domain_min = data["MPG"].min(),
        domain_max = data["MPG"].max(),
    )
    canvas = toyplot.Canvas(width=600, height=400)
    axes = canvas.cartesian(xlabel="Year", ylabel="Horsepower", margin=75)
    axes.scatterplot(
        data["Year"],
        data["Horsepower"],
        color=(data["MPG"], colormap),
        size=8,
        mstyle={"stroke":"black", "stroke-opacity":0.3}
    )
    axes.color_scale(colormap, label="MPG");



.. raw:: html

    <div class="toyplot" id="t60c7041bd3014fd68d78afeb80dd302c" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tcdefd489dfd948c88adcb1e32b29971a" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="te6a54a52d6ee422187982594970b27ea"><clipPath id="td134533080ad4ea3bc7039bfbd6c9740"><rect height="270.0" width="470.0" x="65.0" y="65.0"></rect></clipPath><g clip-path="url(#td134533080ad4ea3bc7039bfbd6c9740)"><g class="toyplot-mark-Scatterplot" id="t1beabb6a6c6e4ac0ac4ef9690bfea24b"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 138.72549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 111.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 117.89215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 105.63725490196079)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 148.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 185.29411764705881)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 105.63725490196079)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 325.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 274.75490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 242.89215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 117.89215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 136.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 124.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(32.9%,18.8%,2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(75.0, 144.85294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 193.87254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 293.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 288.23529411764702)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 296.81372549019602)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 315.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 193.87254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 126.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 191.42156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 185.29411764705881)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 148.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 244.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 288.23529411764702)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 274.75490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 296.81372549019602)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(150.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 213.48039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 138.72549019607843)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 187.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 117.89215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 105.63725490196079)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 166.91176470588238)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 325.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 176.71568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 293.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 266.17647058823525)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 250.24509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 99.509803921568619)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 321.32352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 269.85294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 244.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 231.8627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(187.5, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 317.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 306.61764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 267.4019607843137)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(225.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 293.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 293.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 200.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 223.28431372549022)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 263.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 294.36274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 261.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(262.5, 316.42156862745099)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 282.10784313725492)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 284.55882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(64.2%,40.5%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 195.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 282.10784313725492)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.8%,84.9%,65.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 317.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 316.42156862745099)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 294.36274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.3%,89.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 293.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 256.37254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 249.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(300.0, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 298.03921568627447)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 310.29411764705884)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 263.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 261.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 173.03921568627453)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 148.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 198.77450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 272.30392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 304.16666666666663)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 279.65686274509807)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(337.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.4%,38.9%,35.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 322.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 300.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.9%,88%,85.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 317.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(19%,57.6%,54.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.2%,73.5%,45.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 211.02941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.4%,82%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.7%,78.1%,52.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.8%,64.7%,35%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 203.67647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.8%,58.6%,27.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 179.16666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 211.02941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 209.80392156862749)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 298.03921568627447)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.7%,94.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.2%,92.5%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.4%,79.3%,55%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 264.95098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.5%,87.7%,70.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.9%,90%,74.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 262.5)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.5%,76.2%,49.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 255.14705882352942)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 228.18627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,81.3%,58.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.2%,49%,16.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 218.38235294117646)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 294.36274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.0, 298.03921568627447)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.8%,72.8%,45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.3%,84.1%,63.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 222.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 223.28431372549022)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 212.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.5%,62%,31.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 215.93137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.2%,53.2%,20.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 191.42156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 207.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 228.18627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 197.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(75.5%,90.7%,88.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 294.36274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(47.2%,78.3%,73.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.5%,94%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 287.00980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 228.18627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 294.36274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(58.5%,83.8%,79.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.3%,82.9%,78.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.3%,91%,88.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(34.7%,69.2%,65.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 296.81372549019602)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(93.2%,95.4%,95.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.3%,94.9%,94.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.7%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 240.44117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.5, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(7.7%,46.8%,43.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 288.23529411764702)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(28.5%,64.7%,61.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74%,90.1%,87.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(35.5%,69.8%,65.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.2%,88.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.3%,77.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.5%,68.1%,39.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57.7%,83.5%,79.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 285.78431372549016)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.3%,92.1%,90.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.3%,89.8%,87.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,23.5%,18.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.6%,96%,95.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(11.5%,50.4%,47.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,33.6%,29.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 322.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,37.5%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 322.54901960784315)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(41.7%,74.3%,70.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,32.3%,28.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,85%,81.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 305.39215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.6%,88.3%,85.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 219.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.7%,89.6%,74%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0, 293.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 278.43137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 278.43137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.4%,85.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.2%,88.8%,72.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 278.43137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(20.7%,59.1%,56%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 310.29411764705884)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(21.4%,59.7%,56.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 302.94117647058823)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(51.8%,81.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 307.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.6%,89.5%,87%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(31.6%,67%,63.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 305.39215686274508)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 298.03921568627447)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.8%,82.3%,78%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 304.16666666666663)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57%,83.2%,79.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86%,93.7%,92.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 301.71568627450984)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 290.68627450980398)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(62.2%,85.3%,81.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.1%,87.7%,84.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 258.82352941176475)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(77.7%,91.6%,89.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 290.68627450980398)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.6%,95.7%,95.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 283.33333333333337)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(82.2%,92.8%,91.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 288.23529411764702)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 239.21568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.5%,91.2%,77.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 234.31372549019608)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.5%,84.5%,64.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 252.69607843137251)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.5, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 278.43137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 290.68627450980398)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 298.03921568627447)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 298.03921568627447)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 304.16666666666663)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 273.52941176470591)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 289.46078431372553)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 295.58823529411762)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 299.26470588235298)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 246.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 277.20588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 268.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 244.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 263.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 278.43137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 271.07843137254901)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 275.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,34.9%,31.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 317.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 278.43137254901961)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 284.55882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(525.0, 280.88235294117646)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t682d80336771467fab80bff8db969bb8" transform="translate(75.0,325.0)translate(0,10.0)"><line style="" x1="0" x2="450.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">70</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">74</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">78</text></g><g transform="translate(450.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">82</text></g></g><g transform="translate(225.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.008" y="10.266">Year</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t77154a0ecfe846199ba049a882085ff8" transform="translate(75.0,325.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="225.49019607843138" y1="0" y2="0"></line><g><g transform="translate(4.901960784313726,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.4408920985e-16">50</text></g><g transform="translate(66.17647058823529,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">100</text></g><g transform="translate(127.45098039215685,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">150</text></g><g transform="translate(188.72549019607843,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">200</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">250</text></g></g><g transform="translate(125.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-34.674" y="0.0">Horsepower</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="td2ef00ff0f0f4cf887431e33f73f071f"><clipPath id="td0733e11e3e840bfaf3e0dda7e484bb9"><rect height="20.0" width="250.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#td0733e11e3e840bfaf3e0dda7e484bb9)" transform="translate(545.0,325.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t5ca263e9634841a8bc8f91b8e9aaae8b"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t0f20133dd8204f62bc8bcf59757b5e24" x1="0.0" x2="229.26829268292684" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(32.9%,18.8%,1.96%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(36.4%,20.9%,2.27%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(39.9%,22.9%,2.58%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(43.4%,25%,2.89%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(46.9%,27%,3.21%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(50.4%,29.1%,3.52%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(53.9%,31.1%,3.83%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(57.1%,33.9%,5.45%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(60.3%,36.8%,7.63%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(63.5%,39.8%,9.8%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(66.6%,42.8%,12%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(69.8%,45.8%,14.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(73%,48.8%,16.3%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(75.7%,52.2%,19.6%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(77.7%,56.3%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(79.7%,60.3%,29.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(81.7%,64.3%,34.6%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(83.7%,68.4%,39.6%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(85.7%,72.4%,44.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(87.6%,76.3%,49.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(89%,78.7%,53.8%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(90.5%,81%,58.2%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(91.9%,83.4%,62.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(93.3%,85.8%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(94.8%,88.1%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(96.2%,90.5%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(96.4%,91.6%,79%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(96.4%,92.4%,82.1%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(96.3%,93.2%,85.2%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(96.2%,94.1%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(96.2%,94.9%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(96.1%,95.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(94.6%,95.7%,95.6%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(91.8%,95.1%,94.6%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(88.9%,94.4%,93.6%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(86.1%,93.7%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(83.2%,93%,91.6%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(80.3%,92.3%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(77.2%,91.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(72.7%,89.6%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(68.3%,87.8%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(63.9%,86%,82.6%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(59.5%,84.2%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(55.1%,82.4%,78.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(50.6%,80.6%,75.9%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(46%,77.4%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(41.3%,74%,69.8%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(36.7%,70.6%,66.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(32%,67.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(27.3%,63.9%,60.4%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(22.7%,60.6%,57.3%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(18.8%,57.4%,54.2%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(15.6%,54.3%,51.2%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(12.4%,51.3%,48.1%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(9.13%,48.2%,45.1%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(5.89%,45.2%,42%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(2.66%,42.1%,39%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(0.373%,39.2%,36%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(0.311%,36.6%,33.1%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(0.249%,34%,30.3%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(0.187%,31.4%,27.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(0.124%,28.8%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(0.0622%,26.1%,21.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(0%,23.5%,18.8%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t0f20133dd8204f62bc8bcf59757b5e24);stroke:none;stroke-width:1.0" width="229.26829268292684" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t47c48df053f54f86b4001dec02255c21" transform="translate(545.0,325.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="229.26829268292684" y1="0" y2="0"></line><g><g transform="translate(6.097560975609756,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(67.07317073170732,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(128.0487804878049,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(189.02439024390245,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g transform="translate(125.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.668" y="10.266">MPG</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t60c7041bd3014fd68d78afeb80dd302c";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tcdefd489dfd948c88adcb1e32b29971a";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t1beabb6a6c6e4ac0ac4ef9690bfea24b","data","scatterplot",["x", "y0"],[[70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0], [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0, 87.0, 90.0, 95.0, 113.0, 90.0, 215.0, 200.0, 210.0, 193.0, 88.0, 90.0, 95.0, 100.0, 105.0, 100.0, 88.0, 100.0, 165.0, 175.0, 153.0, 150.0, 180.0, 170.0, 175.0, 110.0, 72.0, 100.0, 88.0, 86.0, 90.0, 70.0, 76.0, 65.0, 69.0, 60.0, 70.0, 95.0, 80.0, 54.0, 90.0, 86.0, 165.0, 175.0, 150.0, 153.0, 150.0, 208.0, 155.0, 160.0, 190.0, 97.0, 150.0, 130.0, 140.0, 150.0, 112.0, 76.0, 87.0, 69.0, 86.0, 92.0, 97.0, 80.0, 88.0, 175.0, 150.0, 145.0, 137.0, 150.0, 198.0, 150.0, 158.0, 150.0, 215.0, 225.0, 175.0, 105.0, 100.0, 100.0, 88.0, 95.0, 46.0, 150.0, 167.0, 170.0, 180.0, 100.0, 88.0, 72.0, 94.0, 90.0, 85.0, 107.0, 90.0, 145.0, 230.0, 49.0, 75.0, 91.0, 112.0, 150.0, 110.0, 122.0, 180.0, 95.0, 100.0, 100.0, 67.0, 80.0, 65.0, 75.0, 100.0, 110.0, 105.0, 140.0, 150.0, 150.0, 140.0, 150.0, 83.0, 67.0, 78.0, 52.0, 61.0, 75.0, 75.0, 75.0, 97.0, 93.0, 67.0, 95.0, 105.0, 72.0, 72.0, 170.0, 145.0, 150.0, 148.0, 110.0, 105.0, 110.0, 95.0, 110.0, 110.0, 129.0, 75.0, 83.0, 100.0, 78.0, 96.0, 71.0, 97.0, 97.0, 70.0, 90.0, 95.0, 88.0, 98.0, 115.0, 53.0, 86.0, 81.0, 92.0, 79.0, 83.0, 140.0, 150.0, 120.0, 152.0, 100.0, 105.0, 81.0, 90.0, 52.0, 60.0, 70.0, 53.0, 100.0, 78.0, 110.0, 95.0, 71.0, 70.0, 75.0, 72.0, 102.0, 150.0, 88.0, 108.0, 120.0, 180.0, 145.0, 130.0, 150.0, 68.0, 80.0, 58.0, 96.0, 70.0, 145.0, 110.0, 145.0, 130.0, 110.0, 105.0, 100.0, 98.0, 180.0, 170.0, 190.0, 149.0, 78.0, 88.0, 75.0, 89.0, 63.0, 83.0, 67.0, 78.0, 97.0, 110.0, 110.0, 48.0, 66.0, 52.0, 70.0, 60.0, 110.0, 140.0, 139.0, 105.0, 95.0, 85.0, 88.0, 100.0, 90.0, 105.0, 85.0, 110.0, 120.0, 145.0, 165.0, 139.0, 140.0, 68.0, 95.0, 97.0, 75.0, 95.0, 105.0, 85.0, 97.0, 103.0, 125.0, 115.0, 133.0, 71.0, 68.0, 115.0, 85.0, 88.0, 90.0, 110.0, 130.0, 129.0, 138.0, 135.0, 155.0, 142.0, 125.0, 150.0, 71.0, 65.0, 80.0, 80.0, 77.0, 125.0, 71.0, 90.0, 70.0, 70.0, 65.0, 69.0, 90.0, 115.0, 115.0, 90.0, 76.0, 60.0, 70.0, 65.0, 90.0, 88.0, 90.0, 90.0, 78.0, 90.0, 75.0, 92.0, 75.0, 65.0, 105.0, 65.0, 48.0, 48.0, 67.0, 67.0, 67.0, 67.0, 62.0, 132.0, 100.0, 88.0, 72.0, 84.0, 84.0, 92.0, 110.0, 84.0, 58.0, 64.0, 60.0, 67.0, 65.0, 62.0, 68.0, 63.0, 65.0, 65.0, 74.0, 75.0, 75.0, 100.0, 74.0, 80.0, 76.0, 116.0, 120.0, 110.0, 105.0, 88.0, 85.0, 88.0, 88.0, 88.0, 85.0, 84.0, 90.0, 92.0, 74.0, 68.0, 68.0, 63.0, 70.0, 88.0, 75.0, 70.0, 67.0, 67.0, 67.0, 110.0, 85.0, 92.0, 112.0, 96.0, 84.0, 90.0, 86.0, 52.0, 84.0, 79.0, 82.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t682d80336771467fab80bff8db969bb8",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 82.0, "min": 70.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 450.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t77154a0ecfe846199ba049a882085ff8",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 46.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t47c48df053f54f86b4001dec02255c21",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 9.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that a colormap must be explicitly specified when creating a color
scale - this is necessary to avoid ambiguity when a single coordinate
system contains multiple visualizations or data series.

Canvas Color Scales
-------------------

For situations where displaying a vertical color scale with a single set
of Cartesian axes is too limiting, you can add horizontal color scales
directly to a canvas using any :ref:`canvas-layout` that makes sense.
For example, the following figure uses a single horizontal color scale
to display a colormap that is shared between two coordinate systems:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=400)
    
    axes = canvas.cartesian(bounds=("10%", "45%", "10%", "65%"), xlabel="Year", ylabel="Horsepower")
    axes.scatterplot(
        data["Year"],
        data["Horsepower"],
        color=(data["MPG"], colormap),
        size=8,
        mstyle={"stroke":"black", "stroke-opacity":0.3}
    )
    
    axes = canvas.cartesian(bounds=("-45%", "-10%", "10%", "65%"), xlabel="Weight", ylabel="Horsepower")
    axes.y.spine.position="high"
    axes.scatterplot(
        data["Weight"],
        data["Horsepower"],
        color=(data["MPG"], colormap),
        size=8,
        mstyle={"stroke":"black", "stroke-opacity":0.3}
    )
    
    canvas.color_scale(colormap, bounds=("10%", "-10%", "75%", "90%"), label="MPG");




.. raw:: html

    <div class="toyplot" id="t86f05362da214929a53fd53fd19880c8" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t2f8fd176e7de4884a49d46f26f573787" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 400.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t4030c4bfb4164ab891036e1405839a10"><clipPath id="t3198ac0bba6e4247a104bdbc6937e520"><rect height="240.0" width="230.0" x="50.0" y="30.0"></rect></clipPath><g clip-path="url(#t3198ac0bba6e4247a104bdbc6937e520)"><g class="toyplot-mark-Scatterplot" id="t4ca2c193cac345ff8da8956bd37974cb"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 96.078431372549005)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 72.352941176470594)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 77.745098039215677)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 66.960784313725497)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 66.960784313725497)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 215.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 187.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 77.745098039215677)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 93.921568627450995)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 83.137254901960773)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(32.9%,18.8%,2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(60.0, 101.47058823529413)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 144.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(77.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 251.37254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 144.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 85.294117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 215.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(95.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 161.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 96.078431372549005)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 139.21568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 77.745098039215677)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 66.960784313725497)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 129.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 208.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 194.21568627450981)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 61.568627450980387)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 256.76470588235293)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 211.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 178.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(112.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 243.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 209.31372549019611)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(130.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 150.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(147.5, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 222.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(64.2%,40.5%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 145.68627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 222.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.8%,84.9%,65.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.3%,89.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 199.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 193.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(165.0, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 148.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 213.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(182.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.4%,38.9%,35.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 238.43137254901958)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.9%,88%,85.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(19%,57.6%,54.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.2%,73.5%,45.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.4%,82%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.7%,78.1%,52.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.8%,64.7%,35%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.8%,58.6%,27.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.7%,94.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.2%,92.5%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.4%,79.3%,55%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.5%,87.7%,70.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.9%,90%,74.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.5%,76.2%,49.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 198.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,81.3%,58.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.2%,49%,16.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 166.17647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(200.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.8%,72.8%,45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.3%,84.1%,63.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.5%,62%,31.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 164.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.2%,53.2%,20.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 156.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(75.5%,90.7%,88.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(47.2%,78.3%,73.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.5%,94%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 226.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(58.5%,83.8%,79.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.3%,82.9%,78.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.3%,91%,88.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(34.7%,69.2%,65.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(93.2%,95.4%,95.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.3%,94.9%,94.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.7%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(217.5, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(7.7%,46.8%,43.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(28.5%,64.7%,61.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74%,90.1%,87.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(35.5%,69.8%,65.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.2%,88.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.3%,77.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.5%,68.1%,39.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57.7%,83.5%,79.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.3%,92.1%,90.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.3%,89.8%,87.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,23.5%,18.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.6%,96%,95.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(11.5%,50.4%,47.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,33.6%,29.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,37.5%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(41.7%,74.3%,70.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,32.3%,28.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,85%,81.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 242.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.6%,88.3%,85.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 167.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.7%,89.6%,74%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(235.0, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.4%,85.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.2%,88.8%,72.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(20.7%,59.1%,56%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(21.4%,59.7%,56.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 240.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(51.8%,81.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.6%,89.5%,87%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(31.6%,67%,63.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 242.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.8%,82.3%,78%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57%,83.2%,79.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86%,93.7%,92.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(62.2%,85.3%,81.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.1%,87.7%,84.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(77.7%,91.6%,89.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.6%,95.7%,95.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(82.2%,92.8%,91.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 184.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.5%,91.2%,77.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.5%,84.5%,64.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(252.5, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,34.9%,31.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(270.0, 221.17647058823528)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t70b899b9d04746399db170b5a0b95dda" transform="translate(60.0,260.0)translate(0,10.0)"><line style="" x1="0" x2="210.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">70</text></g><g transform="translate(70.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">74</text></g><g transform="translate(140.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">78</text></g><g transform="translate(210.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">82</text></g></g><g transform="translate(105.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.008" y="10.266">Year</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t7350c81b498c4ceb9a8168ab2bd676f5" transform="translate(60.0,260.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="198.4313725490196" y1="0" y2="0"></line><g><g transform="translate(4.313725490196078,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.4408920985e-16">50</text></g><g transform="translate(58.23529411764706,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">100</text></g><g transform="translate(112.15686274509804,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">150</text></g><g transform="translate(166.078431372549,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">200</text></g><g transform="translate(220.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">250</text></g></g><g transform="translate(110.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-34.674" y="0.0">Horsepower</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t64a9d9a5d2d746b985f63ecd561b70e9"><clipPath id="t36e19be8e4014fa5a9db30ae550c0636"><rect height="240.0" width="230.0" x="320.0" y="30.0"></rect></clipPath><g clip-path="url(#t36e19be8e4014fa5a9db30ae550c0636)"><g class="toyplot-mark-Scatterplot" id="td4ebf43524c34ad6931ae4790a68aeaa"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(442.59143748227956, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(453.84462716189392, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.54267082506379, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.36404876665722, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(439.31669974482566, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(492.42699177771476, 96.078431372549005)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(493.20102069747662, 72.352941176470594)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(490.70031187978452, 77.745098039215677)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(497.42840941309896, 66.960784313725497)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(463.19251488517153, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(446.1043379642756, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(448.84320952650978, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(457.89339381910975, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(417.70343067762974, 66.960784313725497)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.19138077686421, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(402.63963708534163, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(399.12673660334565, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.99262829600224, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.78253473206689, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.2180323220868, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(393.053586617522, 215.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(378.64474057272469, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.37000283527072, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.97476609016155, 187.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(391.62461015026935, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(508.74113977884889, 77.745098039215677)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(38.8%,22.3%,2.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(494.51091579245815, 93.921568627450995)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(494.86815990927136, 83.137254901960773)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(32.9%,18.8%,2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(515.70740005670541, 101.47058823529413)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.78253473206689, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.76098667422741, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.61752197334846, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.79104054437198, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.72129288347037, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(432.1718174085625, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(430.56421888290333, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(429.73064927700591, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(484.56762120782531, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.75049617238443, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(481.29288347037141, 144.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(477.83952367451093, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(528.98497306492766, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(516.54096966260272, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(540.0, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(410.32038559682451, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(377.3348454777431, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(429.37340516019276, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(420.85908704281258, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.14119648426424, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.36574992911824, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(357.44825630847743, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.91239013325776, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(339.52650978168413, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(330.0, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.15849163595124, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.36291465834989, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(369.59455628012478, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.54437198752481, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.16557981287212, 251.37254901960785)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(377.3348454777431, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.49844060107739, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(488.43776580663456, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(495.04678196767793, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(480.16161043379645, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(479.80436631698325, 144.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(452.5942727530479, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(509.81287212928834, 85.294117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(502.01304224553439, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.27417068330021, 137.05882352941177)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(497.24978735469233, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(372.69067195917211, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(465.69322370286363, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(477.958605046782, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(489.62857952934507, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(476.70825063793592, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(408.59370569889427, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(383.46753614970225, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(411.33257726112845, 215.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.29543521406293, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.5608165579813, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.18996314148001, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(383.16983271902467, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.80691806067483, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(358.99631414800109, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(478.07768641905307, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(452.5942727530479, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(471.40912957187413, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(474.62432662319247, 161.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(458.84604479727813, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(528.80635100652114, 96.078431372549005)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.75049617238443, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(493.73688687269635, 139.21568627450978)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(486.23476041962005, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(515.88602211511204, 77.745098039215677)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(528.74681032038563, 66.960784313725497)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(461.46583498724129, 120.88235294117648)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(419.78735469237313, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(429.13524241565074, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.30819393252057, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(413.83328607882049, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.86702580096397, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.06521122767225, 260.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(531.48568188261982, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(526.06747944428696, 129.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(511.06322653813442, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(50.5%,29.1%,3.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(501.83442018712788, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.01984689537846, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(369.65409696626028, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.91806067479445, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.60816557981286, 208.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.42529061525374, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(371.49985823646159, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(381.14544939041679, 194.21568627450981)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.82052736036292, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(477.00595406861356, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(488.67592855117664, 61.568627450980387)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(345.12333427842361, 256.76470588235293)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.44967394386163, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.69492486532465, 211.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(404.72356110008508, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(436.33966543804934, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.3390983838957, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(401.09157924581797, 178.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.6%,25.7%,3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(452.11794726396369, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(418.65608165579818, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.6884037425574, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(432.58860221151122, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.06521122767225, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(379.89509498157076, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.27757300822225, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(385.31329741990362, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(459.08420754182021, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.21264530762687, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(449.08137227105186, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(480.51885455060955, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(513.74255741423303, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(499.33371136943578, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(510.11057555996598, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(487.42557414233062, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.08165579812874, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.83924014743405, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.90445137510631, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(332.14346470087895, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(353.22086759285509, 243.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.48483130138925, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(359.47263963708531, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(367.68925432378791, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(382.15764105472073, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.32265381343916, 209.31372549019611)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(353.04224553444857, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(428.30167280975331, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(439.91210660618094, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.30450808052171, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(421.99036007938759, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(511.89679614403173, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(498.32151970513183, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(501.77487950099231, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,38%,8.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(511.24184859654099, 150.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(466.58633399489651, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(465.99092713354128, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(456.04763254890844, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(459.32237028636234, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.2%,78.9%,54.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(414.90501842925994, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(425.74142330592576, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(422.64530762687838, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(363.22370286362343, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(391.08874397504962, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(407.46243266231926, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(388.29033172667994, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(394.83980720158775, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.31981854267082, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(385.49191947831014, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(411.63028069180609, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.29118230791045, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(425.14601644457042, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(394.36348171250359, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(410.02268216614686, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.30819393252057, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.99404593138649, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(340.83640487666571, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(380.66912390133257, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.14119648426424, 222.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.09951800396937, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.22512049900763, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.06946413382479, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(484.92486532463852, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(483.43634817125036, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(469.86107173235041, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(64.2%,40.5%,10.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(484.92486532463852, 145.68627450980392)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(426.45591153955201, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(433.6007938758151, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(413.29741990360083, 222.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.8%,84.9%,65.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(417.64388999149418, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(355.12616954919201, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.80691806067483, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.29118230791045, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(340.83640487666571, 252.45098039215688)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(451.34391834420194, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.8%,60.6%,30%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(446.75928551176639, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.98667422738873, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(424.07428409413097, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(342.62262546073151, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.44683867309328, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.27105188545505, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.3%,89.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(386.68273320102071, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,74.2%,46.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(421.51403459030337, 199.60784313725489)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(468.55117663736888, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(428.65891692656646, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(408.41508364048764, 193.13725490196077)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(461.40629430110573, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(494.74907853700029, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(475.39835554295439, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(464.38332860788205, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.2%,33%,4.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(457.5361497022966, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(355.72157641054719, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.27105188545505, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(342.62262546073151, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.90445137510631, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.76750779699461, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(464.97873546923734, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(475.69605897363198, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(480.45931386447404, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(66.8%,43%,12.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(489.68812021548058, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(443.54408846044794, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.88772327757306, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.2%,67.4%,38.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(450.0935639353558, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(443.84179189112558, 203.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(485.2225687553161, 115.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(481.9478310178622, 126.27450980392157)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(491.47434079954633, 104.70588235294116)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.1%,48%,15.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(492.06974766090161, 148.92156862745097)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(349.46980436631696, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.6%,78.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(397.10235327473777, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.82052736036292, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93%,84.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(397.99546356677064, 213.62745098039215)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.07882052736039, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(357.50779699461299, 220.09803921568627)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.1%,93%,91.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.3549759001985, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(401.56790473490219, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(388.7666572157641, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.91153955202719, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.4%,38.9%,35.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(341.13410830734335, 238.43137254901958)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.9%,88%,85.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(19%,57.6%,54.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(357.21009356393535, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.1%,76%,71.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(341.13410830734335, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.2%,73.5%,45.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(434.31528210944145, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(456.34533597958603, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(446.52112276722431, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(444.43719875248087, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(421.81173802098101, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(410.49900765523103, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.4%,82%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.91153955202719, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88%,77%,50.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(438.1854267082507, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(84.5%,70.1%,41.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(425.08647575843497, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(435.20839240147433, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.7%,78.1%,52.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(416.7507796994613, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.8%,64.7%,35%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(449.49815707400057, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(436.99461298554013, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.88772327757306, 153.23529411764704)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.8%,58.6%,27.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(439.07853700028352, 131.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.2%,61.3%,30.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(424.78877232775727, 159.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.2%,57.2%,25.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(476.88687269634255, 158.62745098039218)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.27105188545505, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.7%,94.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(386.38502977034307, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.90445137510631, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.2%,92.5%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(366.73660334561953, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(89.4%,79.3%,55%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(383.70569889424439, 207.15686274509801)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.5%,87.7%,70.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(397.40005670541541, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.9%,90%,74.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(403.94953218032322, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(377.15622341933658, 205.0)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.5%,76.2%,49.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(402.46101502693506, 198.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(420.91862772894808, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,81.3%,58.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.37709101219167, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.2%,49%,16.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(436.99461298554013, 166.17647058823528)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.3%,91.8%,89.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.44683867309328, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.9%,94.1%,93.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.08023816274454, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.4%,80.9%,57.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(427.17039977317836, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.8%,72.8%,45%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(411.98752480861924, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.3%,84.1%,63.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.03345619506661, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(428.36121349588888, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(88.2%,77.3%,51.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(434.01757867876381, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.5%,53.8%,21.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(462.59710802381625, 169.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(455.7499291182308, 170.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,50.5%,17.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(469.44428692940176, 160.78431372549019)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.5%,62%,31.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(462.00170116246102, 164.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.2%,53.2%,20.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(493.55826481428977, 142.45098039215685)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.5%,45.5%,13.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(475.33881485681889, 156.47058823529412)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.8%,68.8%,40%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(448.60504678196764, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(81.5%,64%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(468.55117663736888, 147.84313725490199)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(75.5%,90.7%,88.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(348.57669407428409, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.55372838106041, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(47.2%,78.3%,73.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(347.98128721292886, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.5%,94%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.93450524525088, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(444.13949532180322, 226.56862745098039)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94%,86.9%,68.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(466.16954919194779, 174.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(423.8956620357244, 233.0392156862745)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,90.4%,75.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.59001984689536, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(58.5%,83.8%,79.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.95038276155367, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(56.3%,82.9%,78.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.97334845477741, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(76.3%,91%,88.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(354.23305925715903, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(34.7%,69.2%,65.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.78253473206689, 235.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(93.2%,95.4%,95.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.93450524525088, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.3%,94.9%,94.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(388.46895378508646, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.7%,90.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(394.72072582931673, 185.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(63.7%,85.9%,82.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(386.14686702580093, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(7.7%,46.8%,43.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.61610433796432, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(28.5%,64.7%,61.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.1369435781117, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74%,90.1%,87.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.18712787071161, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(35.5%,69.8%,65.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(354.17351857102352, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(393.41083073433515, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.2%,88.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(404.84264247235609, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,91.3%,77.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(412.76155372838105, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(83.5%,68.1%,39.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(435.26793308760989, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57.7%,83.5%,79.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.23589452792737, 225.49019607843138)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.37567337680753, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(79.3%,92.1%,90.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(385.31329741990362, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(378.88290331726677, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(73.3%,89.8%,87.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(368.82052736036292, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0%,23.5%,18.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(359.59172100935643, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.6%,96%,95.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.67479444286926, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(11.5%,50.4%,47.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(359.59172100935643, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,33.6%,29.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(358.10320385596827, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,37.5%,34.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(372.98837538984969, 257.84313725490193)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(41.7%,74.3%,70.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.60589736319815, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(427.468103203856, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.2%,32.3%,28.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(344.11114261411967, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(61.5%,85%,81.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(361.67564502409982, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86.5%,93.8%,92.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(343.81343918344197, 242.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(69.6%,88.3%,85.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(407.22426991777712, 167.25490196078431)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.7%,89.6%,74%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(378.04933371136946, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(52.6%,81.4%,76.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(382.81258860221152, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.30904451375108, 231.9607843137255)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.1%,95.3%,92.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(382.21718174085629, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.85058123050749, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.4%,85.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(389.95747093847461, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.2%,88.8%,72.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(396.20924298270484, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(85.5%,93.6%,92.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.96540969662601, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(20.7%,59.1%,56%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(338.45477743124468, 247.05882352941174)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(21.4%,59.7%,56.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(345.59965976750777, 240.58823529411765)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(51.8%,81.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(338.75248086192227, 244.90196078431373)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(72.6%,89.5%,87%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.91239013325776, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.55372838106041, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(31.6%,67%,63.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(356.01927984122483, 242.74509803921569)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(59.2%,84.1%,80.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.14913524241564, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(54.8%,82.3%,78%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.8434930535866, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(57%,83.2%,79.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(355.72157641054719, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(86%,93.7%,92.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.66770626594837, 239.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(67.4%,87.4%,84.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(364.3549759001985, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(62.2%,85.3%,81.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.54578962290901, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(71.8%,89.2%,86.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(373.88148568188262, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(68.1%,87.7%,84.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(389.65976750779697, 201.76470588235296)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(77.7%,91.6%,89.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.85058123050749, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(94.6%,95.7%,95.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(426.27728948114543, 223.33333333333334)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(82.2%,92.8%,91.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(422.10944145165865, 227.64705882352939)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,92.8%,83.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(406.62886305642189, 184.50980392156862)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.5%,91.2%,77.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(408.41508364048764, 180.19607843137254)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(92.5%,84.5%,64.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(437.29231641621777, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,94.5%,89.8%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(455.7499291182308, 196.37254901960782)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(87.2%,75.5%,48.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(416.15537283810602, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(78.5%,57.9%,26.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(440.26935072299409, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(389.06436064644174, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(391.14828466118513, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(376.5608165579813, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.27814006237594, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.3%,94.7%,94.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(384.30110575559968, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(396.80464984406012, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,90.8%,76.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(404.5449390416785, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.85143181173805, 229.80392156862746)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(37.1%,70.9%,66.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(354.53076268783667, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(351.25602495038277, 236.27450980392155)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.48483130138925, 241.66666666666666)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.48483130138925, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(362.56875531613269, 214.70588235294122)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(365.24808619223131, 228.72549019607845)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(60%,84.4%,80.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(367.6297136376524, 234.11764705882354)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.95832151970512, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(350.95832151970512, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(352.74454210377093, 237.35294117647061)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.4%,92.3%,81.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.30819393252057, 190.98039215686276)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(29.2%,65.3%,61.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(413.47604196200734, 217.94117647058826)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.3%,93.6%,86.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(387.87354692373117, 210.39215686274511)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(91.6%,82.9%,61.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(402.7587184576127, 188.82352941176472)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(392.63680181457329, 206.07843137254903)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(44.9%,76.6%,72.1%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(375.07229940459314, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(409.60589736319815, 212.54901960784312)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(96.2%,95%,91.9%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(400.07938758151403, 216.86274509803923)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(0.3%,34.9%,31.3%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(360.78253473206689, 253.52941176470588)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(74.8%,90.4%,88.2%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(370.60674794442866, 219.01960784313724)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(95.1%,95.8%,95.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(390.25517436915226, 224.41176470588235)"><circle r="4.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(80.7%,92.4%,90.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:0.3" transform="translate(395.91153955202719, 221.17647058823528)"><circle r="4.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t562cb4373a1148b5b38fae91bf8bb0a2" transform="translate(330.0,260.0)translate(0,10.0)"><line style="" x1="0" x2="210.0" y1="0" y2="0"></line><g><g transform="translate(23.04224553444854,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">2000</text></g><g transform="translate(82.58293166997449,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">3000</text></g><g transform="translate(142.12361780550043,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">4000</text></g><g transform="translate(201.66430394102636,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-11.12" y="8.555">5000</text></g></g><g transform="translate(105.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-19.998" y="10.266">Weight</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="te7acba3af2c8434fb6f86d8f605564a0" transform="translate(540.0,260.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="198.4313725490196" y1="0" y2="0"></line><g><g transform="translate(4.313725490196078,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g><g transform="translate(58.23529411764706,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">100</text></g><g transform="translate(112.15686274509804,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">150</text></g><g transform="translate(166.078431372549,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">200</text></g><g transform="translate(220.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">250</text></g></g><g transform="translate(110.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-34.674" y="10.266">Horsepower</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="td86b7042433a47ab964026a50e2f509d"><clipPath id="t1c2c9af6d76741748612ffce2b2e4d5a"><rect height="20.0" width="480.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t1c2c9af6d76741748612ffce2b2e4d5a)" transform="translate(60.0,330.0)"><g class="toyplot-color-Map" id="t48355dae897d47e2a26b4d76d5147327"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tea0e93d9050d4973a3c43dab2377574c" x1="0.0" x2="440.19512195121951" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(32.9%,18.8%,1.96%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(36.4%,20.9%,2.27%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(39.9%,22.9%,2.58%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(43.4%,25%,2.89%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(46.9%,27%,3.21%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(50.4%,29.1%,3.52%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(53.9%,31.1%,3.83%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(57.1%,33.9%,5.45%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(60.3%,36.8%,7.63%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(63.5%,39.8%,9.8%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(66.6%,42.8%,12%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(69.8%,45.8%,14.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(73%,48.8%,16.3%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(75.7%,52.2%,19.6%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(77.7%,56.3%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(79.7%,60.3%,29.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(81.7%,64.3%,34.6%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(83.7%,68.4%,39.6%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(85.7%,72.4%,44.5%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(87.6%,76.3%,49.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(89%,78.7%,53.8%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(90.5%,81%,58.2%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(91.9%,83.4%,62.5%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(93.3%,85.8%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(94.8%,88.1%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(96.2%,90.5%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(96.4%,91.6%,79%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(96.4%,92.4%,82.1%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(96.3%,93.2%,85.2%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(96.2%,94.1%,88.3%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(96.2%,94.9%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(96.1%,95.7%,94.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(94.6%,95.7%,95.6%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(91.8%,95.1%,94.6%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(88.9%,94.4%,93.6%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(86.1%,93.7%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(83.2%,93%,91.6%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(80.3%,92.3%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(77.2%,91.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(72.7%,89.6%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(68.3%,87.8%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(63.9%,86%,82.6%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(59.5%,84.2%,80.4%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(55.1%,82.4%,78.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(50.6%,80.6%,75.9%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(46%,77.4%,72.9%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(41.3%,74%,69.8%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(36.7%,70.6%,66.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(32%,67.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(27.3%,63.9%,60.4%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(22.7%,60.6%,57.3%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(18.8%,57.4%,54.2%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(15.6%,54.3%,51.2%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(12.4%,51.3%,48.1%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(9.13%,48.2%,45.1%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(5.89%,45.2%,42%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(2.66%,42.1%,39%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(0.373%,39.2%,36%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(0.311%,36.6%,33.1%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(0.249%,34%,30.3%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(0.187%,31.4%,27.4%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(0.124%,28.8%,24.6%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(0.0622%,26.1%,21.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(0%,23.5%,18.8%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tea0e93d9050d4973a3c43dab2377574c);stroke:none;stroke-width:1.0" width="440.19512195121951" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="tcae9f78f95b9439fae5d79c759b394fa" transform="translate(60.0,330.0)translate(0,10.0)"><line style="" x1="0" x2="440.1951219512195" y1="0" y2="0"></line><g><g transform="translate(11.707317073170731,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(128.78048780487805,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(245.85365853658539,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(362.9268292682927,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(480.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g transform="translate(240.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-13.668" y="10.266">MPG</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t86f05362da214929a53fd53fd19880c8";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t2f8fd176e7de4884a49d46f26f573787";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t4ca2c193cac345ff8da8956bd37974cb","data","scatterplot",["x", "y0"],[[70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 71.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 72.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 73.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 74.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 75.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 76.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 77.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 78.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 79.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 80.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 81.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0, 82.0], [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0, 87.0, 90.0, 95.0, 113.0, 90.0, 215.0, 200.0, 210.0, 193.0, 88.0, 90.0, 95.0, 100.0, 105.0, 100.0, 88.0, 100.0, 165.0, 175.0, 153.0, 150.0, 180.0, 170.0, 175.0, 110.0, 72.0, 100.0, 88.0, 86.0, 90.0, 70.0, 76.0, 65.0, 69.0, 60.0, 70.0, 95.0, 80.0, 54.0, 90.0, 86.0, 165.0, 175.0, 150.0, 153.0, 150.0, 208.0, 155.0, 160.0, 190.0, 97.0, 150.0, 130.0, 140.0, 150.0, 112.0, 76.0, 87.0, 69.0, 86.0, 92.0, 97.0, 80.0, 88.0, 175.0, 150.0, 145.0, 137.0, 150.0, 198.0, 150.0, 158.0, 150.0, 215.0, 225.0, 175.0, 105.0, 100.0, 100.0, 88.0, 95.0, 46.0, 150.0, 167.0, 170.0, 180.0, 100.0, 88.0, 72.0, 94.0, 90.0, 85.0, 107.0, 90.0, 145.0, 230.0, 49.0, 75.0, 91.0, 112.0, 150.0, 110.0, 122.0, 180.0, 95.0, 100.0, 100.0, 67.0, 80.0, 65.0, 75.0, 100.0, 110.0, 105.0, 140.0, 150.0, 150.0, 140.0, 150.0, 83.0, 67.0, 78.0, 52.0, 61.0, 75.0, 75.0, 75.0, 97.0, 93.0, 67.0, 95.0, 105.0, 72.0, 72.0, 170.0, 145.0, 150.0, 148.0, 110.0, 105.0, 110.0, 95.0, 110.0, 110.0, 129.0, 75.0, 83.0, 100.0, 78.0, 96.0, 71.0, 97.0, 97.0, 70.0, 90.0, 95.0, 88.0, 98.0, 115.0, 53.0, 86.0, 81.0, 92.0, 79.0, 83.0, 140.0, 150.0, 120.0, 152.0, 100.0, 105.0, 81.0, 90.0, 52.0, 60.0, 70.0, 53.0, 100.0, 78.0, 110.0, 95.0, 71.0, 70.0, 75.0, 72.0, 102.0, 150.0, 88.0, 108.0, 120.0, 180.0, 145.0, 130.0, 150.0, 68.0, 80.0, 58.0, 96.0, 70.0, 145.0, 110.0, 145.0, 130.0, 110.0, 105.0, 100.0, 98.0, 180.0, 170.0, 190.0, 149.0, 78.0, 88.0, 75.0, 89.0, 63.0, 83.0, 67.0, 78.0, 97.0, 110.0, 110.0, 48.0, 66.0, 52.0, 70.0, 60.0, 110.0, 140.0, 139.0, 105.0, 95.0, 85.0, 88.0, 100.0, 90.0, 105.0, 85.0, 110.0, 120.0, 145.0, 165.0, 139.0, 140.0, 68.0, 95.0, 97.0, 75.0, 95.0, 105.0, 85.0, 97.0, 103.0, 125.0, 115.0, 133.0, 71.0, 68.0, 115.0, 85.0, 88.0, 90.0, 110.0, 130.0, 129.0, 138.0, 135.0, 155.0, 142.0, 125.0, 150.0, 71.0, 65.0, 80.0, 80.0, 77.0, 125.0, 71.0, 90.0, 70.0, 70.0, 65.0, 69.0, 90.0, 115.0, 115.0, 90.0, 76.0, 60.0, 70.0, 65.0, 90.0, 88.0, 90.0, 90.0, 78.0, 90.0, 75.0, 92.0, 75.0, 65.0, 105.0, 65.0, 48.0, 48.0, 67.0, 67.0, 67.0, 67.0, 62.0, 132.0, 100.0, 88.0, 72.0, 84.0, 84.0, 92.0, 110.0, 84.0, 58.0, 64.0, 60.0, 67.0, 65.0, 62.0, 68.0, 63.0, 65.0, 65.0, 74.0, 75.0, 75.0, 100.0, 74.0, 80.0, 76.0, 116.0, 120.0, 110.0, 105.0, 88.0, 85.0, 88.0, 88.0, 88.0, 85.0, 84.0, 90.0, 92.0, 74.0, 68.0, 68.0, 63.0, 70.0, 88.0, 75.0, 70.0, 67.0, 67.0, 67.0, 110.0, 85.0, 92.0, 112.0, 96.0, 84.0, 90.0, 86.0, 52.0, 84.0, 79.0, 82.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t70b899b9d04746399db170b5a0b95dda",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 82.0, "min": 70.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 210.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t7350c81b498c4ceb9a8168ab2bd676f5",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 46.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 220.0, "min": 0.0}, "scale": "linear"}]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"td4ebf43524c34ad6931ae4790a68aeaa","data","scatterplot",["x", "y0"],[[3504.0, 3693.0, 3436.0, 3433.0, 3449.0, 4341.0, 4354.0, 4312.0, 4425.0, 3850.0, 3563.0, 3609.0, 3761.0, 3086.0, 2372.0, 2833.0, 2774.0, 2587.0, 2130.0, 1835.0, 2672.0, 2430.0, 2375.0, 2234.0, 2648.0, 4615.0, 4376.0, 4382.0, 4732.0, 2130.0, 2264.0, 2228.0, 2634.0, 3439.0, 3329.0, 3302.0, 3288.0, 4209.0, 4464.0, 4154.0, 4096.0, 4955.0, 4746.0, 5140.0, 2962.0, 2408.0, 3282.0, 3139.0, 2220.0, 2123.0, 2074.0, 2065.0, 1773.0, 1613.0, 1834.0, 1955.0, 2278.0, 2126.0, 2254.0, 2408.0, 2226.0, 4274.0, 4385.0, 4135.0, 4129.0, 3672.0, 4633.0, 4502.0, 4456.0, 4422.0, 2330.0, 3892.0, 4098.0, 4294.0, 4077.0, 2933.0, 2511.0, 2979.0, 2189.0, 2395.0, 2288.0, 2506.0, 2164.0, 2100.0, 4100.0, 3672.0, 3988.0, 4042.0, 3777.0, 4952.0, 4464.0, 4363.0, 4237.0, 4735.0, 4951.0, 3821.0, 3121.0, 3278.0, 2945.0, 3021.0, 2904.0, 1950.0, 4997.0, 4906.0, 4654.0, 4499.0, 2789.0, 2279.0, 2401.0, 2379.0, 2124.0, 2310.0, 2472.0, 2265.0, 4082.0, 4278.0, 1867.0, 2158.0, 2582.0, 2868.0, 3399.0, 2660.0, 2807.0, 3664.0, 3102.0, 2901.0, 3336.0, 1950.0, 2451.0, 1836.0, 2542.0, 3781.0, 3632.0, 3613.0, 4141.0, 4699.0, 4457.0, 4638.0, 4257.0, 2219.0, 1963.0, 2300.0, 1649.0, 2003.0, 2125.0, 2108.0, 2246.0, 2489.0, 2391.0, 2000.0, 3264.0, 3459.0, 3432.0, 3158.0, 4668.0, 4440.0, 4498.0, 4657.0, 3907.0, 3897.0, 3730.0, 3785.0, 3039.0, 3221.0, 3169.0, 2171.0, 2639.0, 2914.0, 2592.0, 2702.0, 2223.0, 2545.0, 2984.0, 1937.0, 3211.0, 2694.0, 2957.0, 2945.0, 2671.0, 1795.0, 2464.0, 2220.0, 2572.0, 2255.0, 2202.0, 4215.0, 4190.0, 3962.0, 4215.0, 3233.0, 3353.0, 3012.0, 3085.0, 2035.0, 2164.0, 1937.0, 1795.0, 3651.0, 3574.0, 3645.0, 3193.0, 1825.0, 1990.0, 2155.0, 2565.0, 3150.0, 3940.0, 3270.0, 2930.0, 3820.0, 4380.0, 4055.0, 3870.0, 3755.0, 2045.0, 2155.0, 1825.0, 2300.0, 1945.0, 3880.0, 4060.0, 4140.0, 4295.0, 3520.0, 3425.0, 3630.0, 3525.0, 4220.0, 4165.0, 4325.0, 4335.0, 1940.0, 2740.0, 2265.0, 2755.0, 2051.0, 2075.0, 1985.0, 2190.0, 2815.0, 2600.0, 2720.0, 1985.0, 1800.0, 1985.0, 2070.0, 1800.0, 3365.0, 3735.0, 3570.0, 3535.0, 3155.0, 2965.0, 2720.0, 3430.0, 3210.0, 3380.0, 3070.0, 3620.0, 3410.0, 3425.0, 3445.0, 3205.0, 4080.0, 2155.0, 2560.0, 2300.0, 2230.0, 2515.0, 2745.0, 2855.0, 2405.0, 2830.0, 3140.0, 2795.0, 3410.0, 1990.0, 2135.0, 3245.0, 2990.0, 2890.0, 3265.0, 3360.0, 3840.0, 3725.0, 3955.0, 3830.0, 4360.0, 4054.0, 3605.0, 3940.0, 1925.0, 1975.0, 1915.0, 2670.0, 3530.0, 3900.0, 3190.0, 3420.0, 2200.0, 2150.0, 2020.0, 2130.0, 2670.0, 2595.0, 2700.0, 2556.0, 2144.0, 1968.0, 2120.0, 2019.0, 2678.0, 2870.0, 3003.0, 3381.0, 2188.0, 2711.0, 2542.0, 2434.0, 2265.0, 2110.0, 2800.0, 2110.0, 2085.0, 2335.0, 2950.0, 3250.0, 1850.0, 2145.0, 1845.0, 2910.0, 2420.0, 2500.0, 2290.0, 2490.0, 2635.0, 2620.0, 2725.0, 2385.0, 1755.0, 1875.0, 1760.0, 2065.0, 1975.0, 2050.0, 1985.0, 2215.0, 2045.0, 2380.0, 2190.0, 2210.0, 2350.0, 2615.0, 2635.0, 3230.0, 3160.0, 2900.0, 2930.0, 3415.0, 3725.0, 3060.0, 3465.0, 2605.0, 2640.0, 2395.0, 2575.0, 2525.0, 2735.0, 2865.0, 1980.0, 2025.0, 1970.0, 2125.0, 2125.0, 2160.0, 2205.0, 2245.0, 1965.0, 1965.0, 1995.0, 2945.0, 3015.0, 2585.0, 2835.0, 2665.0, 2370.0, 2950.0, 2790.0, 2130.0, 2295.0, 2625.0, 2720.0], [130.0, 165.0, 150.0, 150.0, 140.0, 198.0, 220.0, 215.0, 225.0, 190.0, 170.0, 160.0, 150.0, 225.0, 95.0, 95.0, 97.0, 85.0, 88.0, 46.0, 87.0, 90.0, 95.0, 113.0, 90.0, 215.0, 200.0, 210.0, 193.0, 88.0, 90.0, 95.0, 100.0, 105.0, 100.0, 88.0, 100.0, 165.0, 175.0, 153.0, 150.0, 180.0, 170.0, 175.0, 110.0, 72.0, 100.0, 88.0, 86.0, 90.0, 70.0, 76.0, 65.0, 69.0, 60.0, 70.0, 95.0, 80.0, 54.0, 90.0, 86.0, 165.0, 175.0, 150.0, 153.0, 150.0, 208.0, 155.0, 160.0, 190.0, 97.0, 150.0, 130.0, 140.0, 150.0, 112.0, 76.0, 87.0, 69.0, 86.0, 92.0, 97.0, 80.0, 88.0, 175.0, 150.0, 145.0, 137.0, 150.0, 198.0, 150.0, 158.0, 150.0, 215.0, 225.0, 175.0, 105.0, 100.0, 100.0, 88.0, 95.0, 46.0, 150.0, 167.0, 170.0, 180.0, 100.0, 88.0, 72.0, 94.0, 90.0, 85.0, 107.0, 90.0, 145.0, 230.0, 49.0, 75.0, 91.0, 112.0, 150.0, 110.0, 122.0, 180.0, 95.0, 100.0, 100.0, 67.0, 80.0, 65.0, 75.0, 100.0, 110.0, 105.0, 140.0, 150.0, 150.0, 140.0, 150.0, 83.0, 67.0, 78.0, 52.0, 61.0, 75.0, 75.0, 75.0, 97.0, 93.0, 67.0, 95.0, 105.0, 72.0, 72.0, 170.0, 145.0, 150.0, 148.0, 110.0, 105.0, 110.0, 95.0, 110.0, 110.0, 129.0, 75.0, 83.0, 100.0, 78.0, 96.0, 71.0, 97.0, 97.0, 70.0, 90.0, 95.0, 88.0, 98.0, 115.0, 53.0, 86.0, 81.0, 92.0, 79.0, 83.0, 140.0, 150.0, 120.0, 152.0, 100.0, 105.0, 81.0, 90.0, 52.0, 60.0, 70.0, 53.0, 100.0, 78.0, 110.0, 95.0, 71.0, 70.0, 75.0, 72.0, 102.0, 150.0, 88.0, 108.0, 120.0, 180.0, 145.0, 130.0, 150.0, 68.0, 80.0, 58.0, 96.0, 70.0, 145.0, 110.0, 145.0, 130.0, 110.0, 105.0, 100.0, 98.0, 180.0, 170.0, 190.0, 149.0, 78.0, 88.0, 75.0, 89.0, 63.0, 83.0, 67.0, 78.0, 97.0, 110.0, 110.0, 48.0, 66.0, 52.0, 70.0, 60.0, 110.0, 140.0, 139.0, 105.0, 95.0, 85.0, 88.0, 100.0, 90.0, 105.0, 85.0, 110.0, 120.0, 145.0, 165.0, 139.0, 140.0, 68.0, 95.0, 97.0, 75.0, 95.0, 105.0, 85.0, 97.0, 103.0, 125.0, 115.0, 133.0, 71.0, 68.0, 115.0, 85.0, 88.0, 90.0, 110.0, 130.0, 129.0, 138.0, 135.0, 155.0, 142.0, 125.0, 150.0, 71.0, 65.0, 80.0, 80.0, 77.0, 125.0, 71.0, 90.0, 70.0, 70.0, 65.0, 69.0, 90.0, 115.0, 115.0, 90.0, 76.0, 60.0, 70.0, 65.0, 90.0, 88.0, 90.0, 90.0, 78.0, 90.0, 75.0, 92.0, 75.0, 65.0, 105.0, 65.0, 48.0, 48.0, 67.0, 67.0, 67.0, 67.0, 62.0, 132.0, 100.0, 88.0, 72.0, 84.0, 84.0, 92.0, 110.0, 84.0, 58.0, 64.0, 60.0, 67.0, 65.0, 62.0, 68.0, 63.0, 65.0, 65.0, 74.0, 75.0, 75.0, 100.0, 74.0, 80.0, 76.0, 116.0, 120.0, 110.0, 105.0, 88.0, 85.0, 88.0, 88.0, 88.0, 85.0, 84.0, 90.0, 92.0, 74.0, 68.0, 68.0, 63.0, 70.0, 88.0, 75.0, 70.0, 67.0, 67.0, 67.0, 110.0, 85.0, 92.0, 112.0, 96.0, 84.0, 90.0, 86.0, 52.0, 84.0, 79.0, 82.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t562cb4373a1148b5b38fae91bf8bb0a2",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 5140.0, "min": 1613.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 210.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te7acba3af2c8434fb6f86d8f605564a0",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 46.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 220.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tcae9f78f95b9439fae5d79c759b394fa",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 9.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 480.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Note that when manually adding a color scale to a canvas, you can orient
it any way you like (including diagonally!) by explicitly specifying the
endpoints in canvas coordinates:

.. code:: python

    colormap = toyplot.color.brewer.map(
        name="Spectral",
        domain_min=0,
        domain_max=1,
    )
    canvas = toyplot.Canvas(width=400)
    canvas.color_scale(colormap, x1=50, y1=-50, x2=50, y2=50, label="Bottom to Top")
    canvas.color_scale(colormap, x1=150, y1=50, x2=150, y2=-50, label="Top to Bottom")
    canvas.color_scale(colormap, x1=200, y1=150, x2=350, y2=150, label="Left to Right")
    canvas.color_scale(colormap, x1=350, y1=250, x2=200, y2=250, label="Right to Left");



.. raw:: html

    <div class="toyplot" id="td7e1653b94434307a810a0183749586a" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="t06ba0afea30d45c096d3a5e70f402221" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 400.0 400.0" width="400.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="tbd75531c12cb4b33bd16edafca4ff914"><clipPath id="t2854225dd2424f6c8ee115a39f85934a"><rect height="20.0" width="300.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t2854225dd2424f6c8ee115a39f85934a)" transform="translate(50.0,350.0)rotate(-90.0)"><g class="toyplot-color-Map" id="t6ceac2e5bbc4411991a917adfdbeb753"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t48c753e2984e465cad450d53820cf21d" x1="0.0" x2="300.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t48c753e2984e465cad450d53820cf21d);stroke:none;stroke-width:1.0" width="300.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="te2d41bd089c24203bd5fde4be7f933fc" transform="translate(50.0,350.0)rotate(-90.0)translate(0,10.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(150.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-40.992" y="10.266">Bottom to Top</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tc05df0ffedaf4ec3874a18bbdf9354fd"><clipPath id="t31eda03c35cc4bc0af9a2a12269b6eea"><rect height="20.0" width="300.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t31eda03c35cc4bc0af9a2a12269b6eea)" transform="translate(150.0,50.0)rotate(90.0)"><g class="toyplot-color-Map" id="t6ceac2e5bbc4411991a917adfdbeb753"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tf38b7e61ffd5473fa0fde2e8bca201d3" x1="0.0" x2="300.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tf38b7e61ffd5473fa0fde2e8bca201d3);stroke:none;stroke-width:1.0" width="300.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t2ff3e34831a0495aad3a08fb747bc244" transform="translate(150.0,50.0)rotate(90.0)translate(0,10.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(150.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-40.992" y="10.266">Top to Bottom</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t61c1c09202ef4c099cc496699335e0f6"><clipPath id="t5a4478059e5046ddb324aee0804f054b"><rect height="20.0" width="150.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t5a4478059e5046ddb324aee0804f054b)" transform="translate(200.0,150.0)"><g class="toyplot-color-Map" id="t6ceac2e5bbc4411991a917adfdbeb753"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t027a067d49ec43a0b6f29f87ebf3ab93" x1="0.0" x2="150.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t027a067d49ec43a0b6f29f87ebf3ab93);stroke:none;stroke-width:1.0" width="150.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="td84df705b7c64544973fd27bda2ad703" transform="translate(200.0,150.0)translate(0,10.0)"><line style="" x1="0" x2="150.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(75.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(75.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-35.328" y="10.266">Left to Right</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t76b31f9706954ad49d4ddfd3ac23e36f"><clipPath id="t2bdeabe8b0de45609d90e5197cd5c1b2"><rect height="20.0" width="150.0" x="0" y="-10.0"></rect></clipPath><g clip-path="url(#t2bdeabe8b0de45609d90e5197cd5c1b2)" transform="translate(350.0,250.0)rotate(180.0)"><g class="toyplot-color-Map" id="t6ceac2e5bbc4411991a917adfdbeb753"><defs><linearGradient gradientUnits="userSpaceOnUse" id="td82acc7fcafc4ee2bda5197442ea658d" x1="0.0" x2="150.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(36.9%,31%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(34.1%,34.5%,65.2%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(31.4%,38.1%,66.9%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(28.6%,41.6%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(25.9%,45.2%,70.3%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(23.2%,48.7%,71.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(20.4%,52.3%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(21.9%,55.9%,73.1%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(25.1%,59.5%,71.6%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(28.3%,63.1%,70.1%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(31.6%,66.7%,68.6%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(34.8%,70.3%,67.1%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(38.1%,73.9%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(41.7%,76.8%,64.7%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(46%,78.4%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(50.3%,80.1%,64.6%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(54.6%,81.8%,64.5%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(58.9%,83.5%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(63.2%,85.2%,64.4%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(67.4%,86.8%,64.2%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(71.1%,88.3%,63.5%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(74.8%,89.8%,62.7%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(78.4%,91.3%,62%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(82.1%,92.8%,61.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(85.8%,94.3%,60.5%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(89.5%,95.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(91.4%,96.6%,61.5%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(93%,97.2%,64%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(94.6%,97.8%,66.4%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(96.1%,98.4%,68.8%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(97.7%,99.1%,71.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(99.2%,99.7%,73.7%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(100%,99%,73.3%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(99.9%,97.1%,70%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(99.8%,95.2%,66.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(99.8%,93.2%,63.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(99.7%,91.3%,60.3%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(99.7%,89.4%,57.1%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(99.6%,87.2%,54%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(99.5%,84.1%,51.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(99.5%,81%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(99.4%,77.9%,46.1%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(99.3%,74.8%,43.5%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(99.3%,71.7%,40.9%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(99.2%,68.5%,38.3%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(98.7%,64.6%,36.4%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(98.2%,60.5%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(97.6%,56.5%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(97%,52.5%,30.8%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(96.5%,48.4%,28.9%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(95.9%,44.4%,27%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(94.5%,41%,26.7%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(92.6%,38.1%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(90.7%,35.1%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(88.7%,32.2%,29%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(86.8%,29.3%,29.7%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84.9%,26.4%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.5%,23.2%,30.7%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(79.1%,19.4%,29.9%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(75.7%,15.6%,29.1%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(72.2%,11.8%,28.3%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(68.8%,7.99%,27.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(65.4%,4.19%,26.7%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(62%,0.392%,25.9%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#td82acc7fcafc4ee2bda5197442ea658d);stroke:none;stroke-width:1.0" width="150.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t363cedf84bd34715872c469b19646a06" transform="translate(350.0,250.0)rotate(180.0)translate(0,10.0)"><line style="" x1="0" x2="150.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(75.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(75.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-35.328" y="10.266">Right to Left</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/canvas/id"] = "t06ba0afea30d45c096d3a5e70f402221";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"te2d41bd089c24203bd5fde4be7f933fc",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t2ff3e34831a0495aad3a08fb747bc244",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"td84df705b7c64544973fd27bda2ad703",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t363cedf84bd34715872c469b19646a06",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 150.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


Canvas Legends
--------------

Last-but-not-least, Toyplot provides basic support for graphical
legends:

.. code:: python

    observations = numpy.random.power(2, size=(50, 50))
    
    x = numpy.arange(len(observations))
    
    boundaries = numpy.column_stack(
        (numpy.min(observations, axis=1),
         numpy.percentile(observations, 25, axis=1),
         numpy.percentile(observations, 50, axis=1),
         numpy.percentile(observations, 75, axis=1),
         numpy.max(observations, axis=1)))
    
    color = ["blue", "blue", "red", "red"]
    opacity = [0.1, 0.2, 0.2, 0.1]
    
    canvas = toyplot.Canvas(800, 400)
    axes = canvas.cartesian(grid=(1,5,0,1,0,4))
    fill = axes.fill(x, boundaries, color=color, opacity=opacity)
    mean = axes.plot(x, numpy.mean(observations, axis=1), color="blue")
    
    canvas.legend([
        ("Mean", mean),
        ("Quartiles", fill),
        ],
        corner=("right", 100, 100, 50),
        );




.. raw:: html

    <div class="toyplot" id="t5721a12230564cab9f391ab780a13e22" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="400.0px" id="tc8ffd11bdacd4437b12eaf0b9b48fae7" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 800.0 400.0" width="800.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t190e000cd9b5461cbab2a32795deb55e"><clipPath id="t9b92cdbdcdc94f93bf3168cc1ee6a71e"><rect height="320.0" width="560.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#t9b92cdbdcdc94f93bf3168cc1ee6a71e)"><g class="toyplot-mark-FillBoundaries" id="t7fa1b64aa55549a9932dc1d611b483ea" style="stroke:none"><polygon points="50.0,310.529681051571 60.799999999999997,338.2127767728843 71.599999999999994,311.53553288533789 82.400000000000006,322.17043210615105 93.200000000000003,299.81448759025807 104.0,327.32054709954076 114.8,309.40794168444785 125.60000000000001,325.92889561071263 136.40000000000001,301.59217273025746 147.19999999999999,337.66827765002898 158.0,299.90161002270065 168.80000000000001,308.77621001463456 179.59999999999999,296.5515581918126 190.40000000000001,315.32993678759516 201.20000000000002,329.77175301438626 212.0,307.00969965429613 222.80000000000001,345.47755682451844 233.60000000000002,318.59512358790397 244.40000000000001,326.85811079352749 255.19999999999999,278.87555671117883 266.0,323.82687058847671 276.80000000000001,330.85065229962754 287.60000000000002,336.00266120160171 298.40000000000003,331.27306243526573 309.19999999999999,295.41680020903141 320.0,295.03772432933994 330.80000000000001,304.86771847435369 341.60000000000002,335.6064233154388 352.40000000000003,326.83055695896473 363.19999999999999,329.94017522326396 374.0,321.61215724481508 384.80000000000001,308.77566069236133 395.60000000000002,300.72983043200446 406.40000000000003,321.00130270928418 417.20000000000005,309.30492377407103 428.0,308.49798899483767 438.80000000000001,348.03081885948359 449.60000000000002,310.55874250447903 460.39999999999998,307.74029875069022 471.19999999999999,295.76300155064314 482.0,284.7102771688584 492.79999999999995,275.3166503109411 503.59999999999997,290.26400117016368 514.39999999999998,328.0829003038271 525.20000000000005,321.65636423299139 536.0,294.2297217685454 546.80000000000007,320.28285540240495 557.60000000000002,305.47084318156624 568.39999999999998,279.59350772653613 579.20000000000005,339.89354855395294 579.20000000000005,177.05982692073246 568.39999999999998,201.82453339017701 557.60000000000002,228.78252611912851 546.80000000000007,176.84007381383924 536.0,199.7288409939153 525.20000000000005,184.88343792030861 514.39999999999998,208.54701216011208 503.59999999999997,202.76496591342072 492.79999999999995,190.16132728156785 482.0,162.55399241167672 471.19999999999999,194.56945380757668 460.39999999999998,229.90878304398768 449.60000000000002,186.84959820046427 438.80000000000001,215.53837396793469 428.0,219.10523540355584 417.20000000000005,187.98427903568549 406.40000000000003,219.97172833448474 395.60000000000002,190.88017296052618 384.80000000000001,202.86048393247731 374.0,151.41944680044713 363.19999999999999,207.89318183264487 352.40000000000003,187.8578033739974 341.60000000000002,184.77875137982295 330.80000000000001,170.54211777961092 320.0,170.67416705214276 309.19999999999999,226.61981088765177 298.40000000000003,217.12879767584374 287.60000000000002,240.30611862472537 276.80000000000001,238.35762112152938 266.0,188.66478780682553 255.19999999999999,197.04064040942421 244.40000000000001,215.05635258266966 233.60000000000002,222.22761081943116 222.80000000000001,210.32526377147644 212.0,217.27390304117682 201.20000000000002,217.20607871621601 190.40000000000001,241.27848064499705 179.59999999999999,205.43639938205806 168.80000000000001,182.49110182672266 158.0,198.47441917051052 147.19999999999999,253.42408685289939 136.40000000000001,205.45636907396658 125.60000000000001,223.52641820044244 114.8,200.03385763417586 104.0,187.00994987042787 93.200000000000003,155.54598387845036 82.400000000000006,211.8253325570285 71.599999999999994,185.58703931051519 60.799999999999997,169.57578085147924 50.0,225.0809880305612" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.1;stroke:none"></polygon><polygon points="50.0,225.0809880305612 60.799999999999997,169.57578085147924 71.599999999999994,185.58703931051519 82.400000000000006,211.8253325570285 93.200000000000003,155.54598387845036 104.0,187.00994987042787 114.8,200.03385763417586 125.60000000000001,223.52641820044244 136.40000000000001,205.45636907396658 147.19999999999999,253.42408685289939 158.0,198.47441917051052 168.80000000000001,182.49110182672266 179.59999999999999,205.43639938205806 190.40000000000001,241.27848064499705 201.20000000000002,217.20607871621601 212.0,217.27390304117682 222.80000000000001,210.32526377147644 233.60000000000002,222.22761081943116 244.40000000000001,215.05635258266966 255.19999999999999,197.04064040942421 266.0,188.66478780682553 276.80000000000001,238.35762112152938 287.60000000000002,240.30611862472537 298.40000000000003,217.12879767584374 309.19999999999999,226.61981088765177 320.0,170.67416705214276 330.80000000000001,170.54211777961092 341.60000000000002,184.77875137982295 352.40000000000003,187.8578033739974 363.19999999999999,207.89318183264487 374.0,151.41944680044713 384.80000000000001,202.86048393247731 395.60000000000002,190.88017296052618 406.40000000000003,219.97172833448474 417.20000000000005,187.98427903568549 428.0,219.10523540355584 438.80000000000001,215.53837396793469 449.60000000000002,186.84959820046427 460.39999999999998,229.90878304398768 471.19999999999999,194.56945380757668 482.0,162.55399241167672 492.79999999999995,190.16132728156785 503.59999999999997,202.76496591342072 514.39999999999998,208.54701216011208 525.20000000000005,184.88343792030861 536.0,199.7288409939153 546.80000000000007,176.84007381383924 557.60000000000002,228.78252611912851 568.39999999999998,201.82453339017701 579.20000000000005,177.05982692073246 579.20000000000005,128.48497627556466 568.39999999999998,157.64044481270375 557.60000000000002,121.69759968390767 546.80000000000007,138.93886754435746 536.0,142.56214970318112 525.20000000000005,125.18499008443452 514.39999999999998,138.61850469919125 503.59999999999997,135.122525766884 492.79999999999995,148.24083868664303 482.0,121.57645881502913 471.19999999999999,119.42300581145722 460.39999999999998,133.68984404213984 449.60000000000002,122.98351294150788 438.80000000000001,160.3757240017967 428.0,153.34269168978273 417.20000000000005,122.93869975953083 406.40000000000003,144.34883140701453 395.60000000000002,131.18126715388013 384.80000000000001,161.0969219163245 374.0,117.84161019250075 363.19999999999999,132.41708933609533 352.40000000000003,126.87833060627108 341.60000000000002,128.92611777419421 330.80000000000001,99.192604650626834 320.0,121.64234098569193 309.19999999999999,150.65044425727993 298.40000000000003,112.24237881456817 287.60000000000002,171.93232772771103 276.80000000000001,141.25263443105564 266.0,131.50013489728835 255.19999999999999,142.61747646863338 244.40000000000001,131.8023045138103 233.60000000000002,141.6339874677841 222.80000000000001,138.51970410763704 212.0,145.34409852546975 201.20000000000002,127.2381706333554 190.40000000000001,163.21969573239014 179.59999999999999,139.92062057588038 168.80000000000001,124.60747233381954 158.0,145.71338218863394 147.19999999999999,153.64361006151421 136.40000000000001,140.99194501162347 125.60000000000001,141.97697973081202 114.8,155.35973589535524 104.0,126.02934940940057 93.200000000000003,116.7430320382328 82.400000000000006,161.32828917090939 71.599999999999994,117.20755508330123 60.799999999999997,117.33062760385113 50.0,152.31565851979357" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:0.2;stroke:none"></polygon><polygon points="50.0,152.31565851979357 60.799999999999997,117.33062760385113 71.599999999999994,117.20755508330123 82.400000000000006,161.32828917090939 93.200000000000003,116.7430320382328 104.0,126.02934940940057 114.8,155.35973589535524 125.60000000000001,141.97697973081202 136.40000000000001,140.99194501162347 147.19999999999999,153.64361006151421 158.0,145.71338218863394 168.80000000000001,124.60747233381954 179.59999999999999,139.92062057588038 190.40000000000001,163.21969573239014 201.20000000000002,127.2381706333554 212.0,145.34409852546975 222.80000000000001,138.51970410763704 233.60000000000002,141.6339874677841 244.40000000000001,131.8023045138103 255.19999999999999,142.61747646863338 266.0,131.50013489728835 276.80000000000001,141.25263443105564 287.60000000000002,171.93232772771103 298.40000000000003,112.24237881456817 309.19999999999999,150.65044425727993 320.0,121.64234098569193 330.80000000000001,99.192604650626834 341.60000000000002,128.92611777419421 352.40000000000003,126.87833060627108 363.19999999999999,132.41708933609533 374.0,117.84161019250075 384.80000000000001,161.0969219163245 395.60000000000002,131.18126715388013 406.40000000000003,144.34883140701453 417.20000000000005,122.93869975953083 428.0,153.34269168978273 438.80000000000001,160.3757240017967 449.60000000000002,122.98351294150788 460.39999999999998,133.68984404213984 471.19999999999999,119.42300581145722 482.0,121.57645881502913 492.79999999999995,148.24083868664303 503.59999999999997,135.122525766884 514.39999999999998,138.61850469919125 525.20000000000005,125.18499008443452 536.0,142.56214970318112 546.80000000000007,138.93886754435746 557.60000000000002,121.69759968390767 568.39999999999998,157.64044481270375 579.20000000000005,128.48497627556466 579.20000000000005,89.074340481298307 568.39999999999998,119.91146738650599 557.60000000000002,90.950891871367787 546.80000000000007,87.036478338539808 536.0,70.620834601355256 525.20000000000005,89.947607316021418 514.39999999999998,96.847764806814638 503.59999999999997,95.278653506029656 492.79999999999995,101.36480336145445 482.0,83.389480462862736 471.19999999999999,87.210529190832062 460.39999999999998,87.992257614330669 449.60000000000002,87.457559598057202 438.80000000000001,116.09269020114877 428.0,97.815772847468793 417.20000000000005,85.120329420649995 406.40000000000003,91.925039238860506 395.60000000000002,71.277007493618356 384.80000000000001,107.49471354764972 374.0,81.813454458909888 363.19999999999999,76.043145611353793 352.40000000000003,96.715358257914716 341.60000000000002,92.329141619479074 330.80000000000001,78.434674738007061 320.0,82.984166293581467 309.19999999999999,108.04010252234025 298.40000000000003,69.649974470033655 287.60000000000002,102.16159230534217 276.80000000000001,108.21046552975855 266.0,85.199938479626098 255.19999999999999,87.49776189938683 244.40000000000001,85.54003932554744 233.60000000000002,112.93489025261817 222.80000000000001,87.913684152134977 212.0,113.52188990105878 201.20000000000002,74.711799575190469 190.40000000000001,108.85294059319446 179.59999999999999,89.526967510911078 168.80000000000001,91.094530433425348 158.0,87.662947917859071 147.19999999999999,110.99259765503312 136.40000000000001,91.900761542854951 125.60000000000001,91.660657542630162 114.8,82.24409417811745 104.0,85.34842641054523 93.200000000000003,81.107075978725064 82.400000000000006,107.10631628950067 71.599999999999994,74.126814152566737 60.799999999999997,81.008849580508183 50.0,101.45325820175026" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.2;stroke:none"></polygon><polygon points="50.0,101.45325820175026 60.799999999999997,81.008849580508183 71.599999999999994,74.126814152566737 82.400000000000006,107.10631628950067 93.200000000000003,81.107075978725064 104.0,85.34842641054523 114.8,82.24409417811745 125.60000000000001,91.660657542630162 136.40000000000001,91.900761542854951 147.19999999999999,110.99259765503312 158.0,87.662947917859071 168.80000000000001,91.094530433425348 179.59999999999999,89.526967510911078 190.40000000000001,108.85294059319446 201.20000000000002,74.711799575190469 212.0,113.52188990105878 222.80000000000001,87.913684152134977 233.60000000000002,112.93489025261817 244.40000000000001,85.54003932554744 255.19999999999999,87.49776189938683 266.0,85.199938479626098 276.80000000000001,108.21046552975855 287.60000000000002,102.16159230534217 298.40000000000003,69.649974470033655 309.19999999999999,108.04010252234025 320.0,82.984166293581467 330.80000000000001,78.434674738007061 341.60000000000002,92.329141619479074 352.40000000000003,96.715358257914716 363.19999999999999,76.043145611353793 374.0,81.813454458909888 384.80000000000001,107.49471354764972 395.60000000000002,71.277007493618356 406.40000000000003,91.925039238860506 417.20000000000005,85.120329420649995 428.0,97.815772847468793 438.80000000000001,116.09269020114877 449.60000000000002,87.457559598057202 460.39999999999998,87.992257614330669 471.19999999999999,87.210529190832062 482.0,83.389480462862736 492.79999999999995,101.36480336145445 503.59999999999997,95.278653506029656 514.39999999999998,96.847764806814638 525.20000000000005,89.947607316021418 536.0,70.620834601355256 546.80000000000007,87.036478338539808 557.60000000000002,90.950891871367787 568.39999999999998,119.91146738650599 579.20000000000005,89.074340481298307 579.20000000000005,53.422623380005355 568.39999999999998,60.773310556639636 557.60000000000002,55.865140514994827 546.80000000000007,54.991850206354108 536.0,52.175551768501649 525.20000000000005,52.871037670537412 514.39999999999998,58.496530072993238 503.59999999999997,50.34092995630386 492.79999999999995,52.610938869473912 482.0,54.256700689130057 471.19999999999999,50.618681568852878 460.39999999999998,51.181439285457891 449.60000000000002,51.38534021504325 438.80000000000001,57.57670828613125 428.0,51.131687873893924 417.20000000000005,50.44908361918985 406.40000000000003,52.945568324263824 395.60000000000002,52.618469689206393 384.80000000000001,52.696731607616996 374.0,50.589294818836073 363.19999999999999,50.917398722232548 352.40000000000003,62.947621617268076 341.60000000000002,50.843881846332387 330.80000000000001,51.64001927826537 320.0,53.494340248533618 309.19999999999999,54.135715573816277 298.40000000000003,51.491879931203172 287.60000000000002,56.214662402403441 276.80000000000001,58.64348328426734 266.0,50.36728250280489 255.19999999999999,55.867768014243865 244.40000000000001,53.308438233906315 233.60000000000002,50.289832627880436 222.80000000000001,55.494434598347034 212.0,51.639199565123441 201.20000000000002,51.542271963665065 190.40000000000001,50.97002042212052 179.59999999999999,53.917202462575716 168.80000000000001,50.607689328977216 158.0,60.353855635465926 147.19999999999999,56.562291714500482 136.40000000000001,53.975116705867364 125.60000000000001,52.657553344212872 114.8,50.329103317890997 104.0,52.024993466368478 93.200000000000003,50.205456449904084 82.400000000000006,52.613729728947632 71.599999999999994,50.00544148255365 60.799999999999997,54.382062228934636 50.0,59.129560466391617" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:0.1;stroke:none"></polygon></g><g class="toyplot-mark-Plot" id="tf25c347ac77d479489cf436094aea86d" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 163.49667814173617 L 60.799999999999997 137.71154754170277 L 71.599999999999994 139.90158895299604 L 82.400000000000006 159.84360929778228 L 93.200000000000003 126.70521032892651 L 104.0 147.6983684190605 L 114.8 148.88918754095593 L 125.60000000000001 157.61645449104185 L 136.40000000000001 151.27347123236322 L 147.19999999999999 177.87781141943779 L 158.0 154.65045556493641 L 168.80000000000001 137.27643129769862 L 179.59999999999999 151.12810991281049 L 190.40000000000001 173.75261142071071 L 201.20000000000002 147.97965404908931 L 212.0 162.69420943878464 L 222.80000000000001 152.75929313579127 L 233.60000000000002 167.35176858608597 L 244.40000000000001 149.78294773342697 L 255.19999999999999 148.66843657840053 L 266.0 149.54757028800805 L 276.80000000000001 167.29987457499024 L 287.60000000000002 175.23121548310593 L 298.40000000000003 147.42507457048487 L 309.19999999999999 161.6073086181612 L 320.0 137.87165369464151 L 330.80000000000001 132.29775976102169 L 341.60000000000002 146.18216413484359 L 352.40000000000003 146.38168973117547 L 363.19999999999999 149.79202673056622 L 374.0 128.48147974635066 L 384.80000000000001 161.24664087699065 L 395.60000000000002 140.04812154841591 L 406.40000000000003 152.31270593570531 L 417.20000000000005 145.72459407416423 L 428.0 161.94524974279014 L 438.80000000000001 171.5237978525154 L 449.60000000000002 142.18109227494182 L 460.39999999999998 157.03757114504492 L 471.19999999999999 140.47878190760736 L 482.0 135.97458774882278 L 492.79999999999995 148.43991202910274 L 503.59999999999997 151.64646140177766 L 514.39999999999998 157.59718751604669 L 525.20000000000005 140.12905158177691 L 536.0 145.17663656436693 L 546.80000000000007 145.14638335102191 L 557.60000000000002 154.56715103662162 L 568.39999999999998 162.22660535858168 L 579.20000000000005 140.87554354633366" style="stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:2.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="tefba9d0d3b38478b8d45cf9b70eee40d" transform="translate(50.0,350.0)translate(0,10.0)"><line style="" x1="0" x2="529.2" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(108.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">10</text></g><g transform="translate(216.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">20</text></g><g transform="translate(324.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">30</text></g><g transform="translate(432.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">40</text></g><g transform="translate(540.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="8.555">50</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t343648277b3541c6835b364eedb18689" transform="translate(50.0,350.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="1.9691811405164148" x2="299.99455851744636" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(150.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(300.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Table" id="t3cc0e5c693d84a4cbef6933520fee82d"><g transform="translate(645.0,187.5)"><g style="fill:rgb(0%,0%,100%);fill-opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:2.0" transform="translate(-5.5499999999999998, -4.4408920985006262e-16)"><line transform="rotate(45)" y1="-5.55" y2="5.55"></line></g></g><g transform="translate(655.0,187.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Mean</text></g><g transform="translate(645.0,212.5)"><g style="fill:rgb(0%,0%,100%);fill-opacity:0.1;stroke:none" transform="translate(-48.858000000000004, -4.4408920985006262e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-43.308" y="3.066"> </text><g style="fill:rgb(0%,0%,100%);fill-opacity:0.2;stroke:none" transform="translate(-34.421999999999997, -4.4408920985006262e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-28.872" y="3.066"> </text><g style="fill:rgb(100%,0%,0%);fill-opacity:0.2;stroke:none" transform="translate(-19.986000000000001, -4.4408920985006262e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-14.436" y="3.066"> </text><g style="fill:rgb(100%,0%,0%);fill-opacity:0.1;stroke:none" transform="translate(-5.5500000000000016, -4.4408920985006262e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g></g><g transform="translate(655.0,212.5)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Quartiles</text></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t5721a12230564cab9f391ab780a13e22";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "tc8ffd11bdacd4437b12eaf0b9b48fae7";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7fa1b64aa55549a9932dc1d611b483ea","data","fill data",["x", "y0", "y1", "y2", "y3", "y4"],[[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.13156772982809672, 0.039290744090385535, 0.12821489038220688, 0.09276522631282974, 0.16728504136580646, 0.07559817633486413, 0.13530686105184053, 0.08023701463095784, 0.16135942423247518, 0.041105741166569905, 0.16699463325766464, 0.13741263328455153, 0.17816147269395805, 0.11556687737468288, 0.06742748995204582, 0.14330100115234617, 0.015074810584938663, 0.10468292137365344, 0.0771396306882418, 0.23708147762940388, 0.08724376470507762, 0.06383115900124144, 0.046657795994660925, 0.06242312521578101, 0.1819439993032287, 0.18320758556886693, 0.1504409384188211, 0.04797858894853724, 0.07723147680345079, 0.06686608258912034, 0.09462614251728298, 0.13741446435879556, 0.16423389855998521, 0.09666232430238615, 0.1356502540864299, 0.13834003668387446, 0.006563937135054716, 0.1314708583184031, 0.14086567083103252, 0.18078999483118946, 0.21763240943713863, 0.24894449896352963, 0.19911999609945458, 0.07305699898724302, 0.09447878589002875, 0.18590092743818212, 0.0990571486586501, 0.1484305227281125, 0.2346883075782129, 0.0336881714868235], [0.41639670656479594, 0.6014140638284026, 0.5480432022982826, 0.46058222480990507, 0.6481800537384989, 0.5433001670985738, 0.4998871412194138, 0.42157860599852515, 0.481812103086778, 0.3219197104903353, 0.5050852694316316, 0.5583629939109245, 0.48187866872647306, 0.3624050645166765, 0.4426464042792799, 0.44242032319607727, 0.46558245409507865, 0.4259079639352295, 0.4498121580577679, 0.5098645319685859, 0.5377840406439148, 0.37214126292823546, 0.3656462712509155, 0.4429040077471876, 0.41126729704116083, 0.5977527764928574, 0.5981929407346303, 0.5507374954005901, 0.5404739887533421, 0.4736893938911837, 0.6619351773318429, 0.49046505355840897, 0.5303994234649128, 0.4334275722183842, 0.5400524032143817, 0.43631588198814714, 0.4482054201068843, 0.5438346726651191, 0.4003040565200411, 0.5181018206414111, 0.6248200252944109, 0.5327955757281072, 0.4907834469552642, 0.47150995946629304, 0.550388540265638, 0.5009038633536156, 0.5771997539538691, 0.40405824626957165, 0.49391822203274327, 0.5764672435975585], [0.6589478049340214, 0.7755645746538296, 0.7759748163889959, 0.6289057027636353, 0.777523226539224, 0.7465688353019981, 0.6488008803488159, 0.69341006756396, 0.6966935166279218, 0.6545212997949527, 0.6809553927045535, 0.7513084255539348, 0.7002645980803988, 0.6226010142253663, 0.7425394312221487, 0.6821863382484341, 0.7049343196412099, 0.6945533751073864, 0.7273256516206323, 0.6912750784378887, 0.7283328836757055, 0.6958245518964812, 0.5935589075742966, 0.7925254039514394, 0.6644985191424002, 0.7611921967143602, 0.8360246511645772, 0.736912940752686, 0.7437388979790964, 0.7252763688796822, 0.7738612993583308, 0.6296769269455851, 0.7293957761537329, 0.6855038953099516, 0.7568710008015639, 0.6555243610340576, 0.632080919994011, 0.7567216235283071, 0.7210338531928672, 0.7685899806284759, 0.7614118039499029, 0.6725305377111899, 0.71625824744372, 0.7046049843360291, 0.7493833663852183, 0.6914595009893962, 0.7035371081854751, 0.7610080010536411, 0.6411985172909875, 0.7383834124147844], [0.8284891393274991, 0.8966371680649727, 0.9195772861581109, 0.8096456123683311, 0.8963097467375831, 0.8821719119648492, 0.8925196860729419, 0.8611311415245662, 0.8603307948571501, 0.7966913411498896, 0.8744568402738031, 0.8630182318885822, 0.8682434416302964, 0.8038235313560185, 0.9176273347493651, 0.7882603669964707, 0.8736210528262167, 0.7902170324912727, 0.8815332022481752, 0.8750074603353772, 0.8826668717345797, 0.8059651149008048, 0.8261280256488595, 0.9345000850998878, 0.8065329915921992, 0.8900527790213951, 0.9052177508733098, 0.8589028612684031, 0.8442821391402843, 0.9131895146288207, 0.8939551518036337, 0.8083509548411676, 0.9290766416879388, 0.8602498692037983, 0.8829322352645, 0.8406140905084374, 0.7796910326628375, 0.875141468006476, 0.8733591412855645, 0.8759649026972265, 0.8887017317904575, 0.8287839887951518, 0.8490711549799012, 0.8438407839772846, 0.8668413089465953, 0.9312638846621492, 0.8765450722048673, 0.8634970270954407, 0.7669617753783133, 0.8697521983956723], [0.9695681317786946, 0.9853931259035512, 0.9999818617248212, 0.9912875675701746, 0.9993151451669864, 0.9932500217787718, 0.9989029889403633, 0.9911414888526238, 0.9867496109804421, 0.9781256942849984, 0.9654871478817802, 0.9979743689034093, 0.9869426584580809, 0.9967665985929316, 0.9948590934544498, 0.9945360014495885, 0.9816852180055099, 0.9990338912403985, 0.9889718725536456, 0.9804407732858538, 0.9987757249906504, 0.9711883890524422, 0.9792844586586552, 0.9950270668959894, 0.9862142814206124, 0.9883521991715546, 0.9945332690724488, 0.9971870605122254, 0.9568412612757731, 0.9969420042592249, 0.9980356839372131, 0.9910108946412767, 0.9912717677026454, 0.9901814389191206, 0.9985030546027005, 0.9962277070870202, 0.9747443057128958, 0.9953821992831892, 0.9960618690484737, 0.9979377281038238, 0.9858109977028998, 0.991296870435087, 0.9988635668123205, 0.9716782330900225, 0.990429874431542, 0.9927481607716612, 0.983360499312153, 0.9804495316166839, 0.9640889648112012, 0.9885912553999822]],"toyplot");
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"tf25c347ac77d479489cf436094aea86d","data","plot data",["x", "y0"],[[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0, 37.0, 38.0, 39.0, 40.0, 41.0, 42.0, 43.0, 44.0, 45.0, 46.0, 47.0, 48.0, 49.0], [0.6216777395275461, 0.7076281748609907, 0.7003280368233465, 0.6338546356740591, 0.7443159655702449, 0.674338771936465, 0.6703693748634802, 0.6412784850298605, 0.6624217625587893, 0.573740628601874, 0.6511651481168786, 0.7090785623410046, 0.6629063002906317, 0.5874912952642977, 0.6734011531697023, 0.6243526352040513, 0.6574690228806958, 0.6088274380463801, 0.6673901742219102, 0.6711052114053315, 0.6681747657066398, 0.6090004180833659, 0.5825626150563136, 0.6752497514317171, 0.6279756379394626, 0.7070944876845283, 0.7256741341299277, 0.679392786217188, 0.6787277008960818, 0.6673599108981126, 0.7383950675121644, 0.6291778637433645, 0.6998395948386137, 0.6589576468809824, 0.6809180197527859, 0.6268491675240329, 0.5949206738249487, 0.6927296924168607, 0.6432080961831835, 0.6984040603079754, 0.7134180408372574, 0.6718669599029908, 0.6611784619940745, 0.6413427082798444, 0.6995698280607436, 0.6827445447854436, 0.682845388829927, 0.6514428298779279, 0.6259113154713943, 0.6970815215122211]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tefba9d0d3b38478b8d45cf9b70eee40d",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 50.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 540.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t343648277b3541c6835b364eedb18689",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


The call to :func:`toyplot.canvas.Canvas.legend` always includes an
explicit list of entries to add to the legend, plus a
:ref:`canvas-layout` specification of where the layout should appear
on the canvas. Currently, each entry to be displayed in a legend must be
one of the following:

-  A (label, mark) tuple, which will get its appearance from the mark,
   or:
-  A (label, marker) tuple, which can be used to specify an arbitrary
   :ref:`Marker<Markers>`.

Of course, ``label`` is the human-readable text to be displayed next to
an item in the legend, while ``mark`` is a mark that has been added to
the canvas. However, not all marks can map cleanly to a single entry in
the legend - note in the example above that the fill mark added multiple
markers to the "Quartiles" entry in the legend, one for each data
series. While the interpretation is reasonably clear in this case, there
will be occasions when there isn't a sensible one-to-one mapping between
a mark and an entry in the legend. For example, the meaning of multiple
series may not be clear, or you may be plotting categorical information
using custom markers in a line or scatter plot. In these cases use the
second form of legend entry to specify as many explicit :ref:`Markers`
as needed.

There are some subtleties here worth noting, many of which are driven by
Toyplot's deliberate embrace of the philosophy that *explicit is better
than implicit*:

-  You can have as many or as few legends on your canvas as you like.
-  Callers explicitly specify the order and contents of each legend.
-  There is no relationship between axes and legends - you can combine
   marks from multiple axes in a single legend.

Here's an example with all these ideas at work. Note that the legend
overlaps two coordinate systems and its first entry derives directly
from the mark in the first coordinate system, while the second and third
entries document the individual series in the second mark:

.. code:: python

    x = numpy.linspace(0, 1)
    y1 = (1 - x) ** 2
    y2 = numpy.column_stack((1 - (x ** 2), x ** 2))
    
    canvas = toyplot.Canvas(width=600, height=300)
    m1 = canvas.cartesian(grid=(1,2,0), margin=25).scatterplot(x, y1, marker="o", color="rgb(255,0,0)")
    m2 = canvas.cartesian(grid=(1,2,1), margin=25, yshow=False).scatterplot(x, y2, marker="s", color=["green", "blue"])
    
    if True:
        canvas.legend([
            ("Experiment 1", m1),
            ("Experiment 2", m2.markers[0]),
            ("Experiment 3", m2.markers[1]),
            ],
            corner=("top", 100, 100, 70),
            );



.. raw:: html

    <div class="toyplot" id="t4eb6349a50484130b7ec423ea372cba0" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t7f08e4feb6de44088fd132743786f7d1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="t003f5a3bbd0546d783b208c44af72703"><clipPath id="t21828e79dd174eca94a952bdb77b27f4"><rect height="270.0" width="270.0" x="15.0" y="15.0"></rect></clipPath><g clip-path="url(#t21828e79dd174eca94a952bdb77b27f4)"><g class="toyplot-mark-Scatterplot" id="ta49cc1b49bf14213a201e54e2ebc0c31"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(25.0, 25.0)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(30.102040816326529, 35.099958350687224)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(35.204081632653057, 44.991670137442739)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(40.306122448979593, 54.675135360266523)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(45.408163265306122, 64.150354019158669)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(50.510204081632651, 73.41732611411912)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(55.612244897959179, 82.476051645147891)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(60.714285714285715, 91.326530612244852)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(65.816326530612244, 99.968763015410218)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(70.918367346938766, 108.40274885464387)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(76.020408163265301, 116.62848812994588)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(81.122448979591823, 124.64598084131613)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(86.224489795918359, 132.4552269887547)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(91.326530612244895, 140.05622657226155)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(96.428571428571431, 147.44897959183672)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(101.53061224489795, 154.6334860474802)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(106.63265306122449, 161.60974593919198)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(111.73469387755101, 168.37775926697208)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(116.83673469387755, 174.93752603082049)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(121.93877551020408, 181.2890462307372)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(127.0408163265306, 187.4323198667222)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(132.14285714285714, 193.36734693877551)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(137.24489795918365, 199.09412744689712)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(142.34693877551018, 204.61266139108704)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(147.44897959183672, 209.92294877134526)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(152.55102040816328, 215.0249895876718)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(157.65306122448979, 219.9187838400666)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(162.75510204081633, 224.60433152852977)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(167.85714285714286, 229.08163265306123)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(172.9591836734694, 233.35068721366096)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(178.0612244897959, 237.41149521032901)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(183.16326530612244, 241.26405664306537)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(188.26530612244895, 244.90837151187003)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(193.36734693877548, 248.34443981674301)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(198.46938775510202, 251.5722615576843)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(203.57142857142856, 254.59183673469386)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(208.67346938775509, 257.40316534777173)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(213.77551020408163, 260.00624739691796)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(218.87755102040816, 262.40108288213241)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(223.97959183673467, 264.58767180341522)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(229.08163265306121, 266.56601416076637)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(234.18367346938774, 268.33610995418576)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(239.28571428571428, 269.89795918367344)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(244.38775510204081, 271.25156184922946)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(249.48979591836729, 272.39691795085383)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(254.59183673469386, 273.33402748854644)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(259.69387755102036, 274.06289046230739)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(264.79591836734693, 274.58350687213658)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(269.89795918367344, 274.89587671803417)"><circle r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(275.0, 275.0)"><circle r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tab1ea547ca0e45909f1d9e6671c5f516" transform="translate(25.0,275.0)translate(0,10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(125.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t44874d9d469c42e18cb2bdcb46d41688" transform="translate(25.0,275.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><g transform="translate(0.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.0</text></g><g transform="translate(125.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">0.5</text></g><g transform="translate(250.0,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="-4.4408920985e-16">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g><g class="toyplot-coordinates-Cartesian" id="t601c0882e65c412387da0b1264792bf6"><clipPath id="tebad2d18c25141939e8a9bbfd7335358"><rect height="270.0" width="270.0" x="315.0" y="15.0"></rect></clipPath><g clip-path="url(#tebad2d18c25141939e8a9bbfd7335358)"><g class="toyplot-mark-Scatterplot" id="t879607c10c9e40a4bfbdadd6d2af51c6"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(325.0, 25.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(330.10204081632651, 25.104123281965848)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(335.20408163265307, 25.416493127863376)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(340.30612244897964, 25.937109537692631)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(345.40816326530614, 26.665972511453564)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(350.51020408163265, 27.603082049146195)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(355.61224489795916, 28.7484381507705)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(360.71428571428578, 30.102040816326536)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(365.81632653061229, 31.663890045814245)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(370.91836734693874, 33.433985839233657)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(376.0204081632653, 35.412328196584745)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(381.12244897959181, 37.598917117867565)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(386.22448979591832, 39.993752603082058)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(391.32653061224494, 42.596834652228225)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(396.42857142857144, 45.408163265306115)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(401.53061224489795, 48.427738442315686)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(406.63265306122452, 51.655560183256959)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(411.73469387755108, 55.091628488129928)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(416.83673469387753, 58.735943356934612)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(421.9387755102041, 62.588504789670964)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(427.0408163265306, 66.64931278633901)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(432.14285714285711, 70.918367346938766)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(437.24489795918362, 75.395668471470202)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(442.34693877551018, 80.081216159933362)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(447.44897959183675, 84.975010412328189)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(452.55102040816325, 90.077051228654724)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(457.65306122448976, 95.387338608912941)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(462.75510204081633, 100.90587255310285)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(467.85714285714289, 106.63265306122446)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(472.9591836734694, 112.5676801332778)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(478.0612244897959, 118.71095376926277)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(483.16326530612241, 125.06247396917951)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(488.26530612244898, 131.62224073302789)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(493.36734693877554, 138.39025406080799)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(498.46938775510205, 145.36651395251977)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(503.57142857142856, 152.55102040816323)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(508.67346938775506, 159.94377342773842)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(513.77551020408157, 167.5447730112453)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(518.87755102040819, 175.35401915868388)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(523.9795918367347, 183.37151187005409)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(529.08163265306121, 191.59725114535607)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(534.18367346938771, 200.03123698458973)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(539.28571428571422, 208.67346938775509)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(544.38775510204084, 217.52394835485214)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(549.48979591836735, 226.58267388588084)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(554.59183673469386, 235.84964598084127)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(559.69387755102036, 245.32486463973342)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(564.79591836734699, 255.00832986255728)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(569.89795918367338, 264.90004164931275)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(575.0, 275.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g></g><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(325.0, 275.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(330.10204081632651, 274.89587671803417)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(335.20408163265307, 274.58350687213658)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(340.30612244897964, 274.06289046230739)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(345.40816326530614, 273.33402748854644)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(350.51020408163265, 272.39691795085383)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(355.61224489795916, 271.25156184922952)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(360.71428571428578, 269.89795918367344)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(365.81632653061229, 268.33610995418576)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(370.91836734693874, 266.56601416076637)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(376.0204081632653, 264.58767180341528)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(381.12244897959181, 262.40108288213241)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(386.22448979591832, 260.00624739691796)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(391.32653061224494, 257.40316534777179)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(396.42857142857144, 254.59183673469389)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(401.53061224489795, 251.57226155768433)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(406.63265306122452, 248.34443981674303)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(411.73469387755108, 244.90837151187006)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(416.83673469387753, 241.2640566430654)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(421.9387755102041, 237.41149521032904)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(427.0408163265306, 233.35068721366099)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(432.14285714285711, 229.08163265306123)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(437.24489795918362, 224.6043315285298)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(442.34693877551018, 219.91878384006662)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(447.44897959183675, 215.0249895876718)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(452.55102040816325, 209.92294877134526)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(457.65306122448976, 204.61266139108704)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(462.75510204081633, 199.09412744689715)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(467.85714285714289, 193.36734693877551)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(472.9591836734694, 187.4323198667222)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(478.0612244897959, 181.2890462307372)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(483.16326530612241, 174.93752603082049)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(488.26530612244898, 168.37775926697211)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(493.36734693877554, 161.60974593919201)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(498.46938775510205, 154.6334860474802)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(503.57142857142856, 147.44897959183677)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(508.67346938775506, 140.05622657226158)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(513.77551020408157, 132.4552269887547)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(518.87755102040819, 124.64598084131613)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(523.9795918367347, 116.62848812994591)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(529.08163265306121, 108.40274885464393)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(534.18367346938771, 99.968763015410275)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(539.28571428571422, 91.326530612244923)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(544.38775510204084, 82.476051645147891)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(549.48979591836735, 73.417326114119163)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(554.59183673469386, 64.150354019158726)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(559.69387755102036, 54.675135360266587)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(564.79591836734699, 44.991670137442739)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(569.89795918367338, 35.099958350687224)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g><g class="toyplot-Datum" style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(575.0, 25.0)"><rect height="4.0" width="4.0" x="-2.0" y="-2.0"></rect></g></g></g></g><g class="toyplot-coordinates-Axis" id="tae4d1f6daf8542e5983651cbaf673191" transform="translate(325.0,275.0)translate(0,10.0)"><line style="" x1="0" x2="250.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(125.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Table" id="t9f2621f433254b958ec975d73fead88b"><g transform="translate(295.0,111.66666666666666)"><g style="fill:rgb(100%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(100%,0%,0%);stroke-opacity:1.0" transform="translate(-5.5499999999999998, -4.4408920985006262e-16)"><circle r="5.55"></circle></g></g><g transform="translate(305.0,111.66666666666666)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Experiment 1</text></g><g transform="translate(295.0,135.0)"><g style="fill:rgb(0%,50.2%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,50.2%,0%);stroke-opacity:1.0" transform="translate(-5.5499999999999998, -4.4408920985006262e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g></g><g transform="translate(305.0,135.0)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Experiment 2</text></g><g transform="translate(295.0,158.33333333333331)"><g style="fill:rgb(0%,0%,100%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,100%);stroke-opacity:1.0" transform="translate(-5.5499999999999998, -4.4408920985006262e-16)"><rect height="11.1" width="11.1" x="-5.55" y="-5.55"></rect></g></g><g transform="translate(305.0,158.33333333333331)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="0" y="3.066">Experiment 3</text></g></g></svg><div class="toyplot-behavior"><script>(function()
    {
    var modules={};
    modules["toyplot/tables"] = (function()
        {
            var tables = [];
    
            var module = {};
    
            module.set = function(owner, key, names, columns)
            {
                tables.push({owner: owner, key: key, names: names, columns: columns});
            }
    
            module.get = function(owner, key)
            {
                for(var i = 0; i != tables.length; ++i)
                {
                    var table = tables[i];
                    if(table.owner != owner)
                        continue;
                    if(table.key != key)
                        continue;
                    return {names: table.names, columns: table.columns};
                }
            }
    
            module.get_csv = function(owner, key)
            {
                var table = module.get(owner, key);
                if(table != undefined)
                {
                    var csv = "";
                    csv += table.names.join(",") + "\n";
                    for(var i = 0; i != table.columns[0].length; ++i)
                    {
                      for(var j = 0; j != table.columns.length; ++j)
                      {
                        if(j)
                          csv += ",";
                        csv += table.columns[j][i];
                      }
                      csv += "\n";
                    }
                    return csv;
                }
            }
    
            return module;
        })();
    modules["toyplot/root/id"] = "t4eb6349a50484130b7ec423ea372cba0";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t7f08e4feb6de44088fd132743786f7d1";
    modules["toyplot/canvas"] = (function(canvas_id)
        {
            return document.querySelector("#" + canvas_id);
        })(modules["toyplot/canvas/id"]);
    modules["toyplot/menus/context"] = (function(root, canvas)
        {
            var wrapper = document.createElement("div");
            wrapper.innerHTML = "<ul class='toyplot-context-menu' style='background:#eee; border:1px solid #b8b8b8; border-radius:5px; box-shadow: 0px 0px 8px rgba(0%,0%,0%,0.25); margin:0; padding:3px 0; position:fixed; visibility:hidden;'></ul>"
            var menu = wrapper.firstChild;
    
            root.appendChild(menu);
    
            var items = [];
    
            var ignore_mouseup = null;
            function open_menu(e)
            {
                var show_menu = false;
                for(var index=0; index != items.length; ++index)
                {
                    var item = items[index];
                    if(item.show(e))
                    {
                        item.item.style.display = "block";
                        show_menu = true;
                    }
                    else
                    {
                        item.item.style.display = "none";
                    }
                }
    
                if(show_menu)
                {
                    ignore_mouseup = true;
                    menu.style.left = (e.clientX + 1) + "px";
                    menu.style.top = (e.clientY - 5) + "px";
                    menu.style.visibility = "visible";
                    e.stopPropagation();
                    e.preventDefault();
                }
            }
    
            function close_menu()
            {
                menu.style.visibility = "hidden";
            }
    
            function contextmenu(e)
            {
                open_menu(e);
            }
    
            function mousemove(e)
            {
                ignore_mouseup = false;
            }
    
            function mouseup(e)
            {
                if(ignore_mouseup)
                {
                    ignore_mouseup = false;
                    return;
                }
                close_menu();
            }
    
            function keydown(e)
            {
                if(e.key == "Escape" || e.key == "Esc" || e.keyCode == 27)
                {
                    close_menu();
                }
            }
    
            canvas.addEventListener("contextmenu", contextmenu);
            canvas.addEventListener("mousemove", mousemove);
            document.addEventListener("mouseup", mouseup);
            document.addEventListener("keydown", keydown);
    
            var module = {};
            module.add_item = function(label, show, activate)
            {
                var wrapper = document.createElement("div");
                wrapper.innerHTML = "<li class='toyplot-context-menu-item' style='background:#eee; color:#333; padding:2px 20px; list-style:none; margin:0; text-align:left;'>" + label + "</li>"
                var item = wrapper.firstChild;
    
                items.push({item: item, show: show});
    
                function mouseover()
                {
                    this.style.background = "steelblue";
                    this.style.color = "white";
                }
    
                function mouseout()
                {
                    this.style.background = "#eee";
                    this.style.color = "#333";
                }
    
                function choose_item(e)
                {
                    close_menu();
                    activate();
    
                    e.stopPropagation();
                    e.preventDefault();
                }
    
                item.addEventListener("mouseover", mouseover);
                item.addEventListener("mouseout", mouseout);
                item.addEventListener("mouseup", choose_item);
                item.addEventListener("contextmenu", choose_item);
    
                menu.appendChild(item);
            };
            return module;
        })(modules["toyplot/root"],modules["toyplot/canvas"]);
    modules["toyplot/io"] = (function()
        {
            var module = {};
            module.save_file = function(mime_type, charset, data, filename)
            {
                var uri = "data:" + mime_type + ";charset=" + charset + "," + data;
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = filename;
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
            };
            return module;
        })();
    modules["toyplot.coordinates.Axis"] = (
            function(canvas)
            {
                function sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function in_range(a, x, b)
                {
                    var left = Math.min(a, b);
                    var right = Math.max(a, b);
                    return left <= x && x <= right;
                }
    
                function inside(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return sign(segment.domain.min) * Math.pow(base, mix(log(segment.domain.min, base), log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                var axes = {};
    
                function display_coordinates(e)
                {
                    var current = canvas.createSVGPoint();
                    current.x = e.clientX;
                    current.y = e.clientY;
    
                    for(var axis_id in axes)
                    {
                        var axis = document.querySelector("#" + axis_id);
                        var coordinates = axis.querySelector(".toyplot-coordinates-Axis-coordinates");
                        if(coordinates)
                        {
                            var projection = axes[axis_id];
                            var local = current.matrixTransform(axis.getScreenCTM().inverse());
                            if(inside(local.x, projection))
                            {
                                var domain = to_domain(local.x, projection);
                                coordinates.style.visibility = "visible";
                                coordinates.setAttribute("transform", "translate(" + local.x + ")");
                                var text = coordinates.querySelector("text");
                                text.textContent = domain.toFixed(2);
                            }
                            else
                            {
                                coordinates.style.visibility= "hidden";
                            }
                        }
                    }
                }
    
                canvas.addEventListener("click", display_coordinates);
    
                var module = {};
                module.show_coordinates = function(axis_id, projection)
                {
                    axes[axis_id] = projection;
                }
    
                return module;
            })(modules["toyplot/canvas"]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"ta49cc1b49bf14213a201e54e2ebc0c31","data","scatterplot",["x", "y0"],[[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9596001665972511, 0.920033319450229, 0.8812994585589339, 0.8433985839233653, 0.8063306955435235, 0.7700957934194085, 0.7346938775510206, 0.7001249479383591, 0.6663890045814245, 0.6334860474802165, 0.6014160766347355, 0.5701790920449812, 0.5397750937109538, 0.5102040816326531, 0.4814660558100793, 0.4535610162432321, 0.4264889629321117, 0.40024989587671805, 0.3748438150770512, 0.3502707205331112, 0.32653061224489793, 0.3036234902124116, 0.2815493544356518, 0.2603082049146189, 0.23990004164931278, 0.22032486463973353, 0.20158267388588094, 0.18367346938775514, 0.16659725114535612, 0.15035401915868396, 0.1349437734277385, 0.12036651395251982, 0.10662224073302792, 0.0937109537692628, 0.08163265306122454, 0.070387338608913, 0.05997501041232822, 0.050395668471470235, 0.04164931278633907, 0.033735943356934646, 0.026655560183256998, 0.020408163265306135, 0.014993752603082056, 0.01041232819658478, 0.006663890045814259, 0.0037484381507705204, 0.0016659725114535648, 0.0004164931278633912, 0.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tab1ea547ca0e45909f1d9e6671c5f516",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t44874d9d469c42e18cb2bdcb46d41688",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    (function(tables, context_menu, io, owner_id, key, label, names, columns, filename)
            {
                tables.set(owner_id, key, names, columns);
    
                var owner = document.querySelector("#" + owner_id);
                function show_item(e)
                {
                    return owner.contains(e.target);
                }
    
                function choose_item()
                {
                    io.save_file("text/csv", "utf-8", tables.get_csv(owner_id, key), filename + ".csv");
                }
    
                context_menu.add_item("Save " + label + " as CSV", show_item, choose_item);
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t879607c10c9e40a4bfbdadd6d2af51c6","data","scatterplot",["x", "y0", "y1"],[[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0], [1.0, 0.9995835068721366, 0.9983340274885465, 0.9962515618492295, 0.9933361099541858, 0.9895876718034152, 0.985006247396918, 0.9795918367346939, 0.973344439816743, 0.9662640566430654, 0.958350687213661, 0.9496043315285297, 0.9400249895876718, 0.9296126613910871, 0.9183673469387755, 0.9062890462307372, 0.8933777592669722, 0.8796334860474803, 0.8650562265722616, 0.8496459808413162, 0.8334027488546439, 0.8163265306122449, 0.7984173261141192, 0.7796751353602666, 0.7600999583506872, 0.7396917950853811, 0.7184506455643482, 0.6963765097875886, 0.6734693877551021, 0.6497292794668887, 0.6251561849229489, 0.599750104123282, 0.5735110370678884, 0.546438983756768, 0.5185339441899208, 0.48979591836734704, 0.46022490628904633, 0.4298209079550188, 0.3985839233652645, 0.3665139525197836, 0.33361099541857575, 0.2998750520616411, 0.26530612244897966, 0.22990420658059152, 0.19366930445647668, 0.15660141607663491, 0.11870054144106634, 0.07996668054977096, 0.040399833402748886, 0.0], [0.0, 0.00041649312786339016, 0.0016659725114535606, 0.003748438150770512, 0.006663890045814243, 0.010412328196584754, 0.014993752603082049, 0.02040816326530612, 0.02665556018325697, 0.033735943356934604, 0.041649312786339016, 0.05039566847147021, 0.059975010412328195, 0.07038733860891293, 0.08163265306122448, 0.09371095376926278, 0.10662224073302788, 0.12036651395251978, 0.13494377342773842, 0.15035401915868388, 0.16659725114535606, 0.18367346938775508, 0.20158267388588083, 0.22032486463973341, 0.23990004164931278, 0.2603082049146189, 0.2815493544356517, 0.3036234902124114, 0.32653061224489793, 0.3502707205331112, 0.3748438150770511, 0.40024989587671794, 0.4264889629321115, 0.453561016243232, 0.4814660558100791, 0.510204081632653, 0.5397750937109537, 0.5701790920449812, 0.6014160766347355, 0.6334860474802164, 0.6663890045814242, 0.7001249479383589, 0.7346938775510203, 0.7700957934194085, 0.8063306955435233, 0.8433985839233651, 0.8812994585589337, 0.920033319450229, 0.9596001665972511, 1.0]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"tae4d1f6daf8542e5983651cbaf673191",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 250.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>


