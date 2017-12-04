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
import distutils.dir_util


class Progressivecactus(MakefilePackage):
    """Progressive Cactus is a whole-genome alignment package."""

    homepage = "https://github.com/glennhickey/progressiveCactus"
    url      = "https://github.com/glennhickey/progressiveCactus"

    version('2017-5-11', git='https://github.com/glennhickey/progressiveCactus.git',
            commit='86d5e3fb5e0e656c3208e4a34b21ce0068f7981f', submodules=True)

    depends_on('python@2.7.0:2.7.999', type=('build', 'run'))
    depends_on('git')

    def edit(self, spec, prefix):
        with working_dir('bin'):
            edit = FileFilter('runProgressiveCactus.sh')
            edit.filter('. \$\{envFile\} \&\& ', '')

    def install(self, spec, prefix):
        distutils.dir_util.copy_tree(".", prefix)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PATH', self.prefix.submodules.tokyocabinet.bin)
        run_env.set('tokyoCabinetIncl',
                    self.prefix.submodules.tokyocabinet.include)
        run_env.set('tokyoCabinetLib',
                    self.prefix.submodules.tokyocabinet.lib)
        run_env.prepend_path('PATH', self.prefix.submodules.kyotocabinet.bin)
        run_env.prepend_path('LD_LIBRARY_PATH',
                             self.prefix.submodules.kyotocabinet.lib)
        run_env.prepend_path('LD_LIBRARY_PATH',
                             self.prefix.submodules.kyototycoon.lib)
        run_env.prepend_path('PATH', self.prefix.submodules.kyototycoon.bin)
        run_env.set('kyotoTycoonIncl',
                             self.prefix.submodules.kyotocabinet.include)
        run_env.set('kyotoTycoonLib', self.prefix.submodules.kyototycoon.lib)
        run_env.prepend_path('SON_TRACE_DATASETS',
                             self.prefix.submodules.cactusTestData)
        run_env.prepend_path('PATH',
                             self.prefix.submodules.pinchesAndCacti.bin)
        run_env.prepend_path('PATH',
                             self.prefix.submodules.matchingAndOrdering.bin)
        run_env.prepend_path('PATH', self.prefix.submodules.cactus.bin)
        run_env.prepend_path('PATH', self.prefix.submodules.hal.bin)
        run_env.prepend_path('PATH', self.prefix.submodules.cactus2hal.bin)
        run_env.prepend_path('PATH', self.prefix.submodules.kentToolBinaries)
