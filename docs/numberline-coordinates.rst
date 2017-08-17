
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _numberline-coordinates:

Numberline Coordinates
======================

The :class:`toyplot.coordinates.Numberline` class provides a single
axis that maps one-dimensional data values to canvas coordinates. The
numberline *range* (its coordinates on the Toyplot the canvas) is
specified at creation time (see :ref:`canvas-layout`), while the
*domain* is implicitly defined to include all displayed data (but can be
manually overridden by the caller if desired).

If your data is two-dimensional, you should use
:ref:`cartesian-coordinates` instead.

Typically, you create numberlines explicitly using
:meth:`toyplot.canvas.Canvas.numberline`:

.. code:: python

    import numpy
    numpy.random.seed(1234)
    events = numpy.random.uniform(size=(25, 4))

.. code:: python

    import toyplot
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.scatterplot(events.T[0]);



.. raw:: html

    <div align="center" class="toyplot" id="td01153831e9a446fb0ba5e17fa4f1d36"><svg class="toyplot-canvas-Canvas" height="100.0px" id="t1700e4e8b93543de8ba6a09dc93f29b1" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="td73e4b607f9048c5baee7bc1e7d7fbe4"><clipPath id="t7f2f3d6ab2e848698bf36ae024ea2157"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t7f2f3d6ab2e848698bf36ae024ea2157)" transform="translate(50.0,50.0)"><g class="toyplot-mark-Scatterplot" id="td06a32105ee64e58a1f6196f591cca70" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t3d8503e815cf41b19c5f00d40ba03da8" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="29.90461138992595" x2="479.0696768418526" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "td06a32105ee64e58a1f6196f591cca70", "columns": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#td01153831e9a446fb0ba5e17fa4f1d36 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "td01153831e9a446fb0ba5e17fa4f1d36";
                var axes = {"t3d8503e815cf41b19c5f00d40ba03da8": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note that when you add scatterplots to numberlines, they are
one-dimensional scatterplots, so you only supply one set of coordinates.

When you add multiple marks to a numberline, they "stack up" on top of
each other:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.scatterplot(events.T[0])
    numberline.scatterplot(events.T[1]);



.. raw:: html

    <div align="center" class="toyplot" id="t297412ba567341dda31f6d7e66f11432"><svg class="toyplot-canvas-Canvas" height="100.0px" id="t95a54edb2ce84827b2c5b86f123bb5be" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t6c3df2943d68461abb528091b7c7c997"><clipPath id="t57fd991c28054c4c8e356f92685a8ea9"><rect height="60.0" width="500.0" x="0" y="-40.0"></rect></clipPath><g clip-path="url(#t57fd991c28054c4c8e356f92685a8ea9)" transform="translate(50.0,50.0)"><g class="toyplot-mark-Scatterplot" id="tfed86e927a78423c9d2cef123cd98a3d" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="tc58ec9784c684cc2b2ae2e2bd74c0736" style="" transform="translate(0,-20.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="311.05438551991591" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="136.29630264132081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="437.96631737104735" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="356.35101349145009" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="6.8842247953411206" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="307.69808921674684" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="325.68907161328872" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="284.04932631303461" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="71.883412257282288" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="462.43381430778254" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="92.143541906906819" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="266.65508149937529" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="251.48341655630918" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="3.3820309950013949" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="496.04073309418072" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="312.45835265295551" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="26.936842573118291" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="59.690448963124197" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="53.563408596933151" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="267.92583126580791" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="306.07449853287875" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="74.916857994963621" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="219.15494056121375" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="475.71438187679661" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="409.60103353207916" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="te698411ec3f2489c8498a05e7aed0a00" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="3.382030995001395" x2="496.0407330941807" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "tfed86e927a78423c9d2cef123cd98a3d", "columns": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "tc58ec9784c684cc2b2ae2e2bd74c0736", "columns": [[0.6221087710398319, 0.2725926052826416, 0.8759326347420947, 0.7127020269829002, 0.013768449590682241, 0.6153961784334937, 0.6513781432265774, 0.5680986526260692, 0.14376682451456457, 0.924867628615565, 0.18428708381381365, 0.5333101629987506, 0.5029668331126184, 0.00676406199000279, 0.9920814661883615, 0.624916705305911, 0.05387368514623658, 0.1193808979262484, 0.1071268171938663, 0.5358516625316159, 0.6121489970657575, 0.14983371598992723, 0.4383098811224275, 0.9514287637535932, 0.8192020670641583]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#t297412ba567341dda31f6d7e66f11432 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t297412ba567341dda31f6d7e66f11432";
                var axes = {"te698411ec3f2489c8498a05e7aed0a00": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


You can specify the default spacing between marks (and the axis spine)
when you create the numberline:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline(spacing=10)
    numberline.scatterplot(events.T[0])
    numberline.scatterplot(events.T[1]);



.. raw:: html

    <div align="center" class="toyplot" id="t98d20f0bcbed4484a83bc0451b46c2a8"><svg class="toyplot-canvas-Canvas" height="100.0px" id="tf2cb1c79b92f4c82a5a8791112b20195" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t7c66940bd4b74cdb9824cd7ab301f46d"><clipPath id="t08690f1b57504044afadbcf3fe2198f6"><rect height="30.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t08690f1b57504044afadbcf3fe2198f6)" transform="translate(50.0,50.0)"><g class="toyplot-mark-Scatterplot" id="tf54599a19fbc461fbfbee886c37b0b21" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="te54e3d801722484db3fc525a288a2bcb" style="" transform="translate(0,-10.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="311.05438551991591" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="136.29630264132081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="437.96631737104735" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="356.35101349145009" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="6.8842247953411206" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="307.69808921674684" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="325.68907161328872" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="284.04932631303461" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="71.883412257282288" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="462.43381430778254" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="92.143541906906819" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="266.65508149937529" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="251.48341655630918" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="3.3820309950013949" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="496.04073309418072" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="312.45835265295551" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="26.936842573118291" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="59.690448963124197" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="53.563408596933151" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="267.92583126580791" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="306.07449853287875" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="74.916857994963621" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="219.15494056121375" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="475.71438187679661" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="409.60103353207916" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t3af5978e9b714018b1f0b6803cadebb9" transform="translate(50.0,50.0)translate(0,10.0)"><line style="" x1="3.382030995001395" x2="496.0407330941807" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "tf54599a19fbc461fbfbee886c37b0b21", "columns": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "te54e3d801722484db3fc525a288a2bcb", "columns": [[0.6221087710398319, 0.2725926052826416, 0.8759326347420947, 0.7127020269829002, 0.013768449590682241, 0.6153961784334937, 0.6513781432265774, 0.5680986526260692, 0.14376682451456457, 0.924867628615565, 0.18428708381381365, 0.5333101629987506, 0.5029668331126184, 0.00676406199000279, 0.9920814661883615, 0.624916705305911, 0.05387368514623658, 0.1193808979262484, 0.1071268171938663, 0.5358516625316159, 0.6121489970657575, 0.14983371598992723, 0.4383098811224275, 0.9514287637535932, 0.8192020670641583]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#t98d20f0bcbed4484a83bc0451b46c2a8 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t98d20f0bcbed4484a83bc0451b46c2a8";
                var axes = {"t3af5978e9b714018b1f0b6803cadebb9": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


And you can individually control the offset of the individual marks, as
well as the padding (distance between the axis spine and the first
mark):

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200)
    numberline = canvas.numberline(spacing=10, padding=20)
    numberline.scatterplot(events.T[0])
    numberline.scatterplot(events.T[1])
    numberline.scatterplot(events.T[2], offset=40)
    numberline.scatterplot(events.T[3], offset=50);



.. raw:: html

    <div align="center" class="toyplot" id="ta52faea7c70349cf841232ff6dbded27"><svg class="toyplot-canvas-Canvas" height="200.0px" id="tb9bf0d0aa2fa401a9854e51a821cef5e" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="tf2f935e108124d7a82a121423baf9d17"><clipPath id="t423da3d9734a492ebf342c34405ad8d6"><rect height="90.0" width="500.0" x="0" y="-70.0"></rect></clipPath><g clip-path="url(#t423da3d9734a492ebf342c34405ad8d6)" transform="translate(50.0,100.0)"><g class="toyplot-mark-Scatterplot" id="t2fc6d5bb84a74c1d9cf5868dc4c2b55a" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="95.759725189446144" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="389.98790405940179" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.06967684185258" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="341.73146758606816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="251.54158265390487" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="182.44299195068615" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="466.57005099126081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="158.41806108443564" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="401.07382104007957" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="109.39605283704429" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="29.90461138992595" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="297.31238996722442" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="164.8342228104575" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="282.97232152526567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="395.2620665285167" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.62548001225488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="191.15872601575325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.971350243481496" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="235.81626716018388" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="208.37676890134659" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="218.44658608780509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="352.99878254088662" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.86288447548952" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="264.11213879253023" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="268.43909646220487" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t53f5b2fb0cff422296184e3dedefdac5" style="" transform="translate(0,-10.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="311.05438551991591" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="136.29630264132081" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="437.96631737104735" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="356.35101349145009" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="6.8842247953411206" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="307.69808921674684" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="325.68907161328872" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="284.04932631303461" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="71.883412257282288" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="462.43381430778254" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="92.143541906906819" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="266.65508149937529" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="251.48341655630918" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="3.3820309950013949" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="496.04073309418072" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="312.45835265295551" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="26.936842573118291" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="59.690448963124197" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="53.563408596933151" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="267.92583126580791" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="306.07449853287875" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="74.916857994963621" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="219.15494056121375" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="475.71438187679661" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0"><circle cx="409.60103353207916" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t0b694e6b120740f29621b887192b9d9a" style="" transform="translate(0,-40)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="218.86386950355725" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="138.23212757154835" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="178.90863497893332" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="185.12537739519746" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="386.41331080618704" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="37.690620821488274" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="198.60128886307709" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="434.56369478061293" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="352.13048555916771" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="221.07037770208831" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="23.677639400757567" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="21.662031347401744" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="55.947158787201914" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="308.72085440214852" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="479.40088107643322" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="239.04689783533729" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="225.82420413042954" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="369.26152807167341" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="114.60928273030896" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="3.104258293564699" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="459.09903769028654" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="373.03170456835835" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="76.286387337252677" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="240.17958925500804" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(55.3%,62.7%,79.6%);fill-opacity:1.0;opacity:1.0;stroke:rgb(55.3%,62.7%,79.6%);stroke-opacity:1.0"><circle cx="28.557819044429944" cy="0" r="2.0"></circle></g></g></g><g class="toyplot-mark-Scatterplot" id="t0fe4a5ed67ef40069eaf7cdb507c2756" style="" transform="translate(0,-50)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="392.67929185688462" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="400.93608876750966" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="250.49756276172934" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="280.59809303281247" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="441.32059531805828" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="184.41200300098726" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="394.36507147037275" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="218.08671194783969" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="352.29065409478625" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="454.65797948623629" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="337.44047179116512" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="280.71654003169891" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="303.59685310924226" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="456.06144321657717" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="395.98206764581988" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="97.837589332949122" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="491.00237076097727" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="293.65181673199231" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="449.98259741833766" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="150.32085288515057" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="312.86833498126765" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="415.50349621676889" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="284.20480762359506" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="251.27978169127519" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(90.6%,54.1%,76.5%);fill-opacity:1.0;opacity:1.0;stroke:rgb(90.6%,54.1%,76.5%);stroke-opacity:1.0"><circle cx="334.71087153727439" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="ta79ef6f1ca9344db917a399f21d06360" transform="translate(50.0,100.0)translate(0,20.0)"><line style="" x1="3.104258293564699" x2="496.0407330941807" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "t2fc6d5bb84a74c1d9cf5868dc4c2b55a", "columns": [[0.1915194503788923, 0.7799758081188035, 0.9581393536837052, 0.6834629351721363, 0.5030831653078097, 0.3648859839013723, 0.9331401019825216, 0.31683612216887125, 0.8021476420801591, 0.21879210567408858, 0.0598092227798519, 0.5946247799344488, 0.329668445620915, 0.5659446430505314, 0.7905241330570334, 0.2852509600245098, 0.38231745203150647, 0.12394270048696299, 0.4716325343203678, 0.4167535378026932, 0.4368931721756102, 0.7059975650817732, 0.6337257689509791, 0.5282242775850605, 0.5368781929244097]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "t53f5b2fb0cff422296184e3dedefdac5", "columns": [[0.6221087710398319, 0.2725926052826416, 0.8759326347420947, 0.7127020269829002, 0.013768449590682241, 0.6153961784334937, 0.6513781432265774, 0.5680986526260692, 0.14376682451456457, 0.924867628615565, 0.18428708381381365, 0.5333101629987506, 0.5029668331126184, 0.00676406199000279, 0.9920814661883615, 0.624916705305911, 0.05387368514623658, 0.1193808979262484, 0.1071268171938663, 0.5358516625316159, 0.6121489970657575, 0.14983371598992723, 0.4383098811224275, 0.9514287637535932, 0.8192020670641583]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "t0b694e6b120740f29621b887192b9d9a", "columns": [[0.4377277390071145, 0.2764642551430967, 0.35781726995786667, 0.37025075479039493, 0.772826621612374, 0.07538124164297655, 0.3972025777261542, 0.8691273895612258, 0.7042609711183354, 0.44214075540417663, 0.04735527880151513, 0.04332406269480349, 0.11189431757440382, 0.617441708804297, 0.9588017621528665, 0.47809379567067456, 0.45164840826085906, 0.7385230561433468, 0.22921856546061792, 0.006208516587129398, 0.9181980753805731, 0.7460634091367166, 0.15257277467450536, 0.4803591785100161, 0.05711563808885989]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "t0fe4a5ed67ef40069eaf7cdb507c2756", "columns": [[0.7853585837137692, 0.8018721775350193, 0.5009951255234587, 0.5611961860656249, 0.8826411906361166, 0.3688240060019745, 0.7887301429407455, 0.43617342389567937, 0.7045813081895725, 0.9093159589724725, 0.6748809435823302, 0.5614330800633979, 0.6071937062184846, 0.9121228864331543, 0.7919641352916398, 0.19567517866589823, 0.9820047415219545, 0.5873036334639846, 0.8999651948366754, 0.30064170577030114, 0.6257366699625353, 0.8310069924335378, 0.5684096152471901, 0.5025595633825504, 0.6694217430745488]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#ta52faea7c70349cf841232ff6dbded27 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "ta52faea7c70349cf841232ff6dbded27";
                var axes = {"ta79ef6f1ca9344db917a399f21d06360": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Of course, you have control over all the normal parameters of a
scatterplot, such as color and marker type:

.. code:: python

    timestamps = numpy.random.uniform(size=40)
    event_types = numpy.random.choice(2, size=timestamps.shape)

.. code:: python

    colormap = toyplot.color.CategoricalMap()
    
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.scatterplot(
        timestamps,
        color=(event_types, colormap),
        marker="|",
        size=15,
        mstyle={"stroke-width":1.5},
    );



.. raw:: html

    <div align="center" class="toyplot" id="t23452bdaf05f4b52abd12574fa5abfb3"><svg class="toyplot-canvas-Canvas" height="100.0px" id="t4df5e0492c614fccaba99d2d4f8c5990" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t0acc8bf964e44972a9c41a170e6732e8"><clipPath id="t0608a5a9d206427db7fad78b638b1e80"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t0608a5a9d206427db7fad78b638b1e80)" transform="translate(50.0,50.0)"><g class="toyplot-mark-Scatterplot" id="t85a5af90fc614a138306f6ed28f79b89" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 383.55831418973622, 0)" x1="383.55831418973622" x2="383.55831418973622" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 354.05768098880191, 0)" x1="354.05768098880191" x2="354.05768098880191" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 398.43359186259829, 0)" x1="398.43359186259829" x2="398.43359186259829" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 278.88041421372475, 0)" x1="278.88041421372475" x2="278.88041421372475" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 482.91826599606378, 0)" x1="482.91826599606378" x2="482.91826599606378" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 73.578449946498594, 0)" x1="73.578449946498594" x2="73.578449946498594" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 14.823500267707789, 0)" x1="14.823500267707789" x2="14.823500267707789" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 296.94674631238587, 0)" x1="296.94674631238587" x2="296.94674631238587" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 57.032849371331238, 0)" x1="57.032849371331238" x2="57.032849371331238" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 475.40492504206111, 0)" x1="475.40492504206111" x2="475.40492504206111" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 162.85370721267361, 0)" x1="162.85370721267361" x2="162.85370721267361" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 96.809345076888604, 0)" x1="96.809345076888604" x2="96.809345076888604" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 228.90582444871376, 0)" x1="228.90582444871376" x2="228.90582444871376" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 460.20128554654389, 0)" x1="460.20128554654389" x2="460.20128554654389" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 439.53458075733789, 0)" x1="439.53458075733789" x2="439.53458075733789" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 126.30787752326511, 0)" x1="126.30787752326511" x2="126.30787752326511" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 174.00439643467308, 0)" x1="174.00439643467308" x2="174.00439643467308" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 91.294365790154373, 0)" x1="91.294365790154373" x2="91.294365790154373" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 450.89802568549601, 0)" x1="450.89802568549601" x2="450.89802568549601" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 353.26408158589874, 0)" x1="353.26408158589874" x2="353.26408158589874" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 363.32923078107035, 0)" x1="363.32923078107035" x2="363.32923078107035" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 450.04391840485386, 0)" x1="450.04391840485386" x2="450.04391840485386" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 389.58190038466211, 0)" x1="389.58190038466211" x2="389.58190038466211" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 299.57739030214617, 0)" x1="299.57739030214617" x2="299.57739030214617" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 145.56262244893742, 0)" x1="145.56262244893742" x2="145.56262244893742" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 75.697632203716054, 0)" x1="75.697632203716054" x2="75.697632203716054" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 167.58732957471744, 0)" x1="167.58732957471744" x2="167.58732957471744" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 328.7758885789097, 0)" x1="328.7758885789097" x2="328.7758885789097" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 36.67127181630908, 0)" x1="36.67127181630908" x2="36.67127181630908" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 27.503197703111827, 0)" x1="27.503197703111827" x2="27.503197703111827" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 161.59740696058822, 0)" x1="161.59740696058822" x2="161.59740696058822" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 295.24090223149307, 0)" x1="295.24090223149307" x2="295.24090223149307" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 426.94928356282088, 0)" x1="426.94928356282088" x2="426.94928356282088" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 143.5312125000045, 0)" x1="143.5312125000045" x2="143.5312125000045" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 86.533613407396075, 0)" x1="86.533613407396075" x2="86.533613407396075" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 67.010602999421408, 0)" x1="67.010602999421408" x2="67.010602999421408" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 497.32691432214727, 0)" x1="497.32691432214727" x2="497.32691432214727" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 89.748934734695922, 0)" x1="89.748934734695922" x2="89.748934734695922" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(98.8%,55.3%,38.4%);fill-opacity:1.0;opacity:1.0;stroke:rgb(98.8%,55.3%,38.4%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 158.77341151359792, 0)" x1="158.77341151359792" x2="158.77341151359792" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0;stroke-width:1.5"><line transform="rotate(0, 284.14570232955361, 0)" x1="284.14570232955361" x2="284.14570232955361" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="tf33ba673f8934108b645df6316d15965" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="14.82350026770779" x2="497.3269143221473" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "t85a5af90fc614a138306f6ed28f79b89", "columns": [[0.7671166283794725, 0.7081153619776038, 0.7968671837251966, 0.5577608284274495, 0.9658365319921276, 0.14715689989299718, 0.02964700053541558, 0.5938934926247718, 0.11406569874266248, 0.9508098500841222, 0.32570741442534723, 0.1936186901537772, 0.45781164889742754, 0.9204025710930878, 0.8790691615146757, 0.2526157550465302, 0.34800879286934616, 0.18258873158030875, 0.9017960513709921, 0.7065281631717975, 0.7266584615621408, 0.9000878368097077, 0.7791638007693242, 0.5991547806042924, 0.29112524489787484, 0.15139526440743212, 0.3351746591494349, 0.6575517771578194, 0.07334254363261816, 0.05500639540622365, 0.32319481392117644, 0.5904818044629861, 0.8538985671256417, 0.287062425000009, 0.17306722681479214, 0.13402120599884282, 0.9946538286442945, 0.17949786946939184, 0.31754682302719583, 0.5682914046591072]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#t23452bdaf05f4b52abd12574fa5abfb3 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t23452bdaf05f4b52abd12574fa5abfb3";
                var axes = {"tf33ba673f8934108b645df6316d15965": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


In addition to scatterplots, numberlines can be used to display any
:class:`toyplot.color.Map`:

.. code:: python

    colormap = toyplot.color.diverging.map("BlueRed", domain_min=0, domain_max=1)
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap, style={"stroke-width":1})



.. raw:: html

    <div align="center" class="toyplot" id="tff81bfdd9dc0421da7f0cc70330d699f"><svg class="toyplot-canvas-Canvas" height="100.0px" id="tc7ba574ee81c4fd4896856e0cac72b9f" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t4904032b00134731b59c7d429843731c"><clipPath id="t257ad2b6310747c3a576dca2bc6be093"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t257ad2b6310747c3a576dca2bc6be093)" transform="translate(50.0,50.0)"><g class="toyplot-color-Map" id="t6aaafee9bbad435183a79f284aa21394"><defs><linearGradient gradientUnits="userSpaceOnUse" id="td78135002cec47758f2e4b46498f3e9d" x1="0.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(33.5%,28.3%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(35.2%,31.2%,78.1%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(36.9%,34%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(38.6%,36.8%,82.8%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(40.3%,39.6%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(42%,42.3%,86.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(43.8%,45%,88.8%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(45.5%,47.6%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(47.3%,50.2%,92.2%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(49%,52.8%,93.7%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(50.8%,55.3%,95%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(52.6%,57.7%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(54.3%,60.1%,97.2%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(56.1%,62.4%,98.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(57.9%,64.6%,98.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(59.7%,66.7%,99.4%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(61.5%,68.8%,99.8%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(63.3%,70.7%,100%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(65.1%,72.6%,100%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(66.8%,74.3%,100%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(68.6%,76%,99.9%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(70.3%,77.6%,99.5%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(72.1%,79%,99%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.8%,80.3%,98.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(75.4%,81.5%,97.4%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(77.1%,82.6%,96.4%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(78.7%,83.6%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(80.2%,84.4%,94%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(81.7%,85.1%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(83.2%,85.7%,91%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(84.6%,86.1%,89.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(85.9%,86.4%,87.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(87.3%,86.2%,85.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(88.7%,85.4%,83.2%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(90%,84.4%,80.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(91.1%,83.3%,78.5%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(92.2%,82.1%,76.1%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(93%,80.8%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(93.8%,79.3%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(94.4%,77.7%,68.7%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(94.8%,76%,66.2%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(95.2%,74.2%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(95.4%,72.3%,61.2%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(95.4%,70.2%,58.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.3%,68.1%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(95.1%,65.8%,53.7%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(94.8%,63.5%,51.3%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(94.3%,61%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(93.6%,58.5%,46.4%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(92.9%,55.9%,44%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(92%,53.1%,41.6%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(91%,50.3%,39.3%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(89.8%,47.4%,37%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(88.5%,44.5%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(87.1%,41.4%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(85.6%,38.2%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84%,34.9%,28.4%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.2%,31.5%,26.3%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(80.3%,28%,24.4%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(78.4%,24.2%,22.5%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(76.3%,20.1%,20.6%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(74.1%,15.5%,18.8%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(71.8%,9.83%,17.1%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(69.5%,0.296%,15.5%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#td78135002cec47758f2e4b46498f3e9d);stroke:none;stroke-width:1" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="td70133774d064421a8ab58ac58cf5347" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "tff81bfdd9dc0421da7f0cc70330d699f";
                var axes = {"td70133774d064421a8ab58ac58cf5347": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Keep in mind that to display most color maps on a numberline, you *must*
specify their domain (otherwise, there would be no way to map the colors
to coordinates on the axis). You can see above that we specified
:math:`[0, 1]` as the domain.

:class:`toyplot.color.CategoricalMap` is the one exception to this
rule, since it has an implicit :math:`[0, N)` domain where :math:`N` is
the number of colors in the map:

.. code:: python

    colormap = toyplot.color.brewer.map("Set1")
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap)



.. raw:: html

    <div align="center" class="toyplot" id="tdc76c60e79bc4ddabc61939b26ae3833"><svg class="toyplot-canvas-Canvas" height="100.0px" id="td8560d2dbba84570a00b50503d6374a4" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="te3cd57b1bf23411f81c80f50b5c6c661"><clipPath id="t047eff721c2a4716a4be9a1002430f37"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t047eff721c2a4716a4be9a1002430f37)" transform="translate(50.0,50.0)"><g class="toyplot-color-CategoricalMap" id="t2aeccf4662e247de8d2e63b256f1a9e7"><rect height="10" style="fill:rgb(89.4%,10.2%,11%);fill-opacity:1.0;stroke:none" width="62.5" x="0.0" y="-5.0"></rect><rect height="10" style="fill:rgb(21.6%,49.4%,72.2%);fill-opacity:1.0;stroke:none" width="62.5" x="62.5" y="-5.0"></rect><rect height="10" style="fill:rgb(30.2%,68.6%,29%);fill-opacity:1.0;stroke:none" width="62.5" x="125.0" y="-5.0"></rect><rect height="10" style="fill:rgb(59.6%,30.6%,63.9%);fill-opacity:1.0;stroke:none" width="62.5" x="187.5" y="-5.0"></rect><rect height="10" style="fill:rgb(100%,49.8%,0%);fill-opacity:1.0;stroke:none" width="62.5" x="250.0" y="-5.0"></rect><rect height="10" style="fill:rgb(100%,100%,20%);fill-opacity:1.0;stroke:none" width="62.5" x="312.5" y="-5.0"></rect><rect height="10" style="fill:rgb(65.1%,33.7%,15.7%);fill-opacity:1.0;stroke:none" width="62.5" x="375.0" y="-5.0"></rect><rect height="10" style="fill:rgb(96.9%,50.6%,74.9%);fill-opacity:1.0;stroke:none" width="62.5" x="437.5" y="-5.0"></rect><rect height="10" style="fill:none;stroke:none;stroke-width:1.0" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t48c0e8e7380f44248e81aa780bc57a21" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(166.66666666666666,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">3</text></g><g transform="translate(333.3333333333333,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">6</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">9</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "tdc76c60e79bc4ddabc61939b26ae3833";
                var axes = {"t48c0e8e7380f44248e81aa780bc57a21": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 9.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Note that, unlike a scatterplot, a color map has a width that can be
varied:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap, width=20)



.. raw:: html

    <div align="center" class="toyplot" id="t663fc2ddc6ef49fbbf2fbacf69a23d2a"><svg class="toyplot-canvas-Canvas" height="100.0px" id="t5d7e4878069944ef823b7a8f62337c84" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t58bb3e1e7d7846429a08d77a8e2826eb"><clipPath id="t9b1f3a94e4f54fc38d8f94399c4e3ab1"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t9b1f3a94e4f54fc38d8f94399c4e3ab1)" transform="translate(50.0,50.0)"><g class="toyplot-color-CategoricalMap" id="tb2fc797abc8b4be2906eabdf309d0083"><rect height="20" style="fill:rgb(89.4%,10.2%,11%);fill-opacity:1.0;stroke:none" width="62.5" x="0.0" y="-10.0"></rect><rect height="20" style="fill:rgb(21.6%,49.4%,72.2%);fill-opacity:1.0;stroke:none" width="62.5" x="62.5" y="-10.0"></rect><rect height="20" style="fill:rgb(30.2%,68.6%,29%);fill-opacity:1.0;stroke:none" width="62.5" x="125.0" y="-10.0"></rect><rect height="20" style="fill:rgb(59.6%,30.6%,63.9%);fill-opacity:1.0;stroke:none" width="62.5" x="187.5" y="-10.0"></rect><rect height="20" style="fill:rgb(100%,49.8%,0%);fill-opacity:1.0;stroke:none" width="62.5" x="250.0" y="-10.0"></rect><rect height="20" style="fill:rgb(100%,100%,20%);fill-opacity:1.0;stroke:none" width="62.5" x="312.5" y="-10.0"></rect><rect height="20" style="fill:rgb(65.1%,33.7%,15.7%);fill-opacity:1.0;stroke:none" width="62.5" x="375.0" y="-10.0"></rect><rect height="20" style="fill:rgb(96.9%,50.6%,74.9%);fill-opacity:1.0;stroke:none" width="62.5" x="437.5" y="-10.0"></rect><rect height="20" style="fill:none;stroke:none;stroke-width:1.0" width="500.0" x="0.0" y="-10.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t4dd59a4fa1f643559e538c9c2780aadb" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(166.66666666666666,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">3</text></g><g transform="translate(333.3333333333333,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">6</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">9</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t663fc2ddc6ef49fbbf2fbacf69a23d2a";
                var axes = {"t4dd59a4fa1f643559e538c9c2780aadb": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 9.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Also note that some colors may tend to blend-in with the canvas
background:

.. code:: python

    colormap = toyplot.color.brewer.map("Greys", domain_min=0, domain_max=1)
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap)



.. raw:: html

    <div align="center" class="toyplot" id="t9474150bcee64c2ca2da24775a0e3cab"><svg class="toyplot-canvas-Canvas" height="100.0px" id="tb5573f14e64446f593ceab44fca8119d" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t06bd297d19164fedb409c52eed5ed077"><clipPath id="tecef0522395242d38b066834cb3976e1"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tecef0522395242d38b066834cb3976e1)" transform="translate(50.0,50.0)"><g class="toyplot-color-Map" id="t66cba1e5b4ab4962b4e4144d73a117ac"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t1f85642e9a92498f84affbd51122c6ee" x1="0.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(0%,0%,0%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(1.84%,1.84%,1.84%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(3.69%,3.69%,3.69%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(5.53%,5.53%,5.53%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(7.37%,7.37%,7.37%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(9.21%,9.21%,9.21%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(11.1%,11.1%,11.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(12.9%,12.9%,12.9%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(14.8%,14.8%,14.8%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(17%,17%,17%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(19.3%,19.3%,19.3%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(21.5%,21.5%,21.5%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(23.8%,23.8%,23.8%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(26%,26%,26%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(28.2%,28.2%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(30.5%,30.5%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(32.6%,32.6%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(34.2%,34.2%,34.2%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(35.9%,35.9%,35.9%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(37.5%,37.5%,37.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(39.1%,39.1%,39.1%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(40.8%,40.8%,40.8%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(42.4%,42.4%,42.4%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(44.1%,44.1%,44.1%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(45.8%,45.8%,45.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(47.5%,47.5%,47.5%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(49.2%,49.2%,49.2%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(51%,51%,51%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(52.7%,52.7%,52.7%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(54.5%,54.5%,54.5%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(56.2%,56.2%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(58%,58%,58%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(59.8%,59.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(61.7%,61.7%,61.7%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(63.7%,63.7%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(65.6%,65.6%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(67.6%,67.6%,67.6%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(69.5%,69.5%,69.5%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(71.4%,71.4%,71.4%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(73.4%,73.4%,73.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(75%,75%,75%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(76.4%,76.4%,76.4%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(77.8%,77.8%,77.8%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(79.2%,79.2%,79.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(80.6%,80.6%,80.6%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(82%,82%,82%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(83.4%,83.4%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(84.7%,84.7%,84.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(86%,86%,86%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(87.1%,87.1%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(88.2%,88.2%,88.2%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(89.4%,89.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(90.5%,90.5%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(91.7%,91.7%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(92.8%,92.8%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(94%,94%,94%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(94.8%,94.8%,94.8%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(95.5%,95.5%,95.5%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(96.3%,96.3%,96.3%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(97%,97%,97%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(97.8%,97.8%,97.8%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(98.5%,98.5%,98.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(99.3%,99.3%,99.3%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(100%,100%,100%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t1f85642e9a92498f84affbd51122c6ee);stroke:none;stroke-width:1.0" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="t7c39a8eb13fc42c0abb25c0f6875f599" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t9474150bcee64c2ca2da24775a0e3cab";
                var axes = {"t7c39a8eb13fc42c0abb25c0f6875f599": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


To make the color map stand out from the background, you can use the
``style`` parameter to add a border:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline()
    numberline.colormap(colormap, style={"stroke":"lightgrey"})



.. raw:: html

    <div align="center" class="toyplot" id="t7278c28ce34c4a6b8ad93862b49908db"><svg class="toyplot-canvas-Canvas" height="100.0px" id="t900ffb3147e940c2b194d1d8a7d14d29" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t439d075f1e3a4c28961690ff7393c42c"><clipPath id="td09836fc56334e648f8269ff1c1ea174"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#td09836fc56334e648f8269ff1c1ea174)" transform="translate(50.0,50.0)"><g class="toyplot-color-Map" id="t2228c54d33cb4fa2a2c766f2be223f17"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t8655a937f00d42ef8ac03608ea48bad4" x1="0.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(0%,0%,0%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(1.84%,1.84%,1.84%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(3.69%,3.69%,3.69%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(5.53%,5.53%,5.53%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(7.37%,7.37%,7.37%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(9.21%,9.21%,9.21%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(11.1%,11.1%,11.1%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(12.9%,12.9%,12.9%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(14.8%,14.8%,14.8%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(17%,17%,17%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(19.3%,19.3%,19.3%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(21.5%,21.5%,21.5%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(23.8%,23.8%,23.8%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(26%,26%,26%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(28.2%,28.2%,28.2%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(30.5%,30.5%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(32.6%,32.6%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(34.2%,34.2%,34.2%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(35.9%,35.9%,35.9%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(37.5%,37.5%,37.5%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(39.1%,39.1%,39.1%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(40.8%,40.8%,40.8%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(42.4%,42.4%,42.4%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(44.1%,44.1%,44.1%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(45.8%,45.8%,45.8%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(47.5%,47.5%,47.5%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(49.2%,49.2%,49.2%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(51%,51%,51%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(52.7%,52.7%,52.7%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(54.5%,54.5%,54.5%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(56.2%,56.2%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(58%,58%,58%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(59.8%,59.8%,59.8%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(61.7%,61.7%,61.7%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(63.7%,63.7%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(65.6%,65.6%,65.6%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(67.6%,67.6%,67.6%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(69.5%,69.5%,69.5%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(71.4%,71.4%,71.4%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(73.4%,73.4%,73.4%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(75%,75%,75%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(76.4%,76.4%,76.4%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(77.8%,77.8%,77.8%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(79.2%,79.2%,79.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(80.6%,80.6%,80.6%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(82%,82%,82%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(83.4%,83.4%,83.4%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(84.7%,84.7%,84.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(86%,86%,86%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(87.1%,87.1%,87.1%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(88.2%,88.2%,88.2%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(89.4%,89.4%,89.4%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(90.5%,90.5%,90.5%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(91.7%,91.7%,91.7%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(92.8%,92.8%,92.8%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(94%,94%,94%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(94.8%,94.8%,94.8%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(95.5%,95.5%,95.5%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(96.3%,96.3%,96.3%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(97%,97%,97%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(97.8%,97.8%,97.8%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(98.5%,98.5%,98.5%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(99.3%,99.3%,99.3%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(100%,100%,100%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t8655a937f00d42ef8ac03608ea48bad4);stroke:rgb(82.7%,82.7%,82.7%);stroke-opacity:1.0;stroke-width:1.0" width="500.0" x="0.0" y="-5.0"></rect></g></g><g class="toyplot-coordinates-Axis" id="tf23c08956c7641898289ba78cba06ce7" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t7278c28ce34c4a6b8ad93862b49908db";
                var axes = {"tf23c08956c7641898289ba78cba06ce7": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Functions like :meth:`toyplot.coordinates.Cartesian.color_scale`,
:meth:`toyplot.canvas.Canvas.color_scale`, and
:meth:`toyplot.canvas.Canvas.matrix` use numberlines to conveniently
add color scales to visualizations, but by creating a numberline object
of your own, you can create more complex scales. For example, you could
define a multi-range scale, or add marks to highlight critical values:

.. code:: python

    colormap1 = toyplot.color.diverging.map("BlueRed", domain_min=-1, domain_max=1)
    colormap2 = toyplot.color.diverging.map("PurpleGreen", domain_min=-0.5, domain_max=1.5)
    
    canvas = toyplot.Canvas(width=600, height=100)
    numberline = canvas.numberline(spacing=15, padding=10)
    numberline.colormap(colormap1)
    numberline.colormap(colormap2)
    numberline.scatterplot([0], marker="d", color="black");



.. raw:: html

    <div align="center" class="toyplot" id="t89df5e58eb1c4f2c8c5298cf85eec69a"><svg class="toyplot-canvas-Canvas" height="100.0px" id="t1cbde3d15ca4437a885d04ea89e3c82c" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 100.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="td1b088c30583419d9021b1122c7b3dfe"><clipPath id="tff5dcb8b1d894df58b2801881e848561"><rect height="50.0" width="500.0" x="0" y="-40.0"></rect></clipPath><g clip-path="url(#tff5dcb8b1d894df58b2801881e848561)" transform="translate(50.0,50.0)"><g class="toyplot-color-Map" id="t98af683b746a4360ae2134b688a5d815"><defs><linearGradient gradientUnits="userSpaceOnUse" id="t1390af19df204104a3e1c0644bb80718" x1="0.0" x2="400.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(33.5%,28.3%,75.6%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(35.2%,31.2%,78.1%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(36.9%,34%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(38.6%,36.8%,82.8%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(40.3%,39.6%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(42%,42.3%,86.9%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(43.8%,45%,88.8%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(45.5%,47.6%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(47.3%,50.2%,92.2%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(49%,52.8%,93.7%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(50.8%,55.3%,95%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(52.6%,57.7%,96.2%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(54.3%,60.1%,97.2%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(56.1%,62.4%,98.1%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(57.9%,64.6%,98.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(59.7%,66.7%,99.4%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(61.5%,68.8%,99.8%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(63.3%,70.7%,100%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(65.1%,72.6%,100%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(66.8%,74.3%,100%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(68.6%,76%,99.9%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(70.3%,77.6%,99.5%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(72.1%,79%,99%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(73.8%,80.3%,98.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(75.4%,81.5%,97.4%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(77.1%,82.6%,96.4%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(78.7%,83.6%,95.3%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(80.2%,84.4%,94%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(81.7%,85.1%,92.6%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(83.2%,85.7%,91%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(84.6%,86.1%,89.3%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(85.9%,86.4%,87.5%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(87.3%,86.2%,85.4%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(88.7%,85.4%,83.2%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(90%,84.4%,80.8%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(91.1%,83.3%,78.5%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(92.2%,82.1%,76.1%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(93%,80.8%,73.6%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(93.8%,79.3%,71.2%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(94.4%,77.7%,68.7%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(94.8%,76%,66.2%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(95.2%,74.2%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(95.4%,72.3%,61.2%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(95.4%,70.2%,58.7%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(95.3%,68.1%,56.2%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(95.1%,65.8%,53.7%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(94.8%,63.5%,51.3%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(94.3%,61%,48.8%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(93.6%,58.5%,46.4%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(92.9%,55.9%,44%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(92%,53.1%,41.6%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(91%,50.3%,39.3%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(89.8%,47.4%,37%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(88.5%,44.5%,34.8%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(87.1%,41.4%,32.6%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(85.6%,38.2%,30.5%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(84%,34.9%,28.4%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(82.2%,31.5%,26.3%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(80.3%,28%,24.4%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(78.4%,24.2%,22.5%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(76.3%,20.1%,20.6%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(74.1%,15.5%,18.8%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(71.8%,9.83%,17.1%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(69.5%,0.296%,15.5%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#t1390af19df204104a3e1c0644bb80718);stroke:none;stroke-width:1.0" width="400.0" x="0.0" y="-5.0"></rect></g><g class="toyplot-color-Map" id="t1d2fda04fbd64bd4be2199cd86f0a1db" transform="translate(0, -15.0)"><defs><linearGradient gradientUnits="userSpaceOnUse" id="tfb4db9922f4447e4990e7b9a393629ac" x1="100.0" x2="500.0" y1="0" y2="0"><stop offset="0.0" stop-color="rgb(46.7%,29.8%,63.3%)" stop-opacity="1.0"></stop><stop offset="0.015873015873" stop-color="rgb(47.4%,32.3%,65.7%)" stop-opacity="1.0"></stop><stop offset="0.031746031746" stop-color="rgb(48.1%,34.7%,68%)" stop-opacity="1.0"></stop><stop offset="0.047619047619" stop-color="rgb(48.7%,37.1%,70.2%)" stop-opacity="1.0"></stop><stop offset="0.0634920634921" stop-color="rgb(49.3%,39.4%,72.3%)" stop-opacity="1.0"></stop><stop offset="0.0793650793651" stop-color="rgb(50%,41.8%,74.3%)" stop-opacity="1.0"></stop><stop offset="0.0952380952381" stop-color="rgb(50.6%,44.2%,76.3%)" stop-opacity="1.0"></stop><stop offset="0.111111111111" stop-color="rgb(51.3%,46.5%,78.1%)" stop-opacity="1.0"></stop><stop offset="0.126984126984" stop-color="rgb(52%,48.8%,79.9%)" stop-opacity="1.0"></stop><stop offset="0.142857142857" stop-color="rgb(52.7%,51.1%,81.5%)" stop-opacity="1.0"></stop><stop offset="0.15873015873" stop-color="rgb(53.4%,53.3%,83%)" stop-opacity="1.0"></stop><stop offset="0.174603174603" stop-color="rgb(54.2%,55.5%,84.4%)" stop-opacity="1.0"></stop><stop offset="0.190476190476" stop-color="rgb(55.1%,57.7%,85.6%)" stop-opacity="1.0"></stop><stop offset="0.206349206349" stop-color="rgb(56%,59.8%,86.8%)" stop-opacity="1.0"></stop><stop offset="0.222222222222" stop-color="rgb(57%,61.9%,87.8%)" stop-opacity="1.0"></stop><stop offset="0.238095238095" stop-color="rgb(58.1%,64%,88.7%)" stop-opacity="1.0"></stop><stop offset="0.253968253968" stop-color="rgb(59.3%,65.9%,89.5%)" stop-opacity="1.0"></stop><stop offset="0.269841269841" stop-color="rgb(60.5%,67.9%,90.1%)" stop-opacity="1.0"></stop><stop offset="0.285714285714" stop-color="rgb(61.8%,69.7%,90.6%)" stop-opacity="1.0"></stop><stop offset="0.301587301587" stop-color="rgb(63.2%,71.5%,91%)" stop-opacity="1.0"></stop><stop offset="0.31746031746" stop-color="rgb(64.7%,73.2%,91.3%)" stop-opacity="1.0"></stop><stop offset="0.333333333333" stop-color="rgb(66.3%,74.9%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.349206349206" stop-color="rgb(67.9%,76.4%,91.4%)" stop-opacity="1.0"></stop><stop offset="0.365079365079" stop-color="rgb(69.6%,77.9%,91.3%)" stop-opacity="1.0"></stop><stop offset="0.380952380952" stop-color="rgb(71.4%,79.3%,91.1%)" stop-opacity="1.0"></stop><stop offset="0.396825396825" stop-color="rgb(73.3%,80.6%,90.8%)" stop-opacity="1.0"></stop><stop offset="0.412698412698" stop-color="rgb(75.2%,81.8%,90.4%)" stop-opacity="1.0"></stop><stop offset="0.428571428571" stop-color="rgb(77.2%,82.9%,89.9%)" stop-opacity="1.0"></stop><stop offset="0.444444444444" stop-color="rgb(79.2%,83.9%,89.3%)" stop-opacity="1.0"></stop><stop offset="0.460317460317" stop-color="rgb(81.3%,84.8%,88.6%)" stop-opacity="1.0"></stop><stop offset="0.47619047619" stop-color="rgb(83.4%,85.6%,87.8%)" stop-opacity="1.0"></stop><stop offset="0.492063492063" stop-color="rgb(85.5%,86.3%,87%)" stop-opacity="1.0"></stop><stop offset="0.507936507937" stop-color="rgb(85.4%,86.6%,86.3%)" stop-opacity="1.0"></stop><stop offset="0.52380952381" stop-color="rgb(83.1%,86.8%,85.7%)" stop-opacity="1.0"></stop><stop offset="0.539682539683" stop-color="rgb(80.8%,86.9%,84.9%)" stop-opacity="1.0"></stop><stop offset="0.555555555556" stop-color="rgb(78.3%,86.8%,84%)" stop-opacity="1.0"></stop><stop offset="0.571428571429" stop-color="rgb(75.9%,86.7%,83%)" stop-opacity="1.0"></stop><stop offset="0.587301587302" stop-color="rgb(73.4%,86.4%,81.8%)" stop-opacity="1.0"></stop><stop offset="0.603174603175" stop-color="rgb(70.9%,86.1%,80.5%)" stop-opacity="1.0"></stop><stop offset="0.619047619048" stop-color="rgb(68.3%,85.7%,79.1%)" stop-opacity="1.0"></stop><stop offset="0.634920634921" stop-color="rgb(65.7%,85.2%,77.5%)" stop-opacity="1.0"></stop><stop offset="0.650793650794" stop-color="rgb(63.1%,84.6%,75.9%)" stop-opacity="1.0"></stop><stop offset="0.666666666667" stop-color="rgb(60.4%,83.9%,74.1%)" stop-opacity="1.0"></stop><stop offset="0.68253968254" stop-color="rgb(57.8%,83.2%,72.2%)" stop-opacity="1.0"></stop><stop offset="0.698412698413" stop-color="rgb(55.1%,82.3%,70.2%)" stop-opacity="1.0"></stop><stop offset="0.714285714286" stop-color="rgb(52.4%,81.4%,68.1%)" stop-opacity="1.0"></stop><stop offset="0.730158730159" stop-color="rgb(49.7%,80.4%,66%)" stop-opacity="1.0"></stop><stop offset="0.746031746032" stop-color="rgb(47%,79.3%,63.7%)" stop-opacity="1.0"></stop><stop offset="0.761904761905" stop-color="rgb(44.3%,78.1%,61.4%)" stop-opacity="1.0"></stop><stop offset="0.777777777778" stop-color="rgb(41.7%,76.9%,58.9%)" stop-opacity="1.0"></stop><stop offset="0.793650793651" stop-color="rgb(39%,75.6%,56.4%)" stop-opacity="1.0"></stop><stop offset="0.809523809524" stop-color="rgb(36.3%,74.2%,53.9%)" stop-opacity="1.0"></stop><stop offset="0.825396825397" stop-color="rgb(33.6%,72.8%,51.3%)" stop-opacity="1.0"></stop><stop offset="0.84126984127" stop-color="rgb(30.8%,71.3%,48.6%)" stop-opacity="1.0"></stop><stop offset="0.857142857143" stop-color="rgb(28.1%,69.7%,45.9%)" stop-opacity="1.0"></stop><stop offset="0.873015873016" stop-color="rgb(25.4%,68.1%,43.1%)" stop-opacity="1.0"></stop><stop offset="0.888888888889" stop-color="rgb(22.6%,66.5%,40.3%)" stop-opacity="1.0"></stop><stop offset="0.904761904762" stop-color="rgb(19.7%,64.7%,37.4%)" stop-opacity="1.0"></stop><stop offset="0.920634920635" stop-color="rgb(16.7%,63%,34.5%)" stop-opacity="1.0"></stop><stop offset="0.936507936508" stop-color="rgb(13.5%,61.2%,31.6%)" stop-opacity="1.0"></stop><stop offset="0.952380952381" stop-color="rgb(9.85%,59.3%,28.6%)" stop-opacity="1.0"></stop><stop offset="0.968253968254" stop-color="rgb(5.29%,57.5%,25.6%)" stop-opacity="1.0"></stop><stop offset="0.984126984127" stop-color="rgb(0%,55.5%,22.5%)" stop-opacity="1.0"></stop><stop offset="1.0" stop-color="rgb(0%,53.6%,19.3%)" stop-opacity="1.0"></stop></linearGradient></defs><rect height="10" style="fill:url(#tfb4db9922f4447e4990e7b9a393629ac);stroke:none;stroke-width:1.0" width="400.0" x="100.0" y="-5.0"></rect></g><g class="toyplot-mark-Scatterplot" id="tfb05b2f1d9d5433f91f8d775827bf6d9" style="" transform="translate(0,-30.0)"><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(0%,0%,0%);fill-opacity:1.0;opacity:1.0;stroke:rgb(0%,0%,0%);stroke-opacity:1.0"><rect height="4.0" transform="rotate(-45, 200.0, 0)" width="4.0" x="198.0" y="-2.0"></rect></g></g></g></g><g class="toyplot-coordinates-Axis" id="tdddc82347f87488ab42bd2e9acb44caf" transform="translate(50.0,50.0)translate(0,10.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-1.0</text></g><g transform="translate(100.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.615" y="8.555">-0.5</text></g><g transform="translate(200.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(400.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.5</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "tfb05b2f1d9d5433f91f8d775827bf6d9", "columns": [[0.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#t89df5e58eb1c4f2c8c5298cf85eec69a .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t89df5e58eb1c4f2c8c5298cf85eec69a";
                var axes = {"tdddc82347f87488ab42bd2e9acb44caf": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.5, "min": -1.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


Properties
----------

Numberline objects contain sets of nested properties that can be used to
adjust their behavior. The list of available properties includes the
following:

-  numberline.show - set to *False* to hide the numberline completely
   (the plotted data will still be visible).
-  numberline.spacing - the space between each mark added to the
   numberline. Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.padding - the space between the axis spine and the first
   mark. Defaults to the same value as ``spacing``. Uses CSS pixels as
   the default unit, supports all :ref:`units`.
-  numberline.axis.show - set to *False* to hide the axis completely.
-  numberline.axis.scale - "linear", "log" (base 10), "log10", "log2",
   or a ("log", base) tuple. See :ref:`log-scales` for details.
-  numberline.axis.domain.min - override the minimum domain value for
   the axis.
-  numberline.axis.domain.max - override the maximum domain value for
   the axis.
-  numberline.axis.label.location - "above" or "below", to specify on
   which side of the axis the label will be placed.
-  numberline.axis.label.offset - offsets the label from the axis.
   Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.axis.label.text - optional label below the axis.
-  numberline.axis.label.style - styles the axis label.
-  numberline.axis.spine.show - set to *False* to hide the axis spine.
-  numberline.axis.spine.style - styles the axis spine.
-  numberline.axis.ticks.show - set to *True* to display axis tick
   marks.
-  numberline.axis.ticks.locator - assign an instance of
   :py:class:`toyplot.locator.TickLocator` to control the positioning
   and formatting of ticks and tick labels. By default, an appropriate
   locator is automatically chosen based on the axis scale and domain.
   See :ref:`tick-locators` for details.
-  numberline.axis.ticks.location - "above" or "below", to specify on
   which side of the axis the ticks and labels are placed.
-  numberline.axis.ticks.near - length of axis ticks on the same side of
   the axis as the labels. Defaults to CSS pixels, supports all
   :ref:`units`.
-  numberline.axis.ticks.far - length of axis ticks on the side of the
   axis opposite the labels. Defaults to CSS pixels, supports all
   :ref:`units`.
-  numberline.axis.ticks.style - styles the axis ticks.
-  numberline.axis.ticks.labels.angle - angle of axis tick labels in
   degrees.
-  numberline.axis.ticks.labels.offset - offsets labels from the axis.
   Defaults to CSS pixels, supports all :ref:`units`.
-  numberline.axis.ticks.labels.show - set to *False* to hide axis tick
   labels.

-  numberline.axis.ticks.labels.style - style axis tick label text.

As a convenience, some of the most common properties can also be set
when the numberline is created.

Layout
------

Unlike cartesian or table coordinates that are defined over an area of
the canvas, numberlines are defined by two endpoints in canvas
coordinates. When you use :ref:`canvas-layout` functions, you create
numberlines that are horizontal and centered within the bounds of the
area you define:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=200, style={"border":"1px solid lightgray"})
    
    numberline = canvas.numberline(grid=(2, 1, 0))
    numberline.scatterplot(numpy.linspace(0, 1))
    
    numberline = canvas.numberline(grid=(2, 1, 1))
    numberline.scatterplot(numpy.linspace(0, 1));



.. raw:: html

    <div align="center" class="toyplot" id="t71831eef24424be1b4b8fd676f85ccf3"><svg class="toyplot-canvas-Canvas" height="200.0px" id="t61b6ec28e9f0406ca3b7531fe0b4102b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border:1px solid lightgray;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 200.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="t2e1ef2b870774aa78ac15c242fca85dd"><clipPath id="tba8f3620055c4f9ea109e5cfb187f756"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tba8f3620055c4f9ea109e5cfb187f756)" transform="translate(50.0,50.0)"><g class="toyplot-mark-Scatterplot" id="te374ed2d2e224a1a8e90759fd2929ca1" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="0.0" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="10.204081632653061" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.408163265306122" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="30.612244897959183" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.816326530612244" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="51.020408163265301" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.224489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="71.428571428571431" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="81.632653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.836734693877546" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="102.0408163265306" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.24489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="122.44897959183673" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="132.65306122448979" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.85714285714286" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="153.0612244897959" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="163.26530612244898" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="173.46938775510205" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="183.67346938775509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="193.87755102040816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="204.08163265306121" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="214.28571428571428" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="224.48979591836732" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="234.69387755102039" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.89795918367346" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="255.10204081632654" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.30612244897958" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.51020408163265" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.71428571428572" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.91836734693879" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.12244897959181" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.32653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.53061224489795" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.73469387755102" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.9387755102041" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.14285714285711" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="367.34693877551018" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="377.55102040816325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="387.75510204081633" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="397.95918367346934" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="408.16326530612241" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="418.36734693877548" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="428.57142857142856" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="438.77551020408163" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="448.97959183673464" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="459.18367346938771" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="469.38775510204079" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.59183673469386" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="489.79591836734693" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="tb98598cdfe57436b993d4a85e5199cbd" transform="translate(50.0,50.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t477656364a184a1283430d8d0f98c606"><clipPath id="tc22541c731be460da07bdb0ab8095ec6"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#tc22541c731be460da07bdb0ab8095ec6)" transform="translate(50.0,150.0)"><g class="toyplot-mark-Scatterplot" id="td2cb58acf0694ab29da8170b46700fa2" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="0.0" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="10.204081632653061" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="20.408163265306122" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="30.612244897959183" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="40.816326530612244" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="51.020408163265301" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="61.224489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="71.428571428571431" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="81.632653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="91.836734693877546" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="102.0408163265306" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="112.24489795918366" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="122.44897959183673" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="132.65306122448979" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="142.85714285714286" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="153.0612244897959" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="163.26530612244898" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="173.46938775510205" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="183.67346938775509" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="193.87755102040816" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="204.08163265306121" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="214.28571428571428" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="224.48979591836732" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="234.69387755102039" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="244.89795918367346" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="255.10204081632654" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="265.30612244897958" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="275.51020408163265" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="285.71428571428572" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="295.91836734693879" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="306.12244897959181" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="316.32653061224488" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="326.53061224489795" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="336.73469387755102" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="346.9387755102041" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="357.14285714285711" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="367.34693877551018" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="377.55102040816325" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="387.75510204081633" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="397.95918367346934" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="408.16326530612241" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="418.36734693877548" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="428.57142857142856" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="438.77551020408163" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="448.97959183673464" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="459.18367346938771" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="469.38775510204079" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="479.59183673469386" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="489.79591836734693" cy="0" r="2.0"></circle></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><circle cx="500.0" cy="0" r="2.0"></circle></g></g></g></g><g class="toyplot-coordinates-Axis" id="t30645736b995427184b72a0621968f78" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "te374ed2d2e224a1a8e90759fd2929ca1", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "td2cb58acf0694ab29da8170b46700fa2", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#t71831eef24424be1b4b8fd676f85ccf3 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t71831eef24424be1b4b8fd676f85ccf3";
                var axes = {"t30645736b995427184b72a0621968f78": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tb98598cdfe57436b993d4a85e5199cbd": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>


If you look carefully at the above plot, you will see that the *data* is
centered within each cell in the :math:`2 \times 1` grid defined by the
layout.

However, you can also specify the endpoints of a numberline explicitly,
which allows you to create numberlines in any orientation including
diagonal:

.. code:: python

    canvas = toyplot.Canvas(width=600, style={"border":"1px solid lightgray"})
    
    numberline = canvas.numberline(x1=-50, x2=50, y1=100, y2=100, label="Right to left")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=50, x2=-50, y1=150, y2=150, label="Left to right")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=100, x2=100, y1=250, y2=-50, label="Top to bottom")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=150, x2=150, y1=-50, y2=250, label="Bottom to top")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15)
    
    numberline = canvas.numberline(x1=250, x2=-50, y1=-50, y2=250, label="Diagonal")
    numberline.scatterplot(numpy.linspace(0, 1), marker="|", size=15);



.. raw:: html

    <div align="center" class="toyplot" id="t92356a36e5b74855ba1576816f4727d1"><svg class="toyplot-canvas-Canvas" height="600.0px" id="tf04efe1f0de941cf8dab6f10bf417a6b" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;border:1px solid lightgray;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 600.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Numberline" id="ta5a7502b6ac84258abdb9b49ee7bd604"><clipPath id="t11ed04980ba043aa9e37b281258d25c9"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t11ed04980ba043aa9e37b281258d25c9)" transform="translate(550.0,100.0)rotate(180.0)"><g class="toyplot-mark-Scatterplot" id="t2699315103294759826754c3ddc18a05" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 10.204081632653061, 0)" x1="10.204081632653061" x2="10.204081632653061" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 20.408163265306122, 0)" x1="20.408163265306122" x2="20.408163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959183, 0)" x1="30.612244897959183" x2="30.612244897959183" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 40.816326530612244, 0)" x1="40.816326530612244" x2="40.816326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 51.020408163265301, 0)" x1="51.020408163265301" x2="51.020408163265301" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918366, 0)" x1="61.224489795918366" x2="61.224489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 71.428571428571431, 0)" x1="71.428571428571431" x2="71.428571428571431" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 81.632653061224488, 0)" x1="81.632653061224488" x2="81.632653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877546, 0)" x1="91.836734693877546" x2="91.836734693877546" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 102.0408163265306, 0)" x1="102.0408163265306" x2="102.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 112.24489795918366, 0)" x1="112.24489795918366" x2="112.24489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183673, 0)" x1="122.44897959183673" x2="122.44897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 132.65306122448979, 0)" x1="132.65306122448979" x2="132.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 142.85714285714286, 0)" x1="142.85714285714286" x2="142.85714285714286" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.0612244897959, 0)" x1="153.0612244897959" x2="153.0612244897959" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 163.26530612244898, 0)" x1="163.26530612244898" x2="163.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 173.46938775510205, 0)" x1="173.46938775510205" x2="173.46938775510205" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775509, 0)" x1="183.67346938775509" x2="183.67346938775509" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 193.87755102040816, 0)" x1="193.87755102040816" x2="193.87755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 204.08163265306121, 0)" x1="204.08163265306121" x2="204.08163265306121" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571428, 0)" x1="214.28571428571428" x2="214.28571428571428" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 224.48979591836732, 0)" x1="224.48979591836732" x2="224.48979591836732" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 234.69387755102039, 0)" x1="234.69387755102039" x2="234.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367346, 0)" x1="244.89795918367346" x2="244.89795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 255.10204081632654, 0)" x1="255.10204081632654" x2="255.10204081632654" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 265.30612244897958, 0)" x1="265.30612244897958" x2="265.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 285.71428571428572, 0)" x1="285.71428571428572" x2="285.71428571428572" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 295.91836734693879, 0)" x1="295.91836734693879" x2="295.91836734693879" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 306.12244897959181, 0)" x1="306.12244897959181" x2="306.12244897959181" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 316.32653061224488, 0)" x1="316.32653061224488" x2="316.32653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 326.53061224489795, 0)" x1="326.53061224489795" x2="326.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 336.73469387755102, 0)" x1="336.73469387755102" x2="336.73469387755102" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 346.9387755102041, 0)" x1="346.9387755102041" x2="346.9387755102041" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 357.14285714285711, 0)" x1="357.14285714285711" x2="357.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 367.34693877551018, 0)" x1="367.34693877551018" x2="367.34693877551018" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 377.55102040816325, 0)" x1="377.55102040816325" x2="377.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 387.75510204081633, 0)" x1="387.75510204081633" x2="387.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 397.95918367346934, 0)" x1="397.95918367346934" x2="397.95918367346934" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 408.16326530612241, 0)" x1="408.16326530612241" x2="408.16326530612241" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 418.36734693877548, 0)" x1="418.36734693877548" x2="418.36734693877548" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 428.57142857142856, 0)" x1="428.57142857142856" x2="428.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 438.77551020408163, 0)" x1="438.77551020408163" x2="438.77551020408163" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 448.97959183673464, 0)" x1="448.97959183673464" x2="448.97959183673464" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 459.18367346938771, 0)" x1="459.18367346938771" x2="459.18367346938771" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 469.38775510204079, 0)" x1="469.38775510204079" x2="469.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 479.59183673469386, 0)" x1="479.59183673469386" x2="479.59183673469386" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 489.79591836734693, 0)" x1="489.79591836734693" x2="489.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 500.0, 0)" x1="500.0" x2="500.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="td5c63012227347c0a6728c638a454c53" transform="translate(550.0,100.0)rotate(180.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(250.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-33.33" y="10.266">Right to left</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t808863b79a4f4dac854aef6df7d4f8cb"><clipPath id="t20e3303c3e814c48aef9718460fe6c62"><rect height="40.0" width="500.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t20e3303c3e814c48aef9718460fe6c62)" transform="translate(50.0,150.0)"><g class="toyplot-mark-Scatterplot" id="t28fbc69a849d40899701a6db1ce93a9c" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 10.204081632653061, 0)" x1="10.204081632653061" x2="10.204081632653061" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 20.408163265306122, 0)" x1="20.408163265306122" x2="20.408163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959183, 0)" x1="30.612244897959183" x2="30.612244897959183" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 40.816326530612244, 0)" x1="40.816326530612244" x2="40.816326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 51.020408163265301, 0)" x1="51.020408163265301" x2="51.020408163265301" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918366, 0)" x1="61.224489795918366" x2="61.224489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 71.428571428571431, 0)" x1="71.428571428571431" x2="71.428571428571431" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 81.632653061224488, 0)" x1="81.632653061224488" x2="81.632653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877546, 0)" x1="91.836734693877546" x2="91.836734693877546" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 102.0408163265306, 0)" x1="102.0408163265306" x2="102.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 112.24489795918366, 0)" x1="112.24489795918366" x2="112.24489795918366" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183673, 0)" x1="122.44897959183673" x2="122.44897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 132.65306122448979, 0)" x1="132.65306122448979" x2="132.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 142.85714285714286, 0)" x1="142.85714285714286" x2="142.85714285714286" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.0612244897959, 0)" x1="153.0612244897959" x2="153.0612244897959" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 163.26530612244898, 0)" x1="163.26530612244898" x2="163.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 173.46938775510205, 0)" x1="173.46938775510205" x2="173.46938775510205" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775509, 0)" x1="183.67346938775509" x2="183.67346938775509" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 193.87755102040816, 0)" x1="193.87755102040816" x2="193.87755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 204.08163265306121, 0)" x1="204.08163265306121" x2="204.08163265306121" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571428, 0)" x1="214.28571428571428" x2="214.28571428571428" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 224.48979591836732, 0)" x1="224.48979591836732" x2="224.48979591836732" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 234.69387755102039, 0)" x1="234.69387755102039" x2="234.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367346, 0)" x1="244.89795918367346" x2="244.89795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 255.10204081632654, 0)" x1="255.10204081632654" x2="255.10204081632654" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 265.30612244897958, 0)" x1="265.30612244897958" x2="265.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 285.71428571428572, 0)" x1="285.71428571428572" x2="285.71428571428572" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 295.91836734693879, 0)" x1="295.91836734693879" x2="295.91836734693879" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 306.12244897959181, 0)" x1="306.12244897959181" x2="306.12244897959181" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 316.32653061224488, 0)" x1="316.32653061224488" x2="316.32653061224488" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 326.53061224489795, 0)" x1="326.53061224489795" x2="326.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 336.73469387755102, 0)" x1="336.73469387755102" x2="336.73469387755102" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 346.9387755102041, 0)" x1="346.9387755102041" x2="346.9387755102041" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 357.14285714285711, 0)" x1="357.14285714285711" x2="357.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 367.34693877551018, 0)" x1="367.34693877551018" x2="367.34693877551018" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 377.55102040816325, 0)" x1="377.55102040816325" x2="377.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 387.75510204081633, 0)" x1="387.75510204081633" x2="387.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 397.95918367346934, 0)" x1="397.95918367346934" x2="397.95918367346934" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 408.16326530612241, 0)" x1="408.16326530612241" x2="408.16326530612241" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 418.36734693877548, 0)" x1="418.36734693877548" x2="418.36734693877548" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 428.57142857142856, 0)" x1="428.57142857142856" x2="428.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 438.77551020408163, 0)" x1="438.77551020408163" x2="438.77551020408163" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 448.97959183673464, 0)" x1="448.97959183673464" x2="448.97959183673464" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 459.18367346938771, 0)" x1="459.18367346938771" x2="459.18367346938771" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 469.38775510204079, 0)" x1="469.38775510204079" x2="469.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 479.59183673469386, 0)" x1="479.59183673469386" x2="479.59183673469386" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 489.79591836734693, 0)" x1="489.79591836734693" x2="489.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 500.0, 0)" x1="500.0" x2="500.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="t1a750b9686c040f8a26bdc2f4f922614" transform="translate(50.0,150.0)translate(0,20.0)"><line style="" x1="0" x2="500.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(250.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-33.33" y="10.266">Left to right</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t57053154d06d40aa8d4fb1111408d64b"><clipPath id="t7d4277e637bf4993a3e966c41157d5ba"><rect height="40.0" width="300.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t7d4277e637bf4993a3e966c41157d5ba)" transform="translate(100.0,250.0)rotate(90.0)"><g class="toyplot-mark-Scatterplot" id="t7ef92075f65f4a2189886453c3954c42" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 6.1224489795918364, 0)" x1="6.1224489795918364" x2="6.1224489795918364" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 12.244897959183673, 0)" x1="12.244897959183673" x2="12.244897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 18.367346938775508, 0)" x1="18.367346938775508" x2="18.367346938775508" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 24.489795918367346, 0)" x1="24.489795918367346" x2="24.489795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959179, 0)" x1="30.612244897959179" x2="30.612244897959179" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 36.734693877551017, 0)" x1="36.734693877551017" x2="36.734693877551017" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 42.857142857142854, 0)" x1="42.857142857142854" x2="42.857142857142854" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 48.979591836734691, 0)" x1="48.979591836734691" x2="48.979591836734691" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 55.102040816326522, 0)" x1="55.102040816326522" x2="55.102040816326522" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918359, 0)" x1="61.224489795918359" x2="61.224489795918359" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 67.346938775510196, 0)" x1="67.346938775510196" x2="67.346938775510196" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 73.469387755102034, 0)" x1="73.469387755102034" x2="73.469387755102034" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 79.591836734693871, 0)" x1="79.591836734693871" x2="79.591836734693871" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 85.714285714285708, 0)" x1="85.714285714285708" x2="85.714285714285708" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877531, 0)" x1="91.836734693877531" x2="91.836734693877531" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 97.959183673469383, 0)" x1="97.959183673469383" x2="97.959183673469383" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 104.08163265306122, 0)" x1="104.08163265306122" x2="104.08163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 110.20408163265304, 0)" x1="110.20408163265304" x2="110.20408163265304" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 116.32653061224489, 0)" x1="116.32653061224489" x2="116.32653061224489" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183672, 0)" x1="122.44897959183672" x2="122.44897959183672" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 128.57142857142856, 0)" x1="128.57142857142856" x2="128.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 134.69387755102039, 0)" x1="134.69387755102039" x2="134.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 140.81632653061223, 0)" x1="140.81632653061223" x2="140.81632653061223" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 146.93877551020407, 0)" x1="146.93877551020407" x2="146.93877551020407" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.06122448979593, 0)" x1="153.06122448979593" x2="153.06122448979593" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 159.18367346938774, 0)" x1="159.18367346938774" x2="159.18367346938774" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 165.30612244897958, 0)" x1="165.30612244897958" x2="165.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 171.42857142857142, 0)" x1="171.42857142857142" x2="171.42857142857142" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 177.55102040816325, 0)" x1="177.55102040816325" x2="177.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775506, 0)" x1="183.67346938775506" x2="183.67346938775506" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 189.79591836734693, 0)" x1="189.79591836734693" x2="189.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 195.91836734693877, 0)" x1="195.91836734693877" x2="195.91836734693877" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 202.0408163265306, 0)" x1="202.0408163265306" x2="202.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 208.16326530612244, 0)" x1="208.16326530612244" x2="208.16326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571425, 0)" x1="214.28571428571425" x2="214.28571428571425" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 220.40816326530609, 0)" x1="220.40816326530609" x2="220.40816326530609" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 226.53061224489795, 0)" x1="226.53061224489795" x2="226.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 232.65306122448979, 0)" x1="232.65306122448979" x2="232.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 238.7755102040816, 0)" x1="238.7755102040816" x2="238.7755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367344, 0)" x1="244.89795918367344" x2="244.89795918367344" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 251.02040816326527, 0)" x1="251.02040816326527" x2="251.02040816326527" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 257.14285714285711, 0)" x1="257.14285714285711" x2="257.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 263.26530612244898, 0)" x1="263.26530612244898" x2="263.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 269.38775510204079, 0)" x1="269.38775510204079" x2="269.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 281.63265306122446, 0)" x1="281.63265306122446" x2="281.63265306122446" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 287.75510204081633, 0)" x1="287.75510204081633" x2="287.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 293.87755102040813, 0)" x1="293.87755102040813" x2="293.87755102040813" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 300.0, 0)" x1="300.0" x2="300.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="tffd80744f4944189a8c3c93f404fc36e" transform="translate(100.0,250.0)rotate(90.0)translate(0,20.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(150.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-40.326" y="10.266">Top to bottom</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="t103e04188a6c4ab3b9edd85cf2c3dd93"><clipPath id="t3a2c4fe7240b40c7a1bc5fb0d40b72c7"><rect height="40.0" width="300.0" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t3a2c4fe7240b40c7a1bc5fb0d40b72c7)" transform="translate(150.0,550.0)rotate(-90.0)"><g class="toyplot-mark-Scatterplot" id="tbb916f3781c746989eb215c2e07dfc05" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 6.1224489795918364, 0)" x1="6.1224489795918364" x2="6.1224489795918364" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 12.244897959183673, 0)" x1="12.244897959183673" x2="12.244897959183673" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 18.367346938775508, 0)" x1="18.367346938775508" x2="18.367346938775508" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 24.489795918367346, 0)" x1="24.489795918367346" x2="24.489795918367346" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 30.612244897959179, 0)" x1="30.612244897959179" x2="30.612244897959179" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 36.734693877551017, 0)" x1="36.734693877551017" x2="36.734693877551017" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 42.857142857142854, 0)" x1="42.857142857142854" x2="42.857142857142854" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 48.979591836734691, 0)" x1="48.979591836734691" x2="48.979591836734691" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 55.102040816326522, 0)" x1="55.102040816326522" x2="55.102040816326522" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 61.224489795918359, 0)" x1="61.224489795918359" x2="61.224489795918359" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 67.346938775510196, 0)" x1="67.346938775510196" x2="67.346938775510196" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 73.469387755102034, 0)" x1="73.469387755102034" x2="73.469387755102034" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 79.591836734693871, 0)" x1="79.591836734693871" x2="79.591836734693871" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 85.714285714285708, 0)" x1="85.714285714285708" x2="85.714285714285708" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 91.836734693877531, 0)" x1="91.836734693877531" x2="91.836734693877531" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 97.959183673469383, 0)" x1="97.959183673469383" x2="97.959183673469383" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 104.08163265306122, 0)" x1="104.08163265306122" x2="104.08163265306122" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 110.20408163265304, 0)" x1="110.20408163265304" x2="110.20408163265304" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 116.32653061224489, 0)" x1="116.32653061224489" x2="116.32653061224489" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 122.44897959183672, 0)" x1="122.44897959183672" x2="122.44897959183672" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 128.57142857142856, 0)" x1="128.57142857142856" x2="128.57142857142856" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 134.69387755102039, 0)" x1="134.69387755102039" x2="134.69387755102039" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 140.81632653061223, 0)" x1="140.81632653061223" x2="140.81632653061223" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 146.93877551020407, 0)" x1="146.93877551020407" x2="146.93877551020407" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 153.06122448979593, 0)" x1="153.06122448979593" x2="153.06122448979593" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 159.18367346938774, 0)" x1="159.18367346938774" x2="159.18367346938774" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 165.30612244897958, 0)" x1="165.30612244897958" x2="165.30612244897958" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 171.42857142857142, 0)" x1="171.42857142857142" x2="171.42857142857142" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 177.55102040816325, 0)" x1="177.55102040816325" x2="177.55102040816325" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 183.67346938775506, 0)" x1="183.67346938775506" x2="183.67346938775506" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 189.79591836734693, 0)" x1="189.79591836734693" x2="189.79591836734693" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 195.91836734693877, 0)" x1="195.91836734693877" x2="195.91836734693877" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 202.0408163265306, 0)" x1="202.0408163265306" x2="202.0408163265306" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 208.16326530612244, 0)" x1="208.16326530612244" x2="208.16326530612244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 214.28571428571425, 0)" x1="214.28571428571425" x2="214.28571428571425" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 220.40816326530609, 0)" x1="220.40816326530609" x2="220.40816326530609" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 226.53061224489795, 0)" x1="226.53061224489795" x2="226.53061224489795" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 232.65306122448979, 0)" x1="232.65306122448979" x2="232.65306122448979" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 238.7755102040816, 0)" x1="238.7755102040816" x2="238.7755102040816" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 244.89795918367344, 0)" x1="244.89795918367344" x2="244.89795918367344" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 251.02040816326527, 0)" x1="251.02040816326527" x2="251.02040816326527" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 257.14285714285711, 0)" x1="257.14285714285711" x2="257.14285714285711" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 263.26530612244898, 0)" x1="263.26530612244898" x2="263.26530612244898" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 269.38775510204079, 0)" x1="269.38775510204079" x2="269.38775510204079" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 275.51020408163265, 0)" x1="275.51020408163265" x2="275.51020408163265" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 281.63265306122446, 0)" x1="281.63265306122446" x2="281.63265306122446" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 287.75510204081633, 0)" x1="287.75510204081633" x2="287.75510204081633" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 293.87755102040813, 0)" x1="293.87755102040813" x2="293.87755102040813" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 300.0, 0)" x1="300.0" x2="300.0" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="t4193df973f51443d921e17c021c8fc70" transform="translate(150.0,550.0)rotate(-90.0)translate(0,20.0)"><line style="" x1="0" x2="300.0" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(150.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(300.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(150.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-39.324" y="10.266">Bottom to top</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g><g class="toyplot-coordinates-Numberline" id="tbb292706879c4c2bac7599ee51d06fc7"><clipPath id="t2a2b67aece9a49d3a89b688631901543"><rect height="40.0" width="424.26406871192853" x="0" y="-20.0"></rect></clipPath><g clip-path="url(#t2a2b67aece9a49d3a89b688631901543)" transform="translate(250.0,550.0)rotate(-45.0)"><g class="toyplot-mark-Scatterplot" id="t9fbd858964ad41fc977d0fb24236509f" style=""><g class="toyplot-Series"><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 0.0, 0)" x1="0.0" x2="0.0" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 8.6584503818760918, 0)" x1="8.6584503818760918" x2="8.6584503818760918" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 17.316900763752184, 0)" x1="17.316900763752184" x2="17.316900763752184" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 25.975351145628277, 0)" x1="25.975351145628277" x2="25.975351145628277" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 34.633801527504367, 0)" x1="34.633801527504367" x2="34.633801527504367" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 43.292251909380454, 0)" x1="43.292251909380454" x2="43.292251909380454" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 51.950702291256555, 0)" x1="51.950702291256555" x2="51.950702291256555" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 60.609152673132641, 0)" x1="60.609152673132641" x2="60.609152673132641" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 69.267603055008735, 0)" x1="69.267603055008735" x2="69.267603055008735" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 77.926053436884828, 0)" x1="77.926053436884828" x2="77.926053436884828" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 86.584503818760908, 0)" x1="86.584503818760908" x2="86.584503818760908" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 95.242954200637001, 0)" x1="95.242954200637001" x2="95.242954200637001" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 103.90140458251311, 0)" x1="103.90140458251311" x2="103.90140458251311" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 112.55985496438919, 0)" x1="112.55985496438919" x2="112.55985496438919" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 121.21830534626528, 0)" x1="121.21830534626528" x2="121.21830534626528" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 129.87675572814138, 0)" x1="129.87675572814138" x2="129.87675572814138" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 138.53520611001747, 0)" x1="138.53520611001747" x2="138.53520611001747" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 147.19365649189356, 0)" x1="147.19365649189356" x2="147.19365649189356" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 155.85210687376966, 0)" x1="155.85210687376966" x2="155.85210687376966" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 164.51055725564575, 0)" x1="164.51055725564575" x2="164.51055725564575" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 173.16900763752182, 0)" x1="173.16900763752182" x2="173.16900763752182" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 181.82745801939794, 0)" x1="181.82745801939794" x2="181.82745801939794" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 190.485908401274, 0)" x1="190.485908401274" x2="190.485908401274" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 199.14435878315012, 0)" x1="199.14435878315012" x2="199.14435878315012" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 207.80280916502622, 0)" x1="207.80280916502622" x2="207.80280916502622" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 216.46125954690231, 0)" x1="216.46125954690231" x2="216.46125954690231" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 225.11970992877838, 0)" x1="225.11970992877838" x2="225.11970992877838" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 233.77816031065447, 0)" x1="233.77816031065447" x2="233.77816031065447" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 242.43661069253056, 0)" x1="242.43661069253056" x2="242.43661069253056" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 251.09506107440669, 0)" x1="251.09506107440669" x2="251.09506107440669" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 259.75351145628275, 0)" x1="259.75351145628275" x2="259.75351145628275" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 268.41196183815885, 0)" x1="268.41196183815885" x2="268.41196183815885" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 277.07041222003494, 0)" x1="277.07041222003494" x2="277.07041222003494" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 285.72886260191103, 0)" x1="285.72886260191103" x2="285.72886260191103" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 294.38731298378713, 0)" x1="294.38731298378713" x2="294.38731298378713" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 303.04576336566322, 0)" x1="303.04576336566322" x2="303.04576336566322" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 311.70421374753931, 0)" x1="311.70421374753931" x2="311.70421374753931" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 320.36266412941541, 0)" x1="320.36266412941541" x2="320.36266412941541" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 329.0211145112915, 0)" x1="329.0211145112915" x2="329.0211145112915" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 337.67956489316754, 0)" x1="337.67956489316754" x2="337.67956489316754" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 346.33801527504363, 0)" x1="346.33801527504363" x2="346.33801527504363" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 354.99646565691978, 0)" x1="354.99646565691978" x2="354.99646565691978" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 363.65491603879588, 0)" x1="363.65491603879588" x2="363.65491603879588" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 372.31336642067197, 0)" x1="372.31336642067197" x2="372.31336642067197" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 380.97181680254801, 0)" x1="380.97181680254801" x2="380.97181680254801" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 389.6302671844241, 0)" x1="389.6302671844241" x2="389.6302671844241" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 398.28871756630025, 0)" x1="398.28871756630025" x2="398.28871756630025" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 406.94716794817634, 0)" x1="406.94716794817634" x2="406.94716794817634" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 415.60561833005244, 0)" x1="415.60561833005244" x2="415.60561833005244" y1="-7.5" y2="7.5"></line></g><g class="toyplot-Datum" style="fill:rgb(40%,76.1%,64.7%);fill-opacity:1.0;opacity:1.0;stroke:rgb(40%,76.1%,64.7%);stroke-opacity:1.0"><line transform="rotate(0, 424.26406871192853, 0)" x1="424.26406871192853" x2="424.26406871192853" y1="-7.5" y2="7.5"></line></g></g></g></g><g class="toyplot-coordinates-Axis" id="ta48277951e52427aafb11728f601a3ac" transform="translate(250.0,550.0)rotate(-45.0)translate(0,20.0)"><line style="" x1="0" x2="424.26406871192853" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.0</text></g><g transform="translate(212.13203435596427,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">0.5</text></g><g transform="translate(424.26406871192853,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-6.95" y="8.555">1.0</text></g></g><g transform="translate(212.13203435596427,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-25.338" y="10.266">Diagonal</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g></g></svg><div class="toyplot-interactive"><ul class="toyplot-mark-popup" onmouseleave="this.style.visibility='hidden'" style="background:rgba(0%,0%,0%,0.75);border:0;border-radius:6px;color:white;cursor:default;list-style:none;margin:0;padding:5px;position:fixed;visibility:hidden">
                <li class="toyplot-mark-popup-title" style="color:lightgray;cursor:default;padding:5px;list-style:none;margin:0"></li>
                <li class="toyplot-mark-popup-save-csv" onmouseout="this.style.color='white';this.style.background='steelblue'" onmouseover="this.style.color='steelblue';this.style.background='white'" style="border-radius:3px;padding:5px;list-style:none;margin:0">
                    Save as .csv
                </li>
            </ul><script>
            (function()
            {
              var data_tables = [{"title": "Scatterplot Data", "names": ["x0"], "id": "t2699315103294759826754c3ddc18a05", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "t28fbc69a849d40899701a6db1ce93a9c", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "t7ef92075f65f4a2189886453c3954c42", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "tbb916f3781c746989eb215c2e07dfc05", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}, {"title": "Scatterplot Data", "names": ["x0"], "id": "t9fbd858964ad41fc977d0fb24236509f", "columns": [[0.0, 0.02040816326530612, 0.04081632653061224, 0.061224489795918366, 0.08163265306122448, 0.1020408163265306, 0.12244897959183673, 0.14285714285714285, 0.16326530612244897, 0.18367346938775508, 0.2040816326530612, 0.22448979591836732, 0.24489795918367346, 0.26530612244897955, 0.2857142857142857, 0.3061224489795918, 0.32653061224489793, 0.3469387755102041, 0.36734693877551017, 0.3877551020408163, 0.4081632653061224, 0.42857142857142855, 0.44897959183673464, 0.4693877551020408, 0.4897959183673469, 0.5102040816326531, 0.5306122448979591, 0.5510204081632653, 0.5714285714285714, 0.5918367346938775, 0.6122448979591836, 0.6326530612244897, 0.6530612244897959, 0.673469387755102, 0.6938775510204082, 0.7142857142857142, 0.7346938775510203, 0.7551020408163265, 0.7755102040816326, 0.7959183673469387, 0.8163265306122448, 0.836734693877551, 0.8571428571428571, 0.8775510204081632, 0.8979591836734693, 0.9183673469387754, 0.9387755102040816, 0.9591836734693877, 0.9795918367346939, 1.0]], "filename": "toyplot"}];
    
              function save_csv(data_table)
              {
                var uri = "data:text/csv;charset=utf-8,";
                uri += data_table.names.join(",") + "\n";
                for(var i = 0; i != data_table.columns[0].length; ++i)
                {
                  for(var j = 0; j != data_table.columns.length; ++j)
                  {
                    if(j)
                      uri += ",";
                    uri += data_table.columns[j][i];
                  }
                  uri += "\n";
                }
                uri = encodeURI(uri);
    
                var link = document.createElement("a");
                if(typeof link.download != "undefined")
                {
                  link.href = uri;
                  link.style = "visibility:hidden";
                  link.download = data_table.filename + ".csv";
    
                  document.body.appendChild(link);
                  link.click();
                  document.body.removeChild(link);
                }
                else
                {
                  window.open(uri);
                }
              }
    
              function open_popup(data_table)
              {
                return function(e)
                {
                  var popup = document.querySelector("#t92356a36e5b74855ba1576816f4727d1 .toyplot-mark-popup");
                  popup.querySelector(".toyplot-mark-popup-title").innerHTML = data_table.title;
                  popup.querySelector(".toyplot-mark-popup-save-csv").onclick = function() { popup.style.visibility = "hidden"; save_csv(data_table); }
                  popup.style.left = (e.clientX - 50) + "px";
                  popup.style.top = (e.clientY - 20) + "px";
                  popup.style.visibility = "visible";
                  e.stopPropagation();
                  e.preventDefault();
                }
    
              }
    
              for(var i = 0; i != data_tables.length; ++i)
              {
                var data_table = data_tables[i];
                var event_target = document.querySelector("#" + data_table.id);
                event_target.oncontextmenu = open_popup(data_table);
              }
            })();
            </script><script>
            (function()
            {
                function _sign(x)
                {
                    return x < 0 ? -1 : x > 0 ? 1 : 0;
                }
    
                function _mix(a, b, amount)
                {
                    return ((1.0 - amount) * a) + (amount * b);
                }
    
                function _log(x, base)
                {
                    return Math.log(Math.abs(x)) / Math.log(base);
                }
    
                function _in_range(a, x, b)
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
                        if(_in_range(segment.range.min, range, segment.range.max))
                            return true;
                    }
                    return false;
                }
    
                function to_domain(range, projection)
                {
                    for(var i = 0; i != projection.length; ++i)
                    {
                        var segment = projection[i];
                        if(_in_range(segment.range.bounds.min, range, segment.range.bounds.max))
                        {
                            if(segment.scale == "linear")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                return _mix(segment.domain.min, segment.domain.max, amount)
                            }
                            else if(segment.scale[0] == "log")
                            {
                                var amount = (range - segment.range.min) / (segment.range.max - segment.range.min);
                                var base = segment.scale[1];
                                return _sign(segment.domain.min) * Math.pow(base, _mix(_log(segment.domain.min, base), _log(segment.domain.max, base), amount));
                            }
                        }
                    }
                }
    
                function display_coordinates(e)
                {
                    var current = svg.createSVGPoint();
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
    
                var root_id = "t92356a36e5b74855ba1576816f4727d1";
                var axes = {"t1a750b9686c040f8a26bdc2f4f922614": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "t4193df973f51443d921e17c021c8fc70": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}], "ta48277951e52427aafb11728f601a3ac": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 424.26406871192853, "min": 0.0}, "scale": "linear"}], "td5c63012227347c0a6728c638a454c53": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}], "tffd80744f4944189a8c3c93f404fc36e": [{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 1.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 300.0, "min": 0.0}, "scale": "linear"}]};
    
                var svg = document.querySelector("#" + root_id + " svg");
                svg.addEventListener("click", display_coordinates);
            })();
            </script></div></div>

