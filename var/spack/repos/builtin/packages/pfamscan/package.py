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


class Pfamscan(Package):
    """pfam_scan.pl is a Perl script calling HMMER v3 to search a FASTA
    file against a library of Pfam HMMs."""

    homepage = "http://www.sanger.ac.uk/science/tools/pfam"
    url      = "http://ftp.ebi.ac.uk/pub/databases/Pfam/Tools/PfamScan.tar.gz"

    version('1.6', '652b22f19038320fd925db4937134305')

    depends_on('hmmer@3.1b2')
    depends_on('perl-moose')
    depends_on('perl-bio-perl')
    depends_on('perl-ipc-run')

    def install(self, spec, prefix):
        install_tree('Bio', prefix.bin.Bio)
        install('ChangeLog', prefix.bin)
        install('pfam_scan.pl', prefix.bin)
        install('README', prefix.bin)

    def setup_environment(self, spack_env, run_env):
        run_env.prepend_path('PERL5LIB', prefix.bin)
