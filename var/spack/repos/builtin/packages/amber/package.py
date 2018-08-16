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
import os

class Amber(Package):
    """Amber is a suite of biomolecular simulation programs."""

    homepage = "http://ambermd.org"
    url      = "file://{0}/Amber16.tar.bz2".format(os.getcwd())

    version('16', '2d52556093a8c878b64f35b2ac2aae20')

    # depends_on('ambertools') # not in spack yet
    depends_on('flex')
    depends_on('tcsh')
    depends_on('zlib')
    depends_on('bzip2')
    depends_on('libxt')
    depends_on('libxtext')
    depends_on('libxdmcp')
    # depends_on('tkinter') # not in spack yet
    depends_on('openmpi')
    depends_on('cuda', when='+cuda')
    depends_on('perl')
    depends_on('perl-extutils-makemaker')
    depends_on('patch')
    depends_on('bison')
    depends_on('boost')

    variant('cuda', default=False, description='Build with cuda support')

    def install(self, spec, prefix):
        # FIXME: Unknown build system
        make()
        make('install')
