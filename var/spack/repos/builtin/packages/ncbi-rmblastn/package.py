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


class NcbiRmblastn(AutotoolsPackage):
    """RMBlast search engine for NCBI."""

    homepage = "https://www.ncbi.nlm.nih.gov/"
    url      = "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/rmblast/LATEST/ncbi-rmblastn-2.2.28-src.tar.gz"

    version('2.6.0', 'c8ce8055b10c4d774d995f88c7cc6225',
            url='ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-blast-2.6.0+-src.tar.gz')
    version('2.2.28', 'fb5f4e2e02ffcb1b17af2e9f206c5c22')

    # This patch contains the changes by the repeatmasker authors
    # to make ncbi-blast into rmblastn and is how they've decided
    # to distribute version 2.6.0
    patch('isb-2.6.0+-changes-vers2.patch', when='@2.6.0', level=1)

    configure_directory = 'c++'
    build_directory = 'c++'

    def configure_args(self):
        options = [
            '--without-internal',
            '--with-mt',
            '--without-debug',
            '--without-krb5',
            '--without-check',
            '--without-bz2',
            '--without-lzo',
            '--with-strip',
            '--with-ncbi-public',
            '--without-ncbi-c',
            '--without-sss',
            '--without-sssdb',
            '--without-pcre',
            '--without-gcrypt',
            '--without-gnutls',
            '--without-openssl',
            '--without-sybase',
            '--without-ftds',
            '--without-mysql',
            '--without-opengl',
            '--without-mesa',
            '--without-glut',
            '--without-glew',
            '--without-wxwidgets',
            '--without-freetype',
            '--without-ftgl',
            '--without-fastcgi',
            '--without-bdb',
            '--without-sp',
            '--without-orbacus',
            '--without-sqlite3',
            '--without-icu',
            '--without-expat',
            '--without-sablot',
            '--without-libxml',
            '--without-libxslt',
            '--without-libexslt',
            '--without-xerces',
            '--without-xalan',
            '--without-zorba',
            '--without-oechem',
            '--without-sge',
            '--without-muparser',
            '--without-hdf5',
            '--without-gif',
            '--without-png',
            '--without-tiff',
            '--without-xpm',
            '--without-magic',
            '--without-curl',
            '--without-mimetic',
            '--without-3psw',
            '--without-local-lbsm',
            '--without-ncbi-crypt',
            '--without-connext',
            '--without-dbapi',
            '--without-ctools',
            '--without-gui',
            '--without-gbench'
        ]
        if self.spec.version == Version('2.6.0'):
            options += [
                        '--without-vdb',
                        '--without-nettle',
                        '--without-gsoap',
                        '--without-avro',
                        '--without-cereal',
                        '--without-sasl2',
                        '--without-mongodb',
                        '--without-gmock',
                        '--without-lapack',
                        '--without-lmdb'
                       ]
        return options

    @when('@2.6.0')
    def install(self, spec, prefix):
        # make install fails on 2.6.0, override
        with working_dir('c++'):
            mkdirp(prefix.bin)
            install_tree('ReleaseMT/bin', prefix.bin)
