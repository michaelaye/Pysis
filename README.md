# Pysis
A robust toolkit for using [USGS ISIS 3][isis] in Python.

## How to install
First you must have [USGS ISIS 3][isis] installed on your machine. See the ISIS
3 [installation guide][install] for further instructions. Remember to set your
environmental variables (see step 4 of USGS ISIS guide) so Pysis knows where
your installation is.

To then install Pysis first [download][download] and extract Pysis. Then install
the packages with:

    python setup.py install

## Quickstart Guide
How to write ISIS 3 code in python using Pysis.

Using ISIS 3 at the command line you might want to run the following basic
commands (examples for the MDIS camera on the MESSENGER mission):

    mdis2isis from=filename.IMG to=filename.cub
    spiceinit from=filename.cub
    mdiscal from=filename.cub to=filename.cal.cub

using Pysis the syntax is:

    from pysis.isis import mdis2isis, spiceinit, mdiscal
    from pysis.util import file_variations

    def calibrate_mids(img_name):
        (cub_name, cal_name) = file_variations(img_name, ['.cub', '.cal.cub'])

        mdis2isis(from_=img_name, to=cub_name)
        spiceinit(from_=cub_name)
        mdiscal(from_=cub_name, to=cal_name)

You will notice that we use the keyword `from_` when we call a command  because
`from` is a reserved word in python.

### Numerical and String Arguments

Here is an example of the maptemplate and cam2map commands in Pysis:

    from pysis import isis

    isis.maptemplate(map='MDIS_eqr.map', projection='equirectangular',
                     clon=0.0, clat=0.0, resopt='mpp', resolution=1000,
                     rngopt='user', minlat=-10.0, maxlat=10.0, minlon=-10.0,
                     maxlon=10.0)

    isis.cam2map(from_=cal_name, to=proj_name, pixres='map',
                 map='MDIS_eqr.map',defaultrange='map')

### Getting values from ISIS commands

Here is an example of how to receive values that are returned on STDOUT from ISIS tools.
The example command we are using is `getkey` to receive values from the label of an
ISIS cube:

    value = getkey.check_output(from_='W1467351325_4.map.cal.cub',
                                keyword='minimumringradius',
                                grp='mapping')

### Multiprocessing Isis Commands with IsisPool

Pysis has built-in support to make multiprocessing isis commands simple. To run
the above MDIS calibration script for multiple images in multiple processes we
could rewrite the function as so:

    from pysis import IsisPool
    from pysis.util import file_variations

    def calibrate_mdis(images):
        images = [(img_name,) + file_variations(img_name, ['.cub', '.cal.cub'])
                    for img_name in images]

        with IsisPool() as isis_pool:
            for img_name, cub_name, cal_name in images:
                isis_pool.mdis2isis(from_=img_name, to=cub_name)

        with IsisPool() as isis_pool:
            for img_name, cub_name, cal_name in images:
                isis_pool.spiceinit(from_=cub_name)

        with IsisPool() as isis_pool:
            for img_name, cub_name, cal_name in images:
                isis_pool.mdiscal(from_=cub_name, to=cal_name)

When using IsisPool we can't determine which order commands will be executed in
so we much run each command for all the files as a group before moving to the
next command and creating a new IsisPool.

[isis]: http://isis.astrogeology.usgs.gov/  "USGS ISIS 3"
[install]: http://isis.astrogeology.usgs.gov/documents/InstallGuide/
[download]: https://github.com/wtolson/Pysis/tarball/master
