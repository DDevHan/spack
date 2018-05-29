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


class Blasr(Package):
    generator = 'Ninja'
    """The PacBio long read aligner."""

    homepage = "https://github.com/PacificBiosciences/blasr/wiki"
    url      = "https://github.com/PacificBiosciences/blasr/tarball/eab53fd220a05dfd7290962360a6ccce55be9c7c"

    version('2018.04.11', '42b298230213928a43652db7981e82fe',
            url="https://github.com/PacificBiosciences/blasr/tarball/eab53fd220a05dfd7290962360a6ccce55be9c7c") 

    depends_on('ncurses')
    depends_on('hdf5')
    depends_on('htslib')
    depends_on('zlib')
    depends_on('boost')
    depends_on('pbbam')
    depends_on('pkgconfig')
    depends_on('ninja')
    depends_on('blasr-libcpp')
    
    phases = ['configure','install']

    def configure(self, spec, prefix):
	configure_args=[]
        configure_args.append('LIBPBDATA_INC={0}'.format(self.spec['blasr-libcpp'].prefix.pbdata)) 
	configure_args.append('LIBPBDATA_LIB={0}'.format(self.spec['blasr-libcpp'].prefix.pbdata))
	configure_args.append('LIBBLASR_LIB={0}'.format(self.spec['blasr-libcpp'].prefix.alignment))
	configure_args.append('LIBBLASR_INC={0}'.format(self.spec['blasr-libcpp'].prefix.alignment))
	configure_args.append('LIBPBIHDF_INC={0}'.format(self.spec['blasr-libcpp'].prefix.hdf))
	configure_args.append('LIBPBIHDF_LIB={0}'.format(self.spec['blasr-libcpp'].prefix.hdf))
	configure_args.append('RT_LIBFLAGS={0}'.format(self.spec['blasr-libcpp'].prefix.hdf))
	configure_args.append('HDF5_INC={0}'.format(self.spec['hdf5'].prefix.include))
	configure_args.append('--shared')
#	configure_args.append('HDF5_LIB={0}'.format(self.spec['hdf5'].prefix.lib))
#	configure_args.append('Boost_INCLUDE_DIRS={0}'.format(self.spec['boost'].prefix))
    	python('configure.py', *configure_args)
        
    def install(self, spec, prefix):
	make()
