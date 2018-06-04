##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Libcf(AutotoolsPackage):
    """The CF conventions for climate and forecast metadata are designed to
    promote the processing and sharing of files created with the netCDF API.
    This library makes it easier to create and work with CF data files."""

    homepage = "https://www.unidata.ucar.edu/software/libcf/html/index.html"
    url      = "ftp://ftp.unidata.ucar.edu/pub/libcf/libcf-daily.tar.gz"

    version('1.0', 'a03598b2ba389f4a2e00b8b8e494c832')

    depends_on('netcdf@4:')
    depends_on('hdf5')
    depends_on('zlib')

    def configure_args(self):
        return ['--enable-netcdf-4']
