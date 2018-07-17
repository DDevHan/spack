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


class Grnboost(Package):
    """GRNBoost is a library built on top of Apache Spark that implements a
    scalable strategy for gene regulatory network (GRN) inference."""

    homepage = "https://github.com/aertslab/GRNBoost"

    version('2017-10-9', git='https://github.com/aertslab/GRNBoost.git',
            commit='26c836b3dcbb85852d3c6f4b8340e8655434da02')

    depends_on('sbt', type='build')
    depends_on('jdk', type=('build', 'run'))
    depends_on('xgboost+jvm-packages', type='run')
    depends_on('joda-time', type='run')
    depends_on('slf4j', type='run')
    depends_on('spark', type='run')

    def setup_environment(self, spack_env, run_env):
        grnboost_jar = join_path(self.prefix, 'target',
                                 'scala-2.11', 'GRNBoost.jar')
        xgboost_version = self.spec['xgboost'].version.string
        xgboost_jar = join_path(self.spec['xgboost'].prefix,
                                'xgboost4j-'+xgboost_version+'.jar')
        jodatime_version = self.spec['joda-time'].version.string
        jodatime_jar = join_path(self.spec['joda-time'].prefix.bin,
                                 'joda-time-'+jodatime_version+'.jar')
        run_env.set('GRNBOOST_JAR', grnboost_jar)
        run_env.set('JAVA_HOME', self.spec['jdk'].prefix)
        run_env.set('CLASSPATH', xgboost_jar)
        run_env.prepend_path('CLASSPATH', jodatime_jar)
        run_env.set('XGBOOST_JAR', xgboost_jar)

    def install(self, spec, prefix):
        sbt = which('sbt')
        sbt('assembly')
        install_tree('target', prefix.target)
