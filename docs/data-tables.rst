
  .. image:: ../artwork/toyplot.png
    :width: 200px
    :align: right
  
.. _data-tables:

Data Tables
===========

Overview
--------

Data tables, with *rows* containing *observations* and *columns*
containing *variables* or *series*, are arguably the cornerstone of
science. Much of the functionality of Toyplot or any other plotting
package can be reduced to a process of mapping data series from tables
to properties like coordinates and colors. To facilitate this, Toyplot
provides :class:`toyplot.data.Table` - an ordered, heterogeneous
collection of named, equal-length *columns*, where each column is a
Numpy *masked array*. Toyplot data tables are used for internal storage
and manipulation by all of the individual types of plot, and can be
useful for managing data prior to ingestion into Toyplot.

Be careful not to confuse the data tables described in this section with
:ref:`table-coordinates`, which are used to visualize tabular data.

.. code:: python

    import toyplot.data
    import numpy

.. code:: python

    table = toyplot.data.Table()
    table["x"] = numpy.arange(10)
    table["x*2"] = table["x"] * 2
    table["x^2"] = table["x"] ** 2
    table




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x</th><th style="text-align:left;border:none;padding-right:1em;">x*2</th><th style="text-align:left;border:none;padding-right:1em;">x^2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">0</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">1</td><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">1</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">4</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">6</td><td style="border:none;padding-right:1em;">9</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">8</td><td style="border:none;padding-right:1em;">16</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">5</td><td style="border:none;padding-right:1em;">10</td><td style="border:none;padding-right:1em;">25</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">6</td><td style="border:none;padding-right:1em;">12</td><td style="border:none;padding-right:1em;">36</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">7</td><td style="border:none;padding-right:1em;">14</td><td style="border:none;padding-right:1em;">49</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">8</td><td style="border:none;padding-right:1em;">16</td><td style="border:none;padding-right:1em;">64</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">9</td><td style="border:none;padding-right:1em;">18</td><td style="border:none;padding-right:1em;">81</td></tr></table>



You can see from this small example that Toyplot tables provide
automatic pretty-printing when used with Jupyter notebooks, like other
Toyplot objects (Jupyter pretty-printing is provided as a convenience -
to create tabular data graphics, you will likely want the additional
control provided by :ref:`table-coordinates`).

A Toyplot table behaves like a Python dict that maps column names (keys)
to the column values (1D arrays). For example, you assign and access
individual columns using normal indexing notation with column names:

.. code:: python

    print table["x"]
    print table["x*2"]
    print table["x^2"]


.. parsed-literal::

    [0 1 2 3 4 5 6 7 8 9]
    [ 0  2  4  6  8 10 12 14 16 18]
    [ 0  1  4  9 16 25 36 49 64 81]


In addition, the ``keys()``, ``values()``, and ``items()`` methods also
act like their standard library counterparts, providing column-oriented
access to the table contents. However, unlike a normal Python dict, a
Toyplot table remembers the order in which columns were added to the
table, and always returns them in the same order:

.. code:: python

    for name in table.keys():
        print name


.. parsed-literal::

    x
    x*2
    x^2


.. code:: python

    for column in table.values():
        print column


.. parsed-literal::

    [0 1 2 3 4 5 6 7 8 9]
    [ 0  2  4  6  8 10 12 14 16 18]
    [ 0  1  4  9 16 25 36 49 64 81]


.. code:: python

    for name, column in table.items():
        print name, column


.. parsed-literal::

    x [0 1 2 3 4 5 6 7 8 9]
    x*2 [ 0  2  4  6  8 10 12 14 16 18]
    x^2 [ 0  1  4  9 16 25 36 49 64 81]


That's all straightforward, but Toyplot tables also behave like Python
lists. For example, you can use the normal Python length function to get
the number of rows:

.. code:: python

    len(table)




.. parsed-literal::

    10



And you can access a single row using its integer index:

.. code:: python

    table[3]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x</th><th style="text-align:left;border:none;padding-right:1em;">x*2</th><th style="text-align:left;border:none;padding-right:1em;">x^2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">6</td><td style="border:none;padding-right:1em;">9</td></tr></table>



And you can retrieve a range of rows using slice notation:

.. code:: python

    table[2:5]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x</th><th style="text-align:left;border:none;padding-right:1em;">x*2</th><th style="text-align:left;border:none;padding-right:1em;">x^2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">4</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">6</td><td style="border:none;padding-right:1em;">9</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">8</td><td style="border:none;padding-right:1em;">16</td></tr></table>



You can also retrieve a noncontiguous range of rows using Numpy advanced
slicing:

.. code:: python

    table[[1, 3, 4]]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x</th><th style="text-align:left;border:none;padding-right:1em;">x*2</th><th style="text-align:left;border:none;padding-right:1em;">x^2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">1</td><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">1</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">6</td><td style="border:none;padding-right:1em;">9</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">8</td><td style="border:none;padding-right:1em;">16</td></tr></table>



Finally, you can mix both forms of indexing (rows and columns) to
retrieve arbitrary subsets of a table:

.. code:: python

    table[3, "x*2"]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x*2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">6</td></tr></table>



.. code:: python

    table[3:6, ["x", "x*2"]]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x</th><th style="text-align:left;border:none;padding-right:1em;">x*2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">6</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">8</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">5</td><td style="border:none;padding-right:1em;">10</td></tr></table>



.. code:: python

    table[[1, 3, 4], ["x", "x*2"]]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x</th><th style="text-align:left;border:none;padding-right:1em;">x*2</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">1</td><td style="border:none;padding-right:1em;">2</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">6</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">8</td></tr></table>



Passing a sequence of column names allows you to reorder the columns in
a table if necessary:

.. code:: python

    table[["x*2", "x"]]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">x*2</th><th style="text-align:left;border:none;padding-right:1em;">x</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">0</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">1</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">2</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">6</td><td style="border:none;padding-right:1em;">3</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">8</td><td style="border:none;padding-right:1em;">4</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">10</td><td style="border:none;padding-right:1em;">5</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">12</td><td style="border:none;padding-right:1em;">6</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">14</td><td style="border:none;padding-right:1em;">7</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">16</td><td style="border:none;padding-right:1em;">8</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">18</td><td style="border:none;padding-right:1em;">9</td></tr></table>



Note that all of these operations are taking views into the underlying
column storage, so no data is copied.

Initialization
--------------

In the above example, we created a data table from scratch, adding data
one-column-at-a-time to an empty table. However, there are many
different ways to create a table. For example, you can pass a dictionary
that maps column names to column values:

.. code:: python

    data = dict()
    data["Name"] = ["Tim", "Fred", "Jane"]
    data["Age"] = [45, 32, 43]
    toyplot.data.Table(data)




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">Age</th><th style="text-align:left;border:none;padding-right:1em;">Name</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">45</td><td style="border:none;padding-right:1em;">Tim</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">32</td><td style="border:none;padding-right:1em;">Fred</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">43</td><td style="border:none;padding-right:1em;">Jane</td></tr></table>



You can also pass any other object that implements Python's
:class:`collections.abc.Mapping` protocol. Note that the columns are
inserted into the table in alphabetical order, since Python dictionaries
/ maps do not have an explicit ordering.

