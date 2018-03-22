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
import glob
import os.path


class Rdptools(MakefilePackage):
    """An open source command-line tool suite for performing a complete
       workflow of analysis tasks of NGS data."""

    homepage = "https://github.com/rdpstaff/RDPTools"
    url      = "https://github.com/rdpstaff/RDPTools"

    version('2017-05-31', commit='ee73c1c67d2bb577993b23b9886fa984ca974fb5',
            git='https://github.com/rdpstaff/RDPTools.git', submodules=True)

    depends_on('jdk', type=('build', 'run'))
    depends_on('ant@1.9.0:1.9.9', type=('build', 'run'))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.jar)
        for jar_file in glob.glob(join_path(self.stage.source_path, '*.jar')):
            install(jar_file, prefix.jar)

            jar_name = os.path.basename(jar_file).replace('.jar', '')
            script_sh = join_path(os.path.dirname(__file__), jar_name + '.sh')
            script = join_path(prefix.bin, jar_name)
            install(script_sh, script)
            set_executable(script)

            java = join_path(self.spec['jdk'].prefix.bin, 'java')
            kwargs = {'backup': False}
            filter_file('^java', java, script, **kwargs)
            filter_file(jar_name + '.jar', join_path(prefix.jar, jar_name + '.jar'),
                        script, **kwargs)
