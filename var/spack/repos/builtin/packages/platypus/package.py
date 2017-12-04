##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
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
import subprocess
import glob

class Platypus(Package):
    """A Haplotype-Based Variant Caller For Next Generation Sequence Data"""

    homepage = "http://www.well.ox.ac.uk/platypus"
    url      = "http://www.well.ox.ac.uk/bioinformatics/Software/Platypus-latest.tgz"

    version('0.8.1', 'edf3fb5bf080241ddb75a413c8529d57')

    depends_on('python@2.6:')
    depends_on('py-cython', type=('build', 'run'))
    depends_on('htslib')

    def install(self, spec, prefix):
        subprocess.call(['./buildPlatypus.sh'])
        mkdirp(prefix.bin)
        mkdirp(prefix.lib)
        files = glob.iglob("*.py")
        for file in files:
            install(file, prefix.bin)
        files = glob.iglob("*.so")
        for file in files:
            install(file, prefix.lib)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', prefix.lib)
