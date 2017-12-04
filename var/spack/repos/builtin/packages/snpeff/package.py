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


class Snpeff(Package):
    """SnpEff: Genetic variant annotation and effect prediction toolbox."""

    homepage = "http://snpeff.sourceforge.net/"
    url      = "https://github.com/pcingola/SnpEff/archive/v4.3p.tar.gz"

    version('4.3', '977cae1b0baba3e735749312538412ce')

    depends_on('jdk', type=('build', 'run'))
    depends_on('maven', type='build')

    def url_for_version(self, version):
        url = 'https://github.com/pcingola/SnpEff/archive/v{0}p.tar.gz'
        return url.format(version)

    resource(
        name='SnpSift',
        url='https://github.com/pcingola/SnpSift/archive/v4.3p.tar.gz',
        destination='snpsift'
    )

    def install(self, spec, prefix):
        mvn = which('mvn')

        # Build libraries
        with working_dir('lib'):
            mvn('install:install-file', '-Dfile=antlr-4.5.1-complete.jar',
                '-DgroupId=org.antlr', '-DartifactId=antlr', '-Dversion=4.5.1',
                '-Dpackaging=jar')
            mvn('install:install-file', '-Dfile=biojava3-core-3.0.7.jar',
                '-DgroupId=org.biojava', '-DartifactId=biojava3-core',
                '-Dversion=3.0.7', '-Dpackaging=jar')
            mvn('install:install-file', '-Dfile=biojava3-structure-3.0.7.jar',
                '-DgroupId=org.biojava', '-DartifactId=biojava3-structure',
                 '-Dversion=3.0.7', '-Dpackaging=jar')

        # Build SnpEff
        mvn('clean', 'compile', 'assembly:assembly')
        install(join_path('target', 'SnpEff-{0}-jar-with-dependencies.jar'.format(self.version)),
                join_path(self.stage.source_path, 'lib', 'snpEff.jar'))
        mvn('install:install-file', '-Dfile=target/SnpEff-{0}.jar'.format(self.version),
            '-DgroupId=org.snpeff', '-DartifactId=SnpEff', '-Dversion=$VERSION',
	    '-Dpackaging=jar', '-DgeneratePom=true', '--quiet')

        # Build SnpSift
        with working_dir(join_path('snpsift', 'SnpSift-{0}p'.format(self.version))):
            mvn('clean', 'compile', 'assembly:assembly')
            install(join_path('target', 'SnpSift-{0}-jar-with-dependencies.jar'.format(self.version)),
                    join_path(self.stage.source_path, 'lib', 'SnpSift.jar'))
            mvn('install:install-file', '-Dfile=target/SnpSift-{0}.jar'.format(self.version),
                '-DgroupId=org.snpsift', '-DartifactId=SnpSift',
                '-Dversion=$VERSION', '-Dpackaging=jar', '-DgeneratePom=true',
                '--quiet')

        # Update galaxy databases
        with working_dir('scripts_build'):
            galaxy = Executable('./galaxy.sh')
            galaxy()
        
        # install_tree('lib', prefix.lib)
        # install_tree('scripts', prefix.lib.scripts)
