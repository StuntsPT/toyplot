# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import absolute_import
from __future__ import division

import tempfile
import toyplot.compatibility
import toyplot.qt
import toyplot.svg
import xml.etree.ElementTree as xml


def render(canvas, fobj=None, width=None, height=None, scale=None):
    """Render the PDF representation of a canvas using Qt.

    Because the canvas dimensions are specified explicitly at creation time, they
    map directly to real-world units in the output PDF image.  Use one of
    `width`, `height`, or `scale` to override this behavior.

    Parameters
    ----------
    canvas: :class:`toyplot.canvas.Canvas`
      Canvas to be rendered.
    fobj: file-like object or string
      The file to write.  Use a string filepath to write data directly to disk.
      If `None` (the default), the PDF data will be returned to the caller
      instead.
    width: number, string, or (number, string) tuple, optional
      Specify the width of the output image with optional units.  If the units
      aren't specified, defaults to points.  See :ref:`units` for details on
      unit conversion in Toyplot.
    height: number or (number, string) tuple, optional
      Specify the height of the output image with optional units.  If the units
      aren't specified, defaults to points.  See :ref:`units` for details on
      unit conversion in Toyplot.
    scale: number, optional
      Scales the output `canvas` by the given ratio.

    Returns
    -------
    pdf: PDF data, or `None`
      PDF representation of `canvas`, or `None` if the caller specifies the
      `fobj` parameter.

    Examples
    --------

    >>> toyplot.pdf.render(canvas, "figure-1.pdf", width=(4, "inches"))
    """
    qapplication = toyplot.qt.application()

    svg = toyplot.svg.render(canvas)
    scale = canvas._point_scale(width=width, height=height, scale=scale)
    #surface = cairo.PDFSurface(fobj, scale * canvas._width, scale * canvas._height)

    page = toyplot.qt.QWebPage()
    page.mainFrame().setContent(xml.tostring(toyplot.svg.render(canvas)), "image/svg+xml")
    page.setViewportSize(page.mainFrame().contentsSize())

    page_size = toyplot.qt.QPageSize(
        toyplot.qt.QSizeF(
            toyplot.units.convert((canvas._width, "px"), "pt"),
            toyplot.units.convert((canvas._height, "px"), "pt")),
        toyplot.qt.QPageSize.Point,
        matchPolicy=toyplot.qt.QPageSize.ExactMatch)

    printer = toyplot.qt.QPrinter()
    printer.setPageSize(page_size)
    printer.setOutputFormat(toyplot.qt.QPrinter.PdfFormat)
    if isinstance(fobj, toyplot.compatibility.string_type):
        printer.setOutputFileName(fobj)
        page.mainFrame().print_(printer)
    else:
        fd, path = tempfile.mkstemp(suffix=".pdf")
        printer.setOutputFileName(path)
        page.mainFrame().print_(printer)
        if fobj is None:
            return open(path, "r").read()
        else:
            fobj.write(open(path, "r").read())

