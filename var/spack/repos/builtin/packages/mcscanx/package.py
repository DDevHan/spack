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


class Mcscanx(MakefilePackage):
    """MCScanX is an algorithm to scan multiple genomes or subgenomes to
       identify putative homologous chromosomal regions, then align these
       regions using genes as anchors."""

    homepage = "http://chibba.pgml.uga.edu/mcscan2/"
    url      = "https://github.com/wyp1125/MCScanX"

    version('2017-01-04', commit='7b61f32a6bc704cea85ad429bb50b3569d65f3f1',
            git='https://github.com/wyp1125/MCScanX.git')

    depends_on('java', type=('build', 'run'))
    depends_on('perl', type=('build', 'run'))
    depends_on('libpng')

    def install(self, spec, prefix):
        mkdirp('prefix.bin')
        install('MCScanX_h', prefix.bin)
        install('MCScanX', prefix.bin)
        install('duplicate_gene_classifier', prefix.bin)
        install_tree('data', prefix.bin.data)
        install_tree('downstream_analyses', prefix.bin.downstream_analyses)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PREFIX', self.spec.prefix.downstream_analyses)
