##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
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


class Erne(AutotoolsPackage):
    """ERNE (Extended Randomized Numerical alignEr) is a short string
       alignment package whose goal is to provide an all-inclusive set of
       tools to handle short (NGS-like) reads."""

    homepage = "http://erne.sourceforge.net/"
    url      = "https://downloads.sourceforge.net/project/erne/2.1.1/erne-2.1.1-source.tar.gz"

    version('2.1.1', '3c26b80654e1ef6ef61085f0ecf75e65')

    variant('mpi', default=True, description='Enable MPI support.')

    depends_on('boost@1.4.0:1.59')
    depends_on('mpi', when='+mpi')

    def configure_args(self):
        if '+mpi' in self.spec:
            if self.spec['mpi'].name == 'openmpi':
                args = ['--enable-openmpi']
            if self.spec['mpi'].name == 'mpich':
                args = ['--enable-mpich']
        return args
