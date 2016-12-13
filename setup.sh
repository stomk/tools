#!/bin/bash

PROGNAME=$(basename $0)

print_usage() {
	echo "Usage: ./$PROGNAME -d INSTALL_DIR [-f]"
	echo "Options:"
	echo "  -d, --dir INSTALL_DIR    specify path to install directory"
	echo "  -f, --force              overwrite files if files with the same name exist in install directory"
}

guide_to_usage() {
	echo "Type '-h' for help"
}

for OPT in "$@"; do
	case $OPT in
		'-h'|'--help' )
			print_usage
			exit 0
			;;
		'-d'|'--dir' )
			if [[ -z $2 ]] || [[ $2 =~ ^-+ ]]; then
				echo "Error: specify path to install directory"
				guide_to_usage
				exit 1
			fi
			INS_DIR=$2
			shift 2
			;;
		'-f'|'--force' )
			F_FLAG=1
			shift 1
			;;
		-*)
			echo "Error: unknown option -- '$(echo $1 | sed 's/^-*//')'"
			guide_to_usage
			exit 1
			;;
	esac
done

if [ -z $INS_DIR ]; then
	echo "Error: specify install directory with '-d' option."
	guide_to_usage
	exit 1
fi

if [ $F_FLAG -eq 1 ]; then
	F_OPTION="-f"
else
	F_OPTION=""
fi

EXCLUDES="${PROGNAME}\|bash_functions.sh"

for f in $(ls *.py | grep -v ${EXCLUDES}); do ln -s ${F_OPTION} $(pwd)/$f ${INS_DIR}/$(basename $f .py); done
for f in $(ls *.sh | grep -v ${EXCLUDES}); do ln -s ${F_OPTION} $(pwd)/$f ${INS_DIR}/$(basename $f .sh); done

