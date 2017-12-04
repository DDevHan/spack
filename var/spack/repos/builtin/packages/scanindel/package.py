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


class Scanindel(Package):
    """ScanIndel is a python program to detect indels (insertions and
       deletions) from NGS data by re-align and de novo assemble soft clipped
       reads."""

    homepage = "https://github.com/cauyrd/ScanIndel"
    url      = "https://github.com/cauyrd/ScanIndel/archive/v1.2.tar.gz"

    version('1.2', '7cc6f4122149de9b791e48859fe69dbe')

    depends_on('bedtools2')
    depends_on('samtools')
    depends_on('bwa')
    depends_on('blat')
    depends_on('freebayes')
    depends_on('trinity')
    depends_on('python@2.7.0:2.7.999', type=('build', 'run'))
    depends_on('py-pysam', type=('build', 'run'))
    depends_on('py-pyvcf', type=('build', 'run'))
    depends_on('py-biopython', type=('build', 'run'))
    depends_on('py-scipy', type=('build', 'run'))
    depends_on('py-numpy', type=('build', 'run'))

    def setuo_environment(self, spack_env, run_env):
        run_env.set('SCANINDEL_HOME', prefix.bin)

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('ScanIndel.py', prefix.bin)
        install_tree('tools', prefix.bin.tools)
