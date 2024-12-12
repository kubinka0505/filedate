import filedate
from argparse import ArgumentParser

Parser = ArgumentParser(
	prog = "filedate",
	description = "Command-line wrapper for `filedate.core` module.",
	epilog = "If no argument is specified, `File.get` function is called, otherwise `File.set`",
	add_help = 0,
	allow_abbrev = 0
)

#-=-=-=-#
# Groups

Required = Parser.add_argument_group("Required arguments")
Optional = Parser.add_argument_group("Optional arguments")
Switch   = Parser.add_argument_group("Switch arguments")

#-=-=-=-#
# Arguments

Required.add_argument(
	"-i", "--inputs",
	nargs = "*",
	type = str,
	required = True,
	help = "Existing files absolute path."
)

#---#

Optional.add_argument(
	"-c", "--created",
	default = "",
	help = "Date of files creation. Does nothing on non-Windows operating systems."
)
Optional.add_argument(
	"-m", "--modified",
	default = "",
	help = "Date of files modification date."
)
Optional.add_argument(
	"-a", "--accessed",
	default = "",
	help = "Date of files access date."
)

#---#

Switch.add_argument(
	"-e", "--expanded",
	action = "store_false",
	help = "Outputs more precise `datetime.datetime.strftime` format argument pattern."
)

Switch.add_argument(
	"-h", "--help",
	action = "help",
	help = "Shows this message."
)

#-=-=-=-#
# Settings

args = Parser.parse_args()

if args.expanded:
	args.format_string = "%d/%m/%Y %H:%M:%S"
else:
	args.format_string = "%A, %d{} %B %Y, %H:%M:%S.%f"

#-=-=-=-#
# Functions

def main():
	for Input in args.inputs:
		input_obj = filedate.File(Input)
		_get = input_obj.get()

		if not any((args.created, args.modified, args.accessed)):
			longest = [k for k in _get.keys()]
			longest = sorted(longest, key = len)[-1]
			longest = len(longest)

			print(input_obj.path)
			for key, value in _get.items():
				ordinal = "th"

				# Ordinals for "--expanded"
				if value.day % 10 == 1:
					ordinal = "st"

				if value.day % 10 == 2:
					ordinal = "nd"

				if value.day % 10 == 3:
					ordinal = "rd"

				args.format_string = args.format_string.format(ordinal)

				print(
					4 * " " + (key.title() + ":").ljust(longest + 1, " "), value.strftime(args.format_string),
				)

			if Input != args.inputs[-1]:
				print()
		else:
			input_obj.set(
				created  = args.created  if args.created  else None,
				modified = args.modified if args.modified else None,
				accessed = args.accessed if args.accessed else None
			)