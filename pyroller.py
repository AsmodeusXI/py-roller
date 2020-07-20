import sys
import random
import re

def main(args):
	if len(args) > 1:
		print('pyroller only accepts a single string argument.');
		sys.exit();
	else:
		roll(args[0])

def roll(expr):
	parse = re.search(r'^(?P<dice>\d*d\d*)+(?P<mod>[\+|-]\d*)?$', expr)
	dice_str = parse.group('dice')
	mod_str = parse.group('mod')

	roll_results = roll_dice(dice_str)
	roll_value = sum(roll_results)

	if mod_str:
		mod, val = mod_str[0], mod_str[1:]
		if mod == '-':
			roll_value -= int(val)
		else:
			roll_value += int(val)

	report(roll_results, roll_value)

def roll_dice(dice_str):
	dice_parse = re.match(r'^(?P<num>\d*)d(?P<size>\d*)$', dice_str)
	num = int(dice_parse.group('num'))
	size = int(dice_parse.group('size'))

	results = []
	for i in range(num):
		results.append(random.randint(1, size))

	return results

def report(results, value):
	print 'You rolled a', value
	print 'with the following results:', results

if __name__ == "__main__":
	main(sys.argv[1:])
