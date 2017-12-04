##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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
import inspect


class PyIpyrad(Package):
    """Interactive assembly and analysis of RADseq data sets."""

    homepage = "http://ipyrad.readthedocs.io/"
    url      = "https://github.com/dereneaton/ipyrad/archive/0.7.13.tar.gz"

    version('0.7.13', '5009b099d038f7a53c1c390333ea3576')

    depends_on('miniconda2', type=('build', 'link', 'run'))

    def build(self, spec, prefix):
        answer = ['y\n']
        answer_filename = 'spack-config.in'
        conda = which('conda')

        with open(answer_filename, 'w') as f:
            f.writelines(answer)

        with open(answer_filename, 'r') as f:
            conda('install', '-c', 'ipyrad', 'ipyrad', input=f)
