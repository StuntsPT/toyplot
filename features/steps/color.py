# Copyright 2014, Sandia Corporation. Under the terms of Contract
# DE-AC04-94AL85000 with Sandia Corporation, the U.S. Government retains certain
# rights in this software.

from __future__ import division

from behave import *

import json
import nose.tools
import numpy
import toyplot.color
import toyplot.testing


@when(u'toyplot.color.css receives {value}')
def step_impl(context, value):
    context.value = value


@then(u'toyplot.color.css should return {value}')
def step_impl(context, value):
    toyplot.testing.assert_color_equal(
        toyplot.color.css(context.value), eval(value))


@when(u'toyplot.color.to_css receives {value}')
def step_impl(context, value):
    context.value = eval(value)


@then(u'toyplot.color.to_css should return {value}')
def step_impl(context, value):
    nose.tools.assert_equal(toyplot.color.to_css(context.value), value)


@given(u'a color value')
def step_impl(context):
    context.value = toyplot.color.css("red")


@then(u'the color value can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        toyplot.color._jupyter_color_swatches(context.value), "color-swatch")


@given(u'a collection of Color Brewer palettes')
def step_impl(context):
    context.palettes = toyplot.color.brewer.palettes()


@then(u'each palette can be rendered as ipython html')
def step_impl(context):
    for name, palette in context.palettes:
        toyplot.testing.assert_html_equal(
            palette._repr_html_(), "color-brewer-%s" % name)


@given(u'a color brewer category, the palette names for that category can be retrieved.')
def step_impl(context):
    nose.tools.assert_equal(toyplot.color.brewer.names("sequential"), [
        'BlueGreen',
        'BlueGreenYellow',
        'BluePurple',
        'Blues',
        'BrownOrangeYellow',
        'GreenBlue',
        'GreenBluePurple',
        'GreenYellow',
        'Greens',
        'Greys',
        'Oranges',
        'PurpleBlue',
        'PurpleRed',
        'Purples',
        'RedOrange',
        'RedOrangeYellow',
        'RedPurple',
        'Reds',
    ])
    nose.tools.assert_equal(toyplot.color.brewer.names("diverging"), [
      'BlueGreenBrown',
      'BlueRed',
      'BlueYellowRed',
      'GrayRed',
      'GreenYellowRed',
      'PinkGreen',
      'PurpleGreen',
      'PurpleOrange',
      'Spectral',
    ])
    nose.tools.assert_equal(toyplot.color.brewer.names("qualitative"), [
        'Accent',
        'Dark2',
        'Paired',
        'Pastel1',
        'Pastel2',
        'Set1',
        'Set2',
        'Set3',
    ])


@given(u'a color brewer palette name, the color counts for that palette  can be retrieved.')
def step_impl(context):
    nose.tools.assert_equal(toyplot.color.brewer.counts("BlueRed"), [3, 4, 5, 6, 7, 8, 9, 10, 11])


@given(u'a color brewer palette name, the category for that palette  can be retrieved.')
def step_impl(context):
    nose.tools.assert_equal(toyplot.color.brewer.category("BlueRed"), "diverging")


@when(u'the user creates a Color Brewer palette')
def step_impl(context):
    context.palette = toyplot.color.brewer.palette("BlueYellowRed")


@then(u'the Color Brewer palette should have the maximum number of colors')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-brewer")


@when(u'the user creates a sized Color Brewer palette')
def step_impl(context):
    context.palette = toyplot.color.brewer.palette("BlueYellowRed", 5)


@then(u'the Color Brewer palette should have the requested number of colors')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-brewer-count")


@when(u'the user creates a reversed Color Brewer palette')
def step_impl(context):
    context.palette = toyplot.color.brewer.palette("BlueYellowRed", 5, reverse=True)


@then(u'the Color Brewer palette should have its colors reversed')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-brewer-reverse")


@given(u'a collection of diverging color maps')
def step_impl(context):
    context.color_maps = toyplot.color.diverging.maps()


@then(u'each diverging color map can be rendered as ipython html')
def step_impl(context):
    for name, color_map in context.color_maps:
        toyplot.testing.assert_html_equal(
            color_map._repr_html_(), "color-diverging-map-%s" % name)


@when(u'the user creates a default diverging color map')
def step_impl(context):
    context.color_map = toyplot.color.DivergingMap()


@then(u'the default diverging color map can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.color_map._repr_html_(), "color-diverging-map")


@when(u'the user creates a custom diverging color map')
def step_impl(context):
    context.color_map = toyplot.color.DivergingMap(
        toyplot.color.rgb(0.7, 0, 0), toyplot.color.rgb(0, 0.6, 0))


@then(u'the custom diverging color map can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.color_map._repr_html_(), "color-diverging-map-custom")


@when(u'the user creates a default diverging color map with domain')
def step_impl(context):
    context.color_map = toyplot.color.DivergingMap(domain_min=0, domain_max=1)


@then(u'individual values can be mapped to colors by the diverging color map')
def step_impl(context):
    toyplot.testing.assert_color_equal(
        context.color_map.color(-1), [0.33479085, 0.28308437, 0.75649522, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(0), [0.33479085, 0.28308437, 0.75649522, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(0.5), [0.86541961, 0.86538428, 0.86533315, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(1), [0.69462562, 0.00296461, 0.15458183, 1.])
    toyplot.testing.assert_color_equal(
        context.color_map.color(2), [0.69462562, 0.00296461, 0.15458183, 1.])


@then(
    u'individual values can be mapped to css colors by the diverging color map')
def step_impl(context):
    nose.tools.assert_equal(
        context.color_map.css(-1), "rgba(33.5%,28.3%,75.6%,1.000)")
    nose.tools.assert_equal(
        context.color_map.css(0), "rgba(33.5%,28.3%,75.6%,1.000)")
    nose.tools.assert_equal(
        context.color_map.css(0.5), "rgba(86.5%,86.5%,86.5%,1.000)")
    nose.tools.assert_equal(
        context.color_map.css(1), "rgba(69.5%,0.3%,15.5%,1.000)")
    nose.tools.assert_equal(
        context.color_map.css(2), "rgba(69.5%,0.3%,15.5%,1.000)")


@given(u'a linear color map')
def step_impl(context):
    context.color_map = toyplot.color.LinearMap(
        toyplot.color.Palette(["red", "blue"]), domain_min=0, domain_max=1)


@then(u'the linear color map can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.color_map._repr_html_(), "color-linear-map")


@then(u'the linear color map can map scalar values to toyplot colors')
def step_impl(context):
    toyplot.testing.assert_color_equal(
        context.color_map.color(-1), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(0), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(0.5), (0.5, 0, 0.5, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(1), (0, 0, 1, 1))
    toyplot.testing.assert_color_equal(
        context.color_map.color(2), (0, 0, 1, 1))


@then(u'the linear color map can map scalar values to css colors')
def step_impl(context):
    nose.tools.assert_equal(context.color_map.css(-1), "rgba(100.0%,0.0%,0.0%,1.000)")
    nose.tools.assert_equal(context.color_map.css(0), "rgba(100.0%,0.0%,0.0%,1.000)")
    nose.tools.assert_equal(context.color_map.css(0.5), "rgba(50.0%,0.0%,50.0%,1.000)")
    nose.tools.assert_equal(context.color_map.css(1), "rgba(0.0%,0.0%,100.0%,1.000)")
    nose.tools.assert_equal(context.color_map.css(2), "rgba(0.0%,0.0%,100.0%,1.000)")


@then(u'the color map domain can be changed')
def step_impl(context):
    nose.tools.assert_equal(context.color_map.domain.min, 0)
    nose.tools.assert_equal(context.color_map.domain.max, 1)
    context.color_map.domain.min = -1
    context.color_map.domain.max = 2
    nose.tools.assert_equal(context.color_map.domain.min, -1)
    nose.tools.assert_equal(context.color_map.domain.max, 2)


@given(u'a starting color')
def step_impl(context):
    context.color = toyplot.color.Palette().color(0)


@then(u'the color can be used to generate a palette of lighter shades')
def step_impl(context):
    palette = toyplot.color.spread(context.color)
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-spread")


@given(u'two color palettes')
def step_impl(context):
    context.palettes = [
        toyplot.color.brewer.palette("Reds"), toyplot.color.brewer.palette("Blues")]


@then(u'the color palettes can be concatenated into a single palette')
def step_impl(context):
    palette = context.palettes[0] + context.palettes[1]
    toyplot.testing.assert_html_equal(
        palette._repr_html_(), "color-palette-add")


@given(u'a color palette')
def step_impl(context):
    context.palette = toyplot.color.brewer.palette("Reds")


@then(u'another palette can be appended')
def step_impl(context):
    context.palette += toyplot.color.brewer.palette("Blues")
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-palette-iadd")


@given(u'a default color palette')
def step_impl(context):
    context.palette = toyplot.color.Palette()


@then(u'the palette should contain 8 colors')
def step_impl(context):
    nose.tools.assert_equal(len(context.palette), 8)


@then(u'the default palette can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-palette")


@given(u'a reversed default color palette')
def step_impl(context):
    context.palette = toyplot.color.Palette(reverse=True)


@then(u'the reversed palette can be rendered as ipython html')
def step_impl(context):
    toyplot.testing.assert_html_equal(
        context.palette._repr_html_(), "color-palette-reverse")

@given(u'a list of CSS colors, a color palette can be created')
def step_impl(context):
    colors = ["red", "green", "blue", "black"]
    palette = toyplot.color.Palette(colors)
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-palette-css-list")

@given(u'an array of CSS colors, a color palette can be created')
def step_impl(context):
    colors = numpy.array(["red", "green", "blue", "black"])
    palette = toyplot.color.Palette(colors)
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-palette-css-array")

@given(u'a list of RGB tuples, a color palette can be created')
def step_impl(context):
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
    palette = toyplot.color.Palette(colors)
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-palette-rgb-tuples")

@given(u'a list of RGBA tuples, a color palette can be created')
def step_impl(context):
    colors = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (0, 0, 0, 0.5)]
    palette = toyplot.color.Palette(colors)
    toyplot.testing.assert_html_equal(palette._repr_html_(), "color-palette-rgba-tuples")

@given(u'a color palette, colors can be retrieved using item notation')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    toyplot.testing.assert_color_equal(palette[0], (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(palette[1], (0, 1, 0, 1))
    toyplot.testing.assert_color_equal(palette[-1], (0, 0, 1, 1))
    with nose.tools.assert_raises(IndexError):
        palette[3]
    with nose.tools.assert_raises(TypeError):
        palette[0:3]

@given(u'a color palette, callers can iterate over the colors')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    color = iter(palette)
    toyplot.testing.assert_color_equal(next(color), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(next(color), (0, 1, 0, 1))
    toyplot.testing.assert_color_equal(next(color), (0, 0, 1, 1))
    with nose.tools.assert_raises(StopIteration):
        next(color)

@given(u'a color palette, callers can retrieve colors by index')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    toyplot.testing.assert_color_equal(palette.color(0), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(palette.color(-1), (0, 0, 1, 1))

@given(u'a color palette, colors can retrieve css colors by index')
def step_impl(context):
    palette = toyplot.color.Palette([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    nose.tools.assert_equal(palette.css(0), "rgba(100.0%,0.0%,0.0%,1.000)")
    nose.tools.assert_equal(palette.css(-1), "rgba(0.0%,0.0%,100.0%,1.000)")

@given(u'a categorical color map, the map can be rendered as ipython html')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.brewer.palette("BlueGreenBrown", 3))
    toyplot.testing.assert_html_equal(colormap._repr_html_(), "color-categorical-map")

@given(u'a categorical color map, multiple colors can be returned by index')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
    toyplot.testing.assert_colors_equal(colormap.colors(
        [0, 1, 3, 4]), [(1, 0, 0, 1), (0, 1, 0, 1), (1, 1, 1, 1), (1, 0, 0, 1)])

@given(u'a categorical color map, individual colors can be returned by index')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
    toyplot.testing.assert_color_equal(colormap.color(0), (1, 0, 0, 1))
    toyplot.testing.assert_color_equal(colormap.color(-1), (1, 1, 1, 1))

@given(u'a categorical color map, individual css colors can be returned by index')
def step_impl(context):
    colormap = toyplot.color.CategoricalMap(
        toyplot.color.Palette(["red", "lime", "blue", (1, 1, 1)]))
    nose.tools.assert_equal(colormap.css(0), "rgba(100.0%,0.0%,0.0%,1.000)")
    nose.tools.assert_equal(colormap.css(-1), "rgba(100.0%,100.0%,100.0%,1.000)")