If column order matters to you, you can use an instance of
:class:`collections.OrderedDict` instead, which remembers the order in
which data was added:

.. code:: python

    import collections
    data = collections.OrderedDict()
    data["Name"] = ["Tim", "Fred", "Jane"]
    data["Age"] = [45, 32, 43]
    toyplot.data.Table(data)




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">Name</th><th style="text-align:left;border:none;padding-right:1em;">Age</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Tim</td><td style="border:none;padding-right:1em;">45</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Fred</td><td style="border:none;padding-right:1em;">32</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Jane</td><td style="border:none;padding-right:1em;">43</td></tr></table>



Another way to add ordered data to a data table would be to use a
sequence of (column name, column values) tuples:

.. code:: python

    data = [("Name", ["Tim", "Fred", "Jane"]), ("Age", [45, 32, 43])]
    toyplot.data.Table(data)




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">Name</th><th style="text-align:left;border:none;padding-right:1em;">Age</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Tim</td><td style="border:none;padding-right:1em;">45</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Fred</td><td style="border:none;padding-right:1em;">32</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Jane</td><td style="border:none;padding-right:1em;">43</td></tr></table>



Again, you can use any :class:`collections.abc.Sequence` type, not
just a Python list as in this example.

You can also treat any two-dimensional numpy array (matrix) as a table:

.. code:: python

    data = numpy.array([["Tim", 45],["Fred", 32], ["Jane", 43]])
    toyplot.data.Table(data)




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">0</th><th style="text-align:left;border:none;padding-right:1em;">1</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Tim</td><td style="border:none;padding-right:1em;">45</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Fred</td><td style="border:none;padding-right:1em;">32</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">Jane</td><td style="border:none;padding-right:1em;">43</td></tr></table>



... Note that the ordering of the matrix columns is retained, and column
names are created for you.

You can also convert a `Pandas <http://pandas.pydata.org>`__ data frame
into a table:

.. code:: python

    import pandas
    df = pandas.read_csv("temperatures.csv")
    toyplot.data.Table(df)[0:5]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">STATION</th><th style="text-align:left;border:none;padding-right:1em;">STATION_NAME</th><th style="text-align:left;border:none;padding-right:1em;">DATE</th><th style="text-align:left;border:none;padding-right:1em;">TMAX</th><th style="text-align:left;border:none;padding-right:1em;">TMIN</th><th style="text-align:left;border:none;padding-right:1em;">TOBS</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130101</td><td style="border:none;padding-right:1em;">39</td><td style="border:none;padding-right:1em;">-72</td><td style="border:none;padding-right:1em;">-67</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130102</td><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">-133</td><td style="border:none;padding-right:1em;">-133</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130103</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130104</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130105</td><td style="border:none;padding-right:1em;">22</td><td style="border:none;padding-right:1em;">-144</td><td style="border:none;padding-right:1em;">-111</td></tr></table>



By default, the data frame index isn't included in the conversion to a
table, but you can override this if you wish:

.. code:: python

    toyplot.data.Table(df, index=True)[0:5]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">index0</th><th style="text-align:left;border:none;padding-right:1em;">STATION</th><th style="text-align:left;border:none;padding-right:1em;">STATION_NAME</th><th style="text-align:left;border:none;padding-right:1em;">DATE</th><th style="text-align:left;border:none;padding-right:1em;">TMAX</th><th style="text-align:left;border:none;padding-right:1em;">TMIN</th><th style="text-align:left;border:none;padding-right:1em;">TOBS</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130101</td><td style="border:none;padding-right:1em;">39</td><td style="border:none;padding-right:1em;">-72</td><td style="border:none;padding-right:1em;">-67</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">1</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130102</td><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">-133</td><td style="border:none;padding-right:1em;">-133</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130103</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130104</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130105</td><td style="border:none;padding-right:1em;">22</td><td style="border:none;padding-right:1em;">-144</td><td style="border:none;padding-right:1em;">-111</td></tr></table>



If you don't like the auto generated name of the index column, you can
provide an alternate name of your own:

.. code:: python

    toyplot.data.Table(df, index="INDEX")[0:5]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">INDEX</th><th style="text-align:left;border:none;padding-right:1em;">STATION</th><th style="text-align:left;border:none;padding-right:1em;">STATION_NAME</th><th style="text-align:left;border:none;padding-right:1em;">DATE</th><th style="text-align:left;border:none;padding-right:1em;">TMAX</th><th style="text-align:left;border:none;padding-right:1em;">TMIN</th><th style="text-align:left;border:none;padding-right:1em;">TOBS</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130101</td><td style="border:none;padding-right:1em;">39</td><td style="border:none;padding-right:1em;">-72</td><td style="border:none;padding-right:1em;">-67</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">1</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130102</td><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">-133</td><td style="border:none;padding-right:1em;">-133</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">2</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130103</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">3</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130104</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">4</td><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130105</td><td style="border:none;padding-right:1em;">22</td><td style="border:none;padding-right:1em;">-144</td><td style="border:none;padding-right:1em;">-111</td></tr></table>



Note that hierarchical data frame indices will be converted to multiple
table columns.

Demonstration
-------------

As a convenience for pedagogical purposes only, Toyplot provides basic
functionality to load a table from a CSV file - but please note that
Toyplot is emphatically *not* a data manipulation library! For real work
you should use the Python standard library :mod:`csv` module to load
data, or functionality provided by libraries such as ``Numpy`` or
``Pandas``. In the following example, we will load a set of temperature
readings into a data table to use for a visualization:

.. code:: python

    table = toyplot.data.read_csv("temperatures.csv")
    table[0:10]




.. raw:: html

    <table class="toyplot-data-Table" style="border-collapse:collapse; border:none; color: #292724"><tr style="border:none;border-bottom:1px solid #292724"><th style="text-align:left;border:none;padding-right:1em;">STATION</th><th style="text-align:left;border:none;padding-right:1em;">STATION_NAME</th><th style="text-align:left;border:none;padding-right:1em;">DATE</th><th style="text-align:left;border:none;padding-right:1em;">TMAX</th><th style="text-align:left;border:none;padding-right:1em;">TMIN</th><th style="text-align:left;border:none;padding-right:1em;">TOBS</th></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130101</td><td style="border:none;padding-right:1em;">39</td><td style="border:none;padding-right:1em;">-72</td><td style="border:none;padding-right:1em;">-67</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130102</td><td style="border:none;padding-right:1em;">0</td><td style="border:none;padding-right:1em;">-133</td><td style="border:none;padding-right:1em;">-133</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130103</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130104</td><td style="border:none;padding-right:1em;">11</td><td style="border:none;padding-right:1em;">-139</td><td style="border:none;padding-right:1em;">-89</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130105</td><td style="border:none;padding-right:1em;">22</td><td style="border:none;padding-right:1em;">-144</td><td style="border:none;padding-right:1em;">-111</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130106</td><td style="border:none;padding-right:1em;">44</td><td style="border:none;padding-right:1em;">-122</td><td style="border:none;padding-right:1em;">-100</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130107</td><td style="border:none;padding-right:1em;">56</td><td style="border:none;padding-right:1em;">-122</td><td style="border:none;padding-right:1em;">-11</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130108</td><td style="border:none;padding-right:1em;">100</td><td style="border:none;padding-right:1em;">-83</td><td style="border:none;padding-right:1em;">-78</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130109</td><td style="border:none;padding-right:1em;">72</td><td style="border:none;padding-right:1em;">-83</td><td style="border:none;padding-right:1em;">-33</td></tr><tr style="border:none"><td style="border:none;padding-right:1em;">GHCND:USC00294366</td><td style="border:none;padding-right:1em;">JEMEZ DAM NM US</td><td style="border:none;padding-right:1em;">20130111</td><td style="border:none;padding-right:1em;">89</td><td style="border:none;padding-right:1em;">-50</td><td style="border:none;padding-right:1em;">22</td></tr></table>



Then, we convert the readings (which are stored as tenths of a degree
Celsius) to Fahrenheit:

.. code:: python

    table["TMAX_F"] = ((table["TMAX"].astype("float64") * 0.1) * 1.8) + 32
    table["TMIN_F"] = ((table["TMIN"].astype("float64") * 0.1) * 1.8) + 32

Finally, we can pass table columns directly to Toyplot for plotting:

.. code:: python

    canvas = toyplot.Canvas(width=600, height=300)
    axes = canvas.cartesian(xlabel="Day", ylabel=u"Temperature \u00b0F")
    axes.plot(table["TMAX_F"], color="red", stroke_width=1)
    axes.plot(table["TMIN_F"], color="blue", stroke_width=1);



.. raw:: html

    <div class="toyplot" id="t7bfa97f7d1d847c6a6b675849ebe0566" style="text-align:center"><svg class="toyplot-canvas-Canvas" height="300.0px" id="t3f02e4b5f53e4be6b6a7b2feccfcb2a2" preserveAspectRatio="xMidYMid meet" style="background-color:transparent;fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:Helvetica;font-size:12px;opacity:1.0;stroke:rgb(16.1%,15.3%,14.1%);stroke-opacity:1.0;stroke-width:1.0" viewBox="0 0 600.0 300.0" width="600.0px" xmlns="http://www.w3.org/2000/svg" xmlns:toyplot="http://www.sandia.gov/toyplot" xmlns:xlink="http://www.w3.org/1999/xlink"><g class="toyplot-coordinates-Cartesian" id="taaa41aa8f08a454f907961714ebb264a"><clipPath id="tc2e30b32e9c4446284ba5d64f0937415"><rect height="220.0" width="520.0" x="40.0" y="40.0"></rect></clipPath><g clip-path="url(#tc2e30b32e9c4446284ba5d64f0937415)"><g class="toyplot-mark-Plot" id="t7602f253da5848b19c33b0dd72cfc2cc" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 176.31578947368422 L 51.25 189.5585738539898 L 52.5 185.82342954159594 L 53.75 185.82342954159594 L 55.0 182.08828522920206 L 56.25 174.61799660441426 L 57.5 170.54329371816638 L 58.75 155.60271646859081 L 60.0 165.11035653650254 L 61.25 159.33786078098473 L 62.5 174.61799660441426 L 63.75 193.29371816638371 L 65.0 195.33106960950764 L 66.25 202.80135823429541 L 67.5 208.57385398981324 L 68.75 182.08828522920206 L 70.0 157.64006791171477 L 71.25 151.86757215619696 L 72.5 155.60271646859081 L 73.75 149.830220713073 L 75.0 153.56536502546692 L 76.25 140.6621392190153 L 77.5 144.39728353140919 L 78.75 157.64006791171477 L 80.0 144.39728353140919 L 81.25 148.13242784380307 L 82.5 189.5585738539898 L 83.75 176.31578947368422 L 85.0 153.56536502546692 L 86.25 148.13242784380307 L 87.5 142.35993208828526 L 88.75 151.86757215619696 L 90.0 148.13242784380307 L 91.25 138.62478777589135 L 92.5 138.62478777589135 L 93.75 144.39728353140919 L 95.0 144.39728353140919 L 96.25 155.60271646859081 L 97.5 170.54329371816638 L 98.75 165.11035653650254 L 100.0 176.31578947368422 L 101.25 165.11035653650254 L 102.5 159.33786078098473 L 103.75 153.56536502546692 L 105.0 142.35993208828526 L 106.25 140.6621392190153 L 107.5 157.64006791171477 L 108.75 136.58743633276742 L 110.0 153.56536502546692 L 111.25 163.07300509337864 L 112.5 174.61799660441426 L 113.75 159.33786078098473 L 115.0 174.61799660441426 L 116.25 163.07300509337864 L 117.5 168.84550084889645 L 118.75 165.11035653650254 L 120.00000000000001 155.60271646859081 L 121.25 140.6621392190153 L 122.5 129.11714770797965 L 123.75 123.68421052631579 L 125.0 134.88964346349746 L 126.25 138.62478777589135 L 127.5 127.41935483870969 L 128.75 119.60950764006792 L 130.0 136.58743633276742 L 131.25 166.8081494057725 L 132.5 153.56536502546692 L 133.75 136.58743633276742 L 135.0 125.38200339558574 L 136.25 119.60950764006792 L 137.5 108.40407470288628 L 138.75 102.63157894736842 L 140.0 115.87436332767405 L 141.25 123.68421052631579 L 142.5 129.11714770797965 L 143.75 132.85229202037351 L 145.0 132.85229202037351 L 146.25 119.60950764006792 L 147.5 129.11714770797965 L 148.75 174.61799660441426 L 150.0 155.60271646859081 L 151.25 146.09507640067912 L 152.5 127.41935483870969 L 153.75 115.87436332767405 L 155.0 112.13921901528019 L 156.25 112.13921901528019 L 157.5 114.17657045840409 L 158.75 112.13921901528019 L 160.0 112.13921901528019 L 161.25 121.64685908319188 L 162.5 125.38200339558574 L 163.75 112.13921901528019 L 165.0 106.7062818336163 L 166.25 108.40407470288628 L 167.5 112.13921901528019 L 168.75 106.7062818336163 L 170.0 155.60271646859081 L 171.25 161.37521222410868 L 172.5 132.85229202037351 L 173.75 119.60950764006792 L 175.0 110.44142614601023 L 176.25 106.7062818336163 L 177.5 100.93378607809846 L 178.75 98.896434634974554 L 180.0 140.6621392190153 L 181.25 161.37521222410868 L 182.5 131.15449915110358 L 183.75 123.68421052631579 L 185.0 115.87436332767405 L 186.25 98.896434634974554 L 187.5 125.38200339558574 L 188.75 121.64685908319188 L 190.00000000000003 114.17657045840409 L 191.24999999999997 110.44142614601023 L 192.5 106.7062818336163 L 193.75 98.896434634974554 L 195.0 91.42614601018677 L 196.25 87.691001697792899 L 197.5 97.198641765704608 L 198.75 134.88964346349746 L 200.0 125.38200339558574 L 201.25 106.7062818336163 L 202.5 112.13921901528019 L 203.75 121.64685908319188 L 205.0 108.40407470288628 L 206.25 121.64685908319188 L 207.5 114.17657045840409 L 208.75 119.60950764006792 L 210.0 112.13921901528019 L 211.25 100.93378607809846 L 212.5 93.463497453310737 L 213.75 87.691001697792899 L 215.0 89.728353140916809 L 216.25 85.653650254668932 L 217.5 87.691001697792899 L 218.75 102.63157894736842 L 220.0 110.44142614601023 L 221.25000000000003 112.13921901528019 L 222.49999999999997 102.63157894736842 L 223.75 87.691001697792899 L 225.0 78.183361629881148 L 226.25 83.955857385398971 L 227.5 80.220713073005115 L 228.75 85.653650254668932 L 230.0 91.42614601018677 L 231.25 89.728353140916809 L 232.5 98.896434634974554 L 233.75 89.728353140916809 L 235.0 91.42614601018677 L 236.25 85.653650254668932 L 237.5 87.691001697792899 L 238.75 76.485568760611187 L 240.0 76.485568760611187 L 241.25 78.183361629881148 L 242.5 83.955857385398971 L 243.75 80.220713073005115 L 245.0 70.71307300509342 L 246.25 70.71307300509342 L 247.5 61.205432937181655 L 248.75 61.205432937181655 L 250.0 61.205432937181655 L 251.25 64.940577249575583 L 252.50000000000003 74.448217317487277 L 253.74999999999997 74.448217317487277 L 255.0 76.485568760611187 L 256.25 76.485568760611187 L 257.5 81.918505942275075 L 258.75 66.977928692699493 L 260.0 68.675721561969439 L 261.25 70.71307300509342 L 262.5 74.448217317487277 L 263.75 76.485568760611187 L 265.0 74.448217317487277 L 266.25 74.448217317487277 L 267.5 61.205432937181655 L 268.75 50.0 L 270.0 64.940577249575583 L 271.25 66.977928692699493 L 272.5 64.940577249575583 L 273.75 87.691001697792899 L 275.0 87.691001697792899 L 276.25 83.955857385398971 L 277.5 72.750424448217316 L 278.75 72.750424448217316 L 280.0 72.750424448217316 L 281.25 72.750424448217316 L 282.5 68.675721561969439 L 283.75 66.977928692699493 L 285.0 68.675721561969439 L 286.25 80.220713073005115 L 287.5 76.485568760611187 L 288.75 72.750424448217316 L 290.0 66.977928692699493 L 291.25 114.17657045840409 L 292.5 91.42614601018677 L 293.75 91.42614601018677 L 295.0 87.691001697792899 L 296.25 83.955857385398971 L 297.5 81.918505942275075 L 298.75 78.183361629881148 L 300.0 70.71307300509342 L 301.24999999999994 66.977928692699493 L 302.5 76.485568760611187 L 303.75 87.691001697792899 L 305.0 81.918505942275075 L 306.25 93.463497453310737 L 307.5 85.653650254668932 L 308.75 80.220713073005115 L 310.0 72.750424448217316 L 311.25 70.71307300509342 L 312.5 85.653650254668932 L 313.75 76.485568760611187 L 315.0 81.918505942275075 L 316.25 74.448217317487277 L 317.5 80.220713073005115 L 318.75 83.955857385398971 L 320.0 95.161290322580697 L 321.25 91.42614601018677 L 322.5 85.653650254668932 L 323.75 91.42614601018677 L 325.0 91.42614601018677 L 326.25 93.463497453310737 L 327.5 83.955857385398971 L 328.75 83.955857385398971 L 330.00000000000006 76.485568760611187 L 331.25 70.71307300509342 L 332.49999999999994 72.750424448217316 L 333.75 72.750424448217316 L 335.0 74.448217317487277 L 336.25 78.183361629881148 L 337.5 80.220713073005115 L 338.75 76.485568760611187 L 340.0 85.653650254668932 L 341.25 91.42614601018677 L 342.5 91.42614601018677 L 343.75 80.220713073005115 L 345.0 83.955857385398971 L 346.25 83.955857385398971 L 347.5 87.691001697792899 L 348.75 76.485568760611187 L 350.0 70.71307300509342 L 351.25 72.750424448217316 L 352.5 81.918505942275075 L 353.75 76.485568760611187 L 355.0 76.485568760611187 L 356.25 80.220713073005115 L 357.5 80.220713073005115 L 358.75 80.220713073005115 L 360.0 81.918505942275075 L 361.25000000000006 87.691001697792899 L 362.5 119.60950764006792 L 363.74999999999994 98.896434634974554 L 365.0 119.60950764006792 L 366.25 117.91171477079796 L 367.5 110.44142614601023 L 368.75 104.66893039049239 L 370.0 104.66893039049239 L 371.25 104.66893039049239 L 372.5 97.198641765704608 L 373.75 95.161290322580697 L 375.0 95.161290322580697 L 376.25 100.93378607809846 L 377.5 100.93378607809846 L 378.75 117.91171477079796 L 380.0 102.63157894736842 L 381.25 95.161290322580697 L 382.5 95.161290322580697 L 383.75 119.60950764006792 L 385.0 119.60950764006792 L 386.25 106.7062818336163 L 387.5 98.896434634974554 L 388.75 95.161290322580697 L 390.0 100.93378607809846 L 391.25 102.63157894736842 L 392.50000000000006 136.58743633276742 L 393.75 136.58743633276742 L 394.99999999999994 115.87436332767405 L 396.25 110.44142614601023 L 397.5 106.7062818336163 L 398.75 106.7062818336163 L 400.0 119.60950764006792 L 401.25 136.58743633276742 L 402.5 121.64685908319188 L 403.75 104.66893039049239 L 405.0 125.38200339558574 L 406.25 129.11714770797965 L 407.5 138.62478777589135 L 408.75 129.11714770797965 L 410.0 136.58743633276742 L 411.25 129.11714770797965 L 412.5 119.60950764006792 L 413.75 129.11714770797965 L 415.0 121.64685908319188 L 416.25 117.91171477079796 L 417.5 112.13921901528019 L 418.75 129.11714770797965 L 420.0 125.38200339558574 L 421.25 125.38200339558574 L 422.5 123.68421052631579 L 423.75000000000006 123.68421052631579 L 425.0 140.6621392190153 L 426.24999999999994 146.09507640067912 L 427.5 140.6621392190153 L 428.75 132.85229202037351 L 430.0 127.41935483870969 L 431.25 127.41935483870969 L 432.5 161.37521222410868 L 433.75 153.56536502546692 L 435.0 138.62478777589135 L 436.25 134.88964346349746 L 437.5 121.64685908319188 L 438.75 121.64685908319188 L 440.0 119.60950764006792 L 441.25 148.13242784380307 L 442.5 146.09507640067912 L 443.75 134.88964346349746 L 445.0 138.62478777589135 L 446.25 140.6621392190153 L 447.5 142.35993208828526 L 448.75 132.85229202037351 L 450.0 136.58743633276742 L 451.25 157.64006791171477 L 452.5 155.60271646859081 L 453.75 182.08828522920206 L 455.00000000000006 182.08828522920206 L 456.25 195.33106960950764 L 457.49999999999994 168.84550084889645 L 458.75 161.37521222410868 L 460.0 163.07300509337864 L 461.25 157.64006791171477 L 462.5 148.13242784380307 L 463.75 144.39728353140919 L 465.0 170.54329371816638 L 466.25 153.56536502546692 L 467.5 129.11714770797965 L 468.75 140.6621392190153 L 470.0 193.29371816638371 L 471.25 183.78607809847202 L 472.5 189.5585738539898 L 473.75 189.5585738539898 L 475.0 197.0288624787776 L 476.25 178.35314091680817 L 477.5 176.31578947368422 L 478.75 172.58064516129033 L 480.0 166.8081494057725 L 481.25 166.8081494057725 L 482.5 163.07300509337864 L 483.75 149.830220713073 L 485.0 144.39728353140919 L 486.25000000000006 149.830220713073 L 487.5 146.09507640067912 L 488.74999999999994 140.6621392190153 L 490.0 178.35314091680817 L 491.25 170.54329371816638 L 492.5 165.11035653650254 L 493.75 159.33786078098473 L 495.0 163.07300509337864 L 496.25 153.56536502546692 L 497.5 148.13242784380307 L 498.75 161.37521222410868 L 500.0 166.8081494057725 L 501.25 157.64006791171477" style="stroke:rgb(100%,0%,0%);stroke-opacity:1.0;stroke-width:1.0"></path></g></g><g class="toyplot-mark-Plot" id="t0da773f8a5214e668b0089374a7c994c" style="fill:none"><g class="toyplot-Series"><path d="M 50.0 214.00679117147709 L 51.25 234.71986417657047 L 52.5 236.75721561969439 L 53.75 236.75721561969439 L 55.0 238.45500848896435 L 56.25 230.98471986417658 L 57.5 230.98471986417658 L 58.75 217.74193548387098 L 60.0 217.74193548387098 L 61.25 206.53650254668932 L 62.5 244.22750424448219 L 63.75 247.96264855687608 L 65.0 250.0 L 66.25 244.22750424448219 L 67.5 240.49235993208828 L 68.75 240.49235993208828 L 70.0 219.7792869269949 L 71.25 219.7792869269949 L 72.5 221.47707979626483 L 73.75 219.7792869269949 L 75.0 216.04414261460101 L 76.25 219.7792869269949 L 77.5 178.35314091680817 L 78.75 172.58064516129033 L 80.0 176.31578947368422 L 81.25 197.0288624787776 L 82.5 210.27164685908321 L 83.75 210.27164685908321 L 85.0 210.27164685908321 L 86.25 212.30899830220716 L 87.5 204.49915110356537 L 88.75 193.29371816638371 L 90.0 200.76400679117148 L 91.25 206.53650254668932 L 92.5 206.53650254668932 L 93.75 189.5585738539898 L 95.0 200.76400679117148 L 96.25 204.49915110356537 L 97.5 214.00679117147709 L 98.75 214.00679117147709 L 100.0 217.74193548387098 L 101.25 217.74193548387098 L 102.5 208.57385398981324 L 103.75 210.27164685908321 L 105.0 216.04414261460101 L 106.25 216.04414261460101 L 107.5 202.80135823429541 L 108.75 199.06621392190155 L 110.0 193.29371816638371 L 111.25 195.33106960950764 L 112.5 212.30899830220716 L 113.75 212.30899830220716 L 115.0 206.53650254668932 L 116.25 214.00679117147709 L 117.5 219.7792869269949 L 118.75 219.7792869269949 L 120.00000000000001 216.04414261460101 L 121.25 199.06621392190155 L 122.5 199.06621392190155 L 123.75 195.33106960950764 L 125.0 195.33106960950764 L 126.25 195.33106960950764 L 127.5 193.29371816638371 L 128.75 189.5585738539898 L 130.0 189.5585738539898 L 131.25 204.49915110356537 L 132.5 200.76400679117148 L 133.75 195.33106960950764 L 135.0 193.29371816638371 L 136.25 193.29371816638371 L 137.5 182.08828522920206 L 138.75 183.78607809847202 L 140.0 176.31578947368422 L 141.25 185.82342954159594 L 142.5 185.82342954159594 L 143.75 182.08828522920206 L 145.0 182.08828522920206 L 146.25 187.52122241086587 L 147.5 185.82342954159594 L 148.75 216.04414261460101 L 150.0 217.74193548387098 L 151.25 204.49915110356537 L 152.5 191.59592529711378 L 153.75 189.5585738539898 L 155.0 172.58064516129033 L 156.25 178.35314091680817 L 157.5 178.35314091680817 L 158.75 166.8081494057725 L 160.0 168.84550084889645 L 161.25 180.0509337860781 L 162.5 180.0509337860781 L 163.75 180.0509337860781 L 165.0 170.54329371816638 L 166.25 161.37521222410868 L 167.5 159.33786078098473 L 168.75 166.8081494057725 L 170.0 185.82342954159594 L 171.25 189.5585738539898 L 172.5 189.5585738539898 L 173.75 182.08828522920206 L 175.0 174.61799660441426 L 176.25 161.37521222410868 L 177.5 163.07300509337864 L 178.75 161.37521222410868 L 180.0 195.33106960950764 L 181.25 200.76400679117148 L 182.5 199.06621392190155 L 183.75 180.0509337860781 L 185.0 174.61799660441426 L 186.25 174.61799660441426 L 187.5 199.06621392190155 L 188.75 197.0288624787776 L 190.00000000000003 170.54329371816638 L 191.24999999999997 168.84550084889645 L 192.5 174.61799660441426 L 193.75 172.58064516129033 L 195.0 161.37521222410868 L 196.25 159.33786078098473 L 197.5 182.08828522920206 L 198.75 185.82342954159594 L 200.0 185.82342954159594 L 201.25 165.11035653650254 L 202.5 157.64006791171477 L 203.75 170.54329371816638 L 205.0 166.8081494057725 L 206.25 166.8081494057725 L 207.5 161.37521222410868 L 208.75 163.07300509337864 L 210.0 168.84550084889645 L 211.25 161.37521222410868 L 212.5 155.60271646859081 L 213.75 146.09507640067912 L 215.0 153.56536502546692 L 216.25 148.13242784380307 L 217.5 140.6621392190153 L 218.75 149.830220713073 L 220.0 159.33786078098473 L 221.25000000000003 168.84550084889645 L 222.49999999999997 161.37521222410868 L 223.75 148.13242784380307 L 225.0 136.58743633276742 L 226.25 144.39728353140919 L 227.5 140.6621392190153 L 228.75 148.13242784380307 L 230.0 159.33786078098473 L 231.25 155.60271646859081 L 232.5 148.13242784380307 L 233.75 148.13242784380307 L 235.0 151.86757215619696 L 236.25 148.13242784380307 L 237.5 140.6621392190153 L 238.75 144.39728353140919 L 240.0 134.88964346349746 L 241.25 138.62478777589135 L 242.5 140.6621392190153 L 243.75 140.6621392190153 L 245.0 138.62478777589135 L 246.25 131.15449915110358 L 247.5 121.64685908319188 L 248.75 136.58743633276742 L 250.0 129.11714770797965 L 251.25 121.64685908319188 L 252.50000000000003 131.15449915110358 L 253.74999999999997 129.11714770797965 L 255.0 132.85229202037351 L 256.25 127.41935483870969 L 257.5 131.15449915110358 L 258.75 140.6621392190153 L 260.0 144.39728353140919 L 261.25 140.6621392190153 L 262.5 142.35993208828526 L 263.75 140.6621392190153 L 265.0 129.11714770797965 L 266.25 132.85229202037351 L 267.5 127.41935483870969 L 268.75 117.91171477079796 L 270.0 125.38200339558574 L 271.25 121.64685908319188 L 272.5 132.85229202037351 L 273.75 144.39728353140919 L 275.0 138.62478777589135 L 276.25 138.62478777589135 L 277.5 132.85229202037351 L 278.75 129.11714770797965 L 280.0 129.11714770797965 L 281.25 123.68421052631579 L 282.5 125.38200339558574 L 283.75 117.91171477079796 L 285.0 121.64685908319188 L 286.25 129.11714770797965 L 287.5 127.41935483870969 L 288.75 125.38200339558574 L 290.0 127.41935483870969 L 291.25 132.85229202037351 L 292.5 134.88964346349746 L 293.75 134.88964346349746 L 295.0 132.85229202037351 L 296.25 131.15449915110358 L 297.5 127.41935483870969 L 298.75 131.15449915110358 L 300.0 123.68421052631579 L 301.24999999999994 121.64685908319188 L 302.5 132.85229202037351 L 303.75 136.58743633276742 L 305.0 140.6621392190153 L 306.25 132.85229202037351 L 307.5 129.11714770797965 L 308.75 129.11714770797965 L 310.0 123.68421052631579 L 311.25 121.64685908319188 L 312.5 132.85229202037351 L 313.75 132.85229202037351 L 315.0 132.85229202037351 L 316.25 131.15449915110358 L 317.5 129.11714770797965 L 318.75 131.15449915110358 L 320.0 132.85229202037351 L 321.25 132.85229202037351 L 322.5 132.85229202037351 L 323.75 136.58743633276742 L 325.0 136.58743633276742 L 326.25 129.11714770797965 L 327.5 127.41935483870969 L 328.75 136.58743633276742 L 330.00000000000006 138.62478777589135 L 331.25 136.58743633276742 L 332.49999999999994 125.38200339558574 L 333.75 119.60950764006792 L 335.0 132.85229202037351 L 336.25 129.11714770797965 L 337.5 129.11714770797965 L 338.75 129.11714770797965 L 340.0 134.88964346349746 L 341.25 134.88964346349746 L 342.5 132.85229202037351 L 343.75 131.15449915110358 L 345.0 134.88964346349746 L 346.25 134.88964346349746 L 347.5 129.11714770797965 L 348.75 129.11714770797965 L 350.0 125.38200339558574 L 351.25 121.64685908319188 L 352.5 125.38200339558574 L 353.75 131.15449915110358 L 355.0 132.85229202037351 L 356.25 138.62478777589135 L 357.5 136.58743633276742 L 358.75 136.58743633276742 L 360.0 132.85229202037351 L 361.25000000000006 129.11714770797965 L 362.5 136.58743633276742 L 363.74999999999994 134.88964346349746 L 365.0 136.58743633276742 L 366.25 142.35993208828526 L 367.5 144.39728353140919 L 368.75 142.35993208828526 L 370.0 140.6621392190153 L 371.25 140.6621392190153 L 372.5 136.58743633276742 L 373.75 136.58743633276742 L 375.0 140.6621392190153 L 376.25 144.39728353140919 L 377.5 159.33786078098473 L 378.75 163.07300509337864 L 380.0 161.37521222410868 L 381.25 159.33786078098473 L 382.5 157.64006791171477 L 383.75 178.35314091680817 L 385.0 178.35314091680817 L 386.25 178.35314091680817 L 387.5 168.84550084889645 L 388.75 166.8081494057725 L 390.0 168.84550084889645 L 391.25 165.11035653650254 L 392.50000000000006 180.0509337860781 L 393.75 182.08828522920206 L 394.99999999999994 176.31578947368422 L 396.25 178.35314091680817 L 397.5 168.84550084889645 L 398.75 170.54329371816638 L 400.0 183.78607809847202 L 401.25 183.78607809847202 L 402.5 180.0509337860781 L 403.75 157.64006791171477 L 405.0 180.0509337860781 L 406.25 174.61799660441426 L 407.5 195.33106960950764 L 408.75 193.29371816638371 L 410.0 193.29371816638371 L 411.25 197.0288624787776 L 412.5 183.78607809847202 L 413.75 187.52122241086587 L 415.0 191.59592529711378 L 416.25 187.52122241086587 L 417.5 172.58064516129033 L 418.75 172.58064516129033 L 420.0 178.35314091680817 L 421.25 178.35314091680817 L 422.5 170.54329371816638 L 423.75000000000006 174.61799660441426 L 425.0 182.08828522920206 L 426.24999999999994 182.08828522920206 L 427.5 185.82342954159594 L 428.75 176.31578947368422 L 430.0 180.0509337860781 L 431.25 178.35314091680817 L 432.5 197.0288624787776 L 433.75 195.33106960950764 L 435.0 197.0288624787776 L 436.25 193.29371816638371 L 437.5 189.5585738539898 L 438.75 185.82342954159594 L 440.0 178.35314091680817 L 441.25 182.08828522920206 L 442.5 187.52122241086587 L 443.75 197.0288624787776 L 445.0 195.33106960950764 L 446.25 178.35314091680817 L 447.5 191.59592529711378 L 448.75 193.29371816638371 L 450.0 193.29371816638371 L 451.25 178.35314091680817 L 452.5 197.0288624787776 L 453.75 197.0288624787776 L 455.00000000000006 208.57385398981324 L 456.25 210.27164685908321 L 457.49999999999994 208.57385398981324 L 458.75 206.53650254668932 L 460.0 204.49915110356537 L 461.25 202.80135823429541 L 462.5 199.06621392190155 L 463.75 197.0288624787776 L 465.0 191.59592529711378 L 466.25 200.76400679117148 L 467.5 199.06621392190155 L 468.75 195.33106960950764 L 470.0 234.71986417657047 L 471.25 234.71986417657047 L 472.5 214.00679117147709 L 473.75 208.57385398981324 L 475.0 230.98471986417658 L 476.25 234.71986417657047 L 477.5 214.00679117147709 L 478.75 206.53650254668932 L 480.0 206.53650254668932 L 481.25 212.30899830220716 L 482.5 208.57385398981324 L 483.75 206.53650254668932 L 485.0 206.53650254668932 L 486.25000000000006 208.57385398981324 L 487.5 202.80135823429541 L 488.74999999999994 200.76400679117148 L 490.0 200.76400679117148 L 491.25 206.53650254668932 L 492.5 210.27164685908321 L 493.75 212.30899830220716 L 495.0 214.00679117147709 L 496.25 219.7792869269949 L 497.5 216.04414261460101 L 498.75 216.04414261460101 L 500.0 208.57385398981324 L 501.25 214.00679117147709" style="stroke:rgb(0%,0%,100%);stroke-opacity:1.0;stroke-width:1.0"></path></g></g></g><g class="toyplot-coordinates-Axis" id="t2d5a147961fa425e9f90ac47e3810c99" transform="translate(50.0,250.0)translate(0,10.0)"><line style="" x1="0" x2="451.25" y1="0" y2="0"></line><g><g transform="translate(0.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="8.555">0</text></g><g transform="translate(125.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">100</text></g><g transform="translate(250.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">200</text></g><g transform="translate(375.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">300</text></g><g transform="translate(500.0,6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="8.555">400</text></g></g><g transform="translate(250.0,22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-11.004" y="10.266">Day</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="-3.0" y2="4.5"></line><text style="alignment-baseline:alphabetic;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="-6"></text></g></g><g class="toyplot-coordinates-Axis" id="t876091922f364befb0d121f4433ac1d7" transform="translate(50.0,250.0)rotate(-90.0)translate(0,-10.0)"><line style="" x1="0" x2="200.0" y1="0" y2="0"></line><g><g transform="translate(0.07545746085644056,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-2.78" y="-4.4408920985e-16">0</text></g><g transform="translate(94.39728353140916,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-5.56" y="-4.4408920985e-16">50</text></g><g transform="translate(188.71910960196186,-6)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:10.0px;font-weight:normal;stroke:none;vertical-align:baseline;white-space:pre" x="-8.34" y="-4.4408920985e-16">100</text></g></g><g transform="translate(100.0,-22)"><text style="fill:rgb(16.1%,15.3%,14.1%);fill-opacity:1.0;font-family:helvetica;font-size:12.0px;font-weight:bold;stroke:none;vertical-align:baseline;white-space:pre" x="-44.076" y="0.0">Temperature °F</text></g><g class="toyplot-coordinates-Axis-coordinates" style="visibility:hidden" transform=""><line style="stroke:rgb(43.9%,50.2%,56.5%);stroke-opacity:1.0;stroke-width:1.0" x1="0" x2="0" y1="3.0" y2="-4.5"></line><text style="alignment-baseline:hanging;fill:rgb(43.9%,50.2%,56.5%);fill-opacity:1.0;font-size:10px;font-weight:normal;stroke:none;text-anchor:middle" x="0" y="6"></text></g></g></g></svg><div class="toyplot-behavior"><script>(function()
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
    modules["toyplot/root/id"] = "t7bfa97f7d1d847c6a6b675849ebe0566";
    modules["toyplot/root"] = (function(root_id)
        {
            return document.querySelector("#" + root_id);
        })(modules["toyplot/root/id"]);
    modules["toyplot/canvas/id"] = "t3f02e4b5f53e4be6b6a7b2feccfcb2a2";
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t7602f253da5848b19c33b0dd72cfc2cc","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361], [39.02, 32.0, 33.98, 33.98, 35.96, 39.92, 42.08, 50.0, 44.96, 48.019999999999996, 39.92, 30.02, 28.939999999999998, 24.98, 21.919999999999998, 35.96, 48.92, 51.980000000000004, 50.0, 53.06, 51.08, 57.92, 55.94, 48.92, 55.94, 53.96, 32.0, 39.02, 51.08, 53.96, 57.019999999999996, 51.980000000000004, 53.96, 59.0, 59.0, 55.94, 55.94, 50.0, 42.08, 44.96, 39.02, 44.96, 48.019999999999996, 51.08, 57.019999999999996, 57.92, 48.92, 60.08, 51.08, 46.04, 39.92, 48.019999999999996, 39.92, 46.04, 42.980000000000004, 44.96, 50.0, 57.92, 64.03999999999999, 66.92, 60.980000000000004, 59.0, 64.94, 69.08000000000001, 60.08, 44.06, 51.08, 60.08, 66.02000000000001, 69.08000000000001, 75.02000000000001, 78.08000000000001, 71.06, 66.92, 64.03999999999999, 62.06, 62.06, 69.08000000000001, 64.03999999999999, 39.92, 50.0, 55.040000000000006, 64.94, 71.06, 73.03999999999999, 73.03999999999999, 71.96000000000001, 73.03999999999999, 73.03999999999999, 68.0, 66.02000000000001, 73.03999999999999, 75.92, 75.02000000000001, 73.03999999999999, 75.92, 50.0, 46.94, 62.06, 69.08000000000001, 73.94, 75.92, 78.98, 80.06, 57.92, 46.94, 62.96, 66.92, 71.06, 80.06, 66.02000000000001, 68.0, 71.96000000000001, 73.94, 75.92, 80.06, 84.02000000000001, 86.0, 80.96000000000001, 60.980000000000004, 66.02000000000001, 75.92, 73.03999999999999, 68.0, 75.02000000000001, 68.0, 71.96000000000001, 69.08000000000001, 73.03999999999999, 78.98, 82.94, 86.0, 84.92, 87.08000000000001, 86.0, 78.08000000000001, 73.94, 73.03999999999999, 78.08000000000001, 86.0, 91.04, 87.98, 89.96000000000001, 87.08000000000001, 84.02000000000001, 84.92, 80.06, 84.92, 84.02000000000001, 87.08000000000001, 86.0, 91.94000000000001, 91.94000000000001, 91.04, 87.98, 89.96000000000001, 95.0, 95.0, 100.04, 100.04, 100.04, 98.06, 93.02, 93.02, 91.94000000000001, 91.94000000000001, 89.06, 96.98, 96.08, 95.0, 93.02, 91.94000000000001, 93.02, 93.02, 100.04, 105.98, 98.06, 96.98, 98.06, 86.0, 86.0, 87.98, 93.92, 93.92, 93.92, 93.92, 96.08, 96.98, 96.08, 89.96000000000001, 91.94000000000001, 93.92, 96.98, 71.96000000000001, 84.02000000000001, 84.02000000000001, 86.0, 87.98, 89.06, 91.04, 95.0, 96.98, 91.94000000000001, 86.0, 89.06, 82.94, 87.08000000000001, 89.96000000000001, 93.92, 95.0, 87.08000000000001, 91.94000000000001, 89.06, 93.02, 89.96000000000001, 87.98, 82.03999999999999, 84.02000000000001, 87.08000000000001, 84.02000000000001, 84.02000000000001, 82.94, 87.98, 87.98, 91.94000000000001, 95.0, 93.92, 93.92, 93.02, 91.04, 89.96000000000001, 91.94000000000001, 87.08000000000001, 84.02000000000001, 84.02000000000001, 89.96000000000001, 87.98, 87.98, 86.0, 91.94000000000001, 95.0, 93.92, 89.06, 91.94000000000001, 91.94000000000001, 89.96000000000001, 89.96000000000001, 89.96000000000001, 89.06, 86.0, 69.08000000000001, 80.06, 69.08000000000001, 69.98, 73.94, 77.0, 77.0, 77.0, 80.96000000000001, 82.03999999999999, 82.03999999999999, 78.98, 78.98, 69.98, 78.08000000000001, 82.03999999999999, 82.03999999999999, 69.08000000000001, 69.08000000000001, 75.92, 80.06, 82.03999999999999, 78.98, 78.08000000000001, 60.08, 60.08, 71.06, 73.94, 75.92, 75.92, 69.08000000000001, 60.08, 68.0, 77.0, 66.02000000000001, 64.03999999999999, 59.0, 64.03999999999999, 60.08, 64.03999999999999, 69.08000000000001, 64.03999999999999, 68.0, 69.98, 73.03999999999999, 64.03999999999999, 66.02000000000001, 66.02000000000001, 66.92, 66.92, 57.92, 55.040000000000006, 57.92, 62.06, 64.94, 64.94, 46.94, 51.08, 59.0, 60.980000000000004, 68.0, 68.0, 69.08000000000001, 53.96, 55.040000000000006, 60.980000000000004, 59.0, 57.92, 57.019999999999996, 62.06, 60.08, 48.92, 50.0, 35.96, 35.96, 28.939999999999998, 42.980000000000004, 46.94, 46.04, 48.92, 53.96, 55.94, 42.08, 51.08, 64.03999999999999, 57.92, 30.02, 35.06, 32.0, 32.0, 28.04, 37.94, 39.02, 41.0, 44.06, 44.06, 46.04, 53.06, 55.94, 53.06, 55.040000000000006, 57.92, 37.94, 42.08, 44.96, 48.019999999999996, 46.04, 51.08, 53.96, 46.94, 44.06, 48.92]],"toyplot");
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
            })(modules["toyplot/tables"],modules["toyplot/menus/context"],modules["toyplot/io"],"t0da773f8a5214e668b0089374a7c994c","data","plot data",["x", "y0"],[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361], [19.04, 8.059999999999999, 6.98, 6.98, 6.079999999999998, 10.04, 10.04, 17.06, 17.06, 23.0, 3.019999999999996, 1.0399999999999991, -0.03999999999999915, 3.019999999999996, 5.0, 5.0, 15.98, 15.98, 15.079999999999998, 15.98, 17.96, 15.98, 37.94, 41.0, 39.02, 28.04, 21.02, 21.02, 21.02, 19.939999999999998, 24.08, 30.02, 26.06, 23.0, 23.0, 32.0, 26.06, 24.08, 19.04, 19.04, 17.06, 17.06, 21.919999999999998, 21.02, 17.96, 17.96, 24.98, 26.96, 30.02, 28.939999999999998, 19.939999999999998, 19.939999999999998, 23.0, 19.04, 15.98, 15.98, 17.96, 26.96, 26.96, 28.939999999999998, 28.939999999999998, 28.939999999999998, 30.02, 32.0, 32.0, 24.08, 26.06, 28.939999999999998, 30.02, 30.02, 35.96, 35.06, 39.02, 33.98, 33.98, 35.96, 35.96, 33.08, 33.98, 17.96, 17.06, 24.08, 30.919999999999998, 32.0, 41.0, 37.94, 37.94, 44.06, 42.980000000000004, 37.04, 37.04, 37.04, 42.08, 46.94, 48.019999999999996, 44.06, 33.98, 32.0, 32.0, 35.96, 39.92, 46.94, 46.04, 46.94, 28.939999999999998, 26.06, 26.96, 37.04, 39.92, 39.92, 26.96, 28.04, 42.08, 42.980000000000004, 39.92, 41.0, 46.94, 48.019999999999996, 35.96, 33.98, 33.98, 44.96, 48.92, 42.08, 44.06, 44.06, 46.94, 46.04, 42.980000000000004, 46.94, 50.0, 55.040000000000006, 51.08, 53.96, 57.92, 53.06, 48.019999999999996, 42.980000000000004, 46.94, 53.96, 60.08, 55.94, 57.92, 53.96, 48.019999999999996, 50.0, 53.96, 53.96, 51.980000000000004, 53.96, 57.92, 55.94, 60.980000000000004, 59.0, 57.92, 57.92, 59.0, 62.96, 68.0, 60.08, 64.03999999999999, 68.0, 62.96, 64.03999999999999, 62.06, 64.94, 62.96, 57.92, 55.94, 57.92, 57.019999999999996, 57.92, 64.03999999999999, 62.06, 64.94, 69.98, 66.02000000000001, 68.0, 62.06, 55.94, 59.0, 59.0, 62.06, 64.03999999999999, 64.03999999999999, 66.92, 66.02000000000001, 69.98, 68.0, 64.03999999999999, 64.94, 66.02000000000001, 64.94, 62.06, 60.980000000000004, 60.980000000000004, 62.06, 62.96, 64.94, 62.96, 66.92, 68.0, 62.06, 60.08, 57.92, 62.06, 64.03999999999999, 64.03999999999999, 66.92, 68.0, 62.06, 62.06, 62.06, 62.96, 64.03999999999999, 62.96, 62.06, 62.06, 62.06, 60.08, 60.08, 64.03999999999999, 64.94, 60.08, 59.0, 60.08, 66.02000000000001, 69.08000000000001, 62.06, 64.03999999999999, 64.03999999999999, 64.03999999999999, 60.980000000000004, 60.980000000000004, 62.06, 62.96, 60.980000000000004, 60.980000000000004, 64.03999999999999, 64.03999999999999, 66.02000000000001, 68.0, 66.02000000000001, 62.96, 62.06, 59.0, 60.08, 60.08, 62.06, 64.03999999999999, 60.08, 60.980000000000004, 60.08, 57.019999999999996, 55.94, 57.019999999999996, 57.92, 57.92, 60.08, 60.08, 57.92, 55.94, 48.019999999999996, 46.04, 46.94, 48.019999999999996, 48.92, 37.94, 37.94, 37.94, 42.980000000000004, 44.06, 42.980000000000004, 44.96, 37.04, 35.96, 39.02, 37.94, 42.980000000000004, 42.08, 35.06, 35.06, 37.04, 48.92, 37.04, 39.92, 28.939999999999998, 30.02, 30.02, 28.04, 35.06, 33.08, 30.919999999999998, 33.08, 41.0, 41.0, 37.94, 37.94, 42.08, 39.92, 35.96, 35.96, 33.98, 39.02, 37.04, 37.94, 28.04, 28.939999999999998, 28.04, 30.02, 32.0, 33.98, 37.94, 35.96, 33.08, 28.04, 28.939999999999998, 37.94, 30.919999999999998, 30.02, 30.02, 37.94, 28.04, 28.04, 21.919999999999998, 21.02, 21.919999999999998, 23.0, 24.08, 24.98, 26.96, 28.04, 30.919999999999998, 26.06, 26.96, 28.939999999999998, 8.059999999999999, 8.059999999999999, 19.04, 21.919999999999998, 10.04, 8.059999999999999, 19.04, 23.0, 23.0, 19.939999999999998, 21.919999999999998, 23.0, 23.0, 21.919999999999998, 24.98, 26.06, 26.06, 23.0, 21.02, 19.939999999999998, 19.04, 15.98, 17.96, 17.96, 21.919999999999998, 19.04]],"toyplot");
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t2d5a147961fa425e9f90ac47e3810c99",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 400.0, "min": 0.0}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 500.0, "min": 0.0}, "scale": "linear"}]);
    (function(axis, axis_id, projection)
            {
                axis.show_coordinates(axis_id, projection);
            })(modules["toyplot.coordinates.Axis"],"t876091922f364befb0d121f4433ac1d7",[{"domain": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 105.98, "min": -0.03999999999999915}, "range": {"bounds": {"max": Infinity, "min": -Infinity}, "max": 200.0, "min": 0.0}, "scale": "linear"}]);
    })();</script></div></div>

